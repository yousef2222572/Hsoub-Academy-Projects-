from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Slider, Category, Cart , User
from django.utils.translation import gettext as _
# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    models = Product.objects.select_related('vendor')
    slides = Product.objects.select_related('vendor')
    return render(request,'index.html', {'products': models, 'slides': slides})


def product(request, pid):
    where={'user_id':request.user}
    model = Product.objects.get(pk=pid)

    return render(
       request, 'product.html', {'product': model}
    )

def category(request, cid=None):
    cat = None
    if not cid:
        
        cid = request.GET.get('category')

            
    print(cid)
    query = request.GET.get('query')

    where = {}

    if cid: 
        cat = Category.objects.get(pk=cid)
        where['category_id'] = cid

    if query:
        where['name__icontains'] = query
    print(where)


    models = Product.objects.filter(**where)
    paginator = Paginator(models, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
         request, 'category.html', {'page_obj': page_obj, 'category': cat}
    )

@login_required
def cart(request):
    cart_model=Cart.objects.filter(user=request.user).last()

    return render(
        request, 'cart.html',{'cart_model':cart_model}
    )
        



@login_required
def checkout(request):


    user_info=request.user
    return render(
        request, 'checkout.html',{'user_info':user_info}
    )








def checkout_complete(request):
    Cart.objects.filter(user=request.user).delete()
    return render(
       request, 'checkout-complete.html'
    )






@login_required
def cart_update(request): 

    if request.user.is_authenticated:

        pid=request.POST.get('pid')
        sign=request.POST.get('sign')

        cart_model = Cart.objects.filter(user=request.user).last()

        if cart_model is None:
            return 404
            
            
            # cart_model = Cart.objects.create(user=request.user, items=[pid])
        elif pid in cart_model.items:
            if sign == 'true':
                cart_model.items[pid]['quantity'] += 1

            else:
                cart_model.items[pid]['quantity'] = max(1, cart_model.items[pid]['quantity'] - 1)

            cart_model.items[pid]["total_price"]=Product.objects.get(pk=pid).price * cart_model.items[pid]['quantity']
            cart_model.save()
        
        print('success')

        return JsonResponse({
            'status': 'success',
            'message': _('The product has been added to your cart'),
            'product_id':pid,
            'total_price': cart_model.items[pid]['total_price'],
            'quantity': cart_model.items[pid]['quantity']
        })
    else:
        return 404




def cart_add(request, pid):

    if request.user.is_authenticated:


        cart_model = Cart.objects.filter(user=request.user).last()

        if cart_model is None:
            cart_model = Cart.objects.create(user=request.user, items={pid:{
                "quantity": 1,
                "total_price": Product.objects.get(pk=pid).price
            }})
        elif pid not in cart_model.items:
            cart_model.items[pid] = {
                "quantity": 1,
                "total_price": Product.objects.get(pk=pid).price
            }
            cart_model.save()

        return JsonResponse({
            'message': _('The product has been added to your cart'),
            'items_count': len(cart_model.items)
        })
    else:
        return 404


@login_required
def cart_remove(request, pid):
    

    if not request.user.is_authenticated:
        return JsonResponse({})

    cart_model = Cart.objects.filter(user=request.user).last()

    if not cart_model:
        return JsonResponse({})


    cart_model.items.pop(pid,None)
    cart_model.save()

    return JsonResponse({
        'message': _('The product has been removed from your cart')
    })




