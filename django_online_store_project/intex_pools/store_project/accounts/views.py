import email
from django.conf import settings
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView, FormView, View
from accounts.forms import ForgotPasswordEmailForm, UserFormCreation, UserProfileView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
import secrets
from django.contrib.auth import get_user_model
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime ,timedelta
from django.http import JsonResponse, request
import requests
from django.utils import timezone
from . import models 
from django.contrib.auth.mixins import LoginRequiredMixin


from werkzeug.security import check_password_hash
from datetime import datetime, timedelta



          

        

class ChangePasswordView(LoginRequiredMixin,View):

    template_name = 'registration/change_password.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):


        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        user = request.user
        errors = {}
        if not old_password:
            errors['old_password'] = ["Old password is required"]
        if not new_password:
            errors['new_password'] = ["New password is required"]
        if not confirm_password:
            errors['confirm_password'] = ["Confirm password is required"] 
        if errors:
            return JsonResponse({
                "status": "error",
                "errors": errors
            })
        
        if user.check_password(old_password):
            if new_password == confirm_password:
                try:
                    validate_password(new_password, user)
                except ValidationError as error:
                    return JsonResponse({
                        "status": "error",
                        "errors": {
                            "new_password": list(error.messages)
                        }
                    })

                user.set_password(new_password)
                user.save()

                update_session_auth_hash(request, user)

                return JsonResponse({
                    "status": "success",
                    "redirect": "/"
                })
                
            else:
                response_data = {
                    "status": "error",
                    "email": None,
                    "errors": {
                        "confirm_password": ["Passwords do not match"]
                    }
                }
                return JsonResponse(response_data)
        else:
            response_data = {
                "status": "error",
                "email": None,
                "errors": {
                    "old_password": ["Old password is incorrect"]
                }
            }
            return JsonResponse(response_data)
        


    
def send_otp_email(from_email:str,to_email: str, code: str) -> bool:
    url = "https://api.brevo.com/v3/smtp/email" 

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json",
    }

    payload = {
        "sender": {
            "name": "intext",
            "email": from_email
        },
        "to": [
            {
                "email":to_email,
                "name": "User"
            }
        ],
        "subject": "hello i am yousef",
        "textContent": f"Your verification code is: {code}\nThis code expires in 5 minutes."
    }

    if not settings.BREVO_API_KEY:
        return False

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
    except requests.RequestException:
        return False

    return response.status_code in (200, 201)


    
@login_required
def EditProfile(request):
    
    if request.method == 'POST':
        
        form=UserProfileView(request.POST,instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
            
            
        
    else:
        form=UserProfileView(instance=request.user)
                        
        return render(request,'registration/profile.html',{
            'form':form
        })
        


class UserLoginView(LoginView):
    
    template_name = "registration/login.html"



# register view with otp code verification specially for registeration

class register_view(CreateView):
    form_class = UserFormCreation
    template_name = 'registration/register.html'

    def form_valid(self, form):

        email = form.cleaned_data.get("email")
        code = self.request.POST.get("code")


        verification = models.VerificationCode.objects.filter(
            email=email
        ).first()


        if not verification:
            response_data = {
                "status": "error",
                "email": None,
                "message": "verification code not found",
            }
            return JsonResponse(response_data)


        if not check_password_hash(verification.code, code):
            response_data = {
                "status": "error",
                "email": None,
                "message": "wrong code",
            }
            return JsonResponse(response_data)

            


        now = timezone.now()
        if now > verification.created_at + timedelta(minutes=5):
            verification.delete()
            response_data = {
                "status": "false",
                "email": None,
                "message": "code expired.",
            }
            return JsonResponse(response_data)

        models.VerificationCode.objects.filter(email=email).delete()



        return super().form_valid(form)


    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('store.home')




def otpcodeView(request):

    if request.method != 'POST':
        return JsonResponse({
            "status": "error",
            "message": "POST required"
        }, status=405)

    form = UserFormCreation(request.POST)
    print(1)
    if not form.is_valid():
        print(1.5)
        print(form.errors)
        return JsonResponse({
            "status": "error",
            "errors": form.errors
        })
    print(2)
    email = form.cleaned_data['email']

    user_exists = get_user_model().objects.filter(
        email=email
    ).exists()

    if user_exists:
    
        print('successfully_not2')
        
        
        
        response_data = {
            "status": "error",
            "email": None,
            "errors": {
                "email": ["email was used"]
            }
        }
        return JsonResponse(response_data)
    else:
        otp_code = f"{secrets.randbelow(1000000):06d}"
        print(otp_code)
        new_otp_hash=generate_password_hash(otp_code)

        row=models.VerificationCode.objects.filter(email=email).values('created_at')

    

        now = timezone.now()

        print('problem in update otp code')
        if row:
            created_at = row[0]["created_at"]

            if now < created_at + timedelta(minutes=2):
                response_data = {
                    "status": "error",
                    "errors": {
                        "otp_code": ["Wait 2 minutes before retrying"]
                    }
                }
                return JsonResponse(response_data)


            models.VerificationCode.objects.filter(email=email).update(
                code=new_otp_hash,
                created_at=now
            )
            
        else:
            print('problem in insert otp code')
            
            models.VerificationCode.objects.create(email=email, code=new_otp_hash, created_at=now)
            

        print('problem in send email')

        if not send_otp_email('yousefmahmoud2y1@gmail.com', email, otp_code):
            return JsonResponse({
                "status": "error",
                "message": "Unable to send the verification email. Please try again later."
            }, status=502)

        response_data = {
            "status": "successfully",
            "email": email,
            "message": "we are send the code",

        }
        print('successfully')
        return JsonResponse(response_data)







    
# forgot password view , otp code view specifically for forgot password


class ForgotPasswordView(View):

    template_name = 'registration/forgot_password.html'
    

    
    def get(self, request):

        return render(request, self.template_name)


    def post(self, request):

        email = request.POST.get("email")
        code = request.POST.get("code")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        if new_password != confirm_password:
            response_data = {
                "status": "error",
                "email": None,
                "errors": {
                    "confirm_password": ["Passwords do not match"]
                }
            }
            return JsonResponse(response_data)
        
        
        
        verification = models.VerificationCode.objects.filter(
            email=email
        ).first()
        
        user = get_user_model().objects.filter(email=email).first()
        if not user:
            return JsonResponse({
                "status": "error",
                "errors": {"email": ["User not found"]}
            })
        

        if not verification:
            response_data = {
                "status": "error",
                "email": None,
                "message": "verification code not found",
            }
            return JsonResponse(response_data)



        if not check_password_hash(verification.code, code):
            response_data = {
                "status": "error",
                "email": None,
                "message": "wrong code",
            }
            return JsonResponse(response_data)
        
        
        

        now = timezone.now()
        if now > verification.created_at + timedelta(minutes=5):
            verification.delete()
            response_data = {
                "status": "error",
                "errors": {
                    "code": ["code expired"]
                }
            }
            return JsonResponse(response_data)

        


        user.set_password(new_password)
        user.save()
        print('successfully changed password')
        

        if request.user.is_authenticated and request.user.pk == user.pk:
            update_session_auth_hash(request, user)
            redirect_url = "/"
        else:
            redirect_url = "/accounts/login/"

        return JsonResponse({
            "status": "success",
            "redirect": redirect_url
        })
        
        
        
        
        
      

def OtpcodeViewForgotPassword(request):

    if request.method != 'POST':
        return JsonResponse({
            "status": "error",
            "message": "POST required"
        }, status=405)

    form = ForgotPasswordEmailForm(request.POST)
    print(1)
    if not form.is_valid():
        print(1.5)
        print(form.errors)
        return JsonResponse({
            "status": "error",
            "errors": form.errors
        })
    print(2)
    email = form.cleaned_data['email']

    user_exists = get_user_model().objects.filter(
        email=email
    ).exists()

    if not user_exists:
    

        
        
        
        response_data = {
            "status": "error",
            "errors": {
                "email": ["email was not found"]
            }
        }
        return JsonResponse(response_data)
    else:
        otp_code = f"{secrets.randbelow(1000000):06d}"
        print(otp_code)
        new_otp_hash=generate_password_hash(otp_code)

        row=models.VerificationCode.objects.filter(email=email).values('created_at')

    

        now = timezone.now()

        print('problem in update otp code')
        if row:
            created_at = row[0]["created_at"]

            if now < created_at + timedelta(minutes=2):
                response_data = {
                    "status": "error",
                    "errors": {
                        "otp_code": ["Wait 2 minutes before retrying"]
                    }
                }
                return JsonResponse(response_data)


            models.VerificationCode.objects.filter(email=email).update(
                code=new_otp_hash,
                created_at=now
            )
            
        else:
            print('problem in insert otp code')
            
            models.VerificationCode.objects.create(email=email, code=new_otp_hash, created_at=now)
            

        print('problem in send email')
        try:
                
            send_otp_email('yousefmahmoud2y1@gmail.com', email, otp_code)
            response_data = {
                "status": "successfully",
                "email": email,
                "message": "we are send the code",

            }
        except Exception as e:
            response_data = {
                "status": "error",
                "message": f"Unable to send the verification email. Please try again later."
            }
            return JsonResponse(response_data, status=502)
        print('successfully')
        return JsonResponse(response_data)







    
    # models.VerificationCode.insert(email=email,code=enc_code)



    