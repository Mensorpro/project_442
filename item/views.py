from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from .models import Item , Category
from .form import  EditItemForm, NewItemForm
from django.shortcuts import render, redirect

def items(request):
    categories = Category.objects.all() 
    search = request.GET.get('search', '')
    category = request.GET.get('category', 0)
    min_price = request.GET.get('min_price',0)
    max_price = request.GET.get('max_price', 0)  

    request.session['search'] = search
    request.session['category'] = category
    request.session['min_price'] = min_price
    request.session['max_price'] = max_price

    if category !=0 and min_price!='' and max_price!='' and  category != '' and min_price != 0 and max_price != 0:
        min_price =int(min_price)
        max_price =int(max_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__gte=min_price, price__lte=max_price, is_sold=False, category=category)
    elif category !=0 and min_price!='' and category != '' and min_price != 0:
        min_price =int(min_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__gte=min_price, is_sold=False, category=category)
    elif category !=0 and max_price!='' and category != '' and max_price != 0:
        max_price =int(max_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__lte=max_price, is_sold=False, category=category)
    elif category != 0 and category != '': 
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search), is_sold=False, category=category)
    elif min_price!=''and min_price!= 0 and max_price =='':
        min_price =int(min_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__gte=min_price, is_sold=False)
    elif max_price!='' and max_price!= 0 and min_price=='':
        max_price =int(max_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__lte=max_price, is_sold=False)
    elif min_price!='' and max_price!='' and min_price!= 0 and max_price!= 0:
        min_price =int(min_price)
        max_price =int(max_price)
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search),price__gte=min_price, price__lte=max_price, is_sold=False)
    elif search:
        items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search), is_sold=False) 
    else:
        items = Item.objects.filter(is_sold=False)

    return render(request, 'item/items.html', {'items': items, 'search': search, 'categories': categories})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:6]
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form':form,
        'title':'New Item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()  
            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title':'Edit Item',
    })