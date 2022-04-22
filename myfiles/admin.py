from django.contrib import admin

# Register your models here.
from myfiles.models import *


class AdminAccessType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(AccessType,AdminAccessType)
class AdminAccessMax(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'tur','rasm']

admin.site.register(AccessMaxsulot,AdminAccessMax)
class AdminAccessMax1(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'tur','rasm']

admin.site.register(AccessMaxsulot1,AdminAccessMax1)
class AdminAccessMax2(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'tur','rasm']

admin.site.register(AccessMaxsulot2,AdminAccessMax2)



class AdminMobileType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(MobileType,AdminMobileType)
class AdminMobileMax(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'tur','rasm']

admin.site.register(MobileMaxsulot,AdminMobileMax)



class AdminHomeType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(HomeType,AdminHomeType)
class AdminHomeMax(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'tur','rasm']

admin.site.register(HomeMaxsulot,AdminHomeMax)


class AdminSotib_olmoq(admin.ModelAdmin):
    list_display = ['id', 'nomi','narx', 'tur','vaqt']

admin.site.register(Sotib_olngan_maxsulot,AdminSotib_olmoq)


