import  pytest
from data.test_xiansuo import xiansuo_test_data

class TestXianSuo:
    @pytest.mark.parametrize("test_data",xiansuo_test_data)
    def test_add_xiansuo(self,test_login,test_data):
        name=test_data["name"]
        phone=test_data["phone"]
        channel=test_data["channel"]
        activityId=test_data["activityId"]
        sex=test_data["sex"]
        age=test_data["age"]
        weixin=test_data["weixin"]
        qq=test_data["qq"]

        print(f"{'=' * 50}")
        print(f"执行测试用例")

        response=test_login.add_xiansuo(
            name=name,
            phone=phone,
            channel=channel,
            activityId=activityId,
            sex=sex,
            age=age,
            weixin=weixin,
            qq=qq
                                        )
        assert response.status_code==200
        data=response.json()
        print(data)

        if data['code']==500:
            assert data["code"] == 500  and  data["msg"] == "手机号重复"
        if data['code']==200:
            assert data["code"] == 200 and data["msg"] == "操作成功"

        #查询新增线索
        response_select=test_login.select_xiansuo(name=name)
        select_data = response_select.json()
        assert select_data["code"] == 200
        assert len(select_data.get("rows", [])) > 0, \
            f"线索 '{data['name']}' 未在列表中找到"

        #校验查询的结果与新增的信息是否准确
        reslut_xiansuo = select_data["rows"][0]
        assert reslut_xiansuo ["name"] ==name, \
            f"线索名称不匹配: {reslut_xiansuo ["name"]} != {name}"
        assert reslut_xiansuo ["phone"] == phone, \
            f"手机号不匹配: {reslut_xiansuo ["name"]} != {phone}"

        xiansuo_id = reslut_xiansuo["id"]
        print(f"用例 {xiansuo_id} 通过!")
