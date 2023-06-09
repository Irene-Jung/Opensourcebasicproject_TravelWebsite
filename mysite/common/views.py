from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def usa(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/usa.html')


def japan(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/japan.html')


def osaka(request):
    if request.method == 'POST':
        page_url = request.POST.get('japan')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/japan/osaka.html')


def fukuoka(request):
    if request.method == 'POST':
        page_url = request.POST.get('japan')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/japan/fukuoka.html')


def tokyo(request):
    if request.method == 'POST':
        page_url = request.POST.get('japan')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/japan/tokyo.html')


def kyoto(request):
    if request.method == 'POST':
        page_url = request.POST.get('japan')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/japan/kyoto.html')


def china(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/china.html')


def france(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/france.html')


def thailand(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/thailand.html')


def spain(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/spain.html')
