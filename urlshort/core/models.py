from django.db import models
from django.utils.translation import ugettext_lazy as _


class Link(models.Model):
    slug_key = models.SlugField(_(u'Chave'), max_length=6, primary_key=True)
    my_url = models.URLField(_(u'Link'), max_length=200)
    last_access = models.DateTimeField(_(u'Último Acesso'), auto_now=True)
    count = models.IntegerField(_(u'Cliques'), default=0)

    def __str__(self):
        return self.my_url
