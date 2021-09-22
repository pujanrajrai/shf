from django.contrib import messages, auth
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import RegisterForm
from .models import MyUser
from .utlis import generate_token
from django.contrib.auth.decorators import login_required


# Create your views here.

#
# def send_activation_email(user, request):
#     current_site = get_current_site(request)
#     email_subject = "Complete your registration"
#     email_body = render_to_string(
#         "accounts/activate.html",
#         {
#             "user": user,
#             "domain": current_site,
#             "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#             "token": generate_token.make_token(user),
#         },
#     )
#
#     email = EmailMessage(
#         subject=email_subject,
#         body=email_body,
#         to=[
#             user.email,
#         ],
#     )
#
#     email.send()

#
# def register(request):
#     if request.method == "POST":
#         fm = RegisterForm(request.POST)
#         if fm.is_valid():
#             first_name = fm.cleaned_data["first_name"]
#             middle_name = fm.cleaned_data["middle_name"]
#             last_name = fm.cleaned_data["last_name"]
#             address = fm.cleaned_data["address"]
#             email = fm.cleaned_data["email"]
#             password = fm.cleaned_data["password"]
#
#             user = MyUser(
#                 first_name=first_name,
#                 last_name=last_name,
#                 middle_name=middle_name,
#                 address=address,
#                 email=email,
#                 password=password,
#             )
#             user.set_password(password)
#             user.save()
#             send_activation_email(user, request)
#             messages.success(
#                 request,
#                 "User registration successful, an email has been sent to you,"
#                 " Verify to login.",
#             )
#         else:
#             messages.error(request, "registration failed, try again.")
#     return render(request, "accounts/register.html")

#
# def activate_user(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = MyUser.objects.get(pk=uid)
#
#     except Exception as e:
#         user = None
#
#     if user and generate_token.check_token(user, token):
#         user.is_email_verified = True
#         user.save()
#         messages.success(request, "Email verified, login to continue.")
#         return HttpResponse('email verified')
#     else:
#         return render(request, "accounts/activate-failed.html", {"user": user})


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard:dashboard")
        else:
            errors = "User name or password is incorrect"
            return render(request, 'accounts/login.html', {"errors": errors})
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home:home')

#
# @login_required()
# def loggedin(request):
#     return redirect("dashboard:blog")
