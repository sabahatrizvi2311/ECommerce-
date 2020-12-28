from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.views import View
from django.contrib import messages


from .forms import CreateUserForm
from .models.products import Product
from .models.category import Categorie
from .models.customer import Customer
# Create your views here.


def registerPage(request):
	
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(
				user=user,
				)

			messages.success(request, 'Account created for ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request,'stores/register.html',context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			request.session['user'] = user.id

			return redirect('home')
		else:
			messages.info(request, 'Username of Passwod is incorrect')

	context = {}
	return render(request,'stores/login.html',context)
	

def logoutUser(request):
	logout(request)
	return redirect('login')

class Index(View):
	def post(self, request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			
			if quantity:
				if remove:
					if quantity<=1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		request.session['cart'] = cart
		print(cart)
		return redirect('home')


	def get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		products = None
		categories = Categorie.objects.all()
		categoryID = request.GET.get('category')
		if categoryID:
			products = Product.get_all_products_by_categoryid(categoryID)
		else:
			products = Product.objects.all()
		context = {'products': products, 'categories': categories, 'categoryID':categoryID}
		return render(request, 'stores/index.html', context)


def prodview(request, myid):
	product = Product.objects.filter(id=myid)
	context = {'product':product[0]}
	return render(request, 'stores/prodview.html', context)

class Cart(View):
	def get(self, request):
		ids = list(request.session.get('cart').keys())
		products = Product.get_products_by_id(ids)
		context = {'products': products}
		return render(request, 'stores/cart.html', context)