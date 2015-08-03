from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
import json
from django import forms
from django.core.files.images import get_image_dimensions
import datetime
import subprocess
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.

class ImageForm(forms.Form):
    file = forms.ImageField()

    image_size = None  # (width, height)

    def clean_file(self):
        picture = self.cleaned_data.get("file")
        if not picture:
            raise forms.ValidationError("no image!")
        else:
            image_size = get_image_dimensions(picture)
            self.image_size = image_size
        return picture


@csrf_exempt
def save_file_to_liaomeizhi(request):
    '''
    post
    scp file to liaomeizhi server
    '''
    form = ImageForm(request.POST, request.FILES)

    if not form.is_valid():
        return HttpResponseBadRequest(content=json.dumps(form.errors, ensure_ascii=False))

    uploaded = form.cleaned_data['file']
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = timestamp + '_' + uploaded.name

    local_file = default_storage.save(filename, ContentFile(uploaded.read()))

    comm = 'scp /root/workspace/xiaohua/media/' + local_file + \
           ' root@liaomeizhi.com:/home/liaomeizhi_www/static/images/children/' + filename

    try:
        out = subprocess.check_output(comm, shell=True)
    except:
        return u'cant scp'

    file_url = 'http://static.liaomeizhi.com/images/children/' + filename

    return HttpResponse(json.dumps({"file": file_url}),
                        content_type="application/json")
