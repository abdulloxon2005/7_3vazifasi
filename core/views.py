from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import FormView,TemplateView
from  .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user
        return context
    

class LoginFormView(FormView):
    form_class  = LoginForm
    template_name = "core/email-login.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']

        user = authenticate(self.request,username = email,password = password)
        if user:
            if remember_me:
                self.request.session.set_expiry(None)
            else:
                self.request.session.set_expiry(0)
            login(self.request,user)
            return super().form_valid(form)
        else:
            form.add_error(None,"username or password incorrect")
            return self.form_invalid(form)

        
    