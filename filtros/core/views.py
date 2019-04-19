from django.shortcuts import render


def FiltroBoostrapView(request):
    return render(request, 'core/bootstrap_form.html')
