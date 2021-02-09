from django.shortcuts import render, redirect
from . models import Category, Photo

def gallery(request):
	category = request.GET.get('category')
	if category == None:
		photos = Photo.objects.all()
	else:
		photos = Photo.objects.filter(category__name=category)	
		

	categories = Category.objects.order_by('name')
	context = {
		'categories': categories,
		'photos': photos,
	}
	return render(request, 'photos/gallery.html', context)


def addPhoto(request):
	categories = Category.objects.all()
	if request.method == 'POST':
		data = request.POST
		images = request.FILES.getlist('images')

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])
		elif data['category_new'] != '':
			category, created = Category.objects.get_or_create(name=data['category_new'])
		else:
			category = None
		for image in images:	
			photo = Photo.objects.create(category=category, description=data['description'], image=image)
		return redirect('gallery')			
	context = {
		'categories': categories,
	}
	return render(request, 'photos/add.html', context)

def viewPhoto(request, pk):
	photo = Photo.objects.get(id=pk)
	context = {
		'photo': photo,
	}
	return render(request, 'photos/photo.html', context)	


def search(request):
	qs = Photo.objects.all()
	# if 'keywords' in request.GET:
	# 	keywords = request.GET['keywords']
	# 	if keywords:
	# 		qs = qs.filter(description__icontains=keywords)
	if request.method == 'GET':
		keywords = request.GET.get('keywords')
		photos  = Photo.objects.filter(description__icontains=keywords)
	return render(request, 'photos/search.html', {'photos': photos})			