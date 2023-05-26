from django.urls import path
from csk.views import *
aap_name="anything"
urlpatterns = [
    path('msd/',msd, name='msd'),

]
 