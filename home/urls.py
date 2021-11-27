from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   
    #path('addshow',views.add_show,name='addshow'),
    #path('delete/<int:id>/',views.delete_data,name='deletedata'),
    #path('',views.Home_View.as_view,name='home'),
    path('',views.Home_View.as_view(),name='home'),

    path('updatedata/<int:id>/',views.UpdateData_View.as_view(),name='updatedata'),
    path('logout/',views.LogoutView.as_view(),name='logout')
]


  