from rest_framework.authentication import BaseAuthentication
from django.conf import settings
import jwt
from django.contrib.auth.models import User
 
# class CustomAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         token = self.get_token_from_header(request)
#         if not token:
#             return None
 
#         try:
#             decoded_token = jwt.decode(token,"django-insecure-85ce1k^7usnq*@c6whb=y%9aa*jsl5)qlw(fx3&7#^9ypofzek", algorithms=["HS256"])
#             # You can perform additional validation or retrieve user data from the token payload here
#             username = decoded_token["username"]
#             # Fetch user from the database using the username if required
#             # user = User.objects.get(username=username)
#             return (username, None)
#         except jwt.ExpiredSignatureError:
#             return None
 
#     def get_token_from_header(self, request):
#         header = request.headers.get("Authorization")
#         if header and header.startswith("Token "):
#             return header.split(" ")[1]
#         return None

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_header(request)
        if not token:
            return None

        try:
            decoded_token = jwt.decode(token, "django-insecure-85ce1k^7usnq*@c6whb=y%9aa*jsl5)qlw(fx3&7#^9ypofzek", algorithms=["HS256"])
            user_id = decoded_token.get('user_id')  # Replace 'user_id' with the correct key in your token payload
            print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            user_id = decoded_token.get('user_id') 
            print(decoded_token, user_id, 'tokennnnnnnnnnn')
            # Fetch user from the database using the user_id from the token
            user_id = decoded_token.get("user_id")
            # Assuming you have a User model with id field
            user = User.objects.get(id=user_id)

            return (user, None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

    def get_token_from_header(self, request):
        header = request.headers.get("Authorization")
        if header and header.startswith("Token "):
            return header.split(" ")[1]
        return None
