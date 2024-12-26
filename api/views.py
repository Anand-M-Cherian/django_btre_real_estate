from rest_framework import generics, permissions
from .serializers import GetListingsSerializer, CreateListingsSerializer
from listings.models import Listing
from django.http import JsonResponse
from http import HTTPStatus
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response

# Create your views here.

# =============== AUTHENTICATION ===============

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = data['password']

        # Check username
        if User.objects.filter(username=username).exists():
            response = {
                "message": "Username already exists"
            }
            return JsonResponse(response, status=HTTPStatus.CONFLICT)
        else:
            # Check email
            if User.objects.filter(email=email).exists():
                response = {
                    "message": "Email already exists"
                }
                return JsonResponse(response, status=HTTPStatus.CONFLICT)
            # Validations passed
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                token = Token.objects.create(user=user)
                response = {
                    "message": "User has been registered succesfully",
                    'token': str(token)
                }
                return JsonResponse(response, status=HTTPStatus.CREATED)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])

        if user is None:
            return JsonResponse({'error':'Login Failed. Please check credentials'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
                status = 200
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
                status = 201
        return JsonResponse({'token':str(token)}, status=status)
                
class IsStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET for everyone (unauthenticated users)
        if request.method == 'GET':
            return True
        # Everything else (POST, PUT, PATCH, DELETE) is only for the staff user
        return request.user.is_authenticated and request.user.is_staff

# =============== FUNCTIONALITIES ===============

class ListCreateListingsView(generics.ListCreateAPIView):
    serializer_class = CreateListingsSerializer
    queryset = Listing.objects.all().order_by('-list_date')
    permission_classes = [IsStaffUser]

    def perform_create(self, serializer):
        # Save the listing only if the request passes all permission checks
        serializer.save()

        # Optional success response customization
        return Response({"message": "Listing created successfully"}, status=201)
    
class GetUpdateDeleteListingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateListingsSerializer
    queryset = Listing.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsStaffUser]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()