from django.shortcuts import render
from django.utils import timezone
from .models import Experience

def danger(request):
    experiences = Experience.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date')
    return render(request, 'cocaine/danger.html', {'experiences': experiences})
