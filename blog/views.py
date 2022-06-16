from django.shortcuts import render

# Create your views here.
def blog_view(request):
    context = {}
    return render(request, 'blog/blog-grid.html', context)

def list_view(request):
    context = {}
    return render(request, 'blog/blog-listing.html', context)

def single_post_view(request):
    context = {}
    return render(request, 'blog/blog-single-post.html', context)