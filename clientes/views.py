from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm, CPFForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
from django.db.models import Count


# So pode ser acessado com login
@login_required
# Função para retornar a pagina da lista de pessoas
def persons_list(request):
    termo_busca = request.GET.get('pesquisa', None)

    # Filtro para a pesquisa
    if termo_busca:
        persons = Person.objects.filter(first_name__icontains=termo_busca)
    else:
        persons = Person.objects.all()

    return render(request, 'clientes/person.html', {'persons': persons})


# So pode ser acessado com login
@login_required
# Função para retornar a pagina de criação de pessoas
def persons_new(request):
    # Variável que recebe o formulário
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        # Quando salvar, retorna para a lista de pessoas
        return redirect('person_list')
    return render(request, 'clientes/person_form.html', {'form': form})


# So pode ser acessado com login
@login_required
# Função para retornar a pagina de edição de pessoas
def persons_update(request, id):
    # Variavel que recebe o id da pessoa
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'clientes/person_form.html', {'form': form})


# So pode ser acessado com login
@login_required
# Função para retornar a pagina da lista para excluir pessoas
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'clientes/person_delete_confirm.html', {'person': person})


# So pode ser acessado com login
@login_required
# Função para retornar a pagina de criação de documentos para vincular a pessoas
def new_document(request):
    form = CPFForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'clientes/document_form.html', {'form': form})


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        pessoas = Person.objects.all()
        params = {
            'pessoas': pessoas,
            'num_pessoas': pessoas.aggregate(Count('id'))['id__count'],
            'request': request,
        }
        return Render.render('clientes/relatorio.html', params, 'relatorio_pessoas')