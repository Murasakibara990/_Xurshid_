from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    title = models.CharField(max_length=212)

    def __str__(self):
        return self.title


class Tag(TimeStampedModel):
    title = models.CharField(max_length=212)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    @classmethod
    def filter_by_category(cls, category):
        return cls.objects.filter(category=category)

    def __str__(self):
        return self.name
