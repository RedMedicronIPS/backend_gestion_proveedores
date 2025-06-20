from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ..forms import GestionarRevisionForm
from gestionProveedores.models import PendienteRevision

def gestionar_revision(request, revision_id):
    revision = get_object_or_404(PendienteRevision, pk=revision_id)

    if request.method == 'POST':
        form = GestionarRevisionForm(request.POST, instance=revision)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = GestionarRevisionForm(instance=revision)

    return render(request, 'modales/gestionar_revision_modal.html', {'form': form, 'revision': revision})
