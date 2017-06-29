# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_login.models import User
from .models import Trip
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    print "fghjk"
    #Trip.objects.all().delete()
    context = {
        "trips": Trip.objects.all(),
        "name": request.session['first_name'],
        
    }
    print context
    return render(request,'app_travel/index.html',context)



def addtrip(request):
    #Trip.objects.all().delete()
    print request.method
    if request.method == "POST":
        print request.method
        context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
        }
        print context
        result = Trip.objects.addtrip(request.POST,context)
        print result
        if not result['status']:
            print "dfghjkl" 
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            return redirect(reverse('travels:addtrip'))
        else: 
            print "dfghjkl"
            messages.success(request,"Successful")
            return redirect(reverse('travels:index'))
 
    else:
            print "ENTERED GET"   
    return render(request,'app_travel/addtrip.html')

def showtrip(request,id):
    print request.method
    if request.method == "POST":
        context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id'],
                "tripid" : id
                }
        
        result = Trip.objects.destination(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
                return redirect(reverse('travels:showtrip',kwargs={'id': id}))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('travels:showtrip',kwargs={'id': id}))
    else:
        context = {
        'bookdata' :Book.objects.get(id=id),
        'authordata' :Author.objects.get((bookauthor__id)=id),
        'reviewdata' :Review.objects.filter((bookreview__id)=id),
        'userid':request.session['user_id']

        }
        #return redirect(reverse('show',kwargs={'id':id}))
        return render(request,'app_travels/showtrip.html', context)
        

