from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.views import View
from home.models import crms
import io,csv
class EmployeeUploadView(View):
    def get(self, request):
        template_name = 'importfarmer.html'
        return render(request, template_name)
    def post(self, request):
        user = request.user #get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            crms(
            modified_user_id=row['modified_user_id'],
description=row['description'],
assigned_user_id=row['assigned_user_id'],
mass_allocated_by=row['mass_allocated_by'],
mass_allocated_at=row['mass_allocated_at'],
prop_id=row['prop_id'],
profile_id=row['profile_id'],
client_name=row['client_name'],
mobile=row['mobile'],
confirm_address=row['confirm_address'],
preference=row['preference'],
locality_name=row['locality_name'],
locality_id=row['locality_id'],
email=row['email'],
city_id=row['city_id'],
city_name=row['city_name'],
parent_city=row['parent_city'],
price=row['price'],
paid=row['paid'],
class1=row['class1'],
photo_count=row['photo_count'],
activated=row['activated'],
age=row['age'],
age_Name=row['age_Name'],
bedroom_num=row['bedroom_num'],
building_id=row['building_id'],
PROPERTY_TYPE=row['PROPERTY_TYPE'],
Property_Type_Name=row['Property_Type_Name'],
RES_COM=row['RES_COM'],
Transaction_Type=row['Transaction_Type'],
Transaction_Type_Name=row['Transaction_Type_Name'],
property_posting_date=row['property_posting_date'],
acquired=row['acquired'],
recalled=row['recalled'],
caller_name=row['caller_name'],
calling_date=row['calling_date'],
follow_up_date=row['follow_up_date'],
Disposition=row['Disposition'],
final_status=row['final_status'],
Comment=row['Comment'],
Attempts=row['Attempts'],
Modified_By=row['Modified_By'],
language_used_on_call=row['language_used_on_call'],
Interested_for_Self_Verification=row['Interested_for_Self_Verification'],
Ready_to_share_Images=row['Ready_to_share_Images'],
actual_verification_date=row['actual_verification_date'],
New_photo_count=row['New_photo_count'],
Allocated_user=row['Allocated_user'],

           
         )
         for row in list_of_dict
     ]
        try:
            msg = crms.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}
       
        return JsonResponse(returnmsg)