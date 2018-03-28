import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tatu.models import *
from tatu.forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    context_dict = {'current': request.user}
    return render(request, 'tatu/index.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
            registered = True

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,
                  'tatu/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                    'registered': registered
                   })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'tatu/login.html', {})


def artists(request):
    return render(request,'tatu/artists.html',{})

def about(request):
    return render(request,'tatu/about.html',{})

def navigate(request):
    category_list = [ i[1].lower() for i in Post.CATEGORIES ]
    for category in category_list:
        print(category)
    return render(request,'tatu/navigate.html',{'category_list':category_list})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "tatu/contact.html", {'form': form})
  

    

def faq(request):
    context_dict = {}
    image_list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media'))[1:4]
    context_dict['images'] = image_list
    return render(request, 'tatu/faq.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_post(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user

            if 'image' in request.FILES:
                post.image = request.FILES['image']
                post.save()
            else:
                print(post_form.errors)
    else:
        post_form = PostForm()

    return render(request, 'tatu/upload.html', {'post_form': post_form
                                                })


#@login_required
#def submit_comment(request):
#    post = Post.objects.get(pk=1)
#    comments = post.comments.all()
#    #if request.method == 'POST':
#    #    comment_form = CommentForm(data=request.POST)
#    if request.method == 'POST':
#        comment_text = request.POST.get('the_comment')
#        response_data = {}
#        comment = Post(text=comment_text, author=request.user)
#        comment.save()
#        response_data['result'] = 'Create post successful!'
#        response_data['postpk'] = comment.pk
#        response_data['text'] = comment.text
#        response_data['created'] = comment.created.strftime('%B %d, %Y %I:%M %p')
#        response_data['author'] = comment.author.username
#        return HttpResponse(
#            json.dumps(response_data),
#            content_type="application/json"
#        )
#    else:
#        return HttpResponse(
#            json.dumps({"nothing to see": "this isn't happening"}),
#            content_type="application/json"
#        )


def successView(request):
    context_dict = {}
    return render(request, "tatu/success.html", context=context_dict)


# This is the main view for displaying posts for every category
@login_required
def tattoos(request, category):
    context_dict = {}

    # Get the enum name e.g. URL reads 'traditional' becomes enum name 'TRADITIONAL'
    category_enum = [ i[0] for i in Post.CATEGORIES if i[1] == category.title() ][0]

    # Get all the posts objects associated with this category (All posts made under Traditional
    # for example)
    img = Post.objects.all().filter(category=category_enum)

    # Get the current users User object
    current = request.user

    context_dict['current'] = current
    context_dict['img'] = img
    context_dict['category'] = category

    # If a POST request has been made and the POST data contains 'lke' in its keys 
    if request.method == 'POST' and any(item.startswith('lke') for item in list(request.POST.keys())):
        
        # Get the Post object number from the POST data that contains 'lke' and grab the number
        postnum = [i for i in list(request.POST.keys()) if i.startswith('lke')][0][3:]
        
        postobj = Post.objects.get(pk=postnum)

        new_like, created = Like.objects.get_or_create(user=request.user, post=postobj)
        if not created:
            print("Error like already made")
        else:
            postobj.likes = postobj.like_set.all().count()

    # If a POST request has been made a via a form
    if request.method == 'POST' and any(item.startswith('com') for item in list(request.POST.keys())):

        # Load the comment form with extra information from the POST data dictionary of the request
        comment_form = CommentForm(data=request.POST)

        # This searches the POST dictionary for the 3rd item, the name field of the 
        # <input type=submit ... button, and grabs it, which contains the post ID
        postnum = [i for i in list(request.POST.keys()) if i.startswith('com')][0][3:]

        # Get the Post object associated with the ID we just got, as that's the Post we want
        # to reply to
        postobj = Post.objects.get(pk=postnum)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            # Save the thread the comment is replying to to be the Post object
            comment.thread = postobj

            # Save the author of this comment to be the current user (specifically the UserProfile
            # Associated with that user, so that we can get avatars etc)
            comment.poster = request.user.userprofile
            comment.save()
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
        
    context_dict['comment_form'] = comment_form

    # SUM CRISSIE BS
    for i in img:
        i.coms = Comment.objects.all().filter(thread=i)
        i.likes = i.like_set.all().count()


    return render(request, 'tatu/category.html',
                  context=context_dict)


# This is the main view for displaying posts for every category
@login_required
def profile(request, userid):
    context_dict = {}

    # Get all the posts objects associated with this category (All posts made under Traditional
    # for example)
    userid = int(userid)
    img = Post.objects.all().filter(author__id=userid)
    profile = User.objects.get(id=userid)

    #print(type(userid))

    # Get the current users User object
    current = request.user
    #print(type(current.id))
        
    favs = current.userprofile.favourites.all()

    context_dict['favs'] = favs
    context_dict['current'] = current
    context_dict['img'] = img
    context_dict['userid'] = userid
    context_dict['profile']= profile

    if current.id != userid:
        other = UserProfile.objects.get(id=userid)
        context_dict['other'] = other

    if request.method == 'POST' and any(item.startswith('fav') for item in list(request.POST.keys())):
        new = UserProfile.objects.get(id=userid)
        current.userprofile.favourites.add(new) 

        

    # If a POST request has been made and the POST data contains 'lke' in its keys 
    if request.method == 'POST' and any(item.startswith('lke') for item in list(request.POST.keys())):
        
        print([i for i in list(request.POST.keys()) if i.startswith('lke')])
        # Get the Post object number from the POST data that contains 'lke' and grab the number
        postnum = [i for i in list(request.POST.keys()) if i.startswith('lke')][0][3:]
        print(postnum) 
        postobj = Post.objects.get(pk=postnum)

        new_like, created = Like.objects.get_or_create(user=request.user, post=postobj)
        if not created:
            print("Error like already made")
        else:
            postobj.likes = postobj.like_set.all().count()

    # If a POST request has been made a via a form
    if request.method == 'POST' and any(item.startswith('com') for item in list(request.POST.keys())):

        # Load the comment form with extra information from the POST data dictionary of the request
        comment_form = CommentForm(data=request.POST)

        # This searches the POST dictionary for the 3rd item, the name field of the 
        # <input type=submit ... button, and grabs it, which contains the post ID
        postnum = [i for i in list(request.POST.keys()) if i.startswith('com')][0][3:]

        # Get the Post object associated with the ID we just got, as that's the Post we want
        # to reply to
        postobj = Post.objects.get(pk=postnum)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            # Save the thread the comment is replying to to be the Post object
            comment.thread = postobj

            # Save the author of this comment to be the current user (specifically the UserProfile
            # Associated with that user, so that we can get avatars etc)
            comment.poster = request.user.userprofile
            comment.save()
        else:
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
        
    context_dict['comment_form'] = comment_form

    # SUM CRISSIE BS #lol mean u want sum fight
    for i in img:
        i.coms = Comment.objects.all().filter(thread=i)
        i.likes = i.like_set.all().count()


    return render(request, 'tatu/profile.html',
                  context=context_dict)

