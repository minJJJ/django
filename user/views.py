from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            new = authenticate(username=username, password=raw_password)
            login(request, new)    #데이터 저장후 자동 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})
