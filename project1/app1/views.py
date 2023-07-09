from django.shortcuts import render

from django.http import HttpResponse

def vidya(request):
    print("hi bro")
    return HttpResponse('vidya is called and sagar also bro so sorry')


def chaitu(request):
    return HttpResponse('chaitu is called so')




def chaitu1(request):
    return HttpResponse('chaitu1 is called')



def chaitu2(request):
    return HttpResponse('chaitu2 is called')