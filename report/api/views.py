from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView, UpdateAPIView
from .serializers import NewsSerializer, CategoriesSerializer, TagsSerializer, serializers
from report.models import News, Categories, Tags, models
from rest_framework.response import Response

class ListNewsApiView(GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get(self, request,*args, **kwargs ):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DetailNewApiView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer






# class PostUpdateView(UpdateAPIView):
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer
#     lookup_field = 'id'







class CategoriesApiview(GenericAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get(self, request,*args, **kwargs ):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DetailCategoriesApiView(RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
