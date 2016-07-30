from django.db import models
from cms.models import CMSPlugin

# Create your models here.
class Testimonial(models.Model):
    quote = models.CharField(max_length=400, help_text="Quote of customer/client")
    title = models.CharField(max_length=200, help_text="Title of person you are quoting")

    def __str__(self):
        return str(self.title)


class TestimonialPluginModel(CMSPlugin):
    testimonial = models.ForeignKey(Testimonial)

    def __str__(self):
        return self.testimonial.title
