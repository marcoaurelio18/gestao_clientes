from django.urls import path
from .views import (
    persons_list,
    persons_new,
    persons_update,
    persons_delete,
    new_document,
    Pdf
)

# URLs da classe person e cpf, para visualizar, editar, excluir, criar um novo
urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="person_update"),
    path('delete/<int:id>/', persons_delete, name="person_delete"),
    path('new_document', new_document, name="new_document"),
    path('relatorio/', Pdf.as_view(), name="relatorio_pdf")
]