from django.contrib import admin
from .models import CPF, Person


# Personalizar person no django admin
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('first_name', 'last_name', 'cpf')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'bio', 'photo')}),
    )

    # filtro de busca
    list_filter = ('age',)
    # display no django admin
    list_display = ('first_name', 'last_name', 'has_photo')
    # Dados que podem ser pesquisados
    search_fields = ('id', 'first_name')
    # Campos que você deseja alterar para entradas de preenchimento automático
    autocomplete_fields = ('cpf',)

    #função para saber se o cliente possui ou nao foto
    def has_photo(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'

    has_photo.short_description = 'Possui foto'


# Personalizar CPF no django admin
class CpfAdmin(admin.ModelAdmin):
    # Dados que podem ser pesquisados
    search_fields = ('num_doc',)


admin.site.register(Person, PersonAdmin)
admin.site.register(CPF, CpfAdmin)
