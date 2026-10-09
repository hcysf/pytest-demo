ADD_COURSE_TEST_DATA = [
    {
        "id": "TEST_COURSE_ADD_001",
        "description": "正常添加课程--成功",
        # 要添加的课程信息。注意字段名：applicableperson（接口里叫 applicable_person）
        "course": {
            "name": "自动化测试实战课",   # 课程名称
            "subject": "6",              # 学科
            "price": 900,                # 价格
            "applicable_person": "2",     # 适用人群
            "info": "从零开始学习自动化测试",  # 课程介绍
        },
        # 期望结果：接口返回 code=200、msg=操作成功
        "experience": {
            "code": 200,
            "msg": "操作成功",
        },
        "check_exists": True,  # 添加后再去查询验证课程是否存在
    },

    {
            "id": "TEST_COURSE_ADD_002",
            "description": "错误参数，添加课程--失败",
            # 要添加的课程信息。注意字段名：applicableperson（接口里叫 applicable_person）
            "course": {
                "name": "Python",   # 课程名称
                "subject":66666666,              # 学科        超长
                "price":888,                # 价格
                "applicable_person":"2",     # 适用人群  错误的参数类型  预期 str  实际 int
                "info":"Python" # 课程介绍
            },
            # 期望结果：接口返回 code=500、msg=subject超长
            "experience": {
                "code":500,
                "msg": ('\n'
 '### Error updating database.  Cause: '
 'com.mysql.cj.jdbc.exceptions.MysqlDataTruncation: Data truncation: Data too '
 "long for column 'subject' at row 1\n"
 '### The error may exist in URL '
 '[jar:file:/usr/share/nginx/huike-admin.jar!/BOOT-INF/lib/huike-clues-3.4.0.jar!/mapper/clues/TbCourseMapper.xml]\n'
 '### The error may involve '
 'com.huike.clues.mapper.TbCourseMapper.insertTbCourse-Inline\n'
 '### The error occurred while setting parameters\n'
 '### SQL: insert into tb_course          ( code,             '
 'name,             subject,             price,                          '
 'info,             create_time )           values ( ?,             '
 '?,             ?,             ?,                          ?,             ? '
 ')\n'
 '### Cause: com.mysql.cj.jdbc.exceptions.MysqlDataTruncation: Data '
 "truncation: Data too long for column 'subject' at row 1\n"
 "; Data truncation: Data too long for column 'subject' at row 1; nested "
 'exception is com.mysql.cj.jdbc.exceptions.MysqlDataTruncation: Data '
 "truncation: Data too long for column 'subject' at row 1")
            },
            "check_exists": False,  # 添加后再去查询验证课程是否存在
        }
]

# ==================== 查询课程测试数据 ====================
QUERY_COURSE_TEST_DATA = [
    {
        "id": "TEST_COURSE_ADD_001",
        "description": "查询所有课程--成功（不传任何参数）",
        "params": {},  # 查询参数（空 = 查全部）
        "experience": {
            "code": 200,
            "msg": "查询成功",
            "has_data": True,  # 期望能查到数据
        },
    },
    {
        "id": "TEST_COURSE_ADD_002",
        "description": "按课程名称查询--成功",
        "params": {
            "name": "自动化测试实战课",  # 按课程名过滤
        },
        "experience": {
            "code": 200,
            "msg": "查询成功",
            "has_data": True,
        },
    },
]