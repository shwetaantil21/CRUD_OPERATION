
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Manage Employees"
admin.site.index_title = "Welcome to Employee Management System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Operation.urls'))
]
