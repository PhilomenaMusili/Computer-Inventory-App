from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address', 'users_name', 'location', 'purchase_date']
def clean_computer_name(self): # Validates the Computer Name Field
	computer_name = self.cleaned_data.get('computer_name')
	if (computer_name == ""):
		raise forms.ValidationError('This field cannot be left blank')
	return computer_name
def clean_IP_address(self): 
	IP_address = self.cleaned_data.get('IP_address')
	if (IP_address == ""):
		raise forms.ValidationError('This field cannot be left blank')
	return IP_address
class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'users_name']
