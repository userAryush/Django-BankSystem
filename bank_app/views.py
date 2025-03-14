from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #API ma hune sab logic cha
from rest_framework.generics import GenericAPIView # yesma API banauda chai sabei logic affei banauna paro
from rest_framework.response import Response
from .models import Account, Bank
from .serializers import AccountSerializer,BankSerializer
# Create your views here.




#Frontend le API bata communicate garxa to do CRUD operation in backend
#so API ma CRUD ko logic huna paro
# frontend tells through request what operation to perform,, method(GET->data magne kam,PUT-> update garne,POST-> create garne,DELETE->delete garxa)

#API using ModelViewSet
class AccountViewSet(ModelViewSet):
    # tala ko attributes should be of same name
    
    queryset = Account.objects.all()#queryset ma Crud ko logic run hunxa,, all() le model bata data objects ma lera aauxa which cannot be sent to fornted so we need json(need serializer for that)
    
    serializer_class = AccountSerializer
  
# ViewSet vannu chai sab logic cha
# View matra vannu chai halka matra cha aru affei lekhne  
class BankApiView(GenericAPIView):
    #ya ko attribute ko name chai yei hunu parne vanne chaina bcz we're defining out own logic
    
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    def get(self, request):
        bank_objs = Bank.objects.all()
        serializer = BankSerializer(bank_objs,many=True)
        
        
        return Response(serializer.data)
        
        pass



