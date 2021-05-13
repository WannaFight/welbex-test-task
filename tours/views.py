from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

from .models import Tour
from .utils import pagination_manager


# Create your views here.
def index(request):
    all_tours = Tour.objects.all()
    page_obj, pages = pagination_manager(all_tours, 5, 2,
                                         request.GET.get('page', 1))

    return render(request, 'tours/index.html', context={'page_obj': page_obj,
                                                        'pages': pages})
