from django.shortcuts import render,redirect
from django.http import HttpResponse #new
from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import * #new
from .forms import OrderForm, CreateuserForm
from .filters import OrderFilter



#returning a template
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        
        form = CreateuserForm()

        if request.method == 'POST':
            form = CreateuserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')#get username without other attributes
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        #check if user in database
            user = authenticate(request, username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password incorrect')

        context = {}
        return render(request, 'accounts/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

#if the user is not logged in sent thembacktologin 
@login_required(login_url='login')
def home(request):  
    orders = Order.objects.all()                
    customers = Customer.objects.all()
    
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()


    context = {'orders': orders, 'customers': customers, 'total_orders':total_orders, 'delivered':delivered,  'pending':pending}   

    return render(request, 'accounts/dashboard.html', context)

# # #returning a httpresponse
# def products(request):              
#     return HttpResponse('product') 

@login_required(login_url='login')
def products(request):     
    products = Product.objects.all()             
    return render(request, 'accounts/products.html', {'products':products} ) 

def customer(request,pk):    #passing primary key   
    customer = Customer.objects.get(id = pk)   

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs #orders will be updated with filtered items

    context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myfilter':myFilter }

    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet =  inlineformset_factory(Customer, Order, fields=('product', 'status'), extra = 10) 
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)
    # form = OrderForm(initial = {'customer': customer}) #the customer will be already filled in form
    if request.method == 'POST':
        # print ('Printing POST',request.POST)#print in terminal
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance = customer)

        if formset.is_valid():
            formset.save()  #save information to the database
            return redirect('/') #redirect back to dashboard
        
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order) #object of that order will be passesd to the form

    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order  ) #POST will create a new entry .So we need instance.So we sent new post data into this instance oforder
        if form.is_valid():
            form.save()  #save information to the database
            return redirect('/') #redirect back to dashboard
        
    context ={'form':form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)