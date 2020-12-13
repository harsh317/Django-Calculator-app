from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello")


def calculator(request):
    return render(request, 'index.html')

def submit(request):
    query = request.GET['query']
    try:
        ans = eval(query)
        mydictionary = {
            'query':query,
            'ans':ans,
            'error':False
        }
        return render(request,'index.html',context=mydictionary)
    except:
        mydictionary = {
            'error': True
        }
        return render(request, 'index.html', context=mydictionary)