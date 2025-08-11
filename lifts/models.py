from django.db import models

# Create your models here.


class WorkoutLift(models.Model):
    name = models.CharField(max_length=200)
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    timeCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LiftData(models.Model):
    workout = models.ForeignKey(WorkoutLift, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    timeCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
