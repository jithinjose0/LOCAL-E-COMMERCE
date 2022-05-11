from django import forms
from django.contrib.auth.models import User
from .models import *

class shopUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-con trol','placeholder':'Conform Password'}), required=True)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password', 'confirm_password']

    def clean(self):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        cleaned_data=super(shopUserForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        username =cleaned_data.get('username')

        if len(username) < 8:
            self.add_error('username','Username length must be greater than 8 character.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if len(password)  < 8:
            self.add_error('password','Password length must be greater than 8 character.')
        if not any (char.isdigit() for char in password):
            self.add_error('password','Password must contain at least one digit.')
        if not any (char in special_characters for char in password):
            self.add_error('password','Password must contain at least one special Character.')

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not Match")

        return cleaned_data

class shopExtraForm(forms.ModelForm):
    shop_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter shop Name'}), required=True)
    place_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter place Name'}), required=True)
    licenseno = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter license number'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}), required=True)
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Pincode'}), required=True)
    #district = forms.ModelChoiceField(queryset=District.objects.all(),widget=forms.Select(attrs={'class':'form-control'}), empty_label="---Select District---", required=True)

    class Meta:
        model=shop_user
        fields=[ 'pincode','email','shop_name','place_name','licenseno']

#<-----Visistor Login Form----->#
class shopLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}), required=True)
from store.models.product import Products
class productform(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'