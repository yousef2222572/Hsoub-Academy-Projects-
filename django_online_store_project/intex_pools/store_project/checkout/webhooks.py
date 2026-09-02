from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import stripe
from django.http import HttpResponse
from checkout import models
from store.models import Order, Product
from django.template.loader import render_to_string
from django.core.mail import send_mail
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

@csrf_exempt
def stripe_webhook(request):
    
    print('stripe webhook')
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']


    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECERT
        )
    except ValueError as e:
        print('Invalid payload')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print('Invalid signature')
        return HttpResponse(status=400)

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']  # contains a stripe.PaymentIntent
        print('payment_intent.succeeded')
        print(payment_intent.metadata)
        transaction_id = payment_intent.metadata['transaction']
        make_order(transaction_id)
    else:
        print('Unhandled event type {}'.format(event['type']))

    return HttpResponse(status=200)


@csrf_exempt
def paypal_webhook(sender, **kwargs):
    if sender.payment_status == ST_PP_COMPLETED:
        if sender.reciver_email != settings.PAYPAL_EMAIL:
            return
        print("payment seccuess !")
        make_order(sender.invoice)
valid_ipn_received.connect(paypal_webhook)

def make_order(transaction_id):
    transaction = models.Transaction.objects.get(pk=transaction_id)
    order = Order.objects.create(transaction=transaction)
    products = Product.objects.filter(pk__in=transaction.items)
    transaction.status = models.TransactionStatus.Completed
    transaction.save()

    for product in products:
        order.orderproduct_set.create(product_id=product.id, price=product.price)

    msg_html = render_to_string('emails/order.html', {
        'order': order,
        'products': products,
    })
    print(f'emil{transaction.customer_email} name {transaction.customer_name}')

    
    url = "https://api.brevo.com/v3/smtp/email" 

    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,

        "content-type": "application/json",
    }

    payload = {
        "sender": {
            "name": "intext",
            "email": "yousefmahmoud2y1@gmail.com"
        },
        "to": [
            {
                "email":transaction.customer_email,
                "name": transaction.customer_name
            }
        ],
        "subject": "order completed",
        
        "htmlContent": msg_html
        
    }


    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        print("Brevo status:", response.status_code)
        print("Brevo response:", response.text)
    except requests.RequestException:
        return False

    return response.status_code in (200, 201)

