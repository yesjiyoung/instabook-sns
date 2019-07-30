from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User #User에 대한 클래스를 가져온다!
from django.contrib import auth #계정에대한권한에 관한 내용을 가져온다~
from .models import Sns
from .forms import NewSns
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import datetime
def unlog(request):
    return render(request, 'unlog.html')
    
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('real')
        else:
            return render(request, 'unlog.html')
    else:
        return render(request, 'home.html')

    #return render(request, 'home.html')


def real(request):
    snss = Sns.objects.all()
    paginator = Paginator(snss, 3)#블로글 글 3개씩 나눠서 볼 수 있도록!
    page = request.GET.get('page')
    posts = paginator.get_page(page)  
    
    return render(request, 'real.html', {'snss': snss, 'posts':posts})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #auth.login(request, user)
            return redirect('correct')
        else:
            return redirect('uncorrect')
    return render(request, 'signup.html')

def correct(request):
    return render(request, 'correct.html')

def uncorrect(request):
    return render(request, 'uncorrect.html')

def detail(request, sns_id):
    sns_detail = get_object_or_404(Sns, pk = sns_id ) #get_object_or_404(Class, 검색조건) pk = Primary key

    return render(request, 'detail.html', {'sns' : sns_detail})    

# def new(request):
#     return render(request, 'new.html')

def create(request):
    # sns = Sns()
    # sns.title = request.GET['title']
    # sns.body = request.GET['body']
    # sns.date = timezone.datetime.now()
    # sns.save()    
         
    # return redirect('/realhome/' + str(sns.id)) #request()안에 주소는 작성한 db가 그 주소로 넘어가는 기능임
    if request.method == "POST":
        form = NewSns(request.POST)
        if form.is_valid:
            # post = form.save(commit=False)
            # post.date = datetime.now()  #원래는 datetime이 아니라 timezone이여씀
            form.save()
            return redirect('real')
    
    #글을 쓸 수 있는 페이지를 띄워주기 == GET
    else:
        #단순히 입력받을 수 있는 form을 띄워줘라
        form = NewSns()
        return render(request, 'new.html', {'form':form} )


def update(request, sns_id):
    #어떤 객체(고유pk)를 가져올지
    sns = get_object_or_404(Sns, pk = sns_id)

    #해당하는 블로그 객체(고유pk)에 맞는 입력공간 
    form = NewSns(request.POST, instance=sns)
    if form.is_valid():
        form.save()
        return redirect('real')
        
    return render(request, 'new.html', {'form':form} )


#특정객체를 지정한 후에 작업하기 때문에 기본적으로 인자를 두 개  받음.
def delete(request, sns_id):
    sns = get_object_or_404(Sns, pk = sns_id) 
    sns.delete()
    return redirect('home')






# Create your views here.
