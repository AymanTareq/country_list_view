from django.shortcuts import render, redirect
from django.views import View
from .models import CountryInfo
from django.views.generic import TemplateView

def index(request):
    countries = CountryInfo.objects.all()
    context = {
        'countries':countries,
    }
    return render(request,'main_app/index.html',context)



class AboutView(TemplateView):
    template_name = 'main_app/about.html'





#     lastimage= Image.objects.last()

#     imagefile= lastimage.imagefile


#     form= ImageForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST':
            
#         if form.is_valid():
#             form.save()
#         return redirect('img')
#     else:
#         pass

            
        # context= {'imagefile': imagefile,
#                 'form': form
#                 }
    
      
#     return render(request, 'app2/image.html', context)