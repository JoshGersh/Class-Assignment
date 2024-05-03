from django import forms
from .models import student, teacher

class AddStudentForm(forms.ModelForm):
    
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

    reading    = forms.IntegerField(min_value=0, max_value=99,required=True, widget=forms.widgets.NumberInput(attrs={ "class":"form-control"}))
    writing    = forms.IntegerField(min_value=0, max_value=99,required=True, widget=forms.widgets.NumberInput(attrs={ "class":"form-control"}))
    math       = forms.IntegerField(min_value=0, max_value=99,required=True, widget=forms.widgets.NumberInput(attrs={ "class":"form-control"}))
    behavioral = forms.IntegerField(min_value=0, max_value=99,required=True, widget=forms.widgets.NumberInput(attrs={ "class":"form-control"}))
    
    class Meta:
        model = student
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'reading', 'writing', 'math', 'behavioral']
    
    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].label = ''

        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].label = ''

        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].label = ''

        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['city'].label = ''

        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['state'].label = ''

        self.fields['zipcode'].widget.attrs['class'] = 'form-control'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
        self.fields['zipcode'].label = ''

        self.fields['reading'].widget = forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 99})
        self.fields['reading'].label = 'Reading Score'
        self.fields['reading'].help_text = '<div class="d-flex justify-content-between"><label for="0%" class="align-self-start">0%</label> <label for="100%" class="align-self-end">100%</label></div>'

        self.fields['writing'].widget = forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 99})
        self.fields['writing'].label = 'Writing Score'
        self.fields['writing'].help_text = '<div class="d-flex justify-content-between"><label for="0%" class="align-self-start">0%</label> <label for="100%" class="align-self-end">100%</label></div>'

        self.fields['math'].widget = forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 99})
        self.fields['math'].label = 'Math Score'
        self.fields['math'].help_text = '<div class="d-flex justify-content-between"><label for="0%" class="align-self-start">0%</label> <label for="100%" class="align-self-end">100%</label></div>'

        self.fields['behavioral'].widget = forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': 0, 'max': 99})
        self.fields['behavioral'].label = 'Behavioral Score'
        self.fields['behavioral'].help_text = '<div class="d-flex justify-content-between"><label for="0%" class="align-self-start">0%</label> <label for="100%" class="align-self-end">100%</label></div>'

class AddTeacherForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    students = None


    class Meta:
        model = teacher
        fields = ['first_name', 'last_name'] 
    
    def __init__(self, *args, **kwargs):
        super(AddTeacherForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''