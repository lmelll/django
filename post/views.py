from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from post.models import Thing
from post.forms import ThingForm

def thing(request):
	if request.method == "POST":
		form =	ThingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ThingForm()
	return render(request, 'post.html', {'form': form,})
	
def delete(request, num):
	things = Thing(id=num)
	things.delete()
	return HttpResponseRedirect('/')
	
def update(request, num):
	thing = Thing.objects.get(id=num)
	if request.method == "POST":
		thing.text = request.POST.get("text")
		thing.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'update.html', {'thing':thing,})
	
	
	
	
	
	
	
	
def home(request):
	return render(request, 'home.html', {'things': paginate(request, Thing.objects.posts()),})

def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 10:
		limit = 10
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