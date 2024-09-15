from django.shortcuts import render
from .models import FundamentalRights,CivilRights,EnvironmentalRights,EconomicRights,humanRights,LegalRights,politicalRights,DirectivePrincipleofOurStatePolicy
from django.http import JsonResponse
from django.db.models import Q 
# Create your views here.

def home(request):
    query = request.GET.get('q')
    
    # Initialize empty queryset for each model
    fundamental_right = FundamentalRights.objects.none()
    civil_right = CivilRights.objects.none()
    environmental_right = EnvironmentalRights.objects.none()
    economic_right = EconomicRights.objects.none()
    human_right = humanRights.objects.none()
    legal_right = LegalRights.objects.none()
    political_right = politicalRights.objects.none()
    directive = DirectivePrincipleofOurStatePolicy.objects.none()

    if query:
        # Search across all models using the query
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        economic_right = EconomicRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        legal_right = LegalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        political_right = politicalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )

    # Combine all results into context
    context = {
        'fundamental_right': fundamental_right,
        'civil_right': civil_right,
        'environmental_right': environmental_right,
        'economic_right': economic_right,
        'human_right': human_right,
        'legal_right': legal_right,
        'political_right': political_right,
        'directive': directive,
    }
    
    return render(request, 'home.html', context)

def Fundamental(request):
    query = request.GET.get('q')
    if query:
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        
    else:
        fundamental_right = FundamentalRights.objects.all()
    
    return render(request,'FundamentalRights.html',{'fundamental_right': fundamental_right})

def autocomplete_fundamental_rights(request):
    query = request.GET.get('q')
    if query:
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        rights = FundamentalRights.objects.all().values('name')
    return JsonResponse(list(rights), safe=False)




def Civil(request):
    query = request.GET.get('q')
    if query:
        Civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Civil_right = CivilRights.objects.all()

    return render(request,'CivilRights.html',{'Civil_right':Civil_right})


def autocomplete_civil_rights(request):
    query = request.GET.get('q')
    if query:
        Civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Civil_right = CivilRights.objects.all().values('name')
    return JsonResponse(list(Civil_right), safe=False)




def Environmental(request):
    query = request.GET.get('q')
    if query:
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        environmental_right = EnvironmentalRights.objects.all()
    return render(request,'EnvironmentalRights.html',{'environmental_right':environmental_right})

def autocompleteenvironmental(request):
    query = request.GET.get('q')
    if query:
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        environmental_right = EnvironmentalRights.objects.all().values('name')
    return JsonResponse(list(environmental_right), safe=False)




def Economic(request):
    query = request.GET.get('q')
    if query:
        Economic_right = EconomicRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)    
        )
    else:
        Economic_right = EconomicRights.objects.all()
    return render(request,"Economicrights.html",{'Economic_right':Economic_right})

def autocompleteEconomic(request):
    query = request.GET.get('q')
    if query:
        Economic_right = EconomicRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)    
        )
    else:
        Economic_right = EconomicRights.objects.all().values('name')
    return JsonResponse(list(Economic_right), safe=False)


def human(request):
    query = request.GET.get('q')
    if query:
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        human_right = humanRights.objects.all()
        
    return render(request,"humanrights.html",{'human_right':human_right})

def autocompletehuman(request):
    query = request.GET.get('q')
    if query:
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        human_right = humanRights.objects.all().values('name')
    JsonResponse(list(human_right), safe=False)



def Legal(request):
    query = request.GET.get('q')
    if query:
         legal_right = LegalRights.objects.filter(
             Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
         legal_right = LegalRights.objects.all()
    
    return render(request,"legalrights.html",{'legal_right':legal_right})

def autocompletelegal(request):
    query = request.GET.get('q')
    if query:
         legal_right = LegalRights.objects.filter(
             Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
         legal_right = LegalRights.objects.all().values('name')
    JsonResponse(list(legal_right), safe=False)
    


def political(request):
    query = request.GET.get('q')
    if query:
        political_right = politicalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        political_right = politicalRights.objects.all()
        
    return render(request,"politicalRights.html",{'political_right':political_right})

def autocompletepolitical(request):
    query = request.GET.get('q')
    if query:
        political_right = politicalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        political_right = politicalRights.objects.all().values('name')
        
    JsonResponse(list(political_right), safe=False)



def Directive(request):
    query = request.GET.get('q')
    if query:
        Directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Directive = DirectivePrincipleofOurStatePolicy.objects.all()

    return render(request,"Directiveprinciple.html",{'Directive':Directive})

def autocompleteDirective(request):
    query = request.GET.get('q')
    if query:
        Directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        Directive = DirectivePrincipleofOurStatePolicy.objects.all().values('name')
    return JsonResponse(list(Directive), safe=False)