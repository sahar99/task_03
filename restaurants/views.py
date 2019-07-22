from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
       "my_list": [
        {"restaurant_name":"A" ,"food_type":"vegan"},
        {"restaurant_name":"B", "food_type":"seaFood"},
        {"restaurant_name":"C", "food_type":"burgers"},


        ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":
        {"restaurant_name":"A" ,"food_type":"vegan"},
       
    }
    return render(request, 'detail.html', context)
