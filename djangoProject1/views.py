from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

last_id = 13
product_list = [
        {'id': 11, 'name': 'Iphone', 'image': 'https://cdn.mos.cms.futurecdn.net/NSjDb8Q988u8D4c5uaRN3J.jpg', 'done': True},
        {'id': 12, 'name': 'Samsung', 'image': 'https://images.samsung.com/sg/smartphones/galaxy-s20/buy/1-2-hubble-x1-y2-pink-blue-family-mobile-img.jpg', 'done': False},
        {'id': 13, 'name': 'Xiaomi', 'image': 'https://images-na.ssl-images-amazon.com/images/I/91AHzW462WL._AC_SX342_.jpg', 'done': False},
    ]

def homepage(request):
    return HttpResponse("Homepage")

def shoplist(request):

    return render(request,'shoplist.html', {'products': product_list})

def addProduct(request):
    return render(request, 'add-product-form.html')

def saveProduct(request):
    global last_id

    last_id +=1
    new_product = {
        'id': last_id,
        'name': request.GET['product_name'],
        'image': '',
        'done': False
    }

    product_list.append(new_product)
    return HttpResponseRedirect('/shoplist')

def updateProducts(request):
    for p in product_list:
        try:
            checkbox = request.GET['product_' + str(p['id'])]
            p['done'] = True
        except:
            p['done'] = False
    return HttpResponseRedirect('/shoplist')
