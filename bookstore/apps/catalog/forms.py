from django.forms import ModelForm

from trumbowyg.widgets import TrumbowygWidget
from image_cropping import ImageCropWidget

from bookstore.apps.catalog.models import Author, Book, BookImages, AuthorImages


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {"about_of": TrumbowygWidget()}


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {"synopsis": TrumbowygWidget()}


class BookImagesForm(ModelForm):
    class Meta:
        model = BookImages
        fields = "__all__"
        widgets = {
            "list_page_cropping": ImageCropWidget(),
            "detail_page_cropping": ImageCropWidget(),
        }


class AuthorImagesForm(ModelForm):
    class Meta:
        model = AuthorImages
        fields = "__all__"
        widgets = {
            "list_page_cropping": ImageCropWidget(),
            "detail_page_cropping": ImageCropWidget(),
        }
