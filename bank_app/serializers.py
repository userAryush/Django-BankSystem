from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import Group

#json lai object|| object lai json ma convert garna creating serializers using ModelSerializer which have all the required logic


class AccountSerializer(ModelSerializer):
    # ya bata tala ModelSErializer ma already defined cha hamile override gareko ho
    class Meta:
        model = Account
        fields = '__all__'#kun field change garne
        
class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        
class StatementSerializer(ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'
            
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        #json to obj or vv garda field ma jj cha tei matra convert hunxa an data create garda ni specify vako field matra create hunxa
        fields = ['email','password','username','number','address','image','groups']#abstractuser have other fields as well so we need to specify the fields that we have created or need
        
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
        