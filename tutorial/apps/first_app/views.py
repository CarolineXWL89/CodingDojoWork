from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#the index function is called when when root page is visited
def index(response):
	response = "Hello, I am your first request!"
	return HttpResponse(response)

def test(response):
	response = "Hello, I am Test No. 1!"
	return HttpResponse(response)