from django.shortcuts import render
from app.models import *


# Create your views here.
def insert_course(request):
    if request.method=="POST":
        cn=request.POST["cn"]
        CO=Course.objects.get_or_create(cname=cn)[0]

        CO.save()

        QLCO=Course.objects.all()
        d={'courses':QLCO}
        return render (request,'display_course.html',d)
        

    return render (request,'insert_course.html')





def insert_student(request):
    QLCO=Course.objects.all()
    d={'courses':QLCO}
    
    if request.method=="POST":
        cn=request.POST["cn"]
    
        sn=request.POST.get("sn")
       

        sem=request.POST.get("sem")
        sd=request.POST.get("sd")
        co=Course.objects.get(cname=cn)

        SO=Student.objects.get_or_create(cname=co,sname=sn, semail=sem, sid=sd)[0]

        SO.save()

        QLSO=Student.objects.all()
        d={'students':QLSO}
        return render (request,'display_student.html',d)
    return render (request,'insert_student.html',d)




def multipleoption(request):
    QLCO=Course.objects.all()
    d={'courses':QLCO}
    if request.method=="POST":
        cn=request.POST.getlist('cn')

        QLSO=Student.objects.none()
        for i in cn:
            QLSO=QLSO|Student.objects.filter(cname=i)
        d={'students':QLSO}
        return render (request,'display.html',d)
        




    return render (request,'multipleoption.html',d)
    


