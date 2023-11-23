from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomerUserManager(BaseUserManager):
    def _create_user(self,email,name,phone,is_admin,is_staff,is_active,status,password,**extra_fields):
        if not email:
            raise ValueError("The given username must be set")

        email = self.normalize_email(email)
        user = self.model(email = email,name = name,phone = phone,is_admin = is_admin,is_staff = is_staff,is_active = is_active,status = status,password = password,**extra_fields) 
        user.set_password(password)
        user.save(using=self.db)

        return user 

    def create_user(self,email,name,phone,is_admin,is_staff,is_active,status,password = None, **extra_fields):
        return self._create_user(email,name,phone,is_admin,is_staff,True,status,password,**extra_fields)

    def create_superuser(self,email,name,phone,is_admin,is_staff,is_active,status,password= None, **extra_fields):
        return self._create_user(email,name,phone,True,True,True,'admin',password,**extra_fields,is_superuser = True)

class customuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=225, blank=True, null=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status_list = {
        ('admin','admin'),
        ('user','user')
    }          


    password = models.CharField(max_length=225)

    status = models.CharField(max_length=225, choices=status_list,blank=True,null=True,default='admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= [ 'name','password','phone','status','is_admin','is_staff','is_active']

    object = CustomerUserManager()

    def __str__(self):
        return '{}|{}'.format(self.name,self.email)


class kategori(models.Model):
    namakategori = models.CharField(max_length=225)


class berita(models.Model):
    STATUS = ('publish', 'publish'),('draft','draft')

    judul = models.CharField(max_length=255)
    judulLengkap = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    isi = models.CharField(max_length = 9999)
    kategori = models.ForeignKey(kategori,on_delete=models.CASCADE)
    kategoriID = models.IntegerField(max_length=255)
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    penulis = models.CharField(max_length = 255)
    fotoPenulis = models.ImageField(upload_to='media',height_field=None, width_field=None, max_length=100)
    publikasi = models.CharField(max_length = 255)
    status = models.CharField(choices=STATUS, max_length=200)