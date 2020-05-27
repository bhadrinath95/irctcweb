from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from country_list import countries_for_language
from datetime import datetime


# Create your models here.
# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.DO_NOTHING)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
    source = models.CharField(max_length=120)
    destination = models.CharField(max_length=120) 
    travel_date = models.DateField(auto_now=False, auto_now_add=False)
    travel_class = models.CharField(max_length=120)
    train_number = models.CharField(max_length=120)
    destination_address = models.CharField(max_length=120)
    destination_address_2 = models.CharField(max_length=120, blank=True)
    destination_address_3 = models.CharField(max_length=120, blank=True)
    destination_pin = models.CharField(max_length=120)
    destination_state = models.CharField(max_length=120)
    destination_city = models.CharField(max_length=120)
    destination_post_office = models.CharField(max_length=120)
    irctc_username = models.CharField(max_length=30)
    irctc_password = models.CharField(max_length=30)
    
    payoption = models.CharField(max_length=120)
    paymethod = models.CharField(max_length=120)
    
    def __str__(self):
        return self.user.username
    
def get_irctcpay_strings():
    irctcpay_strings = [
        "Credit cards/ Debit cards / UPI (Powered by IRCTC)",
        ]
    return irctcpay_strings 

def get_multiplepay_strings():
    multiplepay_strings = [
        "International cards (Powered by ATOM)",
        "Credit & Debit cards / Net Banking / Wallet (Powered by Paytm)",
        "Credit & Debit cards / Net Banking / Wallet (Powered by EBIX)",
        "Credit & Debit cards /Net Banking/Wallets/UPI/ International Cards (Powered by PayU)",
        "Credit & Debit cards / Net Banking / UPI (Powered by Razorpay)",
        "Credit & Debit cards / Wallet / UPI (Powered by PhonePe)",
        "Amazon Pay Wallet (Powered by Amazon)",
        ]
    return multiplepay_strings

def get_netbanking_strings():
    netbanking_strings = [
        "State Bank of India",
        "Federal Bank",
        "Union Bank of India",
        "Indian Bank",
        "Punjab National Bank",
        "Allahabad Bank",
        "Bank of Baroda",
        "AXIS Bank",
        "Karnataka Bank",
        "Oriental Bank of Commerce",
        "ICICI Bank",
        "IndusInd Bank",
        "Kotak Mahindra Bank",
        "Central Bank of India",
        "Bank of Maharashatra",
        "Corporation Bank",
        "Yes Bank",
        "Nepal SBI Bank Ltd.",
        "South Indian Bank",
        "City Union Bank",
        "Canara Bank",
        "Airtel Payments Bank",
        "IDFC FIRST Bank",
        ]
    return netbanking_strings

def get_debitbanking_strings():
    debitbanking_strings = [
        "HDFC Bank","United Bank of India",
        ]
    return debitbanking_strings

def get_walletsbanking_strings():
    walletsbanking_strings = [
        "Mobikwik Wallet","Paytm Wallet","Freecharge Wallet","Airtel Money","I Cash Card",
        ]
    return walletsbanking_strings

def get_podbanking_strings():
    podbanking_strings = [
        "ePaylater (Powered by Arthashastra Fintech Pvt. Ltd.)",
        ]
    return podbanking_strings

def get_gatewaybanking_strings():
    gatewaybanking_strings = [
        "Visa/Master Card(Powered By HDFC BANK)","American Express","Visa/Master Card(Powered By ICICI BANK)","Visa/Master/RuPay Card (Powered by KOTAK BANK)",
        ]
    return gatewaybanking_strings
    
class Person(models.Model):
    booking = models.ForeignKey(Booking, on_delete= models.DO_NOTHING)
    person_name = models.CharField(max_length=120)
    person_age = models.IntegerField()
    gender = models.CharField(max_length=120)
    preference = models.CharField(max_length=120,default="No Preference*")
    nationality = models.CharField(max_length=120,default="IN")
    
class BookingStatus(models.Model):
    booking = models.ForeignKey(Booking, on_delete= models.DO_NOTHING)
    completion_status = models.BooleanField(default=False)
    status = models.CharField(max_length=120)