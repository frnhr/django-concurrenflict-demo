from django.db import models


class MyTag(models.Model):
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name


class MyModel(models.Model):
    CHOICES_B = (
        ('b1', u'Option B1'),
        ('b2', u'Option B2'),
        ('b3', u'Option B3'),
        ('b4', u'Option B4'),
    )
    field_a = models.CharField(max_length=255)
    field_b = models.CharField(max_length=10, choices=CHOICES_B)
    field_c = models.ManyToManyField(MyTag)
    field_d = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.field_a

