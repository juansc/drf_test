import json

from rest_framework import serializers, fields
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class BaseAPIView(APIView):
    METHOD_SERIALIZERS = {}
    params = {}

    def initial(self, request, *args, **kwargs):
        self.params = kwargs
        method = request.method.lower()
        if method not in self.METHOD_SERIALIZERS.keys():
            print('could not find method. exiting early')
            return
        if method == 'get':
            request_data = request.query_params
        else:
            request_data = request.data
        validated_data = self.METHOD_SERIALIZERS[method](data=request_data) 
        if validated_data.is_valid(raise_exception=True):
            self.params.update(validated_data.validated_data)

class TestView(BaseAPIView):

    class TestSerializer(serializers.Serializer):
        my_num = fields.IntegerField(required=True)
        my_str = fields.CharField(required=True)
        strs = fields.ListField(child=fields.CharField())

    METHOD_SERIALIZERS = {
        'get': TestSerializer, 
    }

    def get(self, request, *args, **kwargs):
        print("Data is {}".format(self.params))
        return Response({'success': True})
