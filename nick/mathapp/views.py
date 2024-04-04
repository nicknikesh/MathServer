from django.shortcuts import render

def surfacerightcylarea(request):
    context = {}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    
    if request.method == 'POST':
        print("POST method is used")
        r = float(request.POST.get('Radius', '0'))
        h = float(request.POST.get('Height', '0'))
        
        print('request =', request)
        print('Radius =', r)
        print('Height =', h)
        
        surfacearea = (2 * 3.14 * r * h) + (2 * 3.14 * r ** 2)
        context['area'] = surfacearea
        context['r'] = r
        context['h'] = h
        
        print('surface area =', surfacearea)
        
    return render(request, 'mathapp/math.html', context)