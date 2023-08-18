from django.urls import re_path
from Employee import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^result$',views.resultAPI),
    re_path(r'^result/([0-9]+)$',views.resultAPI),
    
    re_path(r'^user$',views.UserAPI),
    re_path(r'^user/([0-9]+)$',views.UserAPI),
    
    re_path(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)