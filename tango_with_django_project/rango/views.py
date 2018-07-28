from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context_dict={'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request,'rango/index.html',context=context_dict)
def about(request):
    return HttpResponse("here is about page!  let's go to <a href='/rango/index/'>index</a>")