import  pytest
class TestDeleteXianSuo:
    def test_delete_xiansuo_by_id(self,test_login,add_xiansuo_id,):
        xiansuo_id=add_xiansuo_id
        response=test_login.delete_xiansuo_by_id(xiansuo_id)
        assert response.status_code==200
        data=response.json()
        print(data)
        # assert data["code"]==200 and data["msg"]=="操作成功"


