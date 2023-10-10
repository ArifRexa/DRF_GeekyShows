from django.contrib import admin
from django.urls import path
from api import views
from DeSerialization_and_Insert_Data import views as deView
from CRUD_Api import views as CView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student_info/', views.student_detail),
    path('student_info/<int:pk>', views.student_detail),
    path('all/', views.student_list),
    path('stucreate/', deView.student_create),
    path('stuapi/', CView.student_api),
]
