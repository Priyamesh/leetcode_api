from django.db import models

# Create your models here.


class Questions(models.Model):

    DIFFCULTY_CHOICE = (
        ("EASY", "EASY"),
        ("MEDIUM", "MEDIUM"),
        ("HARD", "HARD"),
    )

    name = models.CharField(max_length=50)
    link = models.URLField()
    difficulty = models.CharField(max_length=50, choices=DIFFCULTY_CHOICE)
    description = models.CharField(max_length=500)
    note = models.CharField(max_length=500, blank=True, null=True)
    tag = models.CharField(max_length=500, default="DSA")
    date_solved = models.DateTimeField(auto_now_add=True)
    date_revised = models.DateTimeField(auto_now=True)
    revision_count = models.IntegerField(default=0)
    # shared_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
