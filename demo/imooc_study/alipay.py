# PyCryptodome 是一个自包含的低级密码原语Python包。
# pip install pycryptodome
# 你只要想：既然是加密，那肯定是不希望别人知道我的消息，所以只有我才能解密，所以可得出公钥负责加密，私钥负责解密；
# 同理，既然是签名，那肯定是不希望有人冒充我发消息，只有我才能发布这个签名，所以可得出私钥负责签名，公钥负责验证
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64decode, b64encode
from urllib.parse import quote_plus
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen
import base64

import json


class Alipay(object):
    '''
    支付宝接口类
    '''

    def __init__(self, appid, app_notify_url, app_private_key_path, alipay_public_key_path,
                 return_url, debug=False):
        self.appid = appid  # 支付宝appid，沙箱环境提供测试的appid
        self.app_notify_url = app_notify_url  # 支付宝服务器主动通知商户服务器里指定的页面http/https路径
        self.app_private_key_path = app_private_key_path  # 商户私钥文件
        self.app_private_key = None  # 读文件生成一个商户私钥key
        self.return_url = return_url  # 用户pc端支付完成后跳转的页面

        # 读取文件获取商户私钥key
        with open(self.app_private_key_path) as fp:
            # fp.read()读取key并导入key，赋值给app_private_key
            self.app_private_key = RSA.importKey(fp.read())

        # 支付宝的公钥
        self.alipay_public_key_path = alipay_public_key_path

        # 读取文件获取支付宝公钥key，赋值给alipay_public_key，验证作用
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = RSA.import_key(fp.read())

        # 如果是True 进入沙箱环境的url，否则进入支付宝的url
        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"

    # 立即支付 请求函数，4个字段是支付宝要求必填字段
    # biz_content 支付宝文档要求，除公共参数外所有请求参数都必须放在这个参数中传递
    def direct_pay(self, subject, out_trade_no, total_amount, return_url=None, **kwargs):
        biz_content = {
            "subject": subject,  # 订单标题
            "out_trade_no": out_trade_no,  # 商户订单号
            "total_amount": total_amount,  # 订单总金额
            "product_code": "FAST_INSTANT_TRADE_PAY",  # 销售产品码
        }

        # 非必填参数用update更新到biz_content中
        biz_content.update(kwargs)

        # build_body公共请求参数
        data = self.build_body(method="alipay.trade.page.pay", biz_content=biz_content, return_url=self.return_url)

        # 获取了所有的消息格式就是开始签名
        return self.sign_data(data)  # 生成最终订单信息字符串

    # build_body公共请求参数 生成一个消息格式
    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,  # 支付宝appid，沙箱环境提供测试的appid
            "method": method,  # 接口名称
            "charset": "utf-8",  # 请求使用的编码格式
            "sign_type": "RSA2",  # 签名算法类型
            # strftime函数接收以时间元组，并返回以可读字符串表示的当地时间
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # 发送请求的时间
            "version": "1.0",  # 调用的接口版本，固定为：1.0
            "biz_content": biz_content,  # 业务请求参数的集合
        }

        # 如果存在 同步返回地址，HTTP/HTTPS开头字符串
        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url

        return data

    # 生成最终订单信息字符串
    def sign_data(self, data):
        data.pop("sign", None)  # 支付宝生成签名是不能有sign字段
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)  # 排序后列表list

        # '分隔符'.join(连接的元素)
        unsigned_string = "&".join("{0}={1}".format(k, v) for k, v in unsigned_items)  # 用&符号拼接

        # 进行签名
        sign = self.sign(unsigned_string=unsigned_string.encode("utf-8"))

        # 用&符号拼接，quote_plus（）如果值是url，我们就需要对其处理，可将字符串以URL编码
        quoted_string = "&".join("{0}={1}".format(k, quote_plus(v)) for k, v in unsigned_items)

        # 获得最终的订单信息字符串,用&符号拼接的字符串 + 生成的签名
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    # ASCII码里边，符号在前，然后是0-9 ，然后是大写字母A-Z，然后是小写字母a-z
    def ordered_data(self, data):
        compile_keys = []
        for key, value in data.items():

            # 如果value是字典类型
            if isinstance(value, dict):
                compile_keys.append(key)  # ['biz_content']

        # 将字典类型的数据dump出来
        for key in compile_keys:
            # separators：分隔符，实际上是(item_separator, dict_separator)
            # 的一个元组，默认的就是(‘, ’, ’:’)；这表示dictionary内keys之间用“, ”隔开，而KEY和value之间用“：”隔开。
            # key = biz_content
            data[key] = json.dumps(data[key], separators=(',', ':'))

        # sorted对可迭代对象进行排序
        return sorted([(k, v) for k, v in data.items()])

    # 进行生成签名函数
    def sign(self, unsigned_string):
        # 开始计算签名
        key = self.app_private_key  # 商户私钥key
        signer = PKCS1_v1_5.new(key)  # 生成一个签名对象
        signature = signer.sign(SHA256.new(unsigned_string))  # 使用SHA256进行签名
        # base64 编码，转换为unicode表示并移除回车,decode将utf-8编码的解码成unicode
        sign = base64.encodebytes(signature).decode("utf8").replace("\n", "")

        # 生成了私钥签名的字符串
        return sign

    # 对支付宝公钥验证
    def _verify(self, raw_content, signature):
        # 开始计算签名
        key = self.alipay_public_key  # 支付宝的公钥
        signer = PKCS1_v1_5.new(key)  # 生成一个签名对象
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))  # encode将unicode码编码成utf-8

        # 验签，如果成功的返回True
        if signer.verify(digest, base64.decodebytes(signature.encode("utf8"))):
            return True
        return False

    # 对支付宝公钥验证
    def verify(self, data, signature):
        if "sign_type" in data:
            sign_type = data.pop("sign_type")

        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(raw_content=message, signature=signature)


# 测试用例
if __name__ == "__main__":
    # 支付宝返回的url
    return_url = "http://127.0.0.1:8000/alipay/return/?total_amount=100.00&timestamp=2018-04-18+01%3A24%3A31&sign=j%2FF1IXN9%2F2DCenN8omUJHnAk%2FAnHgbzKehV2qYpqokftbyfGAUcDETmXUtSyVFH7jhrV5HVpM25Eew%2Bz9x1bVGxz37yEY2nhsu3CqwWkoCpOv3Ou003GwrkMr%2BAjVu5a%2Bpygti%2FEXsoNoQx7K2lCyWQxzKHO2WL%2FDEwvKyctoPYSBSrRsXVYkewd6IgugfiqV1Cx8uiHGJcf6%2FEYvJLi4MozOy6eQE0teb4ULaNzCm%2Fi7F5UsxF8rq4lqarH4Ysuw%2FnZYRXhaCBOH5rvHX4POPTMPM17xHtuTcxGO1zo71hG1d9uIMZmwzqfpkr9hAWCPs9Jn7d1XxQV2iqXt%2BOEUw%3D%3D&trade_no=2018041821001004100200455693&sign_type=RSA2&auth_app_id=2016091100485730&charset=utf-8&seller_id=2088102175133751&method=alipay.trade.page.pay.return&app_id=2016091100485730&out_trade_no=2017020288810&version=1.0"
    o = urlparse(return_url)
    query = parse_qs(o.query)  # 得到是字典，parse_qsl得到是列表
    processed_query = {}
    ali_sign = query.pop("sign")[0]  # pop删除sign，返回得到我们需要的sign，支付宝对本次支付结果的签名,

    # 初始化支付宝类
    alipay = Alipay(
        appid="2016091100485730",
        app_notify_url="http://127.0.0.1:8000/alipay/return/",  # 异步返回接口，支付完成后地址
        app_private_key_path="../trade/keys/private_2048.txt",  # 商户的私钥
        alipay_public_key_path="../trade/keys/alipay_key_2048.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,如果沙箱环境就设置为true
        return_url="http://127.0.0.1:8000/alipay/return/"  # 支付成功后跳转到哪个页面
    )

    for key, values in query.items():
        processed_query[key] = values[0]  # processed_query将返回的query拼接成字典
    print(alipay.verify(processed_query, ali_sign))  # 返回true就是成功了

    # 生成订单的字符串
    url = alipay.direct_pay(
        subject="测试订单",
        out_trade_no="2017020288810",  # 订单号
        total_amount=100,  # 订单总金额
        return_url="http://127.0.0.1:8000/"  # 用户pc端支付完成后跳转的页面，同步返回地址，HTTP/HTTPS开头字符串
    )
    # 生成最终的url
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    print(re_url)