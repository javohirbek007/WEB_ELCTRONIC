from django.db import models

# Create your models here.


class AccessType(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class AccessMaxsulot(models.Model):
    nomi = models.CharField(max_length=40)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    tur = models.ForeignKey(AccessType,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
class AccessMaxsulot1(models.Model):
    nomi = models.CharField(max_length=40)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    tur = models.ForeignKey(AccessType,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
class AccessMaxsulot2(models.Model):
    nomi = models.CharField(max_length=40)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    tur = models.ForeignKey(AccessType,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')


class MobileType(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class MobileMaxsulot(models.Model):
    nomi = models.CharField(max_length=40)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    tur = models.ForeignKey(MobileType, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')


class HomeType(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class HomeMaxsulot(models.Model):
    nomi = models.CharField(max_length=40)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    tur = models.ForeignKey(HomeType, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')


class Sotib_olngan_maxsulot(models.Model):
    nomi= models.CharField(max_length=50)
    narx = models.IntegerField()
    son = models.IntegerField(default=1)
    tur = models.CharField(max_length=50)
    vaqt = models.DateTimeField(auto_now=True)

class Sotib_olngan_maxsulot1(models.Model):
    nomi= models.CharField(max_length=50)
    narx = models.IntegerField()
    son = models.IntegerField(default=1)
    tur = models.CharField(max_length=50)
    vaqt = models.DateTimeField(auto_now=True)

class Sotib_olngan_maxsulot2(models.Model):
    nomi= models.CharField(max_length=50)
    narx = models.IntegerField()
    son = models.IntegerField(default=1)
    tur = models.CharField(max_length=50)
    vaqt = models.DateTimeField(auto_now=True)


