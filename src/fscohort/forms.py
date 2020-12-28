from django import forms
from django.forms import fields
from .models import Student

# class StudentForm(forms.Form):
#     first_name= forms.CharField(max_length=50, label="Your name")
#     last_name= forms.CharField(max_length=50, label="Your surname")
#     number = forms.IntegerField()

class StudentForm(forms.ModelForm):
    #first_name = forms.CharField(label="Your name")
    class Meta:
        model = Student
        fields = "__all__" #("first_name", "last_name", "number")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label= "YOUR NAME"
        # this is equal at the top of this class commet row