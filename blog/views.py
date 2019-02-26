from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Train_data
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from tablib import Dataset
from django.http import HttpResponse
from .resources import PersonResource
from .resources import TrainResource

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

def no_diease(request):
    return render(request, 'blog/no_diease.html', {})


def analysis(request):
    return render(request, 'blog/analysis.html', {})


def result(request):
    return render(request, 'blog/result.html', {})
