from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.shortcuts import render,  redirect
import yfinance as yf
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm
from .models import User, Agent, UserStock, Stock, Transaction, Property, Item

# Create your views here.

# msft = yf.Ticker('msft')
    
# msft_historcal = msft.history(period="1d")
    
# msft_open = msft_historcal.Low.values[0]

def loginPage(request):    
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error occurred')
    context= {'form':form}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    
    context = {}
    return render(request, 'base/home.html', context)

def stocks(request):
    
    stocks = Stock.objects.all()
    
    for stock in stocks:
        
        ticker = yf.Ticker(stock.abbreviation)
    
        stock_info = ticker.history(period="1d")
    
        stock.dayLow = round(stock_info.Low.values[0], 2)
        stock.dayHigh = round(stock_info.High.values[0], 2)
        stock.open = round(stock_info.Open.values[0], 2)
        stock.close = round(stock_info.Close.values[0], 2)
        stock.volume = stock_info.Volume.values[0]
        stock.prevClose = ticker.info["previousClose"]
        stock.save()
        
    context = {'stocks':stocks,}
    return render(request, 'base/stocks.html', context)

def properties(request):
    properties = Property.objects.filter(selling = True)
         
    context = {'properties':properties,}
    return render(request, 'base/properties.html', context)

def items(request):
    items = Item.objects.filter(selling = True)
    
    context = {'items':items,}
    return render(request, 'base/items.html', context) 

@login_required(login_url='login')
def buyItem(request, pk):
    item = Item.objects.get(id=pk)
    
    if request.method == 'POST':
        
        Transaction.objects.create(
            user = request.user,
            seller = property.user,
            type = 'Item',
            itemType = item.name,
            price = item.price
        )
        
        item.user = request.user
        item.selling = False
        item.save()
        
        return redirect('items')

    context = {}
    return render(request, 'base/buyItem.html', context)

@login_required(login_url='login')
def buyProperty(request, pk):
    property = Property.objects.get(id=pk)
    
    if request.method == 'POST':
        
        Transaction.objects.create(
            user = request.user,
            seller = property.user,
            type = 'Property',
            itemType = property.address,
            price = property.price
        )
        
        property.user = request.user
        property.selling = False
        property.save()
        
        return redirect('properties')

    context = {'property':property}
    return render(request, 'base/buyProperty.html', context)

@login_required(login_url='login')
def buyStock(request, pk):
    stock = Stock.objects.get(name=pk)
    
    if request.method == 'POST':
        Transaction.objects.create(
            user = request.user,
            type = 'Stock',
            itemType = stock.name,
            price = request.POST.get('price'),
        )
        
        userStock = UserStock.objects.get_or_create(user = request.user, stock = stock)
        
        ticker = yf.Ticker(stock.abbreviation)
        stock_info = ticker.history(period="1d")
        close = stock_info.Low.values[0]
        
        userStock = UserStock.objects.get(user = request.user, stock = stock)
        
        prevshares = userStock.shares
        userStock.shares = float(prevshares) + (float(request.POST.get('price')) / float(close))
        userStock.save()
        
        
        return redirect('stocks')

    context = {'stock':stock,}
    return render(request, 'base/buyStock.html', context)

@login_required(login_url='login')
def assets(request):
    user = request.user
    stocks = UserStock.objects.filter(user = user)
    properties = Property.objects.filter(user = user)
    items = Item.objects.filter(user = user)
    
    context = {'properties':properties, 'stocks':stocks, 'items':items}
    return render(request, 'base/assets.html', context)