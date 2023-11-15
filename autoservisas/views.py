from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Automobilis, Uzsakymas, Paslauga


def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    automobiliu_kiekis = Automobilis.objects.all().count()
    klientu_kiekis = Automobilis.objects.all().count()
    uzsakymu_kiekis = Uzsakymas.objects.all().count()
    atlikti_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='u').count()
    vykdomi_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='a').count()
    laukiami_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='l').count()
    atsaukti_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='x').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,
        'klientu_kiekis': klientu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'atlikti_uzsakymai': atlikti_uzsakymai,
        'vykdomi_uzsakymai': vykdomi_uzsakymai,
        'laukiami_uzsakymai': laukiami_uzsakymai,
        'atsaukti_uzsakymai': atsaukti_uzsakymai,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all(), 5)
    page_number = request.GET.get('page')
    visi_automobiliai = paginator.get_page(page_number)
    context = {
        'visi_automobiliai': visi_automobiliai,
    }
    return render(request, 'automobiliai.html', context=context)


def kainynas(request):
    kainynas_info = Paslauga.objects.all()
    context = {
        'kainynas': kainynas_info,
    }
    return render(request, 'kainynas.html', context=context)


class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    context_object_name = 'uzsakymai_list'
    paginate_by = 5
    template_name = 'uzsakymai.html'


def klientai(request):
    klientai_pilna_info = Automobilis.objects.all()
    context = {
        'klientai': klientai_pilna_info,
    }
    return render(request, 'klientai.html', context=context)


def uzsakymas(request, uzsakymas_id):
    uzsakymas_pilna_info = get_object_or_404(Uzsakymas, pk=uzsakymas_id)
    context = {
        'uzsakymas': uzsakymas_pilna_info,
    }
    return render(request, 'uzsakymas.html', context=context)


def automobilis(request, automobilis_id):
    automobilis_pilna_info = get_object_or_404(Automobilis, pk=automobilis_id)
    context = {
        'automobilis': automobilis_pilna_info,
    }
    return render(request, 'automobilis.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(Q(valstybinis_nr__icontains=query)
                                                | Q(vin_kodas__icontains=query)
                                                | Q(klientas__icontains=query)
                                                | Q(automobilio_modelis_id__modelis__icontains=query)
                                                | Q(automobilio_modelis_id__marke__icontains=query))
    context = {
        'automobiliu_paieska': search_results,
        'query': query,
    }
    return render(request, 'search.html', context=context)


class KlientoUzsakymaiListView(LoginRequiredMixin, generic.ListView):
    model = Uzsakymas
    context_object_name = 'klientouzsakymai_list'
    template_name = 'mano_uzsakymai.html'
    paginate_by = 5

    def get_queryset(self):
        return Uzsakymas.objects.filter(vartotojas=self.request.user).order_by('grazinimo_terminas')
