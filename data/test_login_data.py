login_test_data = [
     {
         "id":"test001",
         "descripiton":"正确的用户名+正确的密码+正确的验证码，登陆成功",
         "username":"admin",
         "password":"HM_2023_test",
         "code_type":"correct",
         "expected_code":200,
         "expected_msg":"操作成功",
         "check_token":True
     },
    {
        "id": "test002",
        "descripiton": "错误的用户名+正确的密码+正确的验证码，登陆失败",
        "username":"****",
        "password":"HM_2023_test",
        "code_type":"correct",
        "expected_code":500,
        "expected_msg":"用户不存在/密码错误",
        "check_token":False
    },
    {
        "id": "test003",
        "descripiton": "正确的用户名+错误的密码+正确的验证码，登陆失败",
        "username":"admin",
        "password":"****",
        "code_type":"correct",
        "expected_code":500,
        "expected_msg":"用户不存在/密码错误",
        "check_token":False
    },
    {
        "id": "test004",
        "descripiton": "正确的用户名+正确的密码+错误验证码，登陆失败",
        "username":"admin",
        "password":"HM_2023_test",
        "code_type":"*****",
        "expected_code":500,
        "expected_msg":"验证码错误",
        "check_token":False
    }

 ]
