from django.shortcuts import render
from django.views.decorators.cache import cache_page

from app.core.models import Background, Category, Product


@cache_page(60 * 15)  # 15 minutes
def index(request):
    products = Product.objects.filter(active=True).prefetch_related("category")
    filters = Category.objects.all()
    background = Background.objects.filter(active=True).first()

    return render(
        request,
        "index.html",
        context={"products": products, "filters": filters, "background": background},
    )
