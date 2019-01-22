from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import partsInformation, inventoryControl, workOrder, workOrder1, workOrder2, workOrder3, workerInformation, \
    stationInformation, finishedWork
from django.core import serializers
import json


def index(request):

    if request.user.is_authenticated:
        return render(request, 'index.html', {'form': form})
    else:
        return render(request, 'login.html')



def tabletScreen1(request):
    try:
        status = get_object_or_404(stationInformation, pk=1)
        print(status)
    except get_object_or_404(stationInformation, pk=1).DoesNotExist:
        return HttpResponse("No id mached")
    if status.station_state:
        workerPK = status.current_worker
        post = get_object_or_404(workerInformation, pk=workerPK)

        try:
            orderInformation = workOrder1.objects.order_by('create_date')
        except workOrder1.DoesNotExist:
            orderInformation = None
            return HttpResponse("All work is finished.")
        parts = "Null"
        if orderInformation[0].model_type == "1":
            parts = get_object_or_404(partsInformation, pk=1)
        if orderInformation[0].model_type == "2":
            parts = get_object_or_404(partsInformation, pk=2)
        if orderInformation[0].model_type == "3":
            parts = get_object_or_404(partsInformation, pk=3)
        if orderInformation[0].model_type == "4":
            parts = get_object_or_404(partsInformation, pk=4)
        if orderInformation[0].model_type == "5":
            parts = get_object_or_404(partsInformation, pk=5)
        if orderInformation[0].model_type == "6":
            parts = get_object_or_404(partsInformation, pk=6)
        if orderInformation[0].model_type == "7":
            parts = get_object_or_404(partsInformation, pk=7)
        if orderInformation[0].model_type == "8":
            parts = get_object_or_404(partsInformation, pk=8)
        return render(request, 'tabletscreen.html', {'posts': post, 'order': parts})
    else:
        num = "1"
        return render(request, 'readID.html',{'num': num})


def tabletScreen2(request):
    status = get_object_or_404(stationInformation, pk=2)
    if status.station_state:
        workerPK = status.current_worker
        post = get_object_or_404(workerInformation, pk=workerPK)
        orderInformation = workOrder2.objects.order_by('create_date')
        parts = "Null"
        if orderInformation[0].model_type == "1":
            parts = get_object_or_404(partsInformation, pk=1)
        if orderInformation[0].model_type == "2":
            parts = get_object_or_404(partsInformation, pk=2)
        if orderInformation[0].model_type == "3":
            parts = get_object_or_404(partsInformation, pk=3)
        if orderInformation[0].model_type == "4":
            parts = get_object_or_404(partsInformation, pk=4)
        if orderInformation[0].model_type == "5":
            parts = get_object_or_404(partsInformation, pk=5)
        if orderInformation[0].model_type == "6":
            parts = get_object_or_404(partsInformation, pk=6)
        if orderInformation[0].model_type == "7":
            parts = get_object_or_404(partsInformation, pk=7)
        if orderInformation[0].model_type == "8":
            parts = get_object_or_404(partsInformation, pk=8)
        return render(request, 'tabletscreen2.html', {'posts': post, 'order': parts})
    else:
        num = 2
        return render(request, 'readID.html',{'num': num})


def tabletScreen3(request):
    status = get_object_or_404(stationInformation, pk=3)
    if status.station_state:
        workerPK = status.current_worker
        post = get_object_or_404(workerInformation, pk=workerPK)
        orderInformation = workOrder3.objects.order_by('create_date')
        parts = "Null"
        if orderInformation[0].model_type == "1":
            parts = get_object_or_404(partsInformation, pk=1)
        if orderInformation[0].model_type == "2":
            parts = get_object_or_404(partsInformation, pk=2)
        if orderInformation[0].model_type == "3":
            parts = get_object_or_404(partsInformation, pk=3)
        if orderInformation[0].model_type == "4":
            parts = get_object_or_404(partsInformation, pk=4)
        if orderInformation[0].model_type == "5":
            parts = get_object_or_404(partsInformation, pk=5)
        if orderInformation[0].model_type == "6":
            parts = get_object_or_404(partsInformation, pk=6)
        if orderInformation[0].model_type == "7":
            parts = get_object_or_404(partsInformation, pk=7)
        if orderInformation[0].model_type == "8":
            parts = get_object_or_404(partsInformation, pk=8)
        return render(request, 'tabletscreen3.html', {'posts': post, 'order': parts})
    else:
        num = 3
        return render(request, 'readID.html',{'num': num})


def orderList(request):
    posts = workOrder.objects.order_by('create_date')

    return render(request, 'orderList.html', {'posts': posts})


def createWork(request):
    if request.method == 'POST':
        if request.POST.get('model_type') and request.POST.get('customer_name'):
            post = workOrder()
            post.model_type = request.POST.get('model_type')
            post.customer_name = request.POST.get('customer_name')
            post.deadline = request.POST.get('deadline')
            # post.quantity = request.POST.get('quantity')
            post.save()
            post1 = workOrder1()
            post1.pk=post.pk
            post1.model_type = request.POST.get('model_type')
            post1.customer_name = request.POST.get('customer_name')
            post1.deadline = request.POST.get('deadline')
            # post1.quantity = request.POST.get('quantity')
            post1.save()
            post2 = workOrder2()
            post2.pk = post.pk
            post2.model_type = request.POST.get('model_type')
            post2.customer_name = request.POST.get('customer_name')
            post2.deadline = request.POST.get('deadline')
            # post2.quantity = request.POST.get('quantity')
            post2.save()
            post3 = workOrder3()
            post3.pk = post.pk
            post3.model_type = request.POST.get('model_type')
            post3.customer_name = request.POST.get('customer_name')
            post3.deadline = request.POST.get('deadline')
            # post3.quantity = request.POST.get('quantity')
            post3.save()
            return render(request, 'createWork.html')
        else:
            return HttpResponse("noooldu anlamadım")
    else:
        return render(request, 'createWork.html')
def tabletState(request):
    station = request.GET.get('station')
    print(station)
    post = get_object_or_404(stationInformation, pk=station)
    print(post.station_state)
    return HttpResponse(post.station_state)

def makeEdit(request, pk):
    post = get_object_or_404(workOrder, pk=pk)
    post1 = get_object_or_404(workOrder1, pk=pk)
    post2 = get_object_or_404(workOrder2, pk=pk)
    post3 = get_object_or_404(workOrder3, pk=pk)
    if request.method == 'POST':
        post = workOrder(request.POST, pk=pk)
        post.customer_name = request.POST.get('customer_name')
        post.model_type = request.POST.get('model_type')
        post.quantity = request.POST.get('quantity')
        post.deadline = request.POST.get('deadline')
        post.save()
        post1 = workOrder1(request.POST, pk=pk)
        post1.customer_name = request.POST.get('customer_name')
        post1.model_type = request.POST.get('model_type')
        post1.quantity = request.POST.get('quantity')
        post1.deadline = request.POST.get('deadline')
        post1.save()
        post2 = workOrder2(request.POST, pk=pk)
        post2.customer_name = request.POST.get('customer_name')
        post2.model_type = request.POST.get('model_type')
        post2.quantity = request.POST.get('quantity')
        post2.deadline = request.POST.get('deadline')
        post2.save()
        post3 = workOrder3(request.POST, pk=pk)
        post3.customer_name = request.POST.get('customer_name')
        post3.model_type = request.POST.get('model_type')
        post3.quantity = request.POST.get('quantity')
        post3.deadline = request.POST.get('deadline')
        post3.save()
        return render(request, 'editPage.html', {'post': post})
    return render(request, 'editPage.html', {'post': post})


def workerCard(request):  # işçi girişi
    print(request.GET.get('workerid'))
    print(request.GET.get('station'))
    if request.GET.get('workerid') and request.GET.get('station'):
        getworkerpk = request.GET.get('workerid')
        workerInf = get_object_or_404(workerInformation, pk=getworkerpk)
        getstationpk = request.GET.get('station')
        status = get_object_or_404(stationInformation, pk=getstationpk)
        status.station_state = True
        status.current_worker = request.GET.get('workerid')
        status.save()
        if getstationpk == "1":
            modelsData = workOrder1.objects.all()
            return HttpResponse(modelsData[0].model_type)
        if getstationpk == "2":
            modelsData = workOrder2.objects.all()
            return HttpResponse(modelsData[0].model_type)
        if getstationpk == "3":
            modelsData = workOrder3.objects.all()
            return HttpResponse(modelsData[0].model_type)

        return HttpResponse("Success"+getstationpk)
    else:
        return HttpResponse("more information needed.")


def workData(request):


    station = request.GET.get('station')
    if station == "1":
        post = workOrder1.objects.order_by('create_date')
        return HttpResponse(post[0].model_type)
    if station == "2":
        post = workOrder2.objects.order_by('create_date')
        return HttpResponse(post[0].model_type)
    if station == "3":
        post = workOrder3.objects.order_by('create_date')
        return HttpResponse(post[0].model_type)
    return HttpResponse("404 Error")


def elapsedTime(request):
    if request.GET.get('time') and request.GET.get('station'):
        station = request.GET.get('station')
        if station == "1":
            post = workOrder1.objects.order_by('create_date')
            gets = finishedWork()
            id = post[0].pk
            gets.pk = id
            gets.model_type = post[0].model_type
            gets.elapsed_time = request.GET['time']
            gets.work_station = "1"
            post[0].delete()
            gets.save()
        if station == "2":
            post = workOrder2.objects.order_by('create_date')
            gets = finishedWork()
            id = post[0].pk
            gets.pk = id
            gets.model_type = post[0].model_type
            gets.elapsed_time = request.GET['time']
            gets.work_station = "2"
            post[0].delete()
            gets.save()
        if station == "3":
            post = workOrder3.objects.order_by('create_date')
            gets = finishedWork()
            id = post[0].pk
            gets.pk = id
            gets.model_type = post[0].model_type
            gets.elapsed_time = request.GET['time']
            gets.work_station = "3"
            post[0].delete()
            gets.save()
    else:
        return HttpResponse("Something went wrong...")


def workerID(request):
    return HttpResponse("")

def finishedList(request):
    posts = finishedWork.objects.all()

    return render(request, 'finishedWork.html', {'posts': posts})



def stockLevel(request):
    if request.GET.get('level') and request.GET.get('station')and request.GET.get('product'):
        post = inventoryControl()
        post.station = request.GET.get('station')
        post.inventory_amount = request.GET.get('level')
        post.model_number= request.GET.get('product')
        post.save()
        return HttpResponse("IStock Control!")

    return HttpResponse("")


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            # return redirect('articles:list')
            HttpResponse("OK")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


"""
from .models import WorkerList
from .models import FinishedWork
from django.http import JsonResponse
from django.core import serializers
import json
import subprocess


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
    post = WorkerList.objects.order_by('created_date')

    return render(request, 'tbScreen.html', {'posts': post})


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
    post = WorkerList.objects.order_by('created_date')
    gets = FinishedWork()
    id = post[0].id
    gets.model_number = post[0].govde_boyut
    gets.elapsed_time = request.GET['elapsed']
    post[0].delete()
    if (gets.elapsed_time !="\r\n" or gets.elapsed_time !="\n" or gets.elapsed_time !="\r" ):
        gets.save()
    return HttpResponse(id)

def rprogramming(request):
    post = WorkerList.objects.order_by('created_date')[0]

    data = {'post[0].o_ring': 'post[0].pul_boyutu', 'post[0].pul_boyutu': 'post[0].o_ring'}
   # json_data = json.dumps(data)
    #posts = request.POST.get('elapsed')
    data = serializers.serialize("json", WorkerList.objects.first())
    return HttpResponse(post[0].govde_boyut)
    #return render(request, 'rHtml.html',{'posts': posts})
"""
