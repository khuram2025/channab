# Create your views here.

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FileUploadParser, JSONParser, MultiPartParser

from .serializers import *
from .utils import parse_response


class CategoriesView(GenericAPIView):

    def get(self, request):
        cat = Category.objects.all()
        data = CategorySerializer(cat, many=True)
        return parse_response(data=data.data)

    def post(self, request):
        return parse_response(data=None, response="We are accepting only post request")


class AddProducts(GenericAPIView):
    parser_class = [FileUploadParser, MultiPartParser, JSONParser]

    def get(self, request):
        return parse_response(data=None, response="We are accepting only post request")

    def post(self, request):
        try:

            name = request.data['name']
            price = request.data['price']
            phone_number = request.data['phone_number']
            des = request.data['des']
            city = request.data['city']
            image = request.data['image']
            category = request.data['category']

            cat = Category.objects.get(category_name=category)

            product = Product()
            product.name = name
            product.price = price
            product.mobilenumber = phone_number
            product.description = des
            product.name = name
            product.city = city
            product.category = cat
            product.image.save(image.name, image, save=False)
            product.save()

            product_image = ProductImage()
            product_image.product = product
            product_image.image.save(image.name, image, save=False)
            product_image.save()

            s = ProductSerializer(product)
            s2 = ProductImageSerializer(product_image)

            di = {
                "product": s.data,
                "Image": s2.data,
            }

            return parse_response(data=di)

        except Exception as e:
            return parse_response(data=None, response="failed", message=str(e),
                                  status_code=status.HTTP_400_BAD_REQUEST)
