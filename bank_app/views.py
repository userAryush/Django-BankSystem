from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #API ma hune sab logic cha
from rest_framework.generics import GenericAPIView # yesma API banauda chai sabei logic affei banauna paro
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token # fucntion based api ko lagi
from .models import *
from .serializers import *
from django.contrib.auth import authenticate #credential linxa ani valid cha ki nai check garca
from django.contrib.auth.hashers import make_password 
from rest_framework.permissions import DjangoModelPermissions,AllowAny
from django.contrib.auth.models import Group
from .permissions import CustomModelPermissions
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def group_list(request):
    group_obj = Group.objects.all()
    serializer = GroupSerializer(group_obj,many=True)
    return Response(serializer.data)
    

@api_view(['POST']) #kun kun request garna payo
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Registered!')
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])  #login should be allowed to use by anyone so giving permission
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email,password=password)#match vovane user nikalxa or None,  authenticate le password lai as a encrypted value check garxa so user register garda encrypt garna paro 
    if user == None:
        return Response('Invalid credentials!')
    else:
        token,_ = Token.objects.get_or_create(user = user)#duia value return garca so _,, euta user ko euta token banxa arleady cha vane get garxa or create garxa
        return Response(token.key)#token object ho user ra key field hunxa tesma so key call garo to get token
        
    
    


#Frontend le API bata communicate garxa to do CRUD operation in backend
#so API ma CRUD ko logic huna paro
# frontend tells through request what operation to perform,, method(GET->data magne kam,PUT-> update garne,POST-> create garne,DELETE->delete garxa)

#API using ModelViewSet
class AccountViewSet(ModelViewSet):
    # tala ko attributes should be of same name
    
    queryset = Account.objects.all()#queryset ma Crud ko logic run hunxa,, all() le model bata data objects ma lera aauxa which cannot be sent to fornted so we need json(need serializer for that)
    
    serializer_class = AccountSerializer # mathi aako data will be objects but API requires json so serializer_class lai call garera AccountSerialiser call hune vo ani json ma convert
    
    permission_classes = [CustomModelPermissions]
    filterset_fields =['user']
    search_fields = ['user','account_name','mobile_num','acc_num']
  
# ViewSet vannu chai sab logic cha
# View matra vannu chai halka matra cha aru affei lekhne 

#     could have used this for both bankapiview and bankapiviewdetails
# class BankApiView(GenericAPIView):    
#     queryset = Bank.objects.all()
#     serializer_class = BankSerializer 
class BankApiView(GenericAPIView):
    #ya ko attribute ko name chai yei hunu parne vanne chaina bcz we're defining our own logic
    
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [CustomModelPermissions]
    
    # its a class method so self param is compul, 
    def get(self, request):
        bank_objs = Bank.objects.all()
        
        # DRF’s serializer needs to know whether it’s handling one object or multiple objects.

        # If many=True is not specified, DRF will expect a single object and raise an error.
        # after many=True Each bank object is correctly serialized into a list of JSON objects.
            #         [
            #     {
            #         "id": 1,
            #         "name": "Bank A",
            #         "short_name": "A"
            #     },
            #     {
            #         "id": 2,
            #         "name": "Bank B",
            #         "short_name": "B"
            #     }
            # ]
        serializer = BankSerializer(bank_objs,many=True)
        
        #data is a method but it has a decorator so can be called like this
        # response class is sending json data 
        return Response(serializer.data)
     
    # while we post data is sent in request   
    def post(self, request):
        # request.data contains the incoming data(json) sent by the client
        # before saving the data to database we need to change it to obj 
        # data ma pass gareko le it will deserialize the data into an object
        serializer = BankSerializer(data = request.data)
        
        #reuqst.data can have any data so validate tara get garda validate garnu pardeina as data comes from database,, checks data according to model,, outputs True or False
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
  
  
# i wanted to use standard name for get method so made another view for retreiving data id wise   
class BankApiViewDetails(GenericAPIView):   
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [CustomModelPermissions]
    def get(self, request, pk):
        # if no pk requested error will come
        try:
            bank_obj = Bank.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        # before we used many=True but here we only want to serialize one object so by default many=False so we don't need to specify it    
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


class StatementApiViewSet(ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
