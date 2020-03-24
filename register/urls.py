from django.urls import path
from .views import RegisterList, RegisterCreate, CharaCreate, WeaponCreate

urlpatterns = [
    path('list/', RegisterList.as_view(), name='list'),
    path('create/', RegisterCreate.as_view(), name='create'),
    path('ccreate/', CharaCreate.as_view(), name='characreate'),
    path('wcreate/', WeaponCreate.as_view(), name='weaponcreate')
]
