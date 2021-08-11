from django.db import models

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    

    def __str__(self): # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자 



    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'