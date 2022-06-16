from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

# class DashboardView(View):
#     def get(self,request):
#         context = {"title":"Home"}
#         return render(request,"dashboard/index.html",context)
def home_view(request):
    context = {"title":"Home"}
    return render(request, 'dashboard/index.html', context)
class AboutView(View):
    def get(self,request):
        context = {"title":"About"}
        return render(request,"dashboard/about.html",context)
class ServicesView(View):
    def get(self,request):
        context = {"title":"Services"}
        return render(request,"dashboard/services.html",context)    
