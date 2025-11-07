from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Teacher


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def teacher_list(request):
    teachers = Teacher.objects.all().order_by('full_name')
    return render(request, 'teacher_list.html', {'teachers': teachers})

def static_test(request):
    return render(request, 'static_test.html')

from django.shortcuts import render, get_object_or_404
from .models import Meros

def meros_list(request):
    meroslar = Meros.objects.all()
    return render(request, 'meros_list.html', {'meroslar': meroslar})

def meros_detail(request, slug):
    meros = get_object_or_404(Meros, slug=slug)
    return render(request, 'meros_detail.html', {'meros': meros})

def search_view(request):
    query = request.GET.get('q', '')

    teachers = Teacher.objects.filter(
        Q(full_name__icontains=query) | Q(biography__icontains=query) | Q(achievements__icontains=query)
    ) if query else []

    meroslar = Meros.objects.filter(
        Q(title__icontains=query) | Q(lyrics__icontains=query)
    ) if query else []

    context = {
        'query': query,
        'teachers': teachers,
        'meroslar': meroslar,
    }

    return render(request, 'search_results.html', context)