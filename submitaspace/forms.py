from django import forms

from submitaspace.models import PlaceOwner

class ThePlaceOwner(forms.ModelForm):

    class Meta:
        model = PlaceOwner
        fields = [
         'type_of_location', 'location', 'nameofthelocation', 'websiteurl', 'address', 'seatingcapacity', 'thetime', 'thedays', 'name', 'lastname', 'phone_number', 'email', 'theways',
        ]

class SpaceSubmit(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)