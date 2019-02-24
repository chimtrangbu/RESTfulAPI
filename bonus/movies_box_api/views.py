from rest_framework import mixins, generics
from .models import Movie
from .serializers import MovieSerializer


class MovieCollection(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
                Optionally restricts the returned purchases to a given user,
                by filtering against a `username` query parameter in the URL.
                """
        queryset = Movie.objects.all()
        imdbID = self.request.query_params.get('i', None)
        if imdbID is not None:
            queryset = queryset.filter(imdbID=imdbID)
        title = self.request.query_params.get('t', None)
        if title is not None:
            queryset = queryset.filter(Title__icontains=title)
        return queryset



class MovieMember(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
