from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Teacher, Makom, Bolim, Shoba, Kuy


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


def makom_list(request):
    makomlar = Makom.objects.all()
    return render(request, "makom_list.html", {"makomlar": makomlar})


def makom_detail(request, slug):
    makom = get_object_or_404(Makom, slug=slug)
    bolimlar = makom.bolimlar.all()  # mushkilot / nasr
    return render(request, "makom_detail.html", {
        "makom": makom,
        "bolimlar": bolimlar
    })


def bolim_detail(request, makom_slug, bolim_slug):
    bolim = get_object_or_404(Bolim, slug=bolim_slug, makom__slug=makom_slug)

    if bolim.name == "nasr":
        shobalar = bolim.shobalar.all()
        return render(request, "bolim_nasr.html", {
            "bolim": bolim,
            "shobalar": shobalar
        })

    # Mushkilot → здесь сразу выходят kuy
    kuys = Kuy.objects.filter(bolim=bolim)
    return render(request, "bolim_mushkilot.html", {
        "bolim": bolim,
        "kuys": kuys
    })


def shoba_detail(request, makom_slug, bolim_slug, shoba_slug):
    shoba = get_object_or_404(Shoba, slug=shoba_slug, bolim__slug=bolim_slug)
    kuys = Kuy.objects.filter(shoba=shoba)

    return render(request, "shoba_detail.html", {
        "shoba": shoba,
        "kuys": kuys
    })


def kuy_detail(request, slug):
    kuy = get_object_or_404(Kuy, slug=slug)
    return render(request, "kuy_detail.html", {"kuy": kuy})
