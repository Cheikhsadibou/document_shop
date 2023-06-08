from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

User = get_user_model()


def register(request):
    if request.method == "POST":
        # on traite le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)

        login(request, user)
        return redirect('index')

    return render(request, "accounts/register.html")


def connection(request):
    if request.method == "POST":
        # connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("index")
