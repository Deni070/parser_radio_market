from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video
from .parser_for_audio import postRequest


# Create your views here.

def main_page(request):
    context = {}
    if request.POST and request.FILES:
        if request.FILES.get('music'):
            print(request.FILES.get('music').temporary_file_path())
            info = postRequest(request.FILES.get('music').temporary_file_path())
            context.update({'info':info})
    return render(request, 'index.html', context)



def file_page(request):
    return render(request, 'parser_names.html')

def text_page(request):
    return render(request, 'parser_text.html')
