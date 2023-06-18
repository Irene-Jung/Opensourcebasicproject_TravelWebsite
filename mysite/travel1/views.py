from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    """travel1 목록 출력"""
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review.objects.order_by('-create_date')
    paginator = Paginator(review_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'travel1/review_list.html', context)


def detail(request, review_id):
    """travel1 내용 출력"""
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'travel1/review_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, review_id):
    """travel1 답변 등록"""
    review = get_object_or_404(Review, pk=review_id)
    review.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    if form.is_valid():
        answer = form.save(commit=False)
        answer.author = request.user  # author 속성에 로그인 계정 저장
    return redirect('travel1:detail', review_id=review.id)


@login_required(login_url='common:login')
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            review = form.save(commit=False)  # 임시 저장하여 review 객체를 리턴받는다.
            review.author = request.user  # author 속성에 로그인
            review.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            review.save()  # 데이터를 실제로 저장한다.
            return redirect('travel1:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'travel1/review_form.html', context)


def answer_create(request, review_id):
    """travel1 답변등록"""
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.review = review
            answer.save()
            return redirect('travel1:detail', review_id=review.id)
    else:
        form = AnswerForm()
    context = {'review': review, 'form': form}
    return render(request, 'travel1/review_detail.html', context)



def country(request):
    if request.method == 'POST':
        page_url = request.POST.get('country')
        if page_url:
            return redirect(page_url)
    return render(request, 'common/country.html')