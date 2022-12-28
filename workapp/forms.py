from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from workapp.models import *
from ckeditor.widgets import CKEditorWidget
    

class JobForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Ish Sarlavhasi :"
        self.fields['location'].label = "Ish Joylashuvi :"
        self.fields['salary'].label = "Maosh :"
        self.fields['description'].label = "Ish Haqida To'liq Ma'lumot :"
        self.fields['tags'].label = "Teglar :"
        self.fields['last_date'].label = "Ariza topshirishning oxirgi muddati :"
        self.fields['company_name'].label = "Kampaniya nomi :"
        self.fields['url'].label = "Vebsayt :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun : Web Dasturchi',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun : Toshkent',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun $400 - $1000',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Vergul bilan ajrating. Misol uchun: Python, JavaScript ',
            }
        )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-OO-KK ',
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Kampaniya Nomi',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    


    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            
            job.save()
        return job


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']


class JobEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Ish Sarlavhasi :"
        self.fields['location'].label = "Ish Joylashuvi :"
        self.fields['salary'].label = "Maosh :"
        self.fields['description'].label = "Ish Haqida To'liq Ma'lumot :"
        # self.fields['tags'].label = "Teglar :"
        self.fields['last_date'].label = "Tugatish muddati :"
        self.fields['company_name'].label = "Kampaniya nomi :"
        self.fields['url'].label = "Vebsayt :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun : Web Dasturchi',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun : Toshkent',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'Misol uchun $400 - $1000',
            }
        )
        # self.fields['tags'].widget.attrs.update(
        #     {
        #         'placeholder': 'Vergul bilan ajrating. Misol uchun: Python, JavaScript ',
        #     }
        # )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-OO-KK ',
            }
        )        
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Kampaniya Nomi',
            }
        )           
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )   

        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
            ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Job Type is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category


    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
      
        if commit:
            job.save()
        return job

