from .cart import Cart

# Create context processor so our cart works on all sites
def cart(request):
    # Return the default data from our cart
    return {'cart': Cart(request)}