from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')
		

#custom validation
# def check_for_z(value):
# 	if value[0].lower() != 'z':
# 		raise forms.ValidationError("Name must start with z")



#class FormName(forms.Form):

	#custom validation
	# name = forms.CharField(validator=[check_for_z])

	# name = forms.CharField()
	# email = forms.CharField()
	# verify_email = forms.EmailField(label='Enter your email again!')
	# text = forms.CharField(widget= forms.Textarea)
	# botcatcher = forms.CharField(required = False,
	# 							 widget = forms.HiddenInput,
	# 							 validators = [validators.MaxLengthValidator(0)])

	#email matching
	# def clean(self):
	# 	all_clean_data = super().clean()
	# 	email = all_clean_data['email']
	# 	vmail = all_clean_data['verify_email']

	# 	if email != vmail:
	# 		raise forms.ValidationError('Make sure email match!')



	#botcatcher validation
	# def clean_botcatcher(self):
	# 	botcatcher = self.cleaned_data['botcatcher']
	# 	if len(botcatcher)>0:
	# 		raise forms.ValidationError("Got a Bot!")
	# 	return botcatcher