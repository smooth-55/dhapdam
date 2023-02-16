from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.utils.timezone import now

GENDERS_CHOICES = (
    (1, "Male"),
    (2, "Female"),
    (3, "Others"),
)
ID_CHOICES = [("CT", "Citizenship"), ("PS", "Passport"), ("OT", "Others")]

UNIT_CHIEF = 1
ENGINEER = 2
ENGINEER_GEOLOGIST = 3
ACCOUNTANT = 4
ADMINISTRATION = 5

USER_TYPES   = (
    (UNIT_CHIEF, "Unit Chief"),
    (ENGINEER, "Engineer"),
    (ENGINEER_GEOLOGIST, "Engineer Geologist"),
    (ACCOUNTANT, "Accountant"),
    (ADMINISTRATION, "Administration"),
)

class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email=self.normalize_email(email), username=username, phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser):

    designation = models.PositiveIntegerField(choices = USER_TYPES,blank = True,null = True)
    email = models.EmailField(("Email"), max_length=254, unique=True)
    username = models.CharField(
        ("Username"), max_length=50, unique=True, null=True, blank=True
    )
    full_name = models.CharField(("Full Name"), max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField(("Date of birth"), null=True, blank=True)
    identification = models.CharField(choices=ID_CHOICES, max_length=2, null=True)
    id_number = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="user-image", null=True,blank=True)

    is_active = models.BooleanField(("is_active"), default=True)
    is_admin = models.BooleanField(("is_admin"), default=False)
    is_superuser = models.BooleanField(("is_superuser"), default=False)
    is_permitted = models.BooleanField(
        default=False
    ) 


    
    is_staff = models.BooleanField(default=False) # field that defines the created by admin and has  permissions to login

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]

    objects = UserProfileManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True


    @property
    def is_unit_chief(self):
        print("designation",self.designation)
        return self.designation == "1"

    @property
    def is_engineer(self):
        return self.designation == "2"

    @property
    def is_engineer_geologist(self):
        return self.designation == "3"

    @property
    def is_accountant(self):
        return self.designation == "4"

    @property
    def is_adminstration(self):
        return self.designation == "5"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = [
            "-id",
        ]



class EmployeeProfile(models.Model):
    """
    employee profile for all non logged in user
    """
    email = models.EmailField(("Email"), max_length=254, unique=True,null=True,blank=True)
    username = models.CharField(
        ("Username"), max_length=50, unique=True, null=True, blank=True
    )
    full_name = models.CharField(("Full Name"), max_length=50, null=True, )
    designation = models.CharField(max_length=255, null=True,blank=True)
    phone = models.CharField(max_length=15, null=True,)
    image = models.ImageField(upload_to="user-image", null=True)
    temporary_address = models.CharField(max_length=150, blank=True, null=True)
    permanent_address = models.CharField(max_length=150, null=True)
    date_joined = models.CharField(("Join Date"),max_length=30, null=True)
    leave_date = models.CharField(("Leave Date"),max_length=30, null=True, blank=True)
    is_transferred = models.BooleanField(
        default=False
    ) #for ex employee
    is_projecthead = models.BooleanField(
        default=False
    ) #for ex project head
    none = models.BooleanField(
        default=False
    ) 
    def __str__(self):
        return str(self.id)
    
    class  Meta:
        ordering = ['-id']
        verbose_name_plural = "employee profile"

