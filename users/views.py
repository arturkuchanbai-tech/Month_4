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
