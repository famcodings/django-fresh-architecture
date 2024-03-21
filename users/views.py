from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from users.forms import RegisterForm


class HomeView(TemplateView):
    template_name = 'users/home.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).get(request, *args, **kwargs)