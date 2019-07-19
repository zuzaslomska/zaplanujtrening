from django.shortcuts import render
from Zaplanujtrening import urls
from django.http import request
from django.views import View
from .models import UserFile

class MainSite(View):
    def get(self,request):
        return render(request,"__base1__glowna.html")


# Na podstawie https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/
from django.http import HttpResponseRedirect
from .forms import ModelFormWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            model_instance = form.save()
            return HttpResponseRedirect('/show_some_upload/{}/{}'.format(
                model_instance.id,'jakies_bzdury_do_seo.html'))
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})

def upload_view(request,uid,seo_path):
    c = {'uid':uid,'seo_path':seo_path}
    uf = UserFile.objects.get(id=uid)
    c['photo_entity'] = uf
    print(dir(uf.photo))
    return render(request, 'upload_view.html', c)
