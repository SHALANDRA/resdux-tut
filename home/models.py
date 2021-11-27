from django.db import models
from django.contrib import admin

# Create your models here.
class crms(models.Model):
    date_entered=models.DateTimeField(null=True,blank=True) 
    date_modified=models.DateTimeField(null=True,blank=True)
    form_open_timestamp=models.CharField(max_length=100,null=True,blank=True)
    modified_user_id=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    assigned_user_id=models.CharField(max_length=100,null=True,blank=True)
    mass_allocated_by=models.CharField(max_length=100,null=True,blank=True)
    mass_allocated_at=models.CharField(max_length=100,null=True,blank=True)
    prop_id=models.CharField(max_length=100,null=True,blank=True)
    profile_id=models.CharField(max_length=100,null=True,blank=True)
    client_name=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True,blank=True)
    confirm_address=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    preference=models.CharField(max_length=100,null=True,blank=True)
    locality_name=models.CharField(max_length=100,null=True,blank=True)
    locality_id=models.CharField(max_length=100,null=True,blank=True)
    city_id=models.CharField(max_length=100,null=True,blank=True)
    city_name=models.CharField(max_length=100,null=True,blank=True)
    parent_city=models.CharField(max_length=100,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)
    paid=models.CharField(max_length=100,null=True,blank=True)
    class1=models.CharField(max_length=100,null=True,blank=True)
    photo_count=models.CharField(max_length=100,null=True,blank=True)
    activated=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=100,null=True,blank=True)
    age_Name=models.CharField(max_length=100,null=True,blank=True)
    bedroom_num=models.CharField(max_length=100,null=True,blank=True)
    building_id=models.CharField(max_length=100,null=True,blank=True)
    PROPERTY_TYPE=models.CharField(max_length=100,null=True,blank=True)
    Property_Type_Name=models.CharField(max_length=100,null=True,blank=True)
    RES_COM=models.CharField(max_length=100,null=True,blank=True)
    Transaction_Type=models.CharField(max_length=100,null=True,blank=True)
    Transaction_Type_Name=models.CharField(max_length=100,null=True,blank=True)
    property_posting_date=models.CharField(max_length=100,null=True,blank=True)
    acquired=models.CharField(max_length=100,null=True,blank=True)
    recalled=models.CharField(max_length=100,null=True,blank=True)
    caller_name=models.CharField(max_length=100,null=True,blank=True)
    calling_date=models.CharField(max_length=100,null=True,blank=True)
    follow_up_date=models.CharField(max_length=100,null=True,blank=True)
    Disposition=models.CharField(max_length=100,null=True,blank=True)
    final_status=models.CharField(max_length=100,null=True,blank=True)
    Comment=models.CharField(max_length=100,null=True,blank=True)
    Attempts=models.CharField(max_length=100,null=True,blank=True)
    Modified_By=models.CharField(max_length=100,null=True,blank=True)
    language_used_on_call=models.CharField(max_length=100,null=True,blank=True)
    Interested_for_Self_Verification=models.CharField(max_length=100,null=True,blank=True)
    Ready_to_share_Images=models.CharField(max_length=100,null=True,blank=True)
    actual_verification_date=models.CharField(max_length=100,null=True,blank=True)
    New_photo_count=models.CharField(max_length=100,null=True,blank=True)
    Allocated_user=models.CharField(max_length=100,null=True,blank=True)
    #created_at = models.DateTimeField(editable=False)
    #updated_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.profile_id


    
            
    

