from django.urls import path
from . import views
app_name='schoolapp'


urlpatterns = [
    path('',views.allcourses,name='allcourses'),
    path('<slug:c_slug>/',views.allcourses,name='courses_by_department'),
    path('<slug:c_slug>/<slug:course_slug>/', views.courseDetail, name='coursedetail'),
    path('registerlink',views.registerlink,name='registerlink'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),
    path('lastmsg',views.lastmsg,name='lastmsg'),
]