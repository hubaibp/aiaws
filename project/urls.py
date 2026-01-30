# """
# URL configuration for project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from appp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.Home.as_view()),
#     path('reg',views.Register.as_view(),name="register"),
#     path('list',views.ProductList.as_view(),name="list"),
#     path('productview/<int:id>',views.Productview.as_view(),name="view"),
#     path('delete/<int:id>',views.Productdlt.as_view(),name="delete"),
#     path('update/<int:id>',views.Productupdate.as_view(),name="update")
#     ]











from django.contrib import admin
from django.urls import path
from appp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view()),
    path('reg', views.Register.as_view(), name="register"),
    path('list', views.ProductList.as_view(), name="list"),
    path('productview/<int:id>', views.Productview.as_view(), name="view"),
    path('generate-ai/<int:id>', views.GenerateAIDescription.as_view(), name="generate_ai"),
    path('delete/<int:id>', views.Productdlt.as_view(), name="delete"),
    path('update/<int:id>', views.Productupdate.as_view(), name="update"),
    path('analyze/<int:id>', views.AnalyzeProduct.as_view(), name='analyze')

]
