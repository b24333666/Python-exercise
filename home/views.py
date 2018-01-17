from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):    
    # return HttpResponse("<h2>Home Index</h2>")
    datas = [{"name":"Jack","age":30,"email":"Jack@gmail.com"},
             {"name":"Mary","age":25,"email":"Mary@gmail.com"},
             {"name":"Tom","age":25,"email":"Tom@gmail.com"}]

    return render(request,'home/index.html',{'title':'首頁','users':datas,'name':'Jack','now':datetime.datetime.now()})

    # return render(request,'home/index.html',{'title':'首頁','users':datas})
def about(request):
    # return HttpResponse("<h2>Home About</h2>")
    # title1 = "關於"
    # title2 = "我們"
    if request.method == "POST":
        email = request.POST['useremail']
        name = request.POST['username']
    title="關於AIEN"
    return render(request,'home/about.html',locals())

def contact(request):
    # return HttpResponse("<h2>Home Contact</h2>")
    
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "guest"
    if 'id' in request.GET:
        userid = request.GET['id']    

    title="聯絡我們"
    return render(request,'home/contact.html',locals())

def contact1(request,name):
    # return HttpResponse("<h2>Home Contact</h2>")
   
    title="聯絡 " + name
    return render(request,'home/contact1.html',locals())

def uploaddata(request):
    if request.method == "POST" and request.FILES["myfile"]:
        #request.GET、reuest.POST、request.FILES
        myfile = request.FILES['myfile']
        print(myfile.name)
        print(myfile.size)
       
        fs = FileSystemStorage()
        fs.save(myfile.name,myfile)

    title = "檔案上傳"
    return render(request, 'home/uploadfile.html',locals())