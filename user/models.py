from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser

#유저모델
#회원가입[이름, 이메일, 비밀번호, 비밀번호 확인](아이디 따로 없음 ,이메일을 아이디로 사용)
#로그인[이메일, 비밀번호]

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **kwargs):
    
        user = self.model(
            userEmail = email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        
        return 

class User(models.Model):
    userName = models.CharField(max_length=50) 
    userPassword = models.CharField(max_length=50)
    userEmail = models.EmailField(max_length=100)
    userSubartist = models.ManyToManyField('') 
    userBuyalbumList = models.ManyToManyField('') 
    usersSubaumList = models.ManyToManyField('') 

    objects = UserManager()

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ['userEmail']

    class Meta:
        db_table = 'user'



