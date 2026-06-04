from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.common import CommonModel

# Create your models here.


class Staff(CommonModel):
    """Model for storing directors and actors."""

    name = models.CharField(_("Name"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Staff")
        verbose_name_plural = _("Staff")

    def __str__(self):
        return self.name


class Genre(CommonModel):
    """Model for storing movie genres."""

    name = models.CharField(_("Genre Name"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name


class Movie(CommonModel):
    """Model for storing movie details."""

    title = models.CharField(_("Movie Title"), max_length=255, unique=True)
    release_date = models.DateField(_("Release Date"))

    genre = models.ManyToManyField(
        Genre,
        verbose_name=_("Genre"),
        related_name="movies",
    )
    director = models.ForeignKey(
        Staff,
        verbose_name=_("Director"),
        on_delete=models.CASCADE,
        related_name="directed_movies",
    )
    actors = models.ManyToManyField(
        Staff,
        verbose_name=_("Actors"),
        related_name="movies",
    )

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title
