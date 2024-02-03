# customer
# admin
# driver
# superadmin


# admin.
# fleet_add/ get, post, put, delete

# add_driver/

#assign_tracker

#superadmin-> io

# list_admin/

# add_tracker



# raise qoute-- delhi to mumbai, con, material detail, 21jan,

# Trip_table- trip_status = requested, upcoming, ongoing

# admin_response --> 5000, 2day

# customer_quote: confirm_

# customer_pay_

#

# driver: trip_

# start_trip_



# design a model for tracking

# from django.db import models


# class User(models.Model):
#     email = models.EmailField(primary_key=True, max_length=100)
#     first_name = models.CharField(max_length=50, null=True, blank=True)
#     last_name= models.CharField(max_length=50, null=True, blank=True)
#     password = models.CharField(max_length=20)
#     role = models.CharField(max_length=100, choices= choices)

#     choices = (('customer', 'customer'),('admin','admin'),('driver','driver'),('superadmin','superadmin'))



# class TrackingDevice(models.Model):
#     admin  = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     device_id = models.CharField(max_length=20)

# class DeviceData(models.Model):
#     id = FADCDA10
#     lat =
#     long =
#     accelerometer=
#     batter_level =
#     trip_id =

# # customer raised quote,
# class Trip(models.Model):
#     id = uuid-
#     from =  locationA
#     destination = locarionB
#     customer = models.ForeignKey(User)
#     admin = models.ForeignKey(User)
#     driver = models.ForeignKey(User)
#     starttime = models.DateField
#     completed_date = models.DateField()
#     created_at = models.Datetime()

# class Fleet(models.Model):
#     id =
#     admin = models.ForeignKey(User, )
#     truck_no=
#     rc =
#     device_id =

# class AddDriver:
#     pass

# # list of all truck drivers travelled only once till now,
# # name, admin, truck_no, source, destination, datetravelled.

# # trips = 1-jan=2024, 16-jan-2024,


# trip_obj = Trip.objects.filter(starttime__lte=[16-jan-2024])

# # SQL


#**************************************
# 2nd round, abhinav, 03-Feb-2023 Sunday. Meenakshi HR

# monkey patching
# memory mangement in python
# scaling the System
# round robin
# difference between mvc and mvt











