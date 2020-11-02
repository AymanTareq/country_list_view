from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

def index(request):
    return render(request,'main_app/index.html')





# This is from app2 application
# from django.shortcuts import render, redirect
# from .models import Image
# from .forms import ImageForm

# def showimage(request):

#     lastimage= Image.objects.last()

#     imagefile= lastimage.imagefile


#     form= ImageForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST':
            
#         if form.is_valid():
#             form.save()
#         return redirect('img')
#     else:
#         pass

            
#         context= {'imagefile': imagefile,
#                 'form': form
#                 }
    
      
#     return render(request, 'app2/image.html', context)