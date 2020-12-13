from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('calculator',views.calculator,name="calculator"),
    path('submit',views.submit,name="submit"),
]