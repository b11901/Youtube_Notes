from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from index.models import Notes,Liked

# Create your views here.
def index(request):
    return render(request,'index/index.html')

def search(request):
    from . import search_yt 
    #list for thumbnail src
    thumb = []
    link,description,title,thumbnail_link = search_yt.search_youtube(request.POST['query'])

    #Preparing the thumbnail src
    for thumbnail in thumbnail_link:
        thumb.append("http://img.youtube.com/vi/"+thumbnail[9:]+"/hqdefault.jpg")
    #Preparing the base link
    base_link = []
    for l in link:
        base_link.append(l[28:])

    zip_elem = zip(title,description,link,thumb,base_link)
    context = {
        'query' : request.POST['query'],
        'zip_elem' : zip_elem,
        'range' : range(len(title)),
    }
    return render(request,'index/search.html',context)

#Video Template
def video(request,link):
    base_link = 'https://www.youtube.com/embed/'
    costum_link = 'http://127.0.0.1:8000/video/' + link
    link = base_link + link
    context = {
        'link' : link,
    }
    if(request.user):
        notes = Notes.objects.filter(user=request.user,url=costum_link)
        print(costum_link)
        context.update(
            {
                "note" : notes
            }
        )
    return render(request,'index/video.html' ,context)


@login_required
def saveNote(request):
    if request.method == 'POST':
        note = request.POST['note'],
        video_url = request.META.get('HTTP_REFERER')
        #print(note)
        #print(request.user.username)
        note = Notes(user=request.user, note=note, url=video_url)
        note.save()
        print(request.path_info)
    return HttpResponseRedirect(video_url)

def likeVideo(request,link):
    like = Like(user=request.user,url=link)
    like.save()

def test(request):
    return render(request, 'index/test.html',{})