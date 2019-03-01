from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog # 이거써서 가져오기
# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    #몇번객체애 담아 pk 는 프라이머리 키 이거 기준찾아가라
    return render(request, 'detail.html', {'details':details})# 이거 왜쓰는거임?

def new(request): #뉴페이지 문서 뛰어주는거
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수 
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
