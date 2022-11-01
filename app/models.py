from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        'メールアドレス',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'アカウント'



class Place(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    address = models.CharField(max_length=128)
    access = models.CharField(max_length=128)
    floorplan = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name


class PlacePhoto(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    

    def __str__(self):
        return str(self.place )
    
    

class Reserve(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

class ViewedPlace(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Favorite(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

CATEGORY = (('business', 'ビジネス'), ('title', '生活'), ('other','その他'))

class App(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
        )
    
    def __str__(self):
        return self.title

