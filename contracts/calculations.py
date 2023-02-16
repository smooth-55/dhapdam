from datetime import date, datetime


def calculate_time_extended(contract):
    """
    Function to calculate time extended based on original schedule
    """
    if contract.date_of_completion_revised:
        date_first = (contract.date_of_completion_revised - contract.date_of_agreement).days
        date_second = (contract.date_of_completion - contract.date_of_agreement).days
        result = (
            date_first
            / date_second
            * 100
        )
        return result


def calculate_time_elapsed(contract):
    """
    Function to calculate time elapsed based on revised schedule
    """
    try:
        date_first = (date.today() - contract.date_of_agreement).days
        date_second = (contract.date_of_completion_revised - contract.date_of_agreement).days
        result = (
            (date_first)
            / (date_second)
            * 100
        )
    except:
        result = 0
    print("result",result)

    return result


def calculate_time_remaining(contract):
    """
    Function to calculate time remaning based on extended schedule days
    """
    print("date_of_completion_revised",contract.date_of_completion_revised)
    print("date.today",date.today())
    try:

        # result = (contract.date_of_completion_revised - date.today()).days

        start = contract.date_of_completion_revised
        end = date.today()
        difference = start-end
        # result = (end.year - start.year) * 12 + (end.month  - start.month )
        result = (difference.days)
    except:
        result = 0
    print("result",result)
    return result


def calculate_financial_progress(contract, financial_amount):
    result = (float(financial_amount) / float(contract.amount)) * 100
    return result


def calculate_progress_status(physical_percent, contract, financial_date):
    try:
        result = calculate_time_elapsed(contract, financial_date)
        final_result = float(physical_percent) / float(result)

        if final_result >= 1:
            return "Before Schedule"
        else:
            return "After schedule"
    except:
        return "No revised Date of Completion"
