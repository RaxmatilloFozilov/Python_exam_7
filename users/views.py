from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


from config.settings import sended_mails, EMAIL_HOST_USER, emails_list
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from django.core.mail import send_mail
from django.http import HttpResponse
from random import randint


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
def insert_email_4_change_password(request):
    email = request.data['email']
    user = get_user_model()
    if user.objects.filter(email=email).exist():
        num = randint(100000, 999999)
        emails_list[email] = num
        send_mail(
            subject=' Parolni tiklash uchun kod',
            message=f" Parolni o'zgartirish uchun kod: {num}\n",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )
        return Response({'message': 'Parolni tiklash uchun kod yuborildi'}, status=200)
    else:
        return Response({'message': 'Elektron pochta mavjud emas'}, status=400)


@api_view(['POST'])
def reset_password(request):
    code = request.data['code']
    email = request.data['email']
    password1 = request.data['password1']
    password2 = request.data['password2']
    if password1 == password2:
        try:
            if code == emails_list[email]:
                user = get_user_model().objects.get(email=email)
                user.set_password(password1)
                user.save()
                del emails_list[email]
                return Response('Parolni tiklash muvaffaqiyatli', status=200)
            else:
                return Response({'message': 'Elektron pochta yoki kod mos emas'}, status=400)
        except:
            return Response({'message': 'Elektron pochta yoki kod mos emas'}, status=400)


@api_view
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Muvaffaqiyatli tizimga kirildi'})
    else:
        return Response({'error': 'Yaroqsiz foydalanuvchi nomi yoki parol'}, status=400)


@api_view
def change_password(request):
    username = request.POST.get('username')
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    user = authenticate(username=username, password=old_password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Muvaffaqiyatli ozgartirildi'})
    else:
        return Response({'error': 'Yaroqsiz foydalanuvchi nomi yoki parol'}, status=401)


@api_view(['POST'])
def confirm_email(request):
    try:
        recipient_list = [request.POST.get('email')]
        sended_mails[request.POST.get('email')] = f"{randint(100, 999)}-{randint(100, 999)}"

        send_mail(
            subject='Confirm email',
            message=sended_mails[request.POST.get('email')],
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list
        )
        return Response({'message': 'Kod yuborildi'})
    except Exception as e:
        return HttpResponse(f" Noto'g'ri elektron pochta yoki {e}")


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)

    def post(self, request, *args, **kwargs):
        if request.auth:
            request.auth.delete()
            return Response({"detail": "Hisobdan muvaffaqiyatli chiqdi ✅."}, status=200)
        else:
            return Response({"detail": "Siz hech qachon autentifikatsiyadan o'tmagansiz ❎."}, status=401)


