from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib import messages

from .models import *
from .forms import *

from .util import *

# Create your views here.
def index(request):
    brands = Brand.objects.all()
    context = {"brands": brands}
    return render(request, 'nostr/index.html', context)

def brand_create(request):

    if request.POST:
        form = BrandForm(request.POST)

        if not form.is_valid():
            ctx = {'form' : form}
            return render(request, 'nostr/brand/form.html', ctx)

        brand = form.save(commit=False)
        brand_keypair = create_keypair()
        brand.public_key = brand_keypair["pub_key"]
        brand.private_key = brand_keypair["private_key"]
        brand.save()
        messages.success(request, "Brand created successfully.")
        return redirect(reverse('index'))
    else:
        form = BrandForm()
        ctx = { 'form' : form }
        return render(request, 'nostr/brand/form.html', ctx)

def brand_update(request, brand_pk):

    if request.POST:
        brand = get_object_or_404(Brand, id=brand_pk)
        form = BrandForm(request.POST, instance=brand)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'nostr/brand/form.html', ctx)

        brand = form.save()

        messages.success(request, "Brand updated successfully.")
        return redirect(reverse('index'))

    else:
        brand = get_object_or_404(Brand, id=brand_pk)
        form = BrandForm(instance=brand)
        ctx = { 'form': form}
        return render(request, 'nostr/brand/form.html', ctx)

def publish_post(request):

    if request.POST:
        brand_id = int(request.POST["brand"])
        brand = Brand.objects.get(id=brand_id)

        if brand_id is None:
            messages.error(request, "Post failed.")
            return render(request, 'nostr/publish/post.html', ctx)

        content = request.POST["content"]
        brand = Brand.objects.get(id=brand_id)
        #add tag support later
        tags = []

        nostr_event = publish_short_note(brand.private_key, brand.public_key, "wss://relay.snort.social", content, [tags])
        print(nostr_event)


        post = Post.objects.create(
                brand=brand,
                nostr_id=nostr_event["event"]["id"]).save()

        messages.success(request, "Post created successfully.")
        return redirect(reverse('index'))
    else:
        brands = Brand.objects.all()
        ctx = { "brands":brands }
        return render(request, 'nostr/publish/post.html', ctx)

def publish_blog(request):
    if request.POST:
        brand_id = int(request.POST["brand"])
        brand = Brand.objects.get(id=brand_id)

        if brand_id is None:
            messages.error(request, "Blog failed.")
            return render(request, 'nostr/publish/blog.html', ctx)

        content = request.POST["content"]
        brand = Brand.objects.get(id=brand_id)
        #add tag support later
        tags = []

        nostr_event = publish_longform_note(brand.private_key, brand.public_key, "wss://relay.snort.social", content, [tags])
        print(nostr_event)


        blog = Blog.objects.create(
                brand=brand,
                nostr_id=nostr_event["event"]["id"]).save()

        messages.success(request, "Blog created successfully.")
        return redirect(reverse('index'))
    else:
        brands = Brand.objects.all()
        form = BlogForm()
        ctx = { "brands":brands, "form":form }
        return render(request, 'nostr/publish/blog.html', ctx)

