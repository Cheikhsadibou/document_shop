from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from storage.models import Article, Box, Product


# Create your views here.

def index(request):
    products = Product.objects.all()

    return render(request, 'storage/index.html',
                  context={"products": products}
                  )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'storage/detail.html', context={"product": product})


def add_to_box(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    box, _ = Box.objects.get_or_create(user=user)
    article, created = Article.objects.get_or_create(user=user,
                                                     ordered=False,
                                                     product=product)

    if created:
        box.articles.add(article)
        article.save()
    else:
        article.stock += 1
        article.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def box_user(request):
    box = get_object_or_404(Box, user=request.user)
    return render(request, 'storage/box.html', context={
        "articles": box.articles.all()
    }
    )


def delete_box(request):
    if box := request.user.box:
        box.articles.all().delete()
        box.delete()

    return redirect("index")
