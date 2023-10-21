from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=200,
                            blank=False,
                            null=False,
                            verbose_name='Name')
    slug = models.SlugField(max_length=200,
                            blank=False,
                            null=False)
    url = models.CharField(max_length=1000,
                           blank=True,
                           null=False,
                           verbose_name='URL')
    parent = models.ForeignKey('self',
                               on_delete=models.SET_DEFAULT,
                               verbose_name="Parent to this element",
                               null=True,
                               blank=True,
                               default=None)

    class Meta:
        ordering = ['name']
        verbose_name = 'Menu'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tree_menu:menu', args=[self.url])

    def create_url(self):
        if not self.parent:
            self.url = f"{self.slug}"
        else:
            self.url = f"{self.parent.url}-{self.slug}"
