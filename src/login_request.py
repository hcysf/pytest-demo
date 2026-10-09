import requests
from requests import session


class ReDate():
    # 初始化数据
    def __init__(self):
        # 创建会话
        self.session = requests.session()
        # 定义url数据
        self.base_url = "https://kdtx-test.itheima.net"
        # 定义请求头数据
        self.headers = {
            # 告诉服务器我是浏览器
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0",
            "Content-Type": "application/json"
        }

    # 定义获取验证码请求
    def get_captchaImage(self):
        # 定义验证码接口的url
        url = self.base_url + "/api/captchaImage"
        #
        response = self.session.get(url=url, headers=self.headers)
        return response

    # 获取登录请求
    """
        1.url
        2.方法：post
        3.headers
        4.body里面的数据(json)：
                                "username": "admin",
                                "password": "HM_2023_test",
                                "code": "2",
                                "uuid": "{{uuid}}"

    """

    def get_login(self, username, password, code, uuid):
        # 获取url
        url = self.base_url + "/api/login"
        # 定义headers
        headers = self.headers
        # 定义body内容
        date = {
            "username": username,
            "password": password,
            "code": code,
            "uuid": uuid
        }
        # 发送请求 post
        response = self.session.post(url=url, json=date, headers=headers)
        # 返回响应的结果
        return response

    # 关闭会话
    def close_session(self):
        # 关闭掉session会话，释放掉session里面的资源
        self.session.close()