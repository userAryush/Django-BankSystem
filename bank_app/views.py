from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #API ma hune sab logic cha
from rest_framework.generics import GenericAPIView # yesma API banauda chai sabei logic affei banauna paro
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token # fucntion based api ko lagi
from .models import Account, Bank, User
from .serializers import AccountSerializer,BankSerializer,UserSerializer
from django.contrib.auth import authenticate #credential linxa ani valid cha ki nai check garca
# Create your views here.

@api_view(['POST']) #kun kun request garna payo
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Registered!')
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([])  #login lai chai jasle ni chalauna milnu paro so
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email,password=password)#match vovane user nikalxa or None
    if user == None:
        return Response('Invalid credentials!')
    else:
        token,_ = Token.objects.get_or_create(user = user)#duia value return garca so _
        return Response(token.key)
        
    
    


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
        
    def post(self, request):
        #request ma sab data aauxa
        serializer = BankSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
     
class BankApiViewDetails(GenericAPIView):   
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    def get(self, request, pk):
        try:
            bank_obj = Bank.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = BankSerializer(bank_obj)
        return Response(serializer.data)
        
    def put(self, request, pk):
        try:
            bank_obj = Bank.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = BankSerializer(bank_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            bank_obj = Bank.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = BankSerializer(bank_obj,data=request.data)
        bank_obj.delete()
        return Response('Data Deleted')



