from django.db import models


class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    other_information = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return (self.last_name)


class BoardMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name="last_name_board_member")
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    other_information = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return (self.first_name)



class Repair(models.Model):
    type_of_repair = models.TextField(max_length=500)
    costs_incl_VAT = models.CharField(max_length=30)
    VAT_percentage = models.CharField(max_length=30)

    def __str__(self):
        return (self.type_of_repair)


class MeetingDate(models.Model):
    date = models.CharField(max_length=30)

    def __str__(self) -> str:
        return (self.date)


class External_Partie(models.Model):
    company_name = models.CharField(max_length=100)
    type_of_company = models.CharField(max_length=100)
    first_name_contact = models.CharField(max_length=100)
    last_name_contact = models.CharField(max_length=100)
    address_company = models.CharField(max_length=100)
    phone_number_company = models.CharField(max_length=15)
    other_information_company = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return (self.company_name)


