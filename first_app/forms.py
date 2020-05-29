from django import forms
from django.contrib.auth.models import User
from first_app.models import user_signup,Post,Comment




class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    first_name=forms.CharField(max_length=264)
    last_name=forms.CharField(max_length=264)

    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')


class signupform(forms.ModelForm):
    Birth=forms.DateField(input_formats=['%Y-%m-%d','%m/%d/%Y','%d-%m-%Y','%d/%m/%Y','%d-%m-%y','%d/%m/%y'])
    class Meta():
        model=user_signup
        fields=('Mobile','Gender','Birth','propic')



class userform_update(forms.ModelForm):
    #password=forms.CharField(widget=forms.PasswordInput())
    first_name=forms.CharField(max_length=264)
    last_name=forms.CharField(max_length=264)

    class Meta():
        model=User
        fields=('first_name','last_name','username','email')


class signupform_update(forms.ModelForm):
    Birth=forms.DateField(input_formats=['%Y-%m-%d','%m/%d/%Y','%d-%m-%Y','%d/%m/%Y','%d-%m-%y','%d/%m/%y'])
    class Meta():
        model=user_signup
        fields=('Mobile','Gender','Birth','propic')



class signin(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField()



class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
