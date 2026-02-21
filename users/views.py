<<<<<<< HEAD
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomUserForm


# PROFILE
class ProfileView(TemplateView):
    template_name = "profile.html"


# REGISTER
class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        
        login(self.request, self.object)
        return response


# LOGIN
class CustomLoginView(LoginView):
    template_name = "login.html"
    
    def get_success_url(self):
        return reverse_lazy("yaziki:yaizki_programmirovanie")
        

# LOGOUT
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
=======
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

def registetr_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()

    return render(
        request, 
        'register.html', 
        {'form': form})

def auth_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/prog_lang/')
    else:
        form = AuthenticationForm()

    return render(\
        request,
        'login.html',
        {'form': form})
def logout_view(request):
    logout(request)
    return redirect('/login/')
>>>>>>> 88e1fbe6 (Классные работы)
