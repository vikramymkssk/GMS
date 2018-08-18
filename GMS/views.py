from django.shortcuts import render
from .models import GMS
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def GMS_list(request):
    return render(request, 'GMS/GMS_list.html', {'GMS':GMS})
GMS = GMS.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

def GMS_detail(request, pk):
    GMS = get_object_or_404(GMS, pk=pk)
    return render(request, 'GMS/GMS_detail.html', {'GMS': GMS})