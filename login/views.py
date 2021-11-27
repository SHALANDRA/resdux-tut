from django.conf import settings
from django.views.generic import TemplateView,View
from django.shortcuts import render,redirect
from .models import team_login
from django.http import HttpResponse


class Login_View(TemplateView):
    template_name='login_form.html'

    def get(self,request):
        request.session['login_details'] = {'email_id':'','password':''}
        return render(request,self.template_name,{'title':'Login Form'})

    def post(self,request):

        if request.POST.get("login", False)=='':
            email_id=request.POST['email']
            password=request.POST['password']
            
            if email_id==settings.ADMIN_EMAIL and password==settings.ADMIN_PASSWORD:
                request.session['login_details'] = {'email_id':email_id,'password':password}
                return redirect("admin_login")

            user=team_login.objects.filter(email=email_id,password=password)

            if len(user)<1 or user[0].status=="inactive":
                return render(request,self.template_name,{'login_error':True})

            request.session['login_details'] = {'email_id':email_id,'password':password}
            request.session['user_status']="create"
            return redirect("home")    
            #return HttpResponse(request.session['login_details']['email_id'])

                
            #table=team_login.
        elif request.POST.get("reset", False)=='':
            return render(request,'reset_password.html',{'title':'Reset Login Form'})

        elif request.POST.get("reset_password", False)=='':
            email_id=request.POST['email']
            old_password=request.POST['old_password']
            new_password=request.POST['new_password']
            renter_new_password=request.POST['renter_new_password']
            user=team_login.objects.filter(email=email_id)
            if len(user)<1:
                return render(request,'reset_password.html',{"no_email":True})

            elif old_password!=user[0].password:
                return render(request,'reset_password.html',{"no_password":True})

            elif new_password!=renter_new_password:
                return render(request,'reset_password.html',{"no_password_match":True})
            else:
                user[0].password=new_password
                user[0].save()
                return render(request,self.template_name,{'password_changed':True})    

        return render(request,self.template_name)
        
