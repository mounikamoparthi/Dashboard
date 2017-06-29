# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_login.models import User
from django.db import models
import bcrypt
# Create your models here.
class TravelManager(models.Manager):
    def addtrip(self,postData,sessiondata):
        print " In addtrip %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if not postData['Destination'] or len(postData['Destination'])<1:
            print "In validation1 "
            results['status'] = False
            results['errors'].append("Please enter a valid Destination")
            
        if not postData['Description'] or len(postData['Description'])<5:
            print "In validation2 "
            results['status'] = False
            results['errors'].append("Please enter a valid description")
            
        
            
        
        if results['status']:
            traveller1 = User.objects.get(id = sessiondata['id'])
            print traveller1
            trip1 = Trip.objects.create(trip_destination = postData['Destination'],trip_description = postData['Description'],travellers = traveller1)
            y =trip1.save()
            print y 
            print '&&&&&&&&&&&&&&&&&&&'
                #this_trip = Trip.objects.get(travellers_id = 1)
                #this_trip.save()

            results['status'] = True
        return results
       

class Trip(models.Model):
    trip_destination = models.CharField(max_length=100)
    trip_description = models.TextField(max_length=1000)
    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField(auto_now = True)
    travellers = models.ForeignKey('app_login.User', related_name="travellerss")
    objects= TravelManager()
