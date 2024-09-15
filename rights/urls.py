from django.urls import path
from .views import home,Fundamental,Civil,Environmental,Economic,human,Legal,political,Directive,autocomplete_fundamental_rights,autocomplete_civil_rights,autocompleteDirective,autocompleteEconomic,autocompletehuman,autocompletelegal,autocompleteenvironmental,autocompletepolitical


urlpatterns= [ 
    path('',home,name="home"),
    path("FundamentalRights/",Fundamental,name='FundamentalRights'),
    path('autocomplete/fundamental-rights/',autocomplete_fundamental_rights, name="autocomplete_fundamental_rights"),

    path("civilrights/",Civil,name="CivilRights"),
    path('autocomplete_civil_rights',autocomplete_civil_rights,name="autocomplete_civil_rights"),

    path("EnvironmentalRights/",Environmental,name="EnvironmentalRights"),
    path('autocompleteenvironmental',autocompleteenvironmental,name="autocompleteenvironmental"),

    path("EconomicRights/",Economic,name="EconomicRights"),
    path("autocompleteEconomic",autocompleteEconomic,name="autocompleteEconomic"),

    path("humanRights/",human,name="humanRights"),
    path("autocompletehuman",autocompletehuman,name="autocompletehuman"),

    path("LegalRights/",Legal,name="LegalRights"),
    path("autocompletelegal",autocompletelegal,name="autocompletelegal"),

    path("politicalRights/",political,name="politicalRights"),
    path("autocompletepolitical",autocompletepolitical,name="autocompletepolitical"),

    path("Directive/",Directive,name='DirectivePrincipleofOurStatePolicy'),
    path("autocompleteDirective",autocompleteDirective,name="autocompleteDirective")
    
] 


