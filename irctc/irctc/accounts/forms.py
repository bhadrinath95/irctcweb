from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Booking, Person
from country_list import countries_for_language

User = get_user_model()

class BookingForm(forms.ModelForm):
    source = forms.CharField( widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'From Station'}))
    destination = forms.CharField( widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'To Station'}))
    train_number = forms.CharField( widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Train Number'}))
    class_choices = (
        ("All Classes","All Classes"),
        ("Anubhuti Class (EA)","Anubhuti Class (EA)"),
        ("AC First Class (1A) ","AC First Class (1A) "),
        ("Exec. Chair Car (EC)","Exec. Chair Car (EC)"),
        ("AC 2 Tier (2A)","AC 2 Tier (2A)"),
        ("First Class (FC)","First Class (FC)"),
        ("AC 3 Tier (3A)","AC 3 Tier (3A)"),
        ("AC 3 Economy (3E)","AC 3 Economy (3E)"),
        ("AC Chair car (CC)","AC Chair car (CC)"),
        ("Sleeper (SL)","Sleeper (SL)"),
        ("Second Sitting (2S)","Second Sitting (2S)"),
        )
    travel_class =forms.CharField(  widget= forms.Select(choices=class_choices,attrs={'class':'form-control'}))
    travel_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control'}))
    irctc_username = forms.CharField( widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Irctc Username *'}))
    irctc_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Irctc Password *'}))
    destination_address =forms.CharField(  widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 1 *'}))
    destination_address_2 =forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 2 (Optional)'}), required=False)
    destination_address_3 =forms.CharField(  widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 3 (Optional)'}), required=False)
    destination_pin =forms.CharField(  widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'PIN *'}))
    destination_state =forms.CharField( widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'State *'}))
    destination_city =forms.CharField(  widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'City *'}))
    destination_post_office =forms.CharField(  widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Post Office *'}))
    class_payoption = (
        ("",""),
        ("IRCTC iPay (Credit Card/Debit Card/UPI)","IRCTC iPay (Credit Card/Debit Card/UPI)"),
        ("Multiple Payment Service","Multiple Payment Service"),
        ("Debit Card with PIN","Debit Card with PIN"),
        ("Netbanking","Netbanking"),
        ("Wallets / Cash Card","Wallets / Cash Card"),
        ("Pay-On-Delivery/Pay later","Pay-On-Delivery/Pay later"),
        ("Payment Gateway / Credit Card / Debit Card","Payment Gateway / Credit Card / Debit Card"),
        )
    class_paymethod = (
        ("Credit cards/ Debit cards / UPI (Powered by IRCTC)","Credit cards/ Debit cards / UPI (Powered by IRCTC)"),
        ("International cards (Powered by ATOM)","International cards (Powered by ATOM)"),
        ("Credit & Debit cards / Net Banking / Wallet (Powered by Paytm)","Credit & Debit cards / Net Banking / Wallet (Powered by Paytm)"),
        ("Credit & Debit cards / Net Banking / Wallet (Powered by EBIX)","Credit & Debit cards / Net Banking / Wallet (Powered by EBIX)"),
        ("Credit & Debit cards /Net Banking/Wallets/UPI/ International Cards (Powered by PayU)","Credit & Debit cards /Net Banking/Wallets/UPI/ International Cards (Powered by PayU)"),
        ("Credit & Debit cards / Net Banking / UPI (Powered by Razorpay)","Credit & Debit cards / Net Banking / UPI (Powered by Razorpay)"),
        ("Credit & Debit cards / Wallet / UPI (Powered by PhonePe)","Credit & Debit cards / Wallet / UPI (Powered by PhonePe)"),
        ("Amazon Pay Wallet (Powered by Amazon)","Amazon Pay Wallet (Powered by Amazon)"),
        ("State Bank of India","State Bank of India"),
        ("Federal Bank","Federal Bank"),
        ("HDFC Bank","HDFC Bank"),
        ("United Bank of India","United Bank of India"),
        ("Union Bank of India","Union Bank of India"),
        ("Indian Bank","Indian Bank"),
        ("Punjab National Bank","Punjab National Bank"),
        ("Allahabad Bank","Allahabad Bank"),
        ("Bank of Baroda","Bank of Baroda"),
        ("AXIS Bank","AXIS Bank"),
        ("Karnataka Bank","Karnataka Bank"),
        ("Oriental Bank of Commerce","Oriental Bank of Commerce"),
        ("ICICI Bank","ICICI Bank"),
        ("IndusInd Bank","IndusInd Bank"),
        ("Kotak Mahindra Bank","Kotak Mahindra Bank"),
        ("Central Bank of India","Central Bank of India"),
        ("Bank of Maharashatra","Bank of Maharashatra"),
        ("Corporation Bank","Corporation Bank"),
        ("Yes Bank","Yes Bank"),
        ("Nepal SBI Bank Ltd.","Nepal SBI Bank Ltd."),
        ("South Indian Bank","South Indian Bank"),
        ("City Union Bank","City Union Bank"),
        ("Canara Bank","Canara Bank"),
        ("Airtel Payments Bank","Airtel Payments Bank"),
        ("IDFC FIRST Bank","IDFC FIRST Bank"),
        ("Mobikwik Wallet","Mobikwik Wallet"),
        ("Paytm Wallet","Paytm Wallet"),
        ("Freecharge Wallet","Freecharge Wallet"),
        ("Airtel Money","Airtel Money"),
        ("I Cash Card","I Cash Card"),
        ("ePaylater (Powered by Arthashastra Fintech Pvt. Ltd.)","ePaylater (Powered by Arthashastra Fintech Pvt. Ltd.)"),
        ("Visa/Master Card(Powered By HDFC BANK)","Visa/Master Card(Powered By HDFC BANK)"),
        ("American Express","American Express"),
        ("Visa/Master Card(Powered By ICICI BANK)","Visa/Master Card(Powered By ICICI BANK)"),
        ("Visa/Master/RuPay Card (Powered by KOTAK BANK)","Visa/Master/RuPay Card (Powered by KOTAK BANK)"),
        )
    
    payoption =forms.CharField(widget= forms.Select(choices=class_payoption,attrs={'class':'form-control'}))
    paymethod =forms.CharField(widget= forms.Select(choices=class_paymethod,attrs={'class':'form-control'}))
    
    
    class Meta:
        model = Booking
        fields = [
                "source",
                "destination",
                "train_number",
                "travel_class",
                "travel_date",
                "irctc_username",
                "irctc_password",
                "destination_address",
                "destination_address_2",
                "destination_address_3",
                "destination_pin",
                "destination_state",
                "destination_city",
                "destination_post_office",
                "payoption",
                "paymethod",
            ]
        
class UserLoginForm(forms.Form):
    username = forms.CharField( widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username= username, password= password)
            if not user:
                raise  forms.ValidationError("User does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
            if not user.is_active:
                raise forms.ValidationError("User is not longer active.")
            
        return super(UserLoginForm, self).clean(*args, **kwargs)
        
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Person Name *'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter Password *'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm Password *'}), label='Confirm Password')
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder': 'emailaddress@domain.com *'}), label='Email Address')
    
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password',
                'password2',
            ]
        
    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')
        if password != password2:
            raise forms.ValidationError('Password must match.')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has already registered.')
        return super(UserRegisterForm, self).clean(*args, **kwargs)
    
class CreateNewList(forms.ModelForm):
    person_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder': 'Person Name *'}))
    person_age = forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter Age *'}))
    class_preference = (
        ("No Preference*","No Preference*"),
        ("Lower","Lower"),
        ("Middle","Middle"),
        ("Upper","Upper"),
        ("Side Lower","Side Lower"),
        ("Side Upper","Side Upper"),
        )
    class_gender = (
        ("Male","Male"),
        ("Female","Female"),
        ("Transgender","Transgender"),
        )
    countries = countries_for_language('en')
    
    gender =forms.CharField(  widget= forms.Select(choices=class_gender,attrs={'class':'form-control'}))
    preference =forms.CharField(  widget= forms.Select(choices=class_preference,attrs={'class':'form-control'}))
    nationality =forms.CharField(  widget= forms.Select(choices=countries,attrs={'class':'form-control'}), initial='IN')
    
    class Meta:
        model = Person
        fields = [
                "person_name",
                "person_age",
                "gender",
                "preference",
                "nationality",
            ]
    