from django.db import models


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    # TODO: Добавьте требуемые поля

    def __str__(self):
        return self.model
