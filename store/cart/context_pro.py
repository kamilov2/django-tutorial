from .views import cart_init


def cart(request):
    context = {
        "cart": cart_init(request)
    }
    return context