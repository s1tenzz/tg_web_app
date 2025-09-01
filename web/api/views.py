from typing import Union, Tuple

from django.http import JsonResponse, HttpRequest
from rest_framework.views import APIView

from api.models import User


class UserCreate(APIView):

    @staticmethod
    def _get_body(body: dict) -> Union[JsonResponse, Tuple[None, None]]:
        name = body.get('name', None)
        email = body.get('email', None)
        return name, email

    @staticmethod
    def _check_email(email: str) -> bool:
        try:
            # Get user from Database
            user = User.objects.get(email=email)
            if user:
                return False
        except User.DoesNotExist:
            return True

    def post(self, request: HttpRequest, *args, **kwargs,) -> JsonResponse:
        body: dict  = request.data
        name, email = self._get_body(body=body)
        if not name or not email:
            return JsonResponse(
                {
                    "error": "name and email is required",
                },
                status=400,
            )

        if not self._check_email(email=email):
            return JsonResponse(
                {
                    "error": "Such user already exists.",
                },
                status=400,
            )


        user: User = User.objects.create(
            name=name,
            email=email,
        )

        return JsonResponse(
            {
                'id': user.id,
                "name": user.name,
                "email": user.email,
            },
            status=200,
        )


class UserGet(APIView):

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        params: dict = request.GET

        # Get params from query request
        email = params.get("email", None)
        if not email:
            return JsonResponse(
                {
                    "error": "email is required",
                },
                status=400,
            )

        try:
            # Get user from Database
            user = User.objects.get(email=email)
            return JsonResponse(
                {
                    'id': user.id,
                    "name": user.name,
                    "email": user.email,
                },
                status=200,
            )
        except User.DoesNotExist:
            return JsonResponse(
                {
                    "error": "Such user does not exist.",
                },
                status=400,
            )
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
