from django.db import models

class UserInput(models.Model):
    EXERCISE_CHOICES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
    ]

    # Fields for user activity data
    id = models.AutoField(primary_key=True)
    sleep = models.DateTimeField(null=True)
    wake = models.DateTimeField(null=True)
    sunlight_start = models.DateTimeField(null=True)
    sunlight_end = models.DateTimeField(null=True)
    exercise_start = models.DateTimeField(null=True)
    exercise_end = models.DateTimeField(null=True)
    exercise_type = models.CharField(
        max_length=8,
        choices=EXERCISE_CHOICES,
        null=True
    )
    caffeine_intake = models.DateTimeField(null=True)

    def __str__(self):
        return f"UserInput {self.id}"
