from django.db import models
from django_countries.fields import CountryField


class Entrant(models.Model):
    GENDERS = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    EDUCATION_LEVELS = [
        ("primary school only", "Primary school only"),
        ("high school, no degree", "High School, no degree"),
        ("high shool degree", "High School degree"),
        ("vocational shool", "Vocational School"),
        ("some university courses", "Some University Courses"),
        ("university degree", "University Degree"),
        ("some graduate level courses", "Some Graduate Level Courses"),
        ("master's degree", "Master's Degree"),
        ("some doctorate level courses", "Some Doctorate Level Courses"),
        ("doctorate degree", "Doctorate Degree"),
    ]
    MARITAL_STATUS = [
        ("unmarried", "Unmarried"),
        ("married_nlpr", "Married and my spouse is NOT a U.S. citizen or U.S. Lawful Permanent Resident (LPR)"),
        ("married_lpr", "Married and my spouse is a U.S. citizen or U.S. Lawful Permanent Resident (LPR)"),
        ("divorced", "Divorced"),
        ("widowed", "Widowed"),
        ("legally separated", "Legally Separated"),
    ]

    last_name = models.CharField("Last/Family Name", max_length=33)
    first_name = models.CharField("First Name", max_length=33)
    middle_name = models.CharField("Middle Name", max_length=33, null=True)
    gender = models.CharField(max_length=6, choices=GENDERS)
    birth_date = models.DateField(blank=True)
    birth_city = models.CharField("Birth City", max_length=33)
    birth_country = CountryField(blank_label="Select A Country...")
    eligibility_country = CountryField(blank_label="Select A Country...")
    entrant_photograph = models.ImageField(upload_to="")
    mailing_address_in_care_of = models.CharField("In Care Of (optional)", max_length=33, null=True, blank=True)
    mailing_address_address_line_one = models.CharField("Address Line 1", max_length=33)
    mailing_address_address_line_two = models.CharField("Address Line 2 (optional)", max_length=33, null=True, blank=True)
    mailing_adress_city = models.CharField("City/Town", max_length=50)
    mailing_adress_provence = models.CharField("District/County/Province/State", max_length=50)
    mailing_address_zip_code = models.CharField("Postal Code/Zip Code", max_length=33)
    mailing_address_country = CountryField("Country", blank_label="Select A Country...")
    resident_country = CountryField(blank_label="Select A Country...")
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    e_mail = models.EmailField()
    education_level = models.CharField(max_length=33, choices=EDUCATION_LEVELS)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    number_of_children = models.PositiveSmallIntegerField()
    confirmation_number = models.CharField(max_length=16, blank=True)
    digital_signature = models.CharField(max_length=40, blank=True)
    