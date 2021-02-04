from rest_framework import serializers
from .models import TodoApp

class TodoSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = TodoApp

        fields = ['title','img',]
        #image = serializers.Field('image.url')





