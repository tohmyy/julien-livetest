from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.forms import inlineformset_factory
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter
#all views


def home(request):
    orders = Order.objects.all().order_by('-id')
    customers = Customer.objects.all()

    totalcustomers = customers.count()
    totalorders = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    context = {'orders': orders, 'customersA': customers, 'totalorders':totalorders, 'pending':pending, 'delivered':delivered}

    return render(request,'accounts\dashboard.html', context)
    '''rendering(returning) data created in form of dictionary list(context) that 
        that can be looped through'''

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts\products.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    totalorders = orders.count()

    myFilter = OrderFilter()

    context = {'customer':customer, 'orders': orders, 'totalorders': totalorders, }
    return render(request, 'accounts\customer.html', context)


def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)



def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form, 'customer': customer}
    return render(request, 'accounts/update_customer.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
            customer.delete()
            return redirect("/")

    context = {'customer': customer}
    return render(request, 'accounts/delete_customer.html', context)

def createOrder(request):
    form = OrderForm()
    #print('Printing POST:', request.POST)
    if request.method == 'POST':
        #if the type of button request is "post"
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    return render(request, 'accounts\order_form.html', context)

def placeNewOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=4)
    customer = Customer.objects.get(id=pk)

    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})

    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)

        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {'formset':formset, 'customer':customer}
    return render(request, 'accounts\order_form.html', context)

#pass primary key "pk" when you want to perform action on a specific item
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    #(instance = order)-> sets the form with the info
    # of the order that you want to update
    #it also updates the current instance (order) instead of
    # creating a new order after submitting

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect("/")

    context = {'item': order}
    return render(request, 'accounts\delete.html', context)
