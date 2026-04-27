from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm, ProfileForm

User = get_user_model()

class login_view(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        user = self.request.user

        if user.is_staff:
            return reverse_lazy('admin:index')

        return super().get_success_url()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form
    })

@login_required
def profile_view(request):
    user = request.user
    items = user.item_set.all().order_by('-created')[:4]
    
    return render(request, 'users/profile.html', {
        'profile_user': user,
        'items': items
    })

@login_required
@require_http_methods(["POST"])
def update_profile_view(request):
    user = request.user
    form = ProfileForm(request.POST, request.FILES, instance=user)
    
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Perfil actualizado correctamente'})
    else:
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)