from company.models import SecondTrimester,ThirdTrimester


def secondtrim_add_update_secondtrim(year,periodic_amount_diff):
    try:
        second_trim = SecondTrimester.objects.get(year=year)
        if second_trim:
            if second_trim.month1_cumulative_amount:
                print("data@@@@@@@@@@@@@",periodic_amount_diff)
                second_trim.month1_cumulative_amount += periodic_amount_diff
            if second_trim.month2_cumulative_amount:
                second_trim.month2_cumulative_amount += periodic_amount_diff
            if second_trim.month3_cumulative_amount:
                second_trim.month3_cumulative_amount += periodic_amount_diff
            if second_trim.month4_cumulative_amount:
                second_trim.month4_cumulative_amount += periodic_amount_diff
        second_trim.save()
    except SecondTrimester.DoesNotExist:
        pass

    return year



def secondtrim_subtractupdate_secondtrim(year,periodic_amount_diff):
    try:
        second_trim = SecondTrimester.objects.get(year=year)
        if second_trim:
            if second_trim.month1_cumulative_amount:
                print("data@@@@@@@@@@@@@",periodic_amount_diff)
                second_trim.month1_cumulative_amount = second_trim.month1_cumulative_amount - periodic_amount_diff
            if second_trim.month2_cumulative_amount:
                second_trim.month2_cumulative_amount -= periodic_amount_diff
            if second_trim.month3_cumulative_amount:
                second_trim.month3_cumulative_amount -= periodic_amount_diff
            if second_trim.month4_cumulative_amount:
                second_trim.month4_cumulative_amount -= periodic_amount_diff
        second_trim.save()
    except SecondTrimester.DoesNotExist:
        pass

    return year



def thirdtrim_add_update(year,periodic_amount_diff):
    try:
        third_trim = ThirdTrimester.objects.get(year=year)
        if third_trim:
            if third_trim.month1_cumulative_amount:
                third_trim.month1_cumulative_amount += periodic_amount_diff
            if third_trim.month2_cumulative_amount:
                third_trim.month2_cumulative_amount += periodic_amount_diff
            if third_trim.month3_cumulative_amount:
                third_trim.month3_cumulative_amount += periodic_amount_diff
            if third_trim.month4_cumulative_amount:
                third_trim.month4_cumulative_amount += periodic_amount_diff
        third_trim.save()
    except ThirdTrimester.DoesNotExist:
        pass

    return year



def thirdtrim_subtract_update(year,periodic_amount_diff):
    try:
        third_trim = SecondTrimester.objects.get(year=year)
        if third_trim:
            if third_trim.month1_cumulative_amount:
                third_trim.month1_cumulative_amount += periodic_amount_diff
            if third_trim.month2_cumulative_amount:
                third_trim.month2_cumulative_amount += periodic_amount_diff
            if third_trim.month3_cumulative_amount:
                third_trim.month3_cumulative_amount += periodic_amount_diff
            if third_trim.month4_cumulative_amount:
                third_trim.month4_cumulative_amount += periodic_amount_diff
        third_trim.save()
    except SecondTrimester.DoesNotExist:
        pass

    return year