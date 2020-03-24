from django.urls import path
from .views import RegisterList, RegisterCreate, CharaCreate, WeaponCreate, RegisterDetail, RegisterUpdate,RegisterDelete

urlpatterns = [
    path('list/', RegisterList.as_view(), name='list'),
    path('create/', RegisterCreate.as_view(), name='create'),
    path('ccreate/', CharaCreate.as_view(), name='characreate'),
    path('wcreate/', WeaponCreate.as_view(), name='weaponcreate'),
    path('detail/<int:pk>', RegisterDetail.as_view(), name='detail'),
    path('update/<int:pk>', RegisterUpdate.as_view(), name='update'),
    path('delete/<int:pk>', RegisterDelete.as_view(), name='delete'),
]
