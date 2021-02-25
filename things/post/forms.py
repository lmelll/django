from django import forms

from post.models import Thing

from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

class ThingForm(forms.Form):
	text =forms.CharField(label = 'Add new case', widget=forms.TextInput())
	def clean(self):
			pass
	def save(self, *args, **kwargs):
		thing = Thing(**self.cleaned_data)
		thing.author_id = self._user.id
		thing.save()
		return thing


		
class SignupForm(forms.Form):
	username=forms.CharField()
	email=forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError('Email empty')
		return email
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError('Username empty')
##		except User.DoesNotExist:
#			pass
		return username
	def clean_password(self):
		password = self.cleaned_data.get('password')
		if not password:
			raise forms.ValidationError('Password empty')
		self.raw_passeord = password
		return make_password(password)

	def save(self):
		user = User(**self.cleaned_data)
		user.save()
		return user


class LoginForm(forms.Form):
	username =forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError('Username empty')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password')
		if not password:
			raise forms.ValidationError('Password empty')
		return password

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError('try again')
		if not user.check_password(password):
			raise forms.ValidationError('try again')