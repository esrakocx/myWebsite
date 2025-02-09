from django.shortcuts import render
from .models import Post, Portfolio

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def resume(request):
    return render(request, 'blog/resume.html')

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return render(request, 'blog/contact.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'blog/portfolio.html', {'portfolios': portfolios})

def portfolio_detail(request, id=None):
    return render(request, 'blog/portfolio-details.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def starter_page(request):
    return render(request, 'blog/starter-page.html')