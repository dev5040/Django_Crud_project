

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Query

# Create your views here.
def home(request):
    return render(request,'app/home.html')       
def about(request):
    return render(request,'app/about.html')
def contact(request):
    return render(request,'app/contact.html')          
def service(request):
    return render(request,'app/service.html')
def register(request):  
    return render(request,'app/register.html') 
def login(request):
    return render(request,'app/login.html')

def logout(request):
    return render(request,'app/home.html')

def UserRegister(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        city = request.POST['city']
        password = request.POST['password']
        # First we will validate that user already exist
        user = Student.objects.filter(Email=email)
        if user: 
            message = "User already exist"
            return render(request,"app/register.html",{'msg':message})
        else:
                Student.objects.create(
                                            Name=name,
                                            Email=email,
                                            Contact=contact,
                                            City=city,
                                            Password=password,
                                            )
                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
    else:
        message = "Password and Confirm Password Does not Match"
        return render(request,"app/register.html",{'msg':message})
   

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = Student.objects.filter(Email=email)
        if user:
            data = Student.objects.get(Email=email)
            if data.Password == password:
                name = data.Name
                email = data.Email
                contact = data.Contact
                city = data.City
                password=data.Password
                
                user={
                    'name':name,
                    'email':email,
                    'contact':contact,
                    'city':city,
                    'password':password,
                }
                return render(request,"app/dashboard.html",{'user':user})
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})   
        
def query(request,pk):  
    # Data come from HTML to View
    if request.method == "POST":
        email = request.POST['email']
        query = request.POST['query']
        print(email)
        print(query)
        Query.objects.create(Email=email,Queryl=query)
        
        data = Student.objects.get(Email=pk)
        name = data.Name
        email = data.Email
        contact = data.Contact
        city = data.City
        password=data.Password
        
        user={
            'name':name,
            'email':email,
            'contact':contact,
            'city':city,
            'password':password,
            }
        all_data=Query.objects.filter(Email=pk)
        return render(request,'app/dashboard.html',{'key1':all_data,'user':user})
    # After Insert render on Show.html
    else:
        return render(request,"app/dashboard.html")


def showdata(request,pk):
    #select * from tablename
    #for fetching all the data of the table
    data = Student.objects.get(Email=pk)
    name = data.Name
    email = data.Email
    contact = data.Contact
    city = data.City
    password=data.Password
    user={
        'name':name,
        'email':email,
        'contact':contact,
        'city':city,
        'password':password,
        }
    all_data=Query.objects.filter(Email=pk)
    return render(request,'app/dashboard.html',{'key1':all_data,'user':user})



def deleteData(request,pk):
    data = Query.objects.get(id=pk)
    email = data.Email
    data.delete()
    data = Student.objects.get(Email=email)
    name = data.Name
    email = data.Email
    contact = data.Contact
    city = data.City
    password=data.Password
    user={
        'name':name,
        'email':email,
        'contact':contact,
        'city':city,
        'password':password,
        }
    all_data=Query.objects.filter(Email=email)
    return render(request,'app/dashboard.html',{'key1':all_data,'user':user})


def editPage(request,pk):
    #fetching the data of perticular ID
    data1=Query.objects.get(id=pk)
    email = data1.Email
    data = Student.objects.get(Email=email)
    name = data.Name
    email = data.Email
    contact = data.Contact
    city = data.City
    password=data.Password
    user={
        'name':name,
        'email':email,
        'contact':contact,
        'city':city,
        'password':password,
        }
    all_data=Query.objects.filter(Email=email)
    return render(request,'app/dashboard.html',{'key1':all_data,'user':user,'key2':data1})


def updateData(request,pk):
    udata=Query.objects.get(id=pk)
    udata.Email=request.POST['email']
    udata.Queryl=request.POST['query']
    #Query for update
    udata.save()
    data = Student.objects.get(Email=udata.Email)
    name = data.Name
    email = data.Email
    contact = data.Contact
    city = data.City
    password=data.Password
    user={
        'name':name,
        'email':email,
        'contact':contact,
        'city':city,
        'password':password,
        }
    all_data=Query.objects.filter(Email=udata.Email)
    return render(request,'app/dashboard.html',{'key1':all_data,'user':user})


    
def dashboard(request):
    return render(request,'app/dashboard.html')  
