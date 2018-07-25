from rest_framework import status
from rest_framework.response import Response
from permission.models import Category,Perizinan
from django.contrib.auth.models import User
from permission.serializer import PerizinanSerializer,CustomSerializer,CategorySerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, viewsets
from rest_framework import mixins

class PerizinanViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
       permission_classes = (permissions.IsAuthenticated,)
       serializer_class=PerizinanSerializer
       queryset = Perizinan.objects.all()

class CategoryViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
       permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
       serializer_class=CategorySerializer
       queryset = Category.objects.all()

# class PerizinanList(generics.ListCreateAPIView):
#
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = PerizinanSerializer
#
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = Perizinan.objects.filter(pk=24)
#         serializer = PerizinanSerializer(queryset, many=True)
#         return Response(serializer.data)
#
# class PerizinanDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Perizinan.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     serializer_class = PerizinanSerializer

# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def perizinan_list(request):
#     """
#     List all code perizinan
#     """
#     if request.method == 'GET':
#         # user = User.objects.get(pk=1)
#         serializer = CustomSerializer(data={'perizinan':{'id':1,'user':{'firstname':'tes','lastname':'tes','email':'tess@email.com '},'start':'2018-07-21T11:11:30+07:00','end':'2018-07-21T11:11:30+07:00','category':{'id':1,'name':'tes','note':'sss'},'reason':'sss'}})
#         serializer.is_valid()
#         print(serializer.data)
#         return Response(serializer.data)
#     #Create code perizinan
#     elif request.method == 'POST':
#
#         serializer = PerizinanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))
# def perizinan_detail(request, pk):
#     """
#     Retrieve, update or delete a code perizinan.
#     """
#     try:
#         perizinan = Perizinan.objects.get(pk=pk)
#     except Perizinan.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PerizinanSerializer(perizinan)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#
#         serializer = PerizinanSerializer(perizinan, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         perizinan.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
