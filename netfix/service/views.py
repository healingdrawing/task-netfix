from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ServiceForm


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, user=request.user)
        if form.is_valid():
            service = form.save(commit=False)
            service.company_username = request.user
            if request.user.field_of_work != 'ALL_IN_ONE':
                service.field = request.user.field_of_work
            else:
                service.field = form.cleaned_data['field']
            service.save()
            return render(request, 'profile.html', {'user': request.user})
    else:
        form = ServiceForm(user=request.user)
    return render(request, 'add_service.html', {'form': form})


# def add_service(request):
#     return render(request, 'add_service.html')


def book_service(request):
    return render(request, 'book_service.html')
