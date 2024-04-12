from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework import settings
import pdb

class MyAuthentication(TokenAuthentication):
    # def authenticate(self,request):
    #     userid=request.GET.get('user_id')
    #     if userid is None:
    #         return None
    #     try:
    #         user=User.objects.get(userid=id)
    #     except User.DoesNotExist:
    #         raise AuthenticationFailed("user is not available")
    #     return (user,None)
    
    def authenticate_credentials(self, key):
        print(key)
        # pdb.set_trace()
        

        try:
            user =jwt.decode(key,'django-insecure-75zotega+o)b-bh433r*1(&jq9985*ng^o0$cl4_+f03*va-0+',algorithms='HS256')
            print(user)
            user_instance=User.objects.filter(username=user['username'])
            print(user_instance)

        except Exception as err:
            raise exceptions.AuthenticationFailed('invalid token')
        if not user_instance.is_active:
            raise exceptions.AuthenticationFailed('user not available')
        return(user_instance,key)


        


