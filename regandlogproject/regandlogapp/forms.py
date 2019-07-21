from django import forms

class regform(forms.Form):
    firstname=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your first name'
            }
        )
    )
    lastname=forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your last name'
            }
        )
    )
    location=forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your location'
            }
        )
    )
    username=forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your username'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email id'

            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile No",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile'
            }
        )
    )

class loginform(forms.Form):
    username = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your username'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )





