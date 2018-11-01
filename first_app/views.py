from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
# Create your views here.

def index(request):
    # my_dict = {'insert_me':"Hello I am from views.py!"}
    # return render(request,'first_app/index.html',context=my_dict)

    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,'first_app/index.html',context=date_dict)