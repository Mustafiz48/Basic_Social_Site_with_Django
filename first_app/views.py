from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from first_app import forms
from first_app.forms import signupform,signin,userform,userform_update,signupform_update,HomeForm,CommentForm
from first_app.models import user_signup,User,Friend,Post
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:home'))


pro=0


class HomeView(TemplateView):
    template_name = 'first_app/friends.html'

    def get(self, request):
        user = User.objects.exclude(username=request.user.username)

        friend=None
        friends=None

        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friend = None
            friends = None

        args = {
             'users': user,'friends':friends,'pro':pro,
        }
        return render(request, self.template_name, args)

@login_required
def posts(request,post, pk):
    post=Post.objects.get(pk=pk)


    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('first_app:feed')
    else:
        form = CommentForm()

    return render(request,'first_app/posts.html',{'form': form,'post':post})

def index(request):
    # user=user_signup.objects.get(username=username)
    # users = User.objects.exclude(id=request.user.id)
    # friend = Friend.objects.filter(current_user=request.user)
    # try:
    #     friends = friend.users.all()
    # except ObjectDoesNotExist:
    #     friends = None
    return render(request,'first_app/home.html',)

def navbar(request):
    return render(request,'first_app/navbar.html',)

def login2(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # print("Login successful")
                messages.success(request, "Logged in Successfully!")
                return HttpResponseRedirect(reverse('first_app:home'))


            else:
                return HttpResponse("Acount not Active")
        else:
            print("Anauthorised Entry")
            return HttpResponse("Invalid login request")
    else:
        return render(request,'first_app/login2.html')


def signup2(request):

    registred=False

    if request.method =="POST":
        user_form=userform(data=request.POST)
        signup_form=signupform(data=request.POST)

        if user_form.is_valid() and signup_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=signup_form.save(commit=False)
            profile.user=user

            if 'propic' in request.FILES:
                profile.propic=request.FILES['propic']
            else:
                print("No Images Found!")






            profile.save()

            registred=True
            # return render(request,'first_app/signup.html')

        else:
                print(user_form.errors,signup_form.errors)


    else:
        user_form=userform()
        signup_form=signupform()

    return render(request,'first_app/signup2.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred}
                                )


@login_required
def profee(request, proo, pk):
    friend = User.objects.get(pk=pk)
    request.session['friend']=pk

    return redirect('first_app:Friend_profile',)


@login_required
def feed(request):
    posts_a=Post.objects.all().order_by('-created')
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    users=User.objects.exclude(username=request.user.username)
    form = HomeForm(request.POST)
    text=0
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        text = form.cleaned_data['post']
        form = HomeForm()
        return redirect('first_app:home')

    args = {'form': form, 'text': text,'posts_a':posts_a,'friends':friends,'users':users,}


    return render(request,'first_app/feed.html',args)


@login_required
def profile(request):
    me=User.objects.all()
    person=user_signup.objects.all()


    return render(request,'first_app/profile.html',{'me':me})

@login_required
def Friend_profile(request):
    pk=request.session['friend']
    friend = User.objects.get(pk=pk)
    user=friend
    request.session.pop('friend', None)
    request.session.modified = True
    return render(request,'first_app/friends_profile.html',{'user':user})



def signup(request):

    registred=False

    if request.method =="POST":
        user_form=userform(data=request.POST)
        signup_form=signupform(data=request.POST)

        if user_form.is_valid() and signup_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=signup_form.save(commit=False)
            profile.user=user

            if 'propic' in request.FILES:
                profile.propic=request.FILES['propic']
            else:
                print("No Images Found!")






            profile.save()

            registred=True
            # return render(request,'first_app/signup.html')

        else:
                print(user_form.errors,signup_form.errors)


    else:
        user_form=userform()
        signup_form=signupform()

    return render(request,'first_app/signup.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred}
                                )

@login_required
def profile_update(request):

    if request.method == "POST":

        user_update=userform_update(request.POST, instance=request.user)
        signup_update=signupform_update(request.POST,request.FILES, instance=request.user.user_signup)

        if user_update.is_valid() and signup_update.is_valid():
            user_update.save()
            #user.save()

            signup_update.save()

            #profile.save()
            messages.success(request,'Your profile has been Updated Successfully')
            return render(request,'first_app/home.html')

        else:
                print(user_update.errors,signup_update.errors)


    else:
        user_update=userform_update(request.POST, instance=request.user)
        signup_update=signupform_update(request.POST,request.FILES, instance=request.user.user_signup)

    return render(request,'first_app/profile_update.html',
                            {'user_update':user_update,
                             'signup_update':signup_update}
                                )




def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # print("Login successful")
                messages.success(request, "Logged in Successfully!")
                return HttpResponseRedirect(reverse('first_app:home'))


            else:
                return HttpResponse("Acount not Active")
        else:
            print("Anauthorised Entry")
            return HttpResponse("Invalid login request")
    else:
        return render(request,'first_app/login.html')


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('link:first_app')


def add_comment_to_post(request, pk):


    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('link:feed', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'first_app/feed.html', {'form': form})
