import os

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
        self.token=""

    # 定义获取验证码请求
    def get_captchaImage(self):
        # 定义验证码接口的url
        url ="http://kdtx-test.itheima.net/api/captchaImage"
        #发送请求
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

    #追加token
    def set_token(self,token):
        self.token=token
        self.headers["Authorization"]=f"Bearer {self.token}"


    #定义新增课程
    def add_course(self,name,subject,price,applicable_person,info):
        #定义接口rul
        url=self.base_url+"/api/clues/course"
        #定义内容data
        data={
            "name":name,
            "subject":subject,
            "price":price,
            "applicable_person":applicable_person,
            "info":info
        }
        response=self.session.post(url=url,json=data,headers=self.headers)
        return response



    #定义查询课程
    def select_course(self,name=None,subject=None,price=None,applicable_person=None,info=None):
        #定义查询接口url
        url=self.base_url+"/api/clues/course/list"
        #定义查询参数
        params={}
        #通过通的查询信息，插入相应的参数
        if name:
            params["name"]=name
        if subject:
            params["subject"]=subject
        if price:
            params["price"]=price
        if applicable_person:
            params["applicable_person"]=applicable_person
        if info:
            params["info"]=info
        response=self.session.get(url,params=params,headers=self.headers)
        return  response


    #通过id查询相应的课程信息
    def get_course_id(self, course_id):
        url = f"{self.base_url}/api/clues/course/{course_id}"
        response = self.session.get(url, headers=self.headers)
        return response

    #通过id修改相应的课程信息
    def update_course_id(self, course_id, name, subject, price, applicable_person, info):
        url = f"{self.base_url}/api/clues/course"
        data = {
            "id": course_id,
            "name": name,
            "subject": subject,
            "price": price,
            "applicablePerson": applicable_person,
            "info": info
        }
        response = self.session.put(url, json=data, headers=self.headers)
        return response

    #通过id删除相应的课程
    def delete_course_id(self, course_id):
        url = f"{self.base_url}/api/clues/course/{course_id}"
        response = self.session.delete(url, headers=self.headers)
        return response

    # 新增合同接口
    def add_hetong(self, file_path):
        #url
        url = self.base_url + '/api/common/upload'
        # 从文件路径中提取出文件名‌
        file_name = os.path.basename(file_path)
        headers = {
            "Authorization": self.headers["Authorization"],
            "User-Agent": self.headers["User-Agent"],
        }
        with open(file_path, 'rb') as f:
            files = {'file': (file_name, f)}
            response = self.session.post(url, files=files, headers=headers)
        return response



    #新增线索
    def add_xiansuo(self,activityId=None,name=None,phone=None,channel=None,sex=None,age=None,weixin=None,qq=None):
        url=self.base_url+"/api/clues/clue"
        data={
            "activityId":activityId,
            "name": name,
            "phone": phone,
            "channel":channel,
            "sex": sex,
            "age":age,
            "weixin":weixin,
            "qq": qq
        }
        response=self.session.post(url=url,json=data,headers=self.headers)
        return response


    #定义查询线索
    def select_xiansuo(self,id=None,name=None,phone=None):
        #查询的url
        url=self.base_url+"/api/clues/clue/list"
        #定义查询参数
        params={}
        #判断查询的参数
        if id:
            params["id"]=id
        if name:
            params["name"]=name
        if phone:
            params["phone"]=phone
        #发起请求
        response=self.session.get(url=url,params=params,headers=self.headers)
        return response

    #定义通过id删除线索
    def delete_xiansuo_by_id(self,xiansuo_id):
        #定义url
        url=f"{self.base_url}/api/clues/clue/false/{xiansuo_id}"
        #请求参数
        body={
                "reason": "2",
                "remark": "1"
            }
        #发送请求
        response=self.session.put(url=url,headers=self.headers,json=body)
        return response



    # 关闭会话
    def close_session(self):
        # 关闭掉session会话，释放掉session里面的资源
        self.session.close()
