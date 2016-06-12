from django.shortcuts import render

def danger(request):
    return render(request, 'cocaine/danger.html', {})