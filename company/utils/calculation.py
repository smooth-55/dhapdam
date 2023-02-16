import pandas as pd
import numpy as np
from company.models import FirstTrimester, SecondTrimester, ThirdTrimester, FiscalYear
from .progress_calculation import secondtrim_add_update_secondtrim,secondtrim_subtractupdate_secondtrim,thirdtrim_add_update,thirdtrim_subtract_update
from django.db.models import F



def calc_cumulative(periodic_amt, month_name,fiscal_year, obj_id):
    """
     overall fiscal year calcualtion part
    """
    # first trimster
    if month_name == "1" or month_name == "2" or month_name == "3" or month_name == "4":
        total_cumulat = first_trimester(periodic_amt, month_name, obj_id)

    # second trimester
    elif (
        month_name == "5" or month_name == "6" or month_name == "7" or month_name == "8"
    ):
        total_cumulat = second_trimester(periodic_amt, month_name,fiscal_year, obj_id)

    # third trimester
    else:
        total_cumulat = third_trimester(periodic_amt, month_name,fiscal_year, obj_id)

    return total_cumulat


def first_trimester(periodic_amt, month_name, obj_id):
    """
    FirstTrimester cumulative amount calculation
    """

    # check if the month is shrawn
    if month_name == "1":
        first_total_cumulat = periodic_amt

    # check if the first trimster month is bhadra,ashoj,kartik
    elif month_name == "2" or month_name == "3" or month_name == "4":
        # get the recent db objects
        latest_obj = FirstTrimester.objects.get(id=obj_id)
        print("latest objects", latest_obj)
        if month_name == "2":
            first_total_cumulat = int(periodic_amt) + int(
                latest_obj.month1_cumulative_amount
            )
        elif month_name == "3":
            print(
                "month1_cumulative_amount 6666666666",
                latest_obj.month2_cumulative_amount,
            )
            first_total_cumulat = int(periodic_amt) + int(
                latest_obj.month2_cumulative_amount
            )
        elif month_name == "4":
            first_total_cumulat = int(periodic_amt) + int(
                latest_obj.month3_cumulative_amount
            )
        else:
            pass

    return first_total_cumulat


def second_trimester(periodic_amt, month_name,fiscal_year, obj_id):
    """
    SecondTrimester  cumulative amount calculation
    """

    # check if the month is mangsir
    if month_name == "5":
        try:
            first_trim = FirstTrimester.objects.get(year=fiscal_year)
            second_total_cumulat = periodic_amt + first_trim.month4_cumulative_amount
        except FirstTrimester.DoesNotExist:
            pass

    # check if the first trimster month is poush,magh,falgun
    elif month_name == "6" or month_name == "7" or month_name == "8":
        # get the recent db objects
        latest_obj = SecondTrimester.objects.get(id=obj_id)
        if month_name == "6":
            print("pous exectued")
            second_total_cumulat = int(periodic_amt) + int(
                latest_obj.month1_cumulative_amount
            )
        elif month_name == "7":
            second_total_cumulat = int(periodic_amt) + int(
                latest_obj.month2_cumulative_amount
            )
        elif month_name == "8":
            second_total_cumulat = int(periodic_amt) + int(
                latest_obj.month3_cumulative_amount
            )
        else:
            pass

    return second_total_cumulat


def third_trimester(periodic_amt, month_name,fiscal_year, obj_id):
    """
    ThirdTrimester  cumulative amount calculation
    """

    # check if the month is mangsir
    if month_name == "9":
        print("this is chaitra")
        try:
            second_trim = SecondTrimester.objects.get(year=fiscal_year)
            third_total_cumulat = periodic_amt + second_trim.month4_cumulative_amount
        except SecondTrimester.DoesNotExist:
            pass

        # third_total_cumulat = periodic_amt

    # check if the first trimster month is poush,magh,falgun
    # check if the first trimster month is poush,magh,falgun
    elif month_name == "10" or month_name == "11" or month_name == "12":
        # get the recent db objects
        latest_obj = ThirdTrimester.objects.get(id=obj_id)
        if month_name == "10":
            third_total_cumulat = int(periodic_amt) + int(
                latest_obj.month1_cumulative_amount
            )
        elif month_name == "11":
            third_total_cumulat = int(periodic_amt) + int(
                latest_obj.month2_cumulative_amount
            )
        elif month_name == "12":
            third_total_cumulat = int(periodic_amt) + int(
                latest_obj.month3_cumulative_amount
            )
        else:
            pass

    return third_total_cumulat


def periodic_percent(cumulative_amt, periodic_tar):
    """
    total periodic percent calcultion for different trimester
    """
    per_percent = (cumulative_amt / periodic_tar) * 100
    return per_percent


def yearly_percentage(final_year):
    """
    calcualtion of yearly percentage
    """
    # get the year from fiscal year db table
    fiscal_yr = FiscalYear.objects.get(year=final_year)

    # get the trimester_cumulative of first triemester of particular year
    first_trim_data_praticular_year = fiscal_yr.first_trimester.all()

    first_trim_cumulative = []
    first_trim_cumulative_id = []

    for item in first_trim_data_praticular_year:
        print("eam $$$$", item)
        print("eam $$$$", item.trimester_cumulative)

        first_trim_cumulative.append(item.trimester_cumulative)
        first_trim_cumulative_id.append(item.id)

    # get the trimester_cumulative of second triemester of particular year
    second_trim_data_praticular_year = fiscal_yr.second_trimester.all()
    second_trim_cumulative = []
    second_trim_cumulative_id = []

    for item in second_trim_data_praticular_year:
        second_trim_cumulative.append(item.trimester_cumulative)
        second_trim_cumulative_id.append(item.id)

    # get the trimester_cumulative of third triemester of particular year
    third_trim_data_praticular_year = fiscal_yr.third_trimester.all()
    third_trim_cumulative = []
    third_trim_cumulative_id = []

    for item in third_trim_data_praticular_year:
        third_trim_cumulative.append(item.trimester_cumulative)
        third_trim_cumulative_id.append(item.id)

    """
    formula: total_year = cumulative of (first trimester or second trimester or third trimester)/sum(cumulative of 1st trimester+cumulative of 2nd trimester+ cumulative of 3rd trimester)
    """
    for item in first_trim_cumulative:
        first_cumulative = item
    for item in second_trim_cumulative:
        second_cumulative = item
    for item in third_trim_cumulative:
        third_cumulative = item
    
    # first trimester yearly calculation
    first_trim_calc = (
        first_cumulative
        / (first_cumulative + second_cumulative + third_cumulative)
        * 100
    )

    # second trimester yearly calculation
    second_trim_calc = (
        second_cumulative
        / (first_cumulative + second_cumulative + third_cumulative)
        * 100
    )

    third_trim_calc = (
        third_cumulative
        / (first_cumulative + second_cumulative + third_cumulative)
        * 100
    )

    ################### saving all the  caluclated percentage instances into db #################
    # getting all the id
    for i in first_trim_cumulative_id:
        first_cumulative_id = i
    for i in second_trim_cumulative_id:
        second_cumulative_id = i
    for i in third_trim_cumulative_id:
        third_cumulative_id = i

    # getting the first trimester and save the yearly calcualted value into db
    FirstTrimester.objects.update_or_create(
        pk=first_cumulative_id,
        defaults={"yearly_percentage_financial": first_trim_calc},
    )

    # getting the second trimester and save the yearly calcualted value into db
    SecondTrimester.objects.update_or_create(
        pk=second_cumulative_id,
        defaults={"yearly_percentage_financial": second_trim_calc},
    )

    # getting the third trimester and save the yearly calcualted value into db
    ThirdTrimester.objects.update_or_create(
        pk=third_cumulative_id,
        defaults={"yearly_percentage_financial": third_trim_calc},
    )

    return {
        "first_trim_calc":first_trim_calc,
        "second_trim_calc":second_trim_calc,
        "third_trim_calc":third_trim_calc,

    }




def graph_calc(year_name):
    month = []
    for first in year_name.first_trimester.all():
        if first.month1_cumulative_amount == 0 or first.month1_cumulative_amount:
            month.append(first.month1_cumulative_amount)
        if first.month2_cumulative_amount == 0 or first.month2_cumulative_amount:
            month.append(first.month2_cumulative_amount)
        if first.month3_cumulative_amount == 0 or first.month3_cumulative_amount:
            month.append(first.month3_cumulative_amount)
        if first.month4_cumulative_amount == 0 or first.month4_cumulative_amount:
            month.append(first.month4_cumulative_amount)
    
    for second in year_name.second_trimester.all():
        if second.month1_cumulative_amount == 0 or second.month1_cumulative_amount:
            month.append(second.month1_cumulative_amount)
        if second.month2_cumulative_amount == 0 or second.month2_cumulative_amount:
            month.append(second.month2_cumulative_amount)
        if second.month3_cumulative_amount == 0 or second.month3_cumulative_amount:
            month.append(second.month3_cumulative_amount)
        if second.month4_cumulative_amount == 0 or second.month4_cumulative_amount:
            month.append(second.month4_cumulative_amount)


    for third in year_name.third_trimester.all():
        if third.month1_cumulative_amount == 0 or third.month1_cumulative_amount:
            month.append(third.month1_cumulative_amount)
        if third.month2_cumulative_amount == 0 or third.month2_cumulative_amount:
            month.append(third.month2_cumulative_amount)
        if third.month3_cumulative_amount == 0 or third.month3_cumulative_amount:
            month.append(third.month3_cumulative_amount)
        if third.month4_cumulative_amount == 0 or third.month4_cumulative_amount:
            month.append(third.month4_cumulative_amount)
    
    #for percentage
    total_cumulative_in_month = sum(month)
    percentage_permonth = []
    for item in month:
        if total_cumulative_in_month == 0:
            percentage_permonth.append(int(0))
        else:
            percentage_permonth.append(item *100/total_cumulative_in_month)
    return percentage_permonth





def ifnull(col):
    return col if col is not None else 0


def calculate_total(first_trim,second_trim,third_trim):
    """
    function to calculate the all total in progress and cumlative 
    """
    total_periodic = ifnull(first_trim.trimester_periodic if first_trim is not None else 0) + ifnull(second_trim.trimester_periodic if second_trim is not None else 0 )+ifnull(third_trim.trimester_periodic if third_trim is not None else 0)
    total_cumulative = ifnull(first_trim.trimester_cumulative if first_trim is not None else 0) + ifnull(second_trim.trimester_cumulative if second_trim is not None else 0)+ifnull(third_trim.trimester_cumulative if third_trim is not None else 0)
    total_perodic_target = ifnull(first_trim.periodic_target if first_trim is not None else 0) + ifnull(second_trim.periodic_target if second_trim is not None else 0)+ifnull(third_trim.periodic_target if third_trim is not None else 0)
    total_periodic_percentage_financial = ifnull(first_trim.periodic_percentage_financial if first_trim is not None else 0) + ifnull(second_trim.periodic_percentage_financial if second_trim is not None else 0)+ifnull(third_trim.periodic_percentage_financial if third_trim is not None else 0)
    total_year_percentage_financial = ifnull(first_trim.yearly_percentage_financial if first_trim is not None else 0) + ifnull(second_trim.yearly_percentage_financial if second_trim is not None else 0) + ifnull(third_trim.yearly_percentage_financial if third_trim is not None else 0)
    total_periodic_physical_progress = ifnull(first_trim.periodic_physical_progress if first_trim is not None else 0) + ifnull(second_trim.periodic_physical_progress if second_trim is not None else 0) + ifnull(second_trim.periodic_physical_progress if second_trim is not None else 0)
    # total_periodic_physical_progress = int(first_trim.periodic_physical_progress) + int(second_trim.periodic_physical_progress)+int(third_trim.periodic_physical_progress)
    total_cumulative_physical_progress = ifnull(first_trim.cumulative_physical_progress if first_trim is not None else 0) + ifnull(second_trim.cumulative_physical_progress if second_trim is not None else 0) + ifnull(third_trim.cumulative_physical_progress if third_trim is not None else 0)
    total_overall = ifnull(first_trim.overrall if first_trim is not None else 0) + ifnull(second_trim.overrall if second_trim is not None else 0)+ifnull(third_trim.overrall if third_trim is not None else 0)

    return {
        "total_periodic":total_periodic,
        "total_cumulative":total_cumulative,
        "total_perodic_target":total_perodic_target,
        "total_periodic_percentage_financial":total_periodic_percentage_financial,
        "total_year_percentage_financial":total_year_percentage_financial,
        "total_periodic_physical_progress":total_periodic_physical_progress,
        "total_cumulative_physical_progress":total_cumulative_physical_progress,
        "total_overall":total_overall

    }




def firsttrim_data_update(form,instance):
    """
    function to update the all the data of first trimester
    """
    month1_periodic_amount = form.cleaned_data.get("month1_periodic_amount",None)
    month2_periodic_amount = form.cleaned_data.get("month2_periodic_amount",None)
    month3_periodic_amount = form.cleaned_data.get("month3_periodic_amount",None)
    month4_periodic_amount = form.cleaned_data.get("month4_periodic_amount",None)

    month1_cumulative_amount = form.cleaned_data.get("month1_cumulative_amount",None)
    month2_cumulative_amount = form.cleaned_data.get("month2_cumulative_amount",None)
    month3_cumulative_amount = form.cleaned_data.get("month3_cumulative_amount",None)
    month4_cumulative_amount = form.cleaned_data.get("month4_cumulative_amount",None)
    year = form.cleaned_data.get("year",None)
    print("year",form.cleaned_data)

    print("first_trim_data",year)
    print("month1_cumulative_amount",month1_cumulative_amount)
    print("instance",instance.id)




    data = [[year,month1_periodic_amount,month2_periodic_amount,month3_periodic_amount,month4_periodic_amount]]
    first_trim_formdata = pd.DataFrame(data,columns=['year_year', 'month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'])
    print(first_trim_formdata)
    first_trim_obj = pd.DataFrame(FirstTrimester.objects.filter(year=year).values('year__year','month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'))
    print(first_trim_obj)
    #compare the two dataframe
    # difference_firsttrim = diff(first_trim_obj,first_trim_formdata)
    print("month 1 periodic amount#################",first_trim_formdata.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",first_trim_obj.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",first_trim_formdata.loc[0,"month1_periodic_amount"] - first_trim_obj.loc[0,"month1_periodic_amount"])


    #check if the entered month periodic is same as exist periodic amount
    unique_value = (first_trim_formdata.loc[0,"month1_periodic_amount"] != first_trim_obj.loc[0,"month1_periodic_amount"])
    if unique_value:
        #get the differnce between existing data and filled data
        first_trim_month1_formdata = first_trim_formdata.loc[0,"month1_periodic_amount"]
        first_trim_month1_obj = first_trim_obj.loc[0,"month1_periodic_amount"]

        #for bhadra
        print("first_trim_month1_formdata",first_trim_month1_formdata)
        print("first_trim_month1_obj",first_trim_month1_obj)


        if first_trim_month1_formdata > first_trim_month1_obj:
            print("entered into bhadra first")
            periodic_amount_diff = first_trim_month1_formdata - first_trim_month1_obj
            form.instance.month1_cumulative_amount += periodic_amount_diff
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            secondtrim_add_update_secondtrim(year,periodic_amount_diff)
            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month1_formdata < first_trim_month1_obj:
            print("entered into bhadra smaller")
            periodic_amount_diff = first_trim_month1_obj - first_trim_month1_formdata
            form.instance.month1_cumulative_amount -= periodic_amount_diff
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            secondtrim_subtractupdate_secondtrim(year,periodic_amount_diff)
            thirdtrim_subtract_update(year,periodic_amount_diff)
            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )
    unique_value_month2 = (first_trim_formdata.loc[0,"month2_periodic_amount"] != first_trim_obj.loc[0,"month2_periodic_amount"])
    if unique_value_month2:
        #get the differnce between existing data and filled data
        first_trim_month2_formdata = first_trim_formdata.loc[0,"month2_periodic_amount"]
        first_trim_month2_obj = first_trim_obj.loc[0,"month2_periodic_amount"]

        #for bhadra
        if first_trim_month2_formdata > first_trim_month2_obj:
            periodic_amount_diff = first_trim_month2_formdata - first_trim_month2_obj
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            secondtrim_add_update_secondtrim(year,periodic_amount_diff)
            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month2_obj < first_trim_month2_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            

            secondtrim_subtractupdate_secondtrim(year,periodic_amount_diff)
            thirdtrim_subtract_update(year,periodic_amount_diff)
            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )


    unique_value_month3 = (first_trim_formdata.loc[0,"month3_periodic_amount"] != first_trim_obj.loc[0,"month3_periodic_amount"])
    if unique_value_month3:
        #get the differnce between existing data and filled data
        first_trim_month3_formdata = first_trim_formdata.loc[0,"month3_periodic_amount"]
        first_trim_month3_obj = first_trim_obj.loc[0,"month3_periodic_amount"]

        #for bhadra
        if first_trim_month3_formdata > first_trim_month3_obj:
            periodic_amount_diff = first_trim_month3_formdata - first_trim_month3_obj
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            secondtrim_add_update_secondtrim(year,periodic_amount_diff)
            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month3_obj < first_trim_month3_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            secondtrim_subtractupdate_secondtrim(year,periodic_amount_diff)
            thirdtrim_subtract_update(year,periodic_amount_diff)

        

    unique_value_month4 = (first_trim_formdata.loc[0,"month4_periodic_amount"] != first_trim_obj.loc[0,"month4_periodic_amount"])
    if unique_value_month4:
        #get the differnce between existing data and filled data
        first_trim_month4_formdata = first_trim_formdata.loc[0,"month4_periodic_amount"]
        first_trim_month4_obj = first_trim_obj.loc[0,"month4_periodic_amount"]

        #for bhadra
        if first_trim_month4_formdata > first_trim_month4_obj:
            periodic_amount_diff = first_trim_month4_formdata - first_trim_month4_obj
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            secondtrim_add_update_secondtrim(year,periodic_amount_diff)
            thirdtrim_add_update(year,periodic_amount_diff)


        elif first_trim_month4_obj < first_trim_month4_formdata:
            periodic_amount_diff = first_trim_month4_obj - first_trim_month4_formdata
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            secondtrim_subtractupdate_secondtrim(year,periodic_amount_diff)
            thirdtrim_subtract_update(year,periodic_amount_diff)

            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )

    return True
    





def secondtrim_data_update(form,instance):
    """
    function to update the all the data of second trimester
    """
    month1_periodic_amount = form.cleaned_data.get("month1_periodic_amount",None)
    month2_periodic_amount = form.cleaned_data.get("month2_periodic_amount",None)
    month3_periodic_amount = form.cleaned_data.get("month3_periodic_amount",None)
    month4_periodic_amount = form.cleaned_data.get("month4_periodic_amount",None)

    month1_cumulative_amount = form.cleaned_data.get("month1_cumulative_amount",None)
    month2_cumulative_amount = form.cleaned_data.get("month2_cumulative_amount",None)
    month3_cumulative_amount = form.cleaned_data.get("month3_cumulative_amount",None)
    month4_cumulative_amount = form.cleaned_data.get("month4_cumulative_amount",None)
    year = form.cleaned_data.get("year",None)
    print("year",form.cleaned_data)

    print("first_trim_data",year)
    print("month1_cumulative_amount",month1_cumulative_amount)
    print("instance",instance.id)




    data = [[year,month1_periodic_amount,month2_periodic_amount,month3_periodic_amount,month4_periodic_amount]]
    second_trim_formdata = pd.DataFrame(data,columns=['year_year', 'month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'])
    print(second_trim_formdata)
    second_trim_obj = pd.DataFrame(SecondTrimester.objects.filter(year=year).values('year__year','month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'))
    print(second_trim_obj)
    #compare the two dataframe
    # difference_firsttrim = diff(second_trim_obj,second_trim_formdata)
    print("month 1 periodic amount#################",second_trim_formdata.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",second_trim_obj.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",second_trim_formdata.loc[0,"month1_periodic_amount"] - second_trim_obj.loc[0,"month1_periodic_amount"])


    #check if the entered month periodic is same as exist periodic amount
    unique_value = (second_trim_formdata.loc[0,"month1_periodic_amount"] != second_trim_obj.loc[0,"month1_periodic_amount"])
    if unique_value:
        #get the differnce between existing data and filled data
        first_trim_month1_formdata = second_trim_formdata.loc[0,"month1_periodic_amount"]
        first_trim_month1_obj = second_trim_obj.loc[0,"month1_periodic_amount"]

        #for bhadra
        if first_trim_month1_formdata > first_trim_month1_obj:
            periodic_amount_diff = first_trim_month1_formdata - first_trim_month1_obj
            form.instance.month1_cumulative_amount += periodic_amount_diff
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month1_formdata < first_trim_month1_obj:
            periodic_amount_diff = first_trim_month1_obj - first_trim_month1_formdata
            form.instance.month1_cumulative_amount -= periodic_amount_diff
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            thirdtrim_subtract_update(year,periodic_amount_diff)
            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )
    unique_value_month2 = (second_trim_formdata.loc[0,"month2_periodic_amount"] != second_trim_obj.loc[0,"month2_periodic_amount"])
    if unique_value_month2:
        #get the differnce between existing data and filled data
        first_trim_month2_formdata = second_trim_formdata.loc[0,"month2_periodic_amount"]
        first_trim_month2_obj = second_trim_obj.loc[0,"month2_periodic_amount"]

        #for bhadra
        if first_trim_month2_formdata > first_trim_month2_obj:
            periodic_amount_diff = first_trim_month2_formdata - first_trim_month2_obj
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month2_obj < first_trim_month2_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            

            thirdtrim_subtract_update(year,periodic_amount_diff)
            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )


    unique_value_month3 = (second_trim_formdata.loc[0,"month3_periodic_amount"] != second_trim_obj.loc[0,"month3_periodic_amount"])
    if unique_value_month3:
        #get the differnce between existing data and filled data
        first_trim_month3_formdata = second_trim_formdata.loc[0,"month3_periodic_amount"]
        first_trim_month3_obj = second_trim_obj.loc[0,"month3_periodic_amount"]

        #for bhadra
        if first_trim_month3_formdata > first_trim_month3_obj:
            periodic_amount_diff = first_trim_month3_formdata - first_trim_month3_obj
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            thirdtrim_add_update(year,periodic_amount_diff)

        elif first_trim_month3_obj < first_trim_month3_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

            thirdtrim_subtract_update(year,periodic_amount_diff)

        

    unique_value_month4 = (second_trim_formdata.loc[0,"month4_periodic_amount"] != second_trim_obj.loc[0,"month4_periodic_amount"])
    if unique_value_month4:
        #get the differnce between existing data and filled data
        first_trim_month4_formdata = second_trim_formdata.loc[0,"month4_periodic_amount"]
        first_trim_month4_obj = second_trim_obj.loc[0,"month4_periodic_amount"]

        #for bhadra
        if first_trim_month4_formdata > first_trim_month4_obj:
            periodic_amount_diff = first_trim_month4_formdata - first_trim_month4_obj
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            thirdtrim_add_update(year,periodic_amount_diff)


        elif first_trim_month4_obj < first_trim_month4_formdata:
            periodic_amount_diff = first_trim_month4_obj - first_trim_month4_formdata
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            thirdtrim_subtract_update(year,periodic_amount_diff)

            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )

    return True





def thirdtrim_data_update(form,instance):
    """
    function to update the all the data of third trimester
    """
    month1_periodic_amount = form.cleaned_data.get("month1_periodic_amount",None)
    month2_periodic_amount = form.cleaned_data.get("month2_periodic_amount",None)
    month3_periodic_amount = form.cleaned_data.get("month3_periodic_amount",None)
    month4_periodic_amount = form.cleaned_data.get("month4_periodic_amount",None)

    month1_cumulative_amount = form.cleaned_data.get("month1_cumulative_amount",None)
    month2_cumulative_amount = form.cleaned_data.get("month2_cumulative_amount",None)
    month3_cumulative_amount = form.cleaned_data.get("month3_cumulative_amount",None)
    month4_cumulative_amount = form.cleaned_data.get("month4_cumulative_amount",None)
    year = form.cleaned_data.get("year",None)
   

    data = [[year,month1_periodic_amount,month2_periodic_amount,month3_periodic_amount,month4_periodic_amount]]
    third_trim_formdata = pd.DataFrame(data,columns=['year_year', 'month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'])
    print(third_trim_formdata)
    third_trim_obj = pd.DataFrame(ThirdTrimester.objects.filter(year=year).values('year__year','month1_periodic_amount','month2_periodic_amount','month3_periodic_amount','month4_periodic_amount'))
    print(third_trim_obj)
    #compare the two dataframe
    # difference_firsttrim = diff(third_trim_obj,third_trim_formdata)
    print("month 1 periodic amount#################",third_trim_formdata.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",third_trim_obj.loc[0,"month1_periodic_amount"])
    print("month 1 periodic amount#################",third_trim_formdata.loc[0,"month1_periodic_amount"] - third_trim_obj.loc[0,"month1_periodic_amount"])


    #check if the entered month periodic is same as exist periodic amount
    unique_value = (third_trim_formdata.loc[0,"month1_periodic_amount"] != third_trim_obj.loc[0,"month1_periodic_amount"])
    if unique_value:
        #get the differnce between existing data and filled data
        first_trim_month1_formdata = third_trim_formdata.loc[0,"month1_periodic_amount"]
        first_trim_month1_obj = third_trim_obj.loc[0,"month1_periodic_amount"]

        #for bhadra
        if first_trim_month1_formdata > first_trim_month1_obj:
            periodic_amount_diff = first_trim_month1_formdata - first_trim_month1_obj
            print("periodic_amount_diff",periodic_amount_diff)
            form.instance.month1_cumulative_amount += periodic_amount_diff
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

        elif first_trim_month1_formdata < first_trim_month1_obj:
            periodic_amount_diff = first_trim_month1_obj - first_trim_month1_formdata
            form.instance.month1_cumulative_amount -= periodic_amount_diff
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff
            
            # .update(month1_cumulative_amount = periodic_amount_diff,
            # month2_cumulative_amount = periodic_amount_diff,month3_cumulative_amount = periodic_amount_diff,
            # month4_cumulative_amount = periodic_amount_diff
            # )
    unique_value_month2 = (third_trim_formdata.loc[0,"month2_periodic_amount"] != third_trim_obj.loc[0,"month2_periodic_amount"])
    if unique_value_month2:
        #get the differnce between existing data and filled data
        first_trim_month2_formdata = third_trim_formdata.loc[0,"month2_periodic_amount"]
        first_trim_month2_obj = third_trim_obj.loc[0,"month2_periodic_amount"]

        #for bhadra
        if first_trim_month2_formdata > first_trim_month2_obj:
            periodic_amount_diff = first_trim_month2_formdata - first_trim_month2_obj
            form.instance.month2_cumulative_amount += periodic_amount_diff
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff


        elif first_trim_month2_obj < first_trim_month2_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month2_cumulative_amount -= periodic_amount_diff
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

    unique_value_month3 = (third_trim_formdata.loc[0,"month3_periodic_amount"] != third_trim_obj.loc[0,"month3_periodic_amount"])
    if unique_value_month3:
        #get the differnce between existing data and filled data
        first_trim_month3_formdata = third_trim_formdata.loc[0,"month3_periodic_amount"]
        first_trim_month3_obj = third_trim_obj.loc[0,"month3_periodic_amount"]

        #for bhadra
        if first_trim_month3_formdata > first_trim_month3_obj:
            periodic_amount_diff = first_trim_month3_formdata - first_trim_month3_obj
            form.instance.month3_cumulative_amount += periodic_amount_diff
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff


        elif first_trim_month3_obj < first_trim_month3_formdata:
            periodic_amount_diff = first_trim_month2_obj - first_trim_month2_formdata
            form.instance.month3_cumulative_amount -= periodic_amount_diff
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff


        

    unique_value_month4 = (third_trim_formdata.loc[0,"month4_periodic_amount"] != third_trim_obj.loc[0,"month4_periodic_amount"])
    if unique_value_month4:
        #get the differnce between existing data and filled data
        first_trim_month4_formdata = third_trim_formdata.loc[0,"month4_periodic_amount"]
        first_trim_month4_obj = third_trim_obj.loc[0,"month4_periodic_amount"]

        #for bhadra
        if first_trim_month4_formdata > first_trim_month4_obj:
            periodic_amount_diff = first_trim_month4_formdata - first_trim_month4_obj
            form.instance.month4_cumulative_amount += periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff


        elif first_trim_month4_obj < first_trim_month4_formdata:
            periodic_amount_diff = first_trim_month4_obj - first_trim_month4_formdata
            form.instance.month4_cumulative_amount -= periodic_amount_diff
            form.instance.trimester_periodic += periodic_amount_diff
            form.instance.trimester_cumulative += periodic_amount_diff

    return True




"""=====================================
-- yearly percentage in first trimester-----
======================================"""

def overall_yearly_percentage_sum(*args):
    return sum(args)




def yearly_percentage_trimester(year):
    try:
        yearly_target  =  FiscalYear.objects.get(year=year).target
    except FiscalYear.DoesNotExist:
        yearly_target = None
    print("yearly_target",yearly_target)

    try:
        first_trim = FirstTrimester.objects.get(year=year)
        print("first_trim",first_trim.month4_cumulative_amount)
        
    except FirstTrimester.DoesNotExist:
        first_trim = None
    
    if first_trim:
        if first_trim.month4_cumulative_amount:
            first_trim_cumulative = first_trim.month4_cumulative_amount
            first_trim_target = first_trim.periodic_target

        else:
            first_trim_cumulative = 0
            first_trim_target = 0
        
    else:
        first_trim_cumulative = 0
        first_trim_target = 0



    try:
        second_trim = SecondTrimester.objects.get(year=year)
        

    except SecondTrimester.DoesNotExist:
        second_trim = None

    if second_trim:
        if second_trim.month4_cumulative_amount:
            second_trim_cumulative = second_trim.month4_cumulative_amount
            second_trim_target = second_trim.periodic_target

        else:
            second_trim_cumulative = 0
            second_trim_target = 0
        
    else:
        second_trim_cumulative = 0
        second_trim_target = 0


    try:
        third_trim = ThirdTrimester.objects.get(year=year) 

    except ThirdTrimester.DoesNotExist:
        third_trim = None
    print("third_trim",third_trim)
    if third_trim:
        if third_trim.month4_cumulative_amount:
            third_trim_cumulative = third_trim.month4_cumulative_amount
            third_trim_target = third_trim.periodic_target

        else:
            third_trim_cumulative = 0
            third_trim_target = 0

    else:
        third_trim_cumulative = 0
        third_trim_target = 0


    if first_trim_target !=0 and second_trim_target !=0 and third_trim_target !=0:
        periodic_target_total = first_trim_target + second_trim_target + third_trim_target 
    else:
        pass

    # first trimester yearly calculation
    if first_trim_cumulative !=0:
        print("first_trim_calc",first_trim_cumulative)
        print("yearly_target",yearly_target)

        first_trim_calc = (
            first_trim_cumulative
            / yearly_target
            * 100
        )
        print("first_trim_calc",first_trim_calc)
    else:
        first_trim_calc = 0
    if second_trim_cumulative !=0:
        # first trimester yearly calculation
        second_trim_calc = (
            second_trim_cumulative
            / yearly_target
            * 100
        )
    else:
        second_trim_calc = 0
        # first trimester yearly calculation
    if third_trim_cumulative !=0:
        third_trim_calc = (
            third_trim_cumulative
            / yearly_target
            * 100
        )
    else:
        third_trim_calc = 0
    overall_yearly_percentage = first_trim_calc+second_trim_calc+third_trim_calc


        # overall_yearly_percentage = first_trim_calc + second_trim_calc + third_trim_calc
    # else:
    #     first_trim_calc = 0
    #     second_trim_calc = 0
    #     third_trim_calc = 0
    #     overall_yearly_percentage = 0


    return {
        "first_trim_calc":first_trim_calc,
        "second_trim_calc":second_trim_calc,
        "third_trim_calc":third_trim_calc,
        "overall_yearly_percentage":overall_yearly_percentage

    }

    


def calc_cumulative_physical_progress(yrs):
    """
    Function to calculate the cumultive physical progress of second and third trimesters
    """

    #first trimester cumulative data
    try:
        first_trim = FirstTrimester.objects.get(year=yrs)
        print("first_trim",first_trim)
        
    except FirstTrimester.DoesNotExist:
        first_trim = None
    
    if first_trim:
        if first_trim.periodic_physical_progress:
            first_trim_physical_progress = first_trim.periodic_physical_progress

        else:
            first_trim_physical_progress = 0
        
    else:
        first_trim_physical_progress = 0

    #second trimester cumulative data
    try:
        second_trim = SecondTrimester.objects.get(year=yrs)
        print("first_trim",first_trim)
        
    except SecondTrimester.DoesNotExist:
        second_trim = None
    
    if second_trim:
        if second_trim.periodic_physical_progress:
            second_trim_physical_progress = (first_trim_physical_progress+second_trim.periodic_physical_progress)

        else:
            second_trim_physical_progress = 0
        
    else:
        second_trim_physical_progress = 0

    
    #third trimester cumulative data
    try:
        third_trim = ThirdTrimester.objects.get(year=yrs)
        print("third_trim",third_trim)
        
    except ThirdTrimester.DoesNotExist:
        third_trim = None
    if third_trim:
        if third_trim.periodic_physical_progress:
            third_trim_physical_progress = (second_trim_physical_progress+third_trim.periodic_physical_progress)

        else:
            third_trim_physical_progress = 0
        
    else:
        third_trim_physical_progress = 0
    
    return {
        "first_trim_physical_progress":first_trim_physical_progress,
        "second_trim_physical_progress":second_trim_physical_progress,
        "third_trim_physical_progress":third_trim_physical_progress,

    }

    
def overall_graph_calc(year_name):
    """Function to display the different graph based on overall Overall physical progress data"""
    trimester_data = []
    #get the first overall data
    try:
        first_trim_overall = FirstTrimester.objects.values('overrall').get(year__year=year_name)
        if first_trim_overall['overrall'] is not None:
            trimester_data.append(float(first_trim_overall['overrall']))
    except FirstTrimester.DoesNotExist:
        trimester_data.append(float(0))

    try:
        second_trim_overall = SecondTrimester.objects.values('overrall').get(year__year=year_name)
        if second_trim_overall['overrall'] is not None:
            trimester_data.append(float(second_trim_overall['overrall']))
    except SecondTrimester.DoesNotExist:
        trimester_data.append(float(0))
    
    try:
        third_trim_overall = ThirdTrimester.objects.values('overrall').get(year__year=year_name)
        if third_trim_overall['overrall'] is not None:
            trimester_data.append(float(third_trim_overall['overrall']))
    except ThirdTrimester.DoesNotExist:
        trimester_data.append(float(0))
    #for percentage 
    total_trimester = sum(trimester_data)
    percentage_per_trimester = []
    for item in trimester_data:
        if total_trimester == 0:
            percentage_per_trimester.append(0)
        else:
            percentage_per_trimester.append(item *100/total_trimester)
    return percentage_per_trimester




    
    
