from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView

from .models import URL


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)

    return redirect(url.full_url)


def delete(request, id):
    try:
        person = URL.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/urls")
    except URL.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


class MainView(TemplateView):
    template_name = 'urls_main.html'

    def get(self, request):
        if request.user.is_authenticated:
            urls = URL.objects.filter(author=request.user)
            ctx = {'urls': urls}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/urls/'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/urls/')


class AddURLView(CreateView):
    fields = ['full_url', 'short_name']
    model = URL
    success_url = '/urls/'
    template_name = 'add_edit_urls.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return redirect(self.success_url)


class EditURLView(UpdateView):
    fields = ['full_url', 'short_name']
    model = URL
    success_url = '/urls/'
    template_name = 'add_edit_urls.html'

    def get_object(self, queryset=None):
        obj = URL.objects.get(id=self.kwargs['pk'])
        return obj


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"



