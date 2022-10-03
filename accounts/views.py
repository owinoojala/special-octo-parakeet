from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from .tokens import TokenGenerator
from eshopper.views import p_method,address
from django.conf import settings


generate_token = TokenGenerator()
# TO BE MODIFED
def register(request):
    context = {'pay_m': p_method, 'address':address}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email  = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "User already exists, enter your details to log in")
                return redirect('login')
            elif User.objects.filter(username=user_name):
                messages.error(request, f'Username {user_name} already taken')
                return redirect('register')
            else:
                user = user = User.objects.create_user(user_name, email, password1)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = False
                user.save()
                messages.success(request, "Registration was successful," +
                             " click the link sent in your email to verify" + 
                             " your email")

                # Verification email
                send_verification_email(request, user)
                return redirect('login')
        else:
            messages.error(request, 'Passwords are not matching')
            return redirect('register')
    else:
        return render(request, 'accounts/registration.html', context)


# send verification email
def send_verification_email(request, user):
    current_site = get_current_site(request)
    email_subject = 'Verify Email'
    message = render_to_string('accounts/verify.html',
                {
                'name':user.first_name,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)
                })
    email = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                        )
    email.fail_silently=True
    email.send()

# Verify email      
def verify(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoeNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save
        login(request, user)
        return redirect('/') 
    else:
        return render(request, 'accounts/activation_failed.html')   
# Login
def login(request):
    context = {'pay_m': p_method, 'address':address}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'User does not exist or wrong credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html', context)
#Logout
def logout(request):
    auth.logout(request)
    return redirect('/')