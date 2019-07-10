from django.urls import path
from . import views
app_name = 'voice'
urlpatterns = [
    path('compose/',views.Vocie_Compose_View.as_view(),name='compose')
    ]