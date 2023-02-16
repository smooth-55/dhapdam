from django.db import models
from django.urls import reverse
from jsonfield import JSONField
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    """
    category of news
    """

    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="news"
    )
    title = models.CharField(("Title"), max_length=100)
    content = models.TextField(("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.FileField(
        ("File"), upload_to="news/% Y/% m/% d/", null=True, blank=True
    )
    views = models.PositiveIntegerField(default=0, null=True, blank=True)
    display = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "News"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("news:news-detail", kwargs={"pk": self.pk})


class RecentActivities(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="activity"
    )
    title = models.CharField(("Title"), max_length=100)
    content = models.TextField(("Content"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    thumnail = models.ImageField(
        ("Thumnail"), upload_to="recent-activities/% Y/% m/% d/", null=True, blank=True
    )
    views = models.PositiveIntegerField(default=0, null=True, blank=True)
    display = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Recent Activities"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:activities-detail", kwargs={"pk": self.pk})


class HomeNotice(models.Model):
    """
    Notice that describes the important occasion
    """

    DES_CHOICES = [("E", ""), ("UC", "Unit Chief")]
    image = models.ImageField(
        ("Image"), upload_to="home-notice/% Y/% m/% d/", null=True, blank=True
    )
    title = models.CharField(("Title"), max_length=60, null=True, blank=True)
    content = models.TextField(("Content"), null=True, blank=True)
    files = models.FileField(
        ("Upload Files"), upload_to="downloads", null=True, blank=True
    )
    display = models.BooleanField(
        ("Please check the box to display notice in homepage."), default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Home Notice"

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    USER_TYPES = (
        ("U", "Unit Chief"),
        ("E", "Engineer"),
    )
    name = models.CharField(("Name"), max_length=100)
    content = models.TextField(("Content"))
    designation = models.CharField(choices = USER_TYPES,max_length=1, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="message/% Y/% m/% d/", null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.designation)
        super(Message, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name
