import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page 

def populate():

	python_pages = [
		{"title":"Official Python Tutorial",
		"url":"https://docs.python.org/2/tutorial"},
		{"title":"How to Think like a Computer Scientist",
		"url":"http://www.greenteapress.com/thnikpython/"},
		{"title":"Learn Python in 10 Minutes",
		"url":"http://www.korokithakis.net/tutorials/python/"}
	]

	django_pages = [
		{"title":"Official Django Tutorial",
		"url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
		{"title":"Django Rocks",
		"url":"http://www.djangorocks.com/"},
		{"title":"How to Tango with Django",
		"url":"http://www.tangowithdjango.com/"}
	]

	other_pages = [
		{"title":"Bottle",
		"url":"https://bottlepy.org/docs/dev/"},
		{"title":"Flask",
		"url":"http://flask.pocoo.org/"}
	]

	cats = {"Python": {"pages":python_pages},
			"Django": {"pages":django_pages},
			"Other frameworks":{"pages":other_pages}}


	for cat, cat_data in cats.items():
		c = add_cat(cat)
		for p in cat_data["pages"]:
			add_page(c, p["title"],p["url"])

	for c in Category.objects.all():
		for p in Page.objects.filter(category = c):
			print("- {0} - {1}".format(str(c),str(p)))

	page1 = Page.objects.get(title = 'Bottle')
	page1.views = 6
	page1.save()

	page2 = Page.objects.get(title = 'Flask')
	page2.views = 5
	page2.save()

	page3 = Page.objects.get(title = 'Official Django Tutorial')
	page3.views = 4
	page3.save()

	page4 = Page.objects.get(title = 'Django Rocks')
	page4.views = 3
	page4.save()

	
	cate = Category.objects.get(name = 'Python')
	cate.views = 128
	cate.likes = 64
	cate.save()

	categ = Category.objects.get(name = 'Django')
	categ.views = 128
	categ.likes = 64
	categ.save()

	categ1 = Category.objects.get(name = 'Other frameworks')
	categ1.views = 128
	categ1.likes = 64
	categ1.save()



def add_page(cat, title, url, views = 0):
	p = Page.objects.get_or_create(category = cat, title = title)[0]
	p.url = url
	p.views = views
	p.save()
	return p
def add_cat(name):
	c = Category.objects.get_or_create(name = name)[0]
	c.save()
	return c

if __name__ == '__main__':
	print("Starting Rango population script....")
	populate()