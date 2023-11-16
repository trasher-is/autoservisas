from django.contrib import admin
from .models import AutomobilioModelis, Automobilis, Uzsakymas, UzsakymoEilute, Paslauga, UzsakymasReview

# Register your models here.


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_modelis_id', 'valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis_id')
    search_fields = ('valstybinis_nr', 'vin_kodas')


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


class UzsakymoEiluteAdmin(admin.ModelAdmin):
    list_display = ('paslauga_id', 'uzsakymas_id', 'kiekis')


class UzsakymasInstance(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('data', 'automobilis_id', 'vartotojas', 'grazinimo_terminas')
    inlines = [UzsakymasInstance]


class UzsakymasReviewAdmin(admin.ModelAdmin):
    list_display = ('uzsakymas_review_id', 'date_created', 'reviewer', 'atsiliepimo_tekstas')


admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute, UzsakymoEiluteAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(UzsakymasReview, UzsakymasReviewAdmin)
