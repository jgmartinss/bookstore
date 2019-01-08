from django.forms import ModelForm

from trumbowyg.widgets import TrumbowygWidget
from image_cropping import ImageCropWidget

from . import models


class AuthorForm(ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"
        widgets = {"about_of": TrumbowygWidget()}


class BookForm(ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        widgets = {"synopsis": TrumbowygWidget()}


class BookImagesForm(ModelForm):
    class Meta:
        model = models.BookImages
        fields = "__all__"
        widgets = {
            "list_page_cropping": ImageCropWidget(),
            "detail_page_cropping": ImageCropWidget(),
        }
