# Ex.05 Design a Website for Server Side Processing
## Date:04-04-2024

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
math.html
```
<!DOCTYPE html>
<html lang="en">
<head> 
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Surface Area of Right Cylinder</title>

    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        * {
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
        }

        body {
            background-color:blue;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .box {
            display: block;
            width: 500px;
            min-height: 280px;
            font-size: 15px;
            background-color: rgba(255, 255, 255, 0.492);
            animation: colorChange 10s infinite; 
        }

        .formelt {
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }

        h1 {
            color: black;
            text-align: center;
            padding-top: 15px;
        }
        h2{
            color:black;
        }
        input{
            margin: 5px;
            padding: 5px;
            border-radius: 5px;
            border: none;
        }
    </style>
</head>


<body>
    <div class="box">
        <h1>Surface Area of Right Cylinder</h1>
             <h2>        C NikeshKumar(212223040132)</h2>

        <form method="POST">
            <div class="formelt">
                Radius: <input type="text" name="Radius" value="{{r}}"> (in m)<br>
            </div>
            <div class="formelt">
                Height: <input type="text" name="Height" value="{{h}}"> (in m)<br>
            </div>                
            <div class="formelt">
                <input type="submit" value="Calculate"><br>
            </div>
            <div class="formelt">
                Area: <input type="text" name="area" value="{{area}}"> m<sup>2</sup><br>
            </div>
            {% csrf_token %}
        </form>
    </div>
</body>
</html>
```
views.py
```
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
```
urls.py
```
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/',views.surfacerightcylarea,name="surfaceareaofrightanglecylinder"),
    path('',views.surfacerightcylarea,name="surfaceareaofrightanglecylinderroot")
]
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-04-04 154741.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-04-04 154724.png>)

## RESULT:
The program for performing server side processing is completed successfully.
