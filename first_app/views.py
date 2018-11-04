from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
from first_app.forms import UserForm,UserProfileInfoForm
from first_app import forms


from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # my_dict = {'insert_me':"Hello I am from views.py!"}
    # return render(request,'first_app/index.html',context=my_dict)

    # webpage_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_records':webpage_list}
    # return render(request,'first_app/index.html',context=date_dict)

    return render(request,'first_app/index.html')

def base(request):

    return render(request,'first_app/base.html')

# def form_name_view(request):

# 	form = forms.FormName()

# 	if request.method == 'POST':
# 		form = forms.FormName(request.POST)

# 		if form.is_valid():
# 			print('Validation Successful')
# 			print('Name: '+form.cleaned_data['name'])
# 			print('Email: '+form.cleaned_data['email'])
# 			print('Text: '+form.cleaned_data['text'])


# 	return render(request,'first_app/form_page.html',{ 'form':form })

def other(request):
	return render(request, 'first_app/other.html')

def relative(request):
	return render(request, 'first_app/relative_url_templates.html')

@login_required
def spacial(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponse(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/register.html', {'user_form':user_form,
                                                                'profile_form':profile_form,
                                                                'register':registered})




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username='username',password='password')

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not account')
        else:
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse('Invalid login details')
    else:
        return render(request,'first_app/login.html',{})