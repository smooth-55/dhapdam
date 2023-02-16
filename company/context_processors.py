from .models import ImportantLinks, Visitor,CompanyProfile,Videos
from company.utils.visitors import page_visit
from users.models import UserProfile


def links(request):

    # getting all the important links data
    imp_links = ImportantLinks.objects.all()

    # count the number of visitors in page
    count = page_visit(request)

    # company profile
    try:
        profile = CompanyProfile.objects.last()
    except:
        profile = None


    #get the multiple users

    if request.user.is_authenticated:
        user = request.user
        # user_designation = request.user.designation
        # print("user_designation",user_designation)
        # print("user_designation",type(user_designation)) 
        unit_chief = user.is_unit_chief
        engineer = user.is_engineer
        engineer_geologist = user.is_engineer_geologist
        accountant = user.is_accountant
        adminstration = user.is_adminstration
        admin = user.is_admin
        access = [unit_chief,engineer,engineer_geologist,admin]
    else:
        user_designation = None
        unit_chief = None
        engineer = None
        engineer_geologist = None
        accountant = None
        adminstration = None
        admin = None
        access = None
    print(unit_chief)
    print(engineer)


    
    return {
        "links": imp_links,
        "count": count,
        "profile":profile,
        "unit_chief":unit_chief,
        "engineer":engineer,
        "engineer_geologist":engineer_geologist,
        "accountant":accountant,
        "adminstration":adminstration,
        "access":access,

    }
