from .models import Phone
from django import forms

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'price', 'ram', 'info']
        labels = {'brand': '', 'model': '', 'price': '', 'ram': '', 'info': ''}
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Марка','style': 'width: 30rem;'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Модель','style': 'width: 30rem;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена','style': 'width: 30rem;'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ОЗУ','style': 'width: 30rem;'}),
            'info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Информация','style': 'width: 30rem;'}),
        }


    def clean_price(self):
        price = self.cleaned_data['price']
        
        if price < 0:
            raise forms.ValidationError('Цена должна быть больще 0')
        return price
     
    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram < 1:
            raise forms.ValidationError('ОЗУ должна быть больше 0')
        return ram
    
    def clean_info(self):
        info = self.cleaned_data['info']
        if len(info) < 10:
            raise forms.ValidationError('Информация должна быть больше 10 символов')
        return info
    
    def clean_model(self):
        model = self.cleaned_data['model']
        if len(model) < 3:
            raise forms.ValidationError('Модель должна быть больше 3 символов')
        return model
    
    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if len(brand) < 3:
            raise forms.ValidationError('Марка должна быть больше 3 символов')
        return brand
    
