from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item

@login_required
def home(request):
    query = request.GET.get('q')
    items = Item.objects.all()

    if query:
        items = items.filter(
            Q(name__icontains=query) |
            Q(category__category__icontains=query) |
            Q(color__color__icontains=query) |
            Q(zone__zone__icontains=query)
        )

    items = items.order_by('-created')[:6]

    return render(request, 'core/home.html', {
        'items': items,
        'query': query,
        'is_staff': request.user.is_staff
    })

@login_required
def item_found(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.user.is_staff:
        item.status = Item.Status.FOUND
        item.save()
    return redirect('home')