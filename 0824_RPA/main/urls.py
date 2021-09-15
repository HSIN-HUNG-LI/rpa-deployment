from django.urls import path
from main import views

# SET THE NAMESPACE!
#Globle name
app_name = 'main'

urlpatterns=[
	path('',views.index,name='index'),
	path('introduction/',views.introduction,name='introduction_2'),
	path('introduction_demo/',views.introduction_demo,name='introduction_demo'),
	path('tool',views.Tool_View.as_view(),name='tool'),
	path('contect_us/',views.contect_us,name='contect_us'),
]
