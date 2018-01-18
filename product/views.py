from django.shortcuts import render,redirect
from .modelscategory import Category
from .modelsproduct import Product
from django.core.files.storage import FileSystemStorage

# Create your views here..
def index(request):    
    title = "資料管理"
    product = Product()
    products = product.all()
    return render(request,'product/index.html',locals())

def create(request):
    if request.method == "POST" and request.FILES['productimage']:
        categoryid = request.POST['categoryid']
        modelnumber = request.POST['modelnumber']
        modelname = request.POST['modelname']
        unitcost = request.POST['unitcost']
        description = request.POST['description']
        thefile = request.FILES['productimage']
        productimage = thefile.name

        #資料新增
        product = Product()
        datas = tuple([categoryid,modelnumber,modelname,unitcost,productimage,description])
        product.create(datas)

        #檔案上傳
        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        
        return redirect("/product")

    category = Category()
    datas = category.all()

    title = "新增資料"
    return render(request,'product/create.html',locals())

def update(request, id):
    if request.method == "POST" and request.FILES['productimage']:
        categoryid = request.POST['categoryid']
        modelnumber = request.POST['modelnumber']
        modelname = request.POST['modelname']
        unitcost = request.POST['unitcost']
        description = request.POST['description']
        thefile = request.FILES['productimage']
        productimage = thefile.name

        #資料修改
        product = Product()
        datas = tuple([categoryid,modelnumber,modelname,unitcost,productimage,description,id])
        product.update(datas)

        #檔案上傳
        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        
        return redirect("/product")



    title = "資料修改"
    category = Category()
    categories = category.all()

    product = Product()
    singleproduct = product.single(id)



    return render(request,'product/update.html',locals())

def delete(reqeust, id):
    product = Product()
    product.delete(id)
    return redirect("/product")