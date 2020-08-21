#질문 등록을 위한 form
from django import forms
from main.models import Question,Answer


class QuestionForm(forms.ModelForm):
    class Meta:     #내부클래스 정의 필수!!
        model = Question    #Question 모델을 기반
        fields = ['subject', 'content']     #속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }