from django.db import models
from django.urls import reverse
from jsonfield import JSONField


# model for contract
STATUS_CHOICE = (
    ("C", "Completed"),
    ("O", "Ongoing"),
)


def revised_completion():
    return {"revised_date": []}


def work_completed():
    return {"work_completed": []}


class Contract(models.Model):
    contract_id = models.CharField(("Contract ID"), max_length=100)
    project_name = models.CharField(("Contract Name"), max_length=500)
    work_name = models.CharField(("Work Name"), max_length=500)
    contractor_detail = models.CharField(
        ("Contractor Name and Address"), max_length=1000
    )
    amount = models.DecimalField(
        ("Amount of agreement"), max_digits=20, decimal_places=2
    )
    date_of_agreement = models.DateField(
        ("Date of Agreement"), auto_now=False, auto_now_add=False
    )
    date_of_completion = models.DateField(
        ("Date of Completion as Agreement"), auto_now=False, auto_now_add=False
    )
    date_of_completion_revised = models.DateField(
        ("Date of Completion (Revised)"),
        auto_now=False,
        blank=True,
        null=True,
    )
    actual_expenditure = models.DecimalField(
        ("Actual expenditure"), max_digits=20, decimal_places=2
    )
    current_status = models.CharField(
        ("Current Project Status"), max_length=2, choices=STATUS_CHOICE
    )
    contractor_liability_status = models.CharField(
        ("Contractor Liability Status"), max_length=2, choices=STATUS_CHOICE
    )

    works_completed =models.CharField(("Works Completed"), max_length=500)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def get_absolute_url(self):
        return reverse("contracts:contract-detail", kwargs={"pk": self.pk})


class ContractDetail(models.Model):
    contract = models.ForeignKey(
        "contracts.Contract", on_delete=models.CASCADE, related_name="contract_detail"
    )
    introduction = models.TextField(blank=True, null=True)
    location_and_accessibility = models.TextField(blank=True, null=True)
    work_component = models.TextField(blank=True, null=True)
    design_and_quality = models.TextField(blank=True, null=True)
    environmental_aspects = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Contract Detail"
        verbose_name_plural = "Contract Detail"

    def __str__(self):
        return self.contract.project_name

    def get_absolute_url(self):
        return reverse("contracts:contract-detail-detail", kwargs={"pk": self.pk})


# model for each tasks completed on Contracts


class ContractFeature(models.Model):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="contract_feature"
    )
    dam_type = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    top_length = models.CharField(max_length=255, blank=True, null=True)
    crest_elevation = models.CharField(max_length=255, blank=True, null=True)
    upstream_slope = models.CharField(max_length=255, blank=True, null=True)
    downstream_slope = models.CharField(max_length=255, blank=True, null=True)
    crest_width = models.CharField(max_length=255, blank=True, null=True)
    concrete_face_thickness = models.CharField(max_length=255, blank=True, null=True)
    reservoir_volume = models.CharField(max_length=255, blank=True, null=True)
    norma_water_level = models.CharField(max_length=255, blank=True, null=True)
    freeboard = models.CharField(max_length=255, blank=True, null=True)
    saddle_dam = models.CharField(max_length=255, blank=True, null=True)
    dam_volume = models.CharField(max_length=255, blank=True, null=True)
    full_supply_level = models.CharField(max_length=255, blank=True, null=True)
    design_discharge = models.CharField(max_length=255, blank=True, null=True)
    power_production = models.CharField(max_length=255, blank=True, null=True)
    cost = models.CharField(max_length=255, blank=True, null=True)
    reservoir_surface_area = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.contract.project_name

    def get_absolute_url(self):
        return reverse("contracts:contract-feature-detail", kwargs={"pk": self.pk})


PROGRESS_STATUS = (
    ("B", "Before Schedule"),
    ("A", "After Schedule"),
)


class ContractProgress(models.Model):
    contract = models.ForeignKey(
        "contracts.Contract",
        verbose_name=("contract"),
        on_delete=models.CASCADE,
        related_name="contract_progress",
    )
    time_extended_on_original_schedule = models.DecimalField(
        ("Time Extended based on original Schedule"),
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
    )
    time_elapsed_on_revise_schedule = models.DecimalField(
        ("Time Elapsed based on revised schedule"),
        max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
    )
    time_remaining_on_extended_schedule = models.DecimalField(
        ("Time Remaining based on extended schedule"),
         max_digits=20,
        decimal_places=2,
        blank=True,
        null=True,
    )

    # Financial Progress Fields
    financial_progress_amount = models.DecimalField(
        ("Financial Percent Amount"),
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
    )
    financial_percent_amount = models.DecimalField(
        ("Financial Percent Amount"),
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
    )
    financial_progress_date = models.DateField(
        ("Last payment Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )

    # Physcial Progress Fields
    physical_percent_amount = models.DecimalField(
        ("Physical Percent Amount"),
        max_digits=30,
        decimal_places=2,
        blank=True,
        null=True,
    )
    physical_progress_date = models.DateField(
        ("Physical Progress as of date"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )

    # progress status(This field's value should be generated depending on other data)
    progress_status = models.CharField(
        ("Progress Status"), max_length=100, blank=True, null=True
    )

    # Remarks
    remarks = models.CharField(("Remarks"),  max_length=400, blank=True, null=True)

    class Meta:
        verbose_name = "Contract Progress"
        verbose_name_plural = "Contract Progresses"

    def __str__(self):
        return self.contract.project_name

    def get_absolute_url(self):
        return reverse("contract:contract-detail", kwargs={"pk": self.pk})

