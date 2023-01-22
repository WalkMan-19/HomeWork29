from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.serializers import AdListSerializer, AdCreateSerializer, AdRetrieveSerializer, AdUpdateSerializer, \
    AdDestroySerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        category_pks = request.GET.getlist('cat', None)
        text = request.GET.get('text', None)
        location = request.GET.get('loc', None)
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        search_query = None

        for category_pk in category_pks:
            if search_query is None:
                search_query = Q(category__id__exact=category_pk)
            else:
                search_query |= Q(category__id__exact=category_pk)

        if text:
            if search_query is None:
                search_query = Q(name__icontains=text)
            else:
                search_query |= Q(name__icontains=text)

        if location:
            if search_query is None:
                search_query = Q(author__location__name__icontains=location)
            else:
                search_query |= Q(author__location__name__icontains=location)

        if price_from:
            if search_query is None:
                search_query = Q(price__gte=price_from)
            else:
                search_query &= Q(price__gte=price_from)

        if price_to:
            if search_query is None:
                search_query = Q(price__lte=price_to)
            else:
                search_query &= Q(price__lte=price_to)

        if search_query:
            self.queryset = self.queryset.select_related('author').prefetch_related('category').filter(search_query). \
                order_by('-price')

        return super(AdListView, self).get(request, *args, **kwargs)


@permission_classes([IsAuthenticated])
class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    
    def create(self, request, *args, **kwargs):
        request.data['author'] = self.request.user.username
        return super(AdCreateView, self).create(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdRetrieveSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdImageView(UpdateView):
    model = Ad
    fields = ('name', 'image')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()
        return JsonResponse(
            {
                'id': self.object.id,
                'name': self.object.name,
                'image': self.object.image.url
            }
        )
