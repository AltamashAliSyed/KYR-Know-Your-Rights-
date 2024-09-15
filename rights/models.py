from django.db import models


class FundamentalRights(models.Model):

    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class CivilRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class EnvironmentalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class EconomicRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class humanRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class LegalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title

class politicalRights(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=5000)

    def __str__(self):
        return self.Title
  
class DirectivePrincipleofOurStatePolicy(models.Model):
    Title = models.CharField(max_length=400)
    
    Description = models.CharField(max_length=50002)

    def __str__(self):
        return self.Title
  