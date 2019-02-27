from django import forms

from .models import Post
from .models import Person1_train

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

CHOICES = (
    ('당뇨병', '당뇨병'),
    ('고혈압', '고혈압'),
    ('이상지질혈증', '이상지질혈증')
)

class Person1Form(forms.ModelForm):
    class Meta:
        model = Person1_train
        fields = ['disease', 'name', 'gender', 'age', 'height', 'weight', 'waist',
                  'systolic_pressure', 'diastolic_pressure','cavity_screen',]
        labels = {'disease': '질병',
                  'name' : '이름',
                  'gender': '성별',
                  'age' : '나이',
                  'height': '키(cm)',
                  'weight' : '체중(kg)',
                  'waist' : '허리둘레(cm)',
                  'systolic_pressure' : '수축기 혈압',
                  'diastolic_pressure':'이완기 혈압',
                  'cavity_screen' : '구강검진 여부',
                 }



