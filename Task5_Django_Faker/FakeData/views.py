from django.shortcuts import render, redirect
from .models import Fake_Students

from faker import Faker

# Create your views here.

def homepage(request):
    return render(request,'Homepage.html',{})


def createFakeData(request):
    if request.method=='POST':
        no=int(request.POST.get('no'))
        print(type(no))

        fake=Faker('hi_IN')
        for i in range(no):
            n=fake.name()
            p=fake.random_number(digits=2)
            e=fake.email()
            c=fake.city()
            m=fake.random_number(digits=10)
            Fake_Students.objects.create(Name=n,Percentage=p, Email=e,City=c, MobNo=m)
        return redirect('showfake')

    return render(request, 'CreateFakeData.html', {})


def showFakeData(request):
    records=Fake_Students.objects.all()
    return render(request, 'ShowFakeData.html',{'records':records})
