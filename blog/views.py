from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Train_data
from .models import Person1_train
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, Person1Form
from django.shortcuts import redirect
from tablib import Dataset
from django.http import HttpResponse
from .resources import PersonResource
from .resources import TrainResource
from . import web_code
import pandas as pd

predict = "NO RESULT"

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    train_datas = Train_data.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts , 'train_datas': train_datas})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile1']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')


def simple_upload2(request):
    if request.method == 'POST':
        train_resource = TrainResource()
        dataset = Dataset()
        new_train = request.FILES['myfile2']

        imported_data = dataset.load(new_train.read())
        result = train_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            train_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload2.html')


def no_disease(request):
    return render(request, 'blog/no_disease.html', {})



def has_disease(request):
    if request.method == "POST":
        form = Person1Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post.disease)

            bmi = post.weight / ((post.height / 100) ** 2)

            raw_data = {'성별코드': [post.gender],
                        '연령대코드(5세단위)': [post.age//5],
                        '허리둘레': [post.waist],
                        '수축기혈압': [post.systolic_pressure],
                        '이완기혈압': [post.diastolic_pressure],
                        '당뇨병 의사 판정': [1],
                        '고혈압 의사 판정': [1],
                        '지질혈증 의사 판정': [1],
                        'BMI': [bmi],
                        '구강검진 수검여부': [post.cavity_screen],
                        }

            df = pd.DataFrame(raw_data)
            if post.disease == "당뇨병":
                df = df.drop(["고혈압 의사 판정", "지질혈증 의사 판정"], axis = 1)

            elif post.disease == "고혈압":
                df = df.drop(["당뇨병 의사 판정", "지질혈증 의사 판정"], axis = 1)

            elif post.disease == "이상지질혈증":
                df = df.drop(["당뇨병 의사 판정", "고혈압 의사 판정"], axis = 1)


            predict = web_code.run_model(post.disease, df)
            print(predict)
            return render(request, 'blog/result.html', {'name': post.name , 'predict': predict})
    else:
        form = Person1Form()
    return render(request, 'blog/has_disease.html', {'form': form})




def people(request):
    return render(request, 'blog/people.html', {})




def analysis(request):
    return render(request, 'blog/analysis.html', {})


def result(request):
    return render(request, 'blog/result.html', {'predict':predict})

