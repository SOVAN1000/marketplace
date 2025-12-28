from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # activate and log in the user immediately
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout_view(request):
    """Log out the user and redirect to homepage. Supports GET and POST."""
    from django.contrib.auth import logout
    logout(request)
    return redirect('homepage')


def activate(request, uidb64, token):
    """Activate a user's account from an emailed link."""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been activated and you are now logged in.')
        return redirect('homepage')
    else:
        messages.error(request, 'Activation link is invalid or expired.')
        return redirect('homepage')