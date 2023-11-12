from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Converstion
from .forms import ConverstionMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_converstion(request , item_pk):
    item  = get_object_or_404(Item , pk =item_pk)

    if item.owner == request.user:
        return render(request , 'dashboard/index.html' )
    
    converstions = Converstion.objects.filter(item = item). filter(members__in = [request.user.id])

    if converstions:
        return redirect('converstion:detail' , pk = converstions[0].pk)


    if request.method == 'POST':
        form = ConverstionMessageForm(request.POST)
        if form.is_valid():

            converstion = Converstion.objects.create(item=item)
            converstion.members.add(request.user)
            converstion.members.add(item.owner)
            converstion.save()

            converstion_message = form.save(commit=False)
            if isinstance(converstion, Converstion):  # check if converstion is an instance of Converstion
                converstion_message.conversation = converstion
                converstion_message.created_by = request.user
                converstion_message.save()
            
        return redirect('item:detail', pk=item.pk) 
    else:
        form = ConverstionMessageForm()

    return render(request, 'converstion/new.html', {'form': form})


@login_required
def inbox(request):
    converstions = Converstion.objects.filter(members__in=[request.user.id])
    return render(request, 'converstion/inbox.html', {'converstions': converstions})

@login_required
def detail (request , pk):
    converstion = Converstion.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = ConverstionMessageForm(request.POST)
        if form.is_valid():
            converstion_message = form.save(commit=False)
            if isinstance(converstion, Converstion):  # check if converstion is an instance of Converstion
                converstion_message.conversation = converstion
                converstion_message.created_by = request.user
                converstion_message.save()

        return redirect('converstion:detail', pk=pk)
    else:
        form = ConverstionMessageForm()

    return render(request, 'converstion/detail.html', {'converstion': converstion, 'form': form})

