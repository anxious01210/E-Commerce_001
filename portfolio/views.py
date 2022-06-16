from django.shortcuts import render

# Create your views here.
def work_view(request):
        context={"title":"Work"}
        return render(request,'portfolio/work.html',context)

def work_detailes_view(request):
        context={"title":"Work Details"}
        return render(request,'portfolio/work-detail.html',context)


