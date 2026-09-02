from store.models import Category, Cart, Product

def store_website(request):
    print(request.user, type(request.user))

    categories = Category.objects.order_by('order')

    cart_products = []
    cart_total = 0

    cart = None

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).last()

    if cart:
        items = cart.items
        cart_products = Product.objects.filter(pk__in=items)

        for item in cart_products:
            cart_total += item.price

    return {
        'categories': categories,
        'cart_products': cart_products,
        'cart_total': cart_total,
    }