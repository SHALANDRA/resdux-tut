from django.conf import settings
from django.db.models import query
from django.views.generic import TemplateView,View
from django.shortcuts import render,redirect
from .models import crms
from login.models import team_login
import pdb
from django.core.paginator import Paginator
import re,os,time,datetime, json
from .forms import StudentRegistration
from django.contrib.auth import logout




class Home_View(TemplateView):
    template_name='home.html'

    def get(self,request):
        #request.session['login_details'] = {'email_id':'','password':''}
        try:
            email_id=request.session['login_details']['email_id']
        except:
            return redirect("login")
        #column='id,modified_user_id'
        #crm_data=crms.objects.values_list('id', flat=True).filter(Allocated_user=email_id)
        crm_data=crms.objects.all().filter(Allocated_user=email_id)
        paginator = Paginator(crm_data, 50) # Show 25 contacts per page
        #pdb.set_trace()
        print(crm_data.query)
        page = request.GET.get('page')
        crm_data_inpage = paginator.get_page(page)
        #pdb.set_trace()
        #return render(request,self.template_name,{'dataframe':crm_data_inpage})
        return render(request, self.template_name, {'dataframe':crm_data_inpage,'title':'Data List'})

    def post(self,request):

        if request.POST.get("edit", False)=='':
            uniqueid=request.POST['uniqueid']
            pi=crms.objects.filter(id=uniqueid)
            fm=StudentRegistration(request.POST,instance=pi)
            return redirect(self.request,'update.html',{'form':fm})

class UpdateData_View(TemplateView):
    template_name='update1.html'
    
    def post(self,request,id):
        
        if 'Update' in request.POST:
            uniqueid=request.POST['uniqueid']
            #user=crms.objects.filter(id=uniqueid)
            
            
            modified_user_id=request.POST['modified_user_id']
            description=request.POST['description']
            assigned_user_id=request.POST['assigned_user_id']
            mass_allocated_by=request.POST['mass_allocated_by']
            mass_allocated_at=request.POST['mass_allocated_at']
            prop_id=request.POST['prop_id']
            profile_id=request.POST['profile_id']
            client_name=request.POST['client_name']
            mobile=request.POST['mobile']
            confirm_address=request.POST['confirm_address']
            preference=request.POST['preference']
            locality_name=request.POST['locality_name']
            locality_id=request.POST['locality_id']
            email=request.POST['email']
            city_id=request.POST['city_id']
            city_name=request.POST['city_name']
            parent_city=request.POST['parent_city']
            price=request.POST['price']
            paid=request.POST['paid']
            class1=request.POST['class1']
            photo_count=request.POST['photo_count']
            activated=request.POST['activated']
            age=request.POST['age']
            age_Name=request.POST['age_Name']
            bedroom_num=request.POST['bedroom_num']
            building_id=request.POST['building_id']
            PROPERTY_TYPE=request.POST['PROPERTY_TYPE']
            Property_Type_Name=request.POST['Property_Type_Name']
            RES_COM=request.POST['RES_COM']
            Transaction_Type=request.POST['Transaction_Type']
            Transaction_Type_Name=request.POST['Transaction_Type_Name']
            property_posting_date=request.POST['property_posting_date']
            acquired=request.POST['acquired']
            recalled=request.POST['recalled']
            caller_name=request.POST['caller_name']
            calling_date=request.POST['calling_date']
            follow_up_date=request.POST['follow_up_date']
            Disposition=request.POST['Disposition']
            final_status=request.POST['final_status']
            Comment=request.POST['Comment']
            Attempts=request.POST['Attempts']
            Modified_By=request.POST['Modified_By']
            language_used_on_call=request.POST['language_used_on_call']
            Interested_for_Self_Verification=request.POST['Interested_for_Self_Verification']
            Ready_to_share_Images=request.POST['Ready_to_share_Images']
            actual_verification_date=request.POST['actual_verification_date']
            New_photo_count=request.POST['New_photo_count']
            #createdAt=request.POST['createdAt']
            #updatedAt=request.POST['updatedAt']
            Allocated_user=request.POST['Allocated_user']
            '''crms1=crms(modified_user_id=modified_user_id,description=description,assigned_user_id=assigned_user_id,mass_allocated_by=mass_allocated_by,mass_allocated_at=mass_allocated_at,prop_id=prop_id,profile_id=profile_id,client_name=client_name,mobile=mobile,confirm_address=confirm_address,preference=preference,locality_name=locality_name,locality_id=locality_id,email=email,city_id=city_id,city_name=city_name,parent_city=parent_city,price=price,paid=paid,class1=class1,photo_count=photo_count,activated=activated,age=age,age_Name=age_Name,bedroom_num=bedroom_num,building_id=building_id,PROPERTY_TYPE=PROPERTY_TYPE,
            Property_Type_Name=Property_Type_Name,RES_COM=RES_COM,Transaction_Type=Transaction_Type,Transaction_Type_Name=Transaction_Type_Name,property_posting_date=property_posting_date,acquired=acquired,recalled=recalled,caller_name=caller_name,calling_date=calling_date,follow_up_date=follow_up_date,Disposition=Disposition,final_status=final_status,Comment=Comment,Attempts=Attempts,Modified_By=Modified_By,language_used_on_call=language_used_on_call,Interested_for_Self_Verification=Interested_for_Self_Verification,
            Ready_to_share_Images=Ready_to_share_Images,actual_verification_date=actual_verification_date,
            New_photo_count=New_photo_count,Allocated_user=Allocated_user)'''
            
            crms.objects.filter(id=uniqueid).update(modified_user_id=modified_user_id,description=description,assigned_user_id=assigned_user_id,mass_allocated_by=mass_allocated_by,mass_allocated_at=mass_allocated_at,prop_id=prop_id,profile_id=profile_id,client_name=client_name,mobile=mobile,confirm_address=confirm_address,preference=preference,locality_name=locality_name,locality_id=locality_id,email=email,city_id=city_id,city_name=city_name,parent_city=parent_city,price=price,paid=paid,class1=class1,photo_count=photo_count,activated=activated,age=age,age_Name=age_Name,bedroom_num=bedroom_num,building_id=building_id,PROPERTY_TYPE=PROPERTY_TYPE,
            Property_Type_Name=Property_Type_Name,RES_COM=RES_COM,Transaction_Type=Transaction_Type,Transaction_Type_Name=Transaction_Type_Name,property_posting_date=property_posting_date,acquired=acquired,recalled=recalled,caller_name=caller_name,calling_date=calling_date,follow_up_date=follow_up_date,Disposition=Disposition,final_status=final_status,Comment=Comment,Attempts=Attempts,Modified_By=Modified_By,language_used_on_call=language_used_on_call,Interested_for_Self_Verification=Interested_for_Self_Verification,
            Ready_to_share_Images=Ready_to_share_Images,actual_verification_date=actual_verification_date,
            New_photo_count=New_photo_count,Allocated_user=Allocated_user)

            return redirect("home")
        #crm_data=crms.objects.get(pk=id)
        #pi=crms.objects.get(pk=1)
        else:
            uniqueid=request.POST['uniqueid']
            fm=crms.objects.filter(id=uniqueid)
        #pdb.set_trace()

        #fm=StudentRegistration(request.POST,instance=pi)
            return render(self.request,self.template_name,{'form':fm,'title':'Edit Form'})
    

class LogoutView(View):
    def get(self, request):
        #request.session.flush()
        #logout(request)
        try:
            #del request.session['member_id']
            del request.session['login_details']
        except KeyError:
            pass
        return redirect("/")