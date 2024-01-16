from rest_framework.response import Response
from rest_framework.views import APIView  # Fix import statement
from API.models import Product
from API.serializers import ProductSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

class ProductAPIView(APIView):  # Correct class name
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Uploaded Successfully', 'status': 'success',
                             'product': serializer.data},  # Correct variable name
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        products = Product.objects.all()  # Correct variable name
        serializer = ProductSerializer(products, many=True)
        return Response({'status': 'success', 'products': serializer.data},  # Correct variable name
                        status=status.HTTP_200_OK)

# def Product(request, pk):
#     Product=Product.objects.get(id=pk)
#     serializer=ProductSerializer(Product)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')