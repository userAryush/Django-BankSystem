from django.urls import path
from bank_app.views import AccountViewSet, BankApiView

urlpatterns = [
   
    path('account/',AccountViewSet.as_view({'get':'list','post':'create'})),#class based ho view so as_view() garnei parxa also param halnu paro in {} jasma kk req garna paune mention garne
    path('account/<int:pk>/',AccountViewSet.as_view({'put':'update','delete':'destroy','get':'retrieve','post':'create'})),#retrive le euta matra data lyauxa 
    path('bank/',BankApiView.as_view())
]