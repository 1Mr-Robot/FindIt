from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Item
from .forms import LostItemForm

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

    items = items.order_by('-created')

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

@login_required
def report_object(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            time_threshold = timezone.now() - timedelta(minutes=5)
            similar_items = Item.objects.filter(
                creator_user=request.user,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                color=form.cleaned_data['color'],
                zone=form.cleaned_data['zone'],
                status=Item.Status.LOST,
                created__gte=time_threshold
            )
            
            if similar_items.exists():
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': 'duplicate'})
                return render(request, "core/form_lost_item.html", {"form": form, "error": "Ya has enviado un reporte idéntico recientemente."})
            
            item = form.save(commit=False)
            item.creator_user = request.user
            item.status = Item.Status.LOST
            item.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('home')
    else:
        form = LostItemForm()
    return render(request, "core/form_lost_item.html", {"form": form})