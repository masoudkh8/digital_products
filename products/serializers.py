from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.HyperlinkedModelSerializer):#ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title', 'description', 'avatar','url')


class FileSerializer(serializers.ModelSerializer):
    #file_type = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','title', 'file', 'file_type')
        #fields = ('id', 'title', 'file', 'file_type')

    #def get_file_type(self, obj):
    #    return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer): #HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    # foo = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files','url')
        #fields = ('id', 'title', 'description', 'avatar', 'categories', 'url')

    # def get_foo(self, obj):
    #     return 'Hello World'
