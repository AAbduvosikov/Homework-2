from django.shortcuts import render


def avtomobiles(request):
    content = {
        'name':'Malibu', 'color':'qora', 'price':'34000','mark':'sedan', 'image':'images/222.jpg' }

    return render(request,'avtos.html',{'context':content})
