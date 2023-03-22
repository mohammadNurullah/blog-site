from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def archives(request):
    return render(request, 'pages/archives.html')

def posts(request):
    return render(request, 'pages/posts.html')

def contact(request):
    return render(request, 'pages/contact.html')

# def listing(request, listing_id):
#     return render(request, 'pages/listing.html')
