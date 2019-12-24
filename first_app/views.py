from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage,ScheduleRecord
from scheduleObjects import populate
import json
import requests
# Create your views here.

def index(request):

    tmp = requests.get('http://rozklad.nau.edu.ua/api/v1/groups/2').json()
    for i in tmp["groups"]:
        group = i["GRP"]
        course = i["COURSE"]
        stream = i["STRM"]
        print(group,course,stream)
        if course == 4:
            text = requests.get('http://rozklad.nau.edu.ua/api/v1/schedule/2/'+str(course)+'/'+str(stream)+'/'+str(group)+'/2').json()
            #populate(text,group,course)

    sched_list = ScheduleRecord.objects.order_by('dayWeek')
    sched_dict = {'schedule_records':sched_list,'group_name':'24','course_name':'4'}
    '''
    TODO: New concept is to transform "text" to "sched_dict" without models.
    1) transform it
    2) edit index.html 
    '''
    return render(request,'first_app/index.html',context=sched_dict)
