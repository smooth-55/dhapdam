from django.conf import settings
from company.models import Visitor
from django.db.models import Q


def page_visit(request):
    # --- get visitors ip ------#
    address = request.META.get("HTTP_X_FORWARDED_FOR")
    if address:
        ip = address.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")

    u = Visitor(page_visited=ip)
    visit = Visitor.objects.filter(Q(page_visited__icontains=ip))
    #if user exits
    if len(visit)==1:
        pass
    #if it contains same ip
    elif len(visit) > 1:
        pass
    #if user is unique
    else:
        u.save()

    total_count = Visitor.objects.all().count()
    return total_count



