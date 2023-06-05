from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'myapp'
urlpatterns = [
    path('', Test.as_view(), name='Test'),
    path('BuyerView/', BuyerView.as_view(), name='BuyerView'),
    path('StyleView/', StyleView.as_view(), name='StyleView'),
    path('ProductionLineView/', ProductionLineView.as_view(), name='ProductionLineView'),
    path('OrderQtyView/<int:id>/', OrderQtyView.as_view(), name='OrderQtyView'),
    path('SaveOrderQty/', SaveOrderQty.as_view(), name='SaveOrderQty'),
    path('OrederCMPreportView/', OrederCMPreportView.as_view(), name='OrederCMPreportView'),
    path('OrderQtyDetailView/<int:id>/',OrderQtyDetailView.as_view(), name='OrderQtyDetailView'),
    path('EditOrderQtyView/<int:pk>', EditOrderQtyView.as_view(), name='EditOrderQtyView'),
    path('ETAView/', ETAView.as_view(), name='ETAView'),

    path('ProductionInputView/', ProductionInputView.as_view(), name='ProductionInputView'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)