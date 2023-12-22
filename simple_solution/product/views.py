import os
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

from product.models import Item

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


@csrf_exempt
def get_stripe_session(request, id):
    item = get_object_or_404(Item, id=id)
    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 100),
        currency=item.currency,
        metadata={'item_id': item.id},
    )

    return JsonResponse({'session_id': intent.client_secret})


def item_detail(request, id):
    """Представление продукта"""
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})
