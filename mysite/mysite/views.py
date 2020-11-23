
# def index(requests):
#     return(HttpResponse("hello dosto chai pilo"))
# from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

def navigation(request):
    djtext=request.GET.get('text','default')
    rp=request.GET.get('n','off')
    ucr=request.GET.get('uppercaseremover','off')
    if rp=="on":
        punctuations='''!()-[] {};:'"\,<>./?@#$%^&*_~'''
        ans=""
        for char in djtext:
            if char not in punctuations:
                ans=ans+char
        para={'personal':'removed punctuations','analysed_text':ans}
    elif ucr=="on" :
        analysed=""
        for i in djtext:
            i=i.upper()
            analysed=analysed+i
        para={'personal':'uppercaseremover','analysed_text':analysed}
        return render(request, 'analysed.html', para)
    else:
        return HttpResponse("error")

def index(request):
    return render(request,'file.html')

