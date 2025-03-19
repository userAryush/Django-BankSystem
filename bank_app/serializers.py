from rest_framework.serializers import ModelSerializer#yesma json to obj,obj to json convert garne logic cha
from .models import Account,Bank,User

class AccountSerializer(ModelSerializer):
    # ya bata tala ModelSErializer ma already defined cha hamile override gareko ho
    class Meta:
        model = Account
        fields = '__all__'#kun field change garne
        
class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
            
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','username','number','address','image']