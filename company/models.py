import os
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Introduction(models.Model):
    """
    Introduction of BRBIP
    """
    image = models.FileField(("Image"), null=True, blank=True)
    content_upload = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    name = models.CharField(("Name"), max_length=60, null=True)
    email = models.CharField(("Email"),max_length=40)
    phone = models.CharField(("Phone"), max_length=20)
    message = models.TextField("Message")
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact us"

    def __name__(self):
        return self.email


class Structure(models.Model):
    """
    organization structure
    """

    title = models.CharField(
        ("Name of Organization Structure"), max_length=200, null=True, blank=True
    )
    file = models.FileField(upload_to="structure", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "organization structure"

    def __str__(self):
        return str(self.id)


class CitizenCharter(models.Model):
    title = models.CharField(
        ("Name of Citizen Charter"), max_length=200, null=True, blank=True
    )
    file = models.FileField(upload_to="citizen-charter", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Citizen Charter"

    def __str__(self):
        return self.title


class PhotoCategory(models.Model):
    """
    category of news
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photos(models.Model):
    category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(("Title"), max_length=100, null=True, blank=True)
    description = models.TextField(("Description"), null=True, blank=True)
    image = models.FileField(upload_to="photos", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Photos"

    def __str__(self):
        return str(self.id)


class Videos(models.Model):
    title = models.CharField(("Title"), max_length=100, null=True,blank=True)
    description = models.TextField(("Description"), null=True, blank=True)
    link = models.URLField(("Videos Url"), max_length=500, null=True)

    thumbnail = models.ImageField(
        ("Thumbnail"), upload_to="thumbnail", null=True,blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Videos"

    def __str__(self):
        return str(self.id)


class Downloads(models.Model):
    name = models.CharField(("Name"), max_length=50)
    file = models.FileField(upload_to="downloads")
    size = models.CharField(("Size of file"), max_length=50)
    url = models.URLField(("URL of file"), blank=True, null=True, max_length=300)

    class Meta:
        verbose_name_plural = "Downloads"

    def __str__(self):
        return "Filename:" + self.name


class DocumentCategory(models.Model):
    """"
    category should bes related only to documents models
    """

    name = models.CharField(("Type"), max_length=60, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Documents(models.Model):
    """Documents"""

    category = models.ForeignKey(
        DocumentCategory,
        related_name="documents",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(("Title"), max_length=50)
    file = models.FileField(upload_to="documents")
    url = models.URLField(("URL of file"), blank=True, null=True, max_length=300)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Documents"

    def __str__(self):
        return "Filename:" + self.name


class Policy(models.Model):
    """
    Policy/Law
    """

    POLICY_CHOICES = (
        ("1", "Act and Regulations"),
        ("2", "Startegy,Plans and Policies"),
    )

    name = models.CharField(("Name"), max_length=200,)
    file = models.FileField(("Name of File"), upload_to="policy", null=True, blank=True)
    types = models.CharField(
        ("Type of Policy/Law"), max_length=2, choices=POLICY_CHOICES, default=1
    )

    class Meta:
        verbose_name_plural = "Policy/Law"

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.file.name)


class ImportantLinks(models.Model):
    """
    Important Links
    """

    title = models.CharField(("Title"), max_length=200)
    content = models.TextField(("Content"), max_length=200, null=True, blank=True)
    link = models.URLField(("Link"), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Important Links"

    def __str__(self):
        return self.title


class HomepageSliderImages(models.Model):
    image = models.ImageField(upload_to="homepage-slider", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Homepage Slider Images"

    def __str__(self):
        return str(self.image)


class StakeHolders(models.Model):
    """
    Stake holders
    """

    title = models.CharField(("Title"), max_length=200, null=True, blank=True)
    content = models.TextField(("Content"), max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="stakeholders")
    link = models.URLField(("Link"), max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "StakeHolders"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class Reservoir(models.Model):
    """
    Reservoir in nepal(for slider)
    """

    image1 = models.ImageField(upload_to="reservoir", null=True, blank=True)
    image2 = models.ImageField(upload_to="reservoir", null=True, blank=True)
    image3 = models.ImageField(upload_to="reservoir", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Reservoir"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class ConstructionWork(models.Model):
    """
    construction (for slider)
    """

    image1 = models.ImageField(upload_to="construction", null=True, blank=True)
    image2 = models.ImageField(upload_to="construction", null=True, blank=True)
    image3 = models.ImageField(upload_to="construction", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Construction Work"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class Visitor(models.Model):
    """"
    Total Number of visit in a homepage section(footer)
    """

    page_visited = models.TextField()
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_visited


class CompanyProfile(models.Model):
    """
    This model defines the company profile 
    """
    address = models.CharField(("Address"),max_length=150,null=True)
    phone1 = models.CharField(("Phone1"),max_length=16,null=True)
    phone2 = models.CharField(("Phone2"),max_length=16,null=True,blank=True)
    email = models.EmailField(("Email"))
    url = models.URLField(("Site url"), max_length=500, null=True,blank=True)

    class Meta:
        verbose_name_plural = "CompanyProfile"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)



# --------------------------------- Models for company Progress ----------------------------------------


class FiscalYear(models.Model):
    year = models.CharField(max_length=10)
    name = models.CharField(max_length=255, blank=True, null=True)
    target = models.BigIntegerField(("Yearly Target"))

    def __str__(self):
        return str(self.year)


MONTH_CHOICE1 = (
    ("1", "Shrawan"),
    ("2", "Bhadra"),
    ("3", "Ashoj"),
    ("4", "Kartik"),
)

MONTH_CHOICE2 = (
    ("5", "Mangsir"),
    ("6", "Paush"),
    ("7", "Magh"),
    ("8", "Falgun"),
)

MONTH_CHOICE3 = (
    ("9", "Chaitra"),
    ("10", "Baisakh"),
    ("11", "Jestha"),
    ("12", "Ashar"),
)


class FirstTrimester(models.Model):
    name = models.CharField(("Trimester Name"), max_length=50, blank=True, null=True)
    year = models.ForeignKey(
        FiscalYear,
        related_name="first_trimester",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    month1 = models.CharField(
        ("Month 1"), max_length=2, choices=MONTH_CHOICE1, null=True, blank=True
    )
    month1_periodic_amount = models.BigIntegerField(
        ("Month1 Periodic Amount"), null=True, blank=True
    )
    month1_cumulative_amount = models.BigIntegerField(
        ("Month1 cumulative Amount"), null=True, blank=True
    )

    month2 = models.CharField(
        ("Month 2"), max_length=2, choices=MONTH_CHOICE1, null=True, blank=True
    )
    month2_periodic_amount = models.BigIntegerField(
        ("Month2 Periodic Amount"), null=True, blank=True
    )
    month2_cumulative_amount = models.BigIntegerField(
        ("Month2 cumulative Amount"), null=True, blank=True
    )

    month3 = models.CharField(
        ("Month 3"), max_length=2, choices=MONTH_CHOICE1, null=True, blank=True
    )
    month3_periodic_amount = models.BigIntegerField(
        ("Month3 Periodic Amount"), null=True, blank=True
    )
    month3_cumulative_amount = models.BigIntegerField(
        ("Month3 Cumulative Amount"), null=True, blank=True
    )

    month4 = models.CharField(
        ("Month 4"), max_length=2, choices=MONTH_CHOICE1, null=True, blank=True
    )
    month4_periodic_amount = models.BigIntegerField(
        ("Month4 Periodic Amount"), null=True, blank=True
    )
    month4_cumulative_amount = models.BigIntegerField(
        ("Month4 Cumulative Amount"), null=True, blank=True
    )

    trimester_periodic = models.BigIntegerField(
        ("trimester Periodic Amount"), null=True, blank=True
    )
    trimester_cumulative = models.BigIntegerField(
        ("trimester cumulative Amount"), null=True, blank=True
    )

    periodic_target = models.BigIntegerField(
        ("Periodic Target Amount"), null=True, blank=True
    )
    periodic_percentage_financial = models.DecimalField(
        ("Periodic Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    yearly_percentage_financial = models.DecimalField(
        ("Yearly Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    periodic_physical_progress = models.DecimalField(
        ("Periodic Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    cumulative_physical_progress = models.DecimalField(
        ("Cumulative Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    overrall = models.DecimalField(
        ("Overall"), max_digits=10, decimal_places=2, null=True, blank=True,
    )

    def __str__(self):
        return str(self.id) + " " + "Trimester=" + str(self.name)


class SecondTrimester(models.Model):
    name = models.CharField(("Trimester Name"), max_length=50, blank=True, null=True)
    year = models.ForeignKey(
        FiscalYear,
        related_name="second_trimester",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    month1 = models.CharField(
        ("Month 1"), max_length=2, choices=MONTH_CHOICE2, null=True, blank=True
    )
    month1_periodic_amount = models.BigIntegerField(
        ("Month1 Periodic Amount"), null=True, blank=True
    )
    month1_cumulative_amount = models.BigIntegerField(
        ("Month1 cumulative Amount"), null=True, blank=True
    )

    month2 = models.CharField(
        ("Month 2"), max_length=2, choices=MONTH_CHOICE2, null=True, blank=True
    )
    month2_periodic_amount = models.BigIntegerField(
        ("Month2 Periodic Amount"), null=True, blank=True
    )
    month2_cumulative_amount = models.BigIntegerField(
        ("Month2 cumulative Amount"), null=True, blank=True
    )

    month3 = models.CharField(
        ("Month 3"), max_length=2, choices=MONTH_CHOICE2, null=True, blank=True
    )
    month3_periodic_amount = models.BigIntegerField(
        ("Month3 Periodic Amount"), null=True, blank=True
    )
    month3_cumulative_amount = models.BigIntegerField(
        ("Month3 cumulative Amount"), null=True, blank=True
    )

    month4 = models.CharField(
        ("Month 4"), max_length=2, choices=MONTH_CHOICE2, null=True, blank=True
    )
    month4_periodic_amount = models.BigIntegerField(
        ("Month4 Periodic Amount"), null=True, blank=True
    )
    month4_cumulative_amount = models.BigIntegerField(
        ("Month4 cumulative Amount"), null=True, blank=True
    )

    trimester_periodic = models.BigIntegerField(
        ("trimester Periodic Amount"), null=True, blank=True
    )
    trimester_cumulative = models.BigIntegerField(
        ("trimester cumulative Amount"), null=True, blank=True
    )

    periodic_target = models.BigIntegerField(
        ("Periodic Target Amount"), null=True, blank=True
    )
    periodic_percentage_financial = models.DecimalField(
        ("Periodic Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    yearly_percentage_financial = models.DecimalField(
        ("Yearly Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    periodic_physical_progress = models.DecimalField(
        ("Periodic Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    cumulative_physical_progress = models.DecimalField(
        ("Cumulative Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    overrall = models.DecimalField(
        ("Overall"), max_digits=10, decimal_places=2, null=True, blank=True,
    )

    def __str__(self):
        return str(self.id) + " " + "Trimester=" + str(self.name)


class ThirdTrimester(models.Model):
    name = models.CharField(("Trimester Name"), max_length=50, blank=True, null=True)
    year = models.ForeignKey(
        FiscalYear,
        related_name="third_trimester",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    month1 = models.CharField(
        ("Month 1"), max_length=2, choices=MONTH_CHOICE3, null=True, blank=True
    )
    month1_periodic_amount = models.BigIntegerField(
        ("Month1 Periodic Amount"), null=True, blank=True
    )
    month1_cumulative_amount = models.BigIntegerField(
        ("Month1 cumulative Amount"), null=True, blank=True
    )

    month2 = models.CharField(
        ("Month 2"), max_length=2, choices=MONTH_CHOICE3, null=True, blank=True
    )
    month2_periodic_amount = models.BigIntegerField(
        ("Month2 Periodic Amount"), null=True, blank=True
    )
    month2_cumulative_amount = models.BigIntegerField(
        ("Month2 cumulative Amount"), null=True, blank=True
    )

    month3 = models.CharField(
        ("Month 3"), max_length=2, choices=MONTH_CHOICE3, null=True, blank=True
    )
    month3_periodic_amount = models.BigIntegerField(
        ("Month3 Periodic Amount"), null=True, blank=True
    )
    month3_cumulative_amount = models.BigIntegerField(
        ("Month3 cumulative Amount"), null=True, blank=True
    )

    month4 = models.CharField(
        ("Month 4"), max_length=2, choices=MONTH_CHOICE3, null=True, blank=True
    )
    month4_periodic_amount = models.BigIntegerField(
        ("Month4 Periodic Amount"), null=True, blank=True
    )
    month4_cumulative_amount = models.BigIntegerField(
        ("Month4 cumulative Amount"), null=True, blank=True
    )

    trimester_periodic = models.BigIntegerField(
        ("trimester Periodic Amount"), null=True, blank=True
    )
    trimester_cumulative = models.BigIntegerField(
        ("trimester cumulative Amount"), null=True, blank=True
    )

    periodic_target = models.BigIntegerField(
        ("Periodic Target Amount"), null=True, blank=True
    )
    periodic_percentage_financial = models.DecimalField(
        ("Periodic Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    yearly_percentage_financial = models.DecimalField(
        ("Yearly Percentage"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    periodic_physical_progress = models.DecimalField(
        ("Periodic Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    cumulative_physical_progress = models.DecimalField(
        ("Cumulative Physical Progress"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    overrall = models.DecimalField(
        ("Overall"), max_digits=10, decimal_places=2, null=True, blank=True,
    )

    def __str__(self):
        return str(self.id) + " " + "Trimester=" + str(self.name)


# ------------------------------------End of Model for Company Progress -----------------------------------


class Darta(models.Model):
    
    darta_no = models.CharField(("Darta number"), max_length=50, blank=True, null=True)
    date = models.CharField(("Darta Date"),max_length=80)
    patra_no = models.CharField(
        ("Prapta Patra number"), max_length=50, blank=True, null=True
    )
    cha_no = models.CharField(
        ("Prapta Patra Chha number"), max_length=50, blank=True, null=True
    )
    patra_received_date = models.CharField(
        ("Patra Received Date"), max_length=80
    )
    sender = models.CharField(
        ("Prapta sender office/person"), max_length=50, blank=True, null=True
    )
    address = models.CharField(
        ("Prapta sender office/person address"), max_length=100, blank=True, null=True
    )
    subject = models.CharField(
        ("Prapta Subject"), max_length=100, blank=True, null=True
    )
    medium = models.CharField(("Sending Medium"), max_length=100, blank=True, null=True)
    remark = models.CharField(("Remark"), max_length=100, blank=True, null=True)
    image = models.FileField(
        ("Image"),
        upload_to="darta-images",
        null=True,
        blank=True,
    )
    eng_date = models.DateField(null=True,blank=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Dartas"

    def __str__(self):
        return self.darta_no + " / " + self.subject

    def get_absolute_url(self):
        return reverse("company:darta-detail", kwargs={"pk": self.pk})


class Chalani(models.Model):
    MEDIUM_CHOICES = (
        ("E", "Email"),
        ("H", "Hard Copy"),
    )
    chalani_no = models.CharField(
        ("Chalani number"), max_length=50, blank=True, null=True
    )
    date = models.CharField(("Chalani Date"),max_length=80)
    chalani_perform_date = models.CharField(("Chalani Perform Date"),max_length=80,null=True)
    patra_no = models.CharField(
        ("Prapta Patra number"), max_length=50, blank=True, null=True
    )
    sender = models.CharField(
        ("Prapta sender office/person"), max_length=50, blank=True, null=True
    )
    address = models.CharField(
        ("Prapta sender office/person address"), max_length=100, blank=True, null=True
    )
    subject = models.CharField(
        ("Prapta Subject"), max_length=100, blank=True, null=True
    )
    medium = models.CharField(max_length=20, choices=MEDIUM_CHOICES,null=True,blank=True)
    remark = models.CharField(("Remark"), max_length=100, blank=True, null=True)
    image = models.FileField(
        ("Image"),
        upload_to="chalani-images",
        null=True,
        blank=True,
    )
    
   
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Chalanis"

    def __str__(self):
        return self.chalani_no + " / " + self.subject

    def get_absolute_url(self):
        return reverse("company:chalani-detail", kwargs={"pk": self.pk})

    

# <------------------------------------adminstration upload files section ----------------------------------------------->
class UploadFile(models.Model):
    """models to store files of adminstration and accountant"""
    fiscal_year = models.CharField(
        ("Fiscal Year"), max_length=100, null=True, blank=True
    )
    title = models.CharField(
        ("Title"),max_length=60,null=True, blank=True
    )
    files = models.FileField(upload_to="adminstration_and_account/uploaded_files/")

    class Meta:
        abstract = True
        ordering = ("-id",)


class AccountUploadFile(UploadFile):
    """
    models to store the account files
    """
    FILE_TYPES   = (
        ("Cu", "Current Budget"),
        ("Ca", "Capital Budget"),
    )
    types = models.CharField(
        ("Type of Files"), max_length=2, choices=FILE_TYPES, null=True
    )
    
    def __str__(self):
        return "account files"+ " " +str(self.id)

    class Meta:
        ordering =['-id']
        verbose_name = "Account Upload file"

class AdminstrationUploadFile(UploadFile):
    """
    models to store admintration files
    """

    pass

    def __str__(self):
        return "adminsitration files"+" "+str(self.id)

    class Meta:        
        verbose_name = "Adminstration upload file"





# <------------------------------------file upload section  ends ----------------------------------------------->


# <------------------------------------account section ----------------------------------------------->
class Account(models.Model):
    """
    Includes all the common attributes of current budget and capital budget
    """
    fiscal_year = models.CharField(
        ("Fiscal Year"), max_length=100, null=True, 
    )
    annual_budget = models.DecimalField(
        ("Annual Budget"), max_digits=10, decimal_places=2, null=True
    )
    expenditure = models.DecimalField(
        ("Expenditure"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    remaining = models.DecimalField(
        ("Remaning"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ("-id",)

class CurrentBudget(Account):
    """
    models of current budget
    """

    pass

    def __str__(self):
        return "current budget"+ str(self.id)

    class Meta:
        verbose_name_plural = "Current Budget"


class CapitalBudget(Account):
    """
    models of capital budget
    """

    pass

    def __str__(self):
        return "capital budget" + str(self.id)

    class Meta:
        verbose_name_plural = "capital Budget"
