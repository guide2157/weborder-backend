from django.db import models
import tagulous.models as tagulous_models


class MenuTag(tagulous_models.TagTreeModel):
    ordering = models.PositiveIntegerField(default=0)
    long_label = models.CharField(blank=True, max_length=255,
                                  help_text='Set the default title for the tag if not set, use the label')
    description = models.TextField(blank=True, default='', help_text='Set the default tag description')

    class TagMeta:
        space_delimiter = False

    @property
    def title(self):
        return self.long_label or self.label

    def __str__(self):
        return self.long_label or self.label


class Menu(models.Model):
    category_name = models.CharField(max_length=120)
    detail = models.TextField(default='Food')
    image = models.CharField(max_length=120)
    meta_description = models.CharField(max_length=120)
    meta_title = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.CharField(max_length=120)
    tags = tagulous_models.TagField(blank=True, to=MenuTag)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

