from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique =True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length = 264,unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class ScheduleRecord(models.Model):
    dayWeek = models.CharField(max_length=264)
    discipline = models.CharField(max_length=264)
    group = models.CharField(max_length=264)
    teacher = models.CharField(max_length=264)
    classroom = models.CharField(max_length=264)
    isLecture = models.BooleanField()
    course = models.CharField(max_length=264)
    def __str__(self):
        return self.course+self.group +' ' + self.dayWeek
