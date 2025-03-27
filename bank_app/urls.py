from django.urls import path
from bank_app.views import AccountViewSet, BankApiView, BankApiViewDetails,StatementApiViewSet,register,login,group_list

urlpatterns = [
   
    path('account/',AccountViewSet.as_view({'get':'list','post':'create'})),#class based ho view so as_view() garnei parxa also param halnu paro in {} jasma kk req garna paune mention garne
    path('account/<int:pk>/',AccountViewSet.as_view({'put':'update','delete':'destroy','get':'retrieve','post':'create'})),#retrive le euta matra data lyauxa 
    path('bank/',BankApiView.as_view()),
    path('bank/<int:pk>/',BankApiViewDetails.as_view()),
    path('statement/',StatementApiViewSet.as_view({'get':'list','post':'create'})),
    path('statement/<int:pk>/',StatementApiViewSet.as_view({'put':'update','delete':'destroy','get':'retrieve','post':'create'})),
    path('register/',register),
    path('login/',login),
    path('group/',group_list)
]