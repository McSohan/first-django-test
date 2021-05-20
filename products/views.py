from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, response


from .models import Product
from .forms import ProductForm

# Create your views here.
def search_view (request, *args, **kwargs):
    #return HttpResponse("<h1>Hello</h1>")
    #query = request.GET.get('q')
    #qs = Product.objects.filter(title__icontains=query[0])
    #print(qs)
    #context = {"name":"sohan", "query":query}
    context = {"name":"sohan"}
    return render (request, "home.html", context)

# def product_create_request (request, *args, **kwargs):
#     print(request.POST)
#     print (request.GET)
#     if request.method == "POST":
#         postdata = request.POST or None
#         if postdata != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 print (my_form.cleaned_data.get("title"))
#     return render (request, "products/forms.html", {})

def product_create_request (request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        Product.objects.create (**data) #unpacking
        #redirect ()
        form = ProductForm()
    return render (request, "products/forms.html", {"form":form})

def product_detail_view (request, pk):
    try:
        obj = Product.objects.get(id = pk)
    except Product.DoesNotExist:
        raise Http404
    #return HttpResponse(f"Product id {obj.id=}")
    return render (request, "products/detail.html", {"object":obj})

def product_list_view (request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list":qs} #context dictionary
    return render (request, "products/list.html", context)

def product_detail_view_api (request, pk):
    try:
        obj = Product.objects.get(id = pk)
    except Product.DoesNotExist:
        return JsonResponse({"message":"Not found"}, status=404)
    return JsonResponse ({"id":obj.id})
