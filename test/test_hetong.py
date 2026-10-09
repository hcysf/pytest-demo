import  pytest


@pytest.mark.smoke
class TestHeTong:
    def test_hetong(self,test_login):
        file=r"C:\Users\DELL\Desktop\工具\1.docx"
        response=test_login.add_hetong(file)
        assert response.status_code==200
        data=response.json()
        print(data)
        assert data["code"]==200

