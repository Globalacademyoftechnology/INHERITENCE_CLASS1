from django.urls import path
app_name="MYAPP"
from MYAPP import views

urlpatterns=[

    path('',views.child,name="child"),
]
