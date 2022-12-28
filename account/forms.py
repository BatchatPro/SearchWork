from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import User

class EmployeeRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "Ism :"
        self.fields['last_name'].label = "Familya :"
        self.fields['password1'].label = "Parol :"
        self.fields['password2'].label = "Parol (qayta) :"
        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Jins :"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Ism kiriting',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Familya kiriting',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email kiriting',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Password kiriting',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Password (qayta) kiriting',
            }
        )

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Jins kiritish majburiy")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].label = "Kompaniya Nomi"
        self.fields['last_name'].label = "Kompaniya Manzili"
        self.fields['password1'].label = "Parol"
        self.fields['password2'].label = "Parol (qayta)"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Kompaniya Nomini kiriting',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Kompaniya Manzilini kiriting',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email kiriting',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Parol kiriting',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Parol (qayta kiriting)',
            }
        )
    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]


    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email =  forms.EmailField(
        widget=forms.EmailInput(attrs={ 'placeholder':'Email',})
    ) 
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={
        'placeholder':'Parol',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Foydalanuvchi mavjud emas.")

            if not user.check_password(password):
                raise forms.ValidationError("Parol Mos kelmaydi.")

            if not user.is_active:
                raise forms.ValidationError("Foydalanuvchi faol emas.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class EmployeeProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Ismingizni kiriting',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Familyangizni kiriting',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]
