import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
import requests
django.setup()
from first_app.models import ScheduleRecord



def populate(text,gr,cour):

    for entry in text['schedule']:

        ob = ScheduleRecord.objects.get_or_create(course = cour,dayWeek = entry,teacher = text['schedule'][entry]['teacher'],discipline=text['schedule'][entry]['discipline'],group=gr,classroom = text['schedule'][entry]['classroom'],isLecture=text['schedule'][entry]['isLecture'])[0]

if __name__ == '__main__':
    print("populating script!")
    text = requests.get('http://rozklad.nau.edu.ua/api/v1/schedule/2/4/2/24/2').json()
    populate(text,24,4)
    print("populating complete")
