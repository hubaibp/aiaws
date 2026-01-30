# from django.shortcuts import render,redirect
# from django.views import View
# from .models import Product
# # Create your views here.


# class Home(View):
#     def get(self,request):
#         return render(request,"index.html")
    
# class Register(View):
#     def get(self,request):
#         return render(request,"register.html")   #load template
    
#     def post(self,request):
#         n=request.POST.get ("items")  #items in form / name in model/ n in django
#         c=request.POST.get("cost")
#         Product.objects.create(
#             name=n,
#             pricr=c
#         ) #create query 
#         return redirect("list")
          
# class ProductList(View):
#     def get(self,request):
#         x=Product.objects.all() #take all from Product Table
#         return render (request,"list.html",{"y":x}) #pass objects in x  to Y so we can use it in list.html
    
# class Productview(View):
#     def get(self,request,*args,**kwargs):
#         d=kwargs.get("id")  #fetch  the  id  from the url on clilkg it
#         v=Product.objects.get(id=d) #ORM to get details of that fetched  id from table
#         return render(request,"detail.html",{"det":v})
        
# class Productdlt(View):
#     def get(self,request,*args,**kwargs):
#         m=kwargs.get("id")
#         n=Product.objects.get(id=m)
#         n.delete()
#         return redirect("list") #give name in  url for that template page
    
    
# class Productupdate(View):
#     def get(self,request,*args,**kwargs):
#         h=kwargs.get("id")
#         o=Product.objects.get(id=h)
#         return render(request,"register.html",{"k":o})  
#     # u have 2  way either create a new html for edit  and pass the above key inside "value"
#     # or
#     # in the register form give "value" and  call inside  it 
    
#     def post(self,request,*args,**kwargs):
#         w=kwargs.get("id")
#         u=Product.objects.get(id=w)
#         u.name=request.POST.get("items")  #post.get name in (form)
#         u.pricr=request.POST.get("cost")
#         u.save()
#         return redirect("list")




from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .ai import generate_ai_description

class Home(View):
    def get(self, request):
        return render(request, "index.html")

class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        n = request.POST.get("items")
        c = request.POST.get("cost")
        Product.objects.create(name=n, pricr=c)
        return redirect("list")

class ProductList(View):
    def get(self, request):
        x = Product.objects.all()
        return render(request, "list.html", {"y": x})

class Productview(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get("id")
        product = Product.objects.get(id=pid)
        return render(request, "detail.html", {"det": product})

class GenerateAIDescription(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get("id")
        product = Product.objects.get(id=pid)

        # Always regenerate AI description
        product.ai_description = generate_ai_description(product.name, product.pricr)
        product.save()

        return redirect("view", id=pid)
    
    
class AnalyzeProduct(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs.get("id"))

        # Prompt for Groq
        prompt = f"""
        You are a data analyst for an e-commerce store.
        Product Name: {product.name}
        Price: ₹{product.pricr}
        Units Sold: {product.sold_units}
        Cost per unit: ₹{product.cost_per_unit}

        Give me:
        1. Estimated profit
        2. Suggestions to improve sales
        """
        from .ai import groq_analyze  # new helper
        analysis = groq_analyze(prompt)

        return render(request, "analysis.html", {"det": product, "analysis": analysis})

class Productdlt(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get("id")
        Product.objects.get(id=pid).delete()
        return redirect("list")

class Productupdate(View):
    def get(self, request, *args, **kwargs):
        pid = kwargs.get("id")
        product = Product.objects.get(id=pid)
        return render(request, "register.html", {"k": product})

    def post(self, request, *args, **kwargs):
        pid = kwargs.get("id")
        product = Product.objects.get(id=pid)
        product.name = request.POST.get("items")
        product.pricr = request.POST.get("cost")
        product.save()
        return redirect("list")
