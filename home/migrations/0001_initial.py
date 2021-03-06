# Generated by Django 3.0.1 on 2021-11-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entered', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('form_open_timestamp', models.CharField(blank=True, max_length=100, null=True)),
                ('modified_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('assigned_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('mass_allocated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('mass_allocated_at', models.CharField(blank=True, max_length=100, null=True)),
                ('prop_id', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_id', models.CharField(blank=True, max_length=100, null=True)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('confirm_address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('preference', models.CharField(blank=True, max_length=100, null=True)),
                ('locality_name', models.CharField(blank=True, max_length=100, null=True)),
                ('locality_id', models.CharField(blank=True, max_length=100, null=True)),
                ('city_id', models.CharField(blank=True, max_length=100, null=True)),
                ('city_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_city', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.CharField(blank=True, max_length=100, null=True)),
                ('class1', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_count', models.CharField(blank=True, max_length=100, null=True)),
                ('activated', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('age_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('bedroom_num', models.CharField(blank=True, max_length=100, null=True)),
                ('building_id', models.CharField(blank=True, max_length=100, null=True)),
                ('PROPERTY_TYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('Property_Type_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('RES_COM', models.CharField(blank=True, max_length=100, null=True)),
                ('Transaction_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Transaction_Type_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('property_posting_date', models.CharField(blank=True, max_length=100, null=True)),
                ('acquired', models.CharField(blank=True, max_length=100, null=True)),
                ('recalled', models.CharField(blank=True, max_length=100, null=True)),
                ('caller_name', models.CharField(blank=True, max_length=100, null=True)),
                ('calling_date', models.CharField(blank=True, max_length=100, null=True)),
                ('follow_up_date', models.CharField(blank=True, max_length=100, null=True)),
                ('Disposition', models.CharField(blank=True, max_length=100, null=True)),
                ('final_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Comment', models.CharField(blank=True, max_length=100, null=True)),
                ('Attempts', models.CharField(blank=True, max_length=100, null=True)),
                ('Modified_By', models.CharField(blank=True, max_length=100, null=True)),
                ('language_used_on_call', models.CharField(blank=True, max_length=100, null=True)),
                ('Interested_for_Self_Verification', models.CharField(blank=True, max_length=100, null=True)),
                ('Ready_to_share_Images', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_verification_date', models.CharField(blank=True, max_length=100, null=True)),
                ('New_photo_count', models.CharField(blank=True, max_length=100, null=True)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('updatedAt', models.DateTimeField(blank=True, null=True)),
                ('Allocated_user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
