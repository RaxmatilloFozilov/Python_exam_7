from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

# class ChangePasswordView(APIView):
#     def post(self, request):
#         serializer = ChangePasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             # Parolni o'zgartirish logikasi
#             return Response("Parol muvaffaqiyatli o'zgartirildi", status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ResetPasswordView(APIView):
#     def post(self, request):
#         serializer = ResetPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             # Parolni tiklash logikasi
#             return Response("Parolni tiklash uchun havola yuborildi", status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # Basseyn view lar uchun
# class ExampleAPIView(APIView):
#     def get(self, request):
#         # Handle GET request
#         data = {'message': 'This is a GET request.'}
#         return Response(data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         # Handle POST request
#         data = {'message': 'This is a POST request.'}
#         return Response(data, status=status.HTTP_201_CREATED)
