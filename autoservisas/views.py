from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin

# Create your views here.
from .models import Automobilis, Uzsakymas, Paslauga
from .forms import UzsakymasReviewForm


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
    paginator = Paginator(Automobilis.objects.all(), 8)
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
    paginate_by = 10
    template_name = 'uzsakymai.html'


def klientai(request):
    klientai_pilna_info = Automobilis.objects.all()
    context = {
        'klientai': klientai_pilna_info,
    }
    return render(request, 'klientai.html', context=context)


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
    paginate_by = 10

    def get_queryset(self):
        return Uzsakymas.objects.filter(vartotojas=self.request.user).order_by('grazinimo_terminas')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class UzsakymasDetailView(FormMixin, generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas.html'
    context_object_name = 'uzsakymas'
    form_class = UzsakymasReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('uzsakymas', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.uzsakymas_review_id = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(UzsakymasDetailView, self).form_valid(form)
