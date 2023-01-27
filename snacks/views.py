from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack

# Create your views here.


class SnackListView(ListView):
    template_name = "snacks/templates/snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = "snacks/templates/snack_detail.html"
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = "snacks/templates/snack_update.html"
    model = Snack
    fields = "__all__"


class SnackCreateView(CreateView):
    template_name = "snacks/templates/snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    template_name = "snacks/templates/snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
