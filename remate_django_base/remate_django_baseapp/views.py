from django.shortcuts import render
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
from .models import Customer,MenuItem,OrderDate
from .forms import NewCustomerForm, UserForm,UserProfileInfoForm

def index(request):
    my_dict = {'example_tag':'Hello I am from remate_django_baseapp/index.html en views.py within remate_django_baseapp'}
    return render(request,'remate_django_baseapp/index.html',context=my_dict)# Create your views here.

@login_required
def other(request):
    # return render(request,'remate_django_baseapp/other.html')
    form = NewCustomerForm()
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'remate_django_baseapp/other.html',{'form':form})

@login_required
def customers(request):
    customer_list = Customer.objects.order_by('customer_name')
    customer_dict = {"customers":customer_list}
    return render(request,'remate_django_baseapp/customers.html',context=customer_dict)
    #return render(request,'remate_django_baseapp/customers.html')

# def user_login(request):
#     return HttpResponse('<em><h1>not implemented!</h1></em>')
#     #
#     # Hello World
#     #
#     #return HttpResponse('<em><h1>Hello World!</h1></em>')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'remate_django_baseapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'remate_django_baseapp/login.html', {})


#
# def index(request):
#     menuitems_list = OrderDate.objects.order_by('date')
#     date_dict = {"order_records":menuitems_list}
#     return render(request,'remate_django_baseapp_app/index.html',date_dict)
