from django import forms

class EmployeeForm(forms.Form):
    id=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control "}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        exp=cleaned_data.get("experience")
        if exp<0:
            msg="invalid exp"
            self.add_error("experience",msg)


class LoginForms(forms.Form):
    usrname=forms.CharField()
    pwd=forms.CharField()
class RegForm(forms.Form):
    f_name=forms.CharField()
    l_name=forms.CharField()
    email=forms.EmailField()

