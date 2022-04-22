from django.shortcuts import render
from myfiles.models import *
# Create your views here.
import datetime

def index(malumot):
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    access_types = AccessType.objects.all()
    return render(malumot,'index.html',{'mobile_type':mobile_types,'home_type':home_types,'access_type':access_types})

def about(malumot):
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'about.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})
def single(malumot):
    return render(malumot, 'single.html')
def products(malumot):
    if malumot.method=="POST":
        nomi = malumot.POST.get("nomi")
        narx=malumot.POST.get('narx')
        son=malumot.POST.get('son')
        tur=malumot.POST.get('tur')
        vaqt = datetime.datetime.now()

        try:
            maxsulot = Sotib_olngan_maxsulot.objects.filter(nomi=nomi)[0]
        except Exception :
            pass

        if maxsulot:
            max_id = maxsulot.id
            max_soni=maxsulot.son+1
            vaqt = datetime.datetime.now()
            Sotib_olngan_maxsulot(id=max_id, nomi=nomi, narx=narx, son=max_soni, tur=tur, vaqt=vaqt).save()
        else:
            Sotib_olngan_maxsulot(nomi=nomi, narx=narx, son=son, tur=tur, vaqt=vaqt).save()




        Sotib_olngan_maxsulot(nomi = nomi,narx = narx,son = son,tur = tur,vaqt = vaqt).save()
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'products.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})




def codes(malumot):
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'codes.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})
def faq(malumot):
    return render(malumot,'faq.html')
def icons(malumot):
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'icons.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})
def mail(malumot):
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'mail.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})
def products1(malumot):
    if malumot.method=="POST":
        nomi = malumot.POST.get("nomi")
        narx=malumot.POST.get('narx')
        son=malumot.POST.get('son')
        tur=malumot.POST.get('tur')
        vaqt = datetime.datetime.now()
        Sotib_olngan_maxsulot1(nomi = nomi,narx = narx,son = son,tur = tur,vaqt = vaqt).save()
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()
    return render(malumot,'products1.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})
def products2(malumot):
    if malumot.method=="POST":
        nomi = malumot.POST.get("nomi")
        narx=malumot.POST.get('narx')
        son=malumot.POST.get('son')
        tur=malumot.POST.get('tur')
        vaqt = datetime.datetime.now()
        Sotib_olngan_maxsulot2(nomi = nomi,narx = narx,son = son,tur = tur,vaqt = vaqt).save()
    access_types = AccessType.objects.all()
    mobile_types = MobileType.objects.all()
    home_types = HomeType.objects.all()

    return render(malumot,'products2.html',{'access_type':access_types,'mobile_type':mobile_types,'home_type':home_types})



def pro(malumot,id):
    mobiles = MobileMaxsulot.objects.filter(tur_id=id)
    return render(malumot,'products.html',{'mobile_type':mobiles})
def pro1(malumot,id):
    mobiles = MobileMaxsulot.objects.filter(tur_id=id)
    return render(malumot,'products1.html',{'mobile_type':mobiles})
def pro2(malumot,id):
    mobiles = MobileMaxsulot.objects.filter(tur_id=id)
    return render(malumot,'products2.html',{'mobile_type':mobiles})
def karzinka(malumot):
    maxsulotlar = Sotib_olngan_maxsulot.objects.all()
    return render(malumot,'karzinka.html',{'maxs':maxsulotlar})
