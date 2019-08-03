from django import forms

from post.models import Thing

class ThingForm(forms.Form):
	text =forms.CharField(label = 'Добавить новое дело', widget=forms.Textarea(attrs={'rows':35, 'cols':185,}))
	def clean(self):
			pass
	def save(self, *args, **kwargs):
		thing = Thing(**self.cleaned_data)
		thing.save()
		return thing


# from django.forms import ModelForm
# from django import forms

# from .models import Thing

# class ThingForm(ModelForm):
	# class Meta:
		# model = Thing
		# fields = ['text']

	# def clean(self):
		# return super(ThingForm, self).clean()


	# def save(self):
		# thing = Thing(**self.cleaned_data)
		# thing.save()
		# return thing