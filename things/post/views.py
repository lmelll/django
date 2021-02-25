from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404, HttpResponse

from django.core.paginator import Paginator, EmptyPage

from post.models import Thing

from post.forms import ThingForm, SignupForm, LoginForm


from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User, AnonymousUser



def thing(request):
	if request.method == "POST":
		form =	ThingForm(request.POST)
		if form.is_valid():
			form._user= request.user
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ThingForm()
	return render(request, 'home.html', {'form': form, 'user': request.user, 'session':request.session,})
	
def delete(request, num):
	things = Thing(id=num)
	things.delete()
	return HttpResponseRedirect('/')
	
def update(request, num):
	thing = Thing.objects.get(id=num)
	if request.method == "POST":
		thing.text = request.POST.get("text")
		thing._user= request.user
		thing.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'update.html', {'thing':thing, 'user': request.user, 'session':request.session,})
	
	
	
	
	
	
	
	
def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {'author': request.user, 'things': paginate(request, Thing.objects.posts().filter(author = request.user)), 'user': request.user, 'session':request.session,})
	else:
		return HttpResponseRedirect('/login')
def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 5))
	except ValueError:
		limit = 5
	if limit > 5:
		limit = 5
	try:
		page = int(request.GET.get('page',1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page
	
	
	
def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form, 'user': request.user, 'session': request.session,})


def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data["username"]
			password = form.raw_passeord
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request, 'signup.html', {'form': form, 'user': request.user, 'session': request.session,})
