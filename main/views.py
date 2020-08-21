from django.shortcuts import redirect,render,get_object_or_404
from .models import Question
from django.utils import timezone
from .forms import QuestionForm,AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#!!!! related_name = answer
def index(request):

    question_list=Question.objects.order_by('-create_date') #날짜 역순으로 정렬
    paginator=Paginator(question_list,3)                    #한페이지 글3개
    page=request.GET.get('page','1')                        #url 에서 page 값 가져오는거 1은 디폴트
    posts=paginator.get_page(page)
    info={'question_list':posts}
    return render(request,'main/question_list.html',info) #context 데이터를 해당 html 파일에 적용

def detail(request, question_id):       #question_id는 url 매핑에 의해 전달
    question = get_object_or_404(Question, pk=question_id)  #id에 해당하는 객체 없으면 404error
    info = {'question': question}
    return render(request, 'main/question_detail.html', info)

@login_required(login_url='user:login') #로그인이 필요한 함수 로그아웃상태면 login url 로 이동
def answer_create(request, question_id):
    question= get_object_or_404(Question,pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():             #값이 유효한지 검사
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author=request.user
            answer.save()
            return redirect('main:detail', question_id=question.id) #답변 생성후 
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'main/question_detail.html', context) #answer생성 후 해당 질문으로 이동

@login_required(login_url='user:login')
def question_create(request):
    if request.method == 'POST':    #POST
        form = QuestionForm(request.POST)  #전달받은 form
        if form.is_valid():
            question = form.save(commit=False)  #폼에는 date값이 없기때문에 commit=False
            question.create_date = timezone.now()
            question.author=request.user
            question.save()
            return redirect('main:index')
    else:                           #GET
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'main/question_form.html', context)

@login_required(login_url='user:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:     #작성자가 아니면
        messages.error(request, '수정권한이 없습니다')
        return redirect('main:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('main:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'main/question_form.html', context)

@login_required(login_url='user:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('main:detail', question_id=question.id)
    question.delete()
    return redirect('main:index')
