from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SingleForm
from pytube import YouTube

# Create your views here.

def yousingle(request):
    return render(request, "youtube/youtube_single.html")

def yousinglepage(request, context = None):
    url = request.GET["single_link"]
    yt = YouTube(url)
    return render(request, "youtube/yousinglepage.html",{"yt": yt} )

def download(request, theid):
    url = "www.youtube.com/watch?v=" + theid
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    download_path = "C:\\Users\\FEST-TECH\\Downloads"
    [stream.download(download_path) for stream in streams]

    return redirect("/")
