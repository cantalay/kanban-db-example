from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import WorkerList


def index(request):
    posts = WorkerList.objects.all()

    if request.method == 'POST':
        if request.POST.get('govde') and request.POST.get('kece'):
            post = WorkerList()
            post.govde_boyut = request.POST.get('govde')
            post.kece_boyutu = request.POST.get('kece')
            post.mil_boyutu = request.POST.get('mil')
            post.pul_boyutu = request.POST.get('pul')
            post.o_ring = request.POST.get('oring')
            #ADET
            post.save()
            return render(request, 'createpost.html', {'posts': posts})
            # return HttpResponse(request, 'templates/createpost.html/')
            # return render(request, 'createpost.html/')
        else:
            # return HttpResponse("tg2")
            return render(request, 'createpost.html')
    return render(request, 'createpost.html', {'posts': posts})

    # return HttpResponse("<h1> this is a kanban homepage")


def makeEdit(request, pk):
    post = get_object_or_404(WorkerList, pk = pk)
    if request.method == 'POST':
        post = WorkerList(request.POST , pk =pk)
        post.govde_boyut = request.POST.get('govde')
        post.kece_boyutu = request.POST.get('kece')
        post.mil_boyutu = request.POST.get('mil')
        post.pul_boyutu = request.POST.get('pul')
        post.o_ring = request.POST.get('oring')
        # ADET
        post.save()
        return render(request, 'editPage.html', {'post': post})
    return render(request, 'editPage.html', {'post': post})


def tabletScreen(request):
    return HttpResponse("Selam Tablet")


def createWork(request):
    posts = WorkerList.objects.all()


    if request.POST.get('AddWork'):
        post = WorkerList()
        return HttpResponse("can")
        if request.POST.get('mil') == "V1D":
            V1D = ["SC1","Small","Small","Small"]
            govdeInfo = "SC1"
            keceInfo = "Small"
            pulInfo = "Small"
            oringInfo = "Small"
            if request.POST.get('AddWork'):
                post.mil_boyutu = "V1D"
                post.govde_boyut = V1D[0]
                post.kece_boyutu = V1D[1]
                post.pul_boyutu = V1D[2]
                post.o_ring = V1D[3]
                post.save()
                return render(request, 'createWork.html')

            return render(request, 'createWork.html', {'V1D': V1D})

        # ADET

        return HttpResponse("Oldu")
        # return HttpResponse(request, 'templates/createpost.html/')
        # return render(request, 'createpost.html/')
    else:
        # return HttpResponse("tg2")
        return render(request, 'createWork.html', {'posts': posts})



def arduino(request):
    post = WorkerList()
    if (request.GET['model'] == '1'):
        modelNumber = request.GET['model']
        V1D = ["SC1","Small","Small","Small"]
        post.govde_boyut = V1D[0]
        post.kece_boyutu = V1D[1]
        post.pul_boyutu = V1D[2]
        post.o_ring = V1D[3]
        post.save()
        return HttpResponse('model : %s' % (modelNumber))
    return HttpResponse('nope')
