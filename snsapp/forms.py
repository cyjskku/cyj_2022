#사용자의 입력값을 받아들이는 방법은 3가지가 존재.
#html로 부터 받아들이는 방식
#django의 form을 통해 받아들이는 방식
#model form(model 기반)을 이용하는 받아들이는 방식.

from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
         # 특정 field만 입력받고 싶다면, list를 이용해
         # fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }