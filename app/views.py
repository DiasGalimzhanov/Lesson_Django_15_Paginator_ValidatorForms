from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Phone
from django.core.paginator import Paginator
from .forms import PhoneForm
from django.urls import reverse_lazy

# def home(request):
#     phones = Phone.objects.all()
#     paginator = Paginator(phones, 3)

#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
    
#     page = paginator.get_page(page_num)
#     return render(request, 'home.html', {'page': page})

class PhoneList(ListView):
    model = Phone
    template_name = 'home.html'
    context_object_name = 'phones'
    paginate_by = 3

class PhoneCreate(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

