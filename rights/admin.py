from django.contrib import admin

# Register your models here.
from .models import FundamentalRights,CivilRights,EnvironmentalRights,EconomicRights,humanRights,LegalRights,politicalRights,DirectivePrincipleofOurStatePolicy


admin.site.register(FundamentalRights)
admin.site.register(CivilRights)
admin.site.register(EnvironmentalRights)
admin.site.register(EconomicRights)
admin.site.register(humanRights)
admin.site.register(LegalRights)
admin.site.register(politicalRights)
admin.site.register(DirectivePrincipleofOurStatePolicy)

# name = KYR
# password = ALIKYR#@