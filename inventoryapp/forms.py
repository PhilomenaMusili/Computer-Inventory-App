from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'operating_system','IP_address', 'MAC_address', 'users_name', 'location', 'purchase_date']

    def clean_computer_name(self):  # Validates the Computer Name Field
        computer_name = self.cleaned_data.get('computer_name')
        if computer_name == "":
            raise forms.ValidationError('This field cannot be left blank')
        
        for instance in Computer.objects.all():
            if instance.computer_name == computer_name:
                raise forms.ValidationError('There is a computer with the name {}'.format(computer_name))
        
        return computer_name

    def clean_IP_address(self): 
        IP_address = self.cleaned_data.get('IP_address')
        if IP_address == "":
            raise forms.ValidationError('This field cannot be left blank')
        for instance in Computer.objects.all():
            if instance.IP_address == IP_address:
                raise forms.ValidationError('There is a computer with the Ip Address {}'.format(IP_address))
        
        return IP_address

    def clean_users_name(self): 
        users_name = self.cleaned_data.get('users_name')
        if users_name == "":
            raise forms.ValidationError('This field cannot be left blank')
        for instance in Computer.objects.all():
            if instance.users_name == users_name:
                raise forms.ValidationError('There is a computer with the username {}'.format(users_name))
                
        return users_name    

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'users_name', 'export_to_CSV']
