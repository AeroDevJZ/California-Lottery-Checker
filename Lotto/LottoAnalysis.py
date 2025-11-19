import requests
import datetime

current_date = datetime.datetime.now()
print(current_date)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Input the list of numbers you want to check here
chosen_numbers = [[]]


# Gets the json file from the url and parse's it into python data types
def fetch_json(url):
    r = requests.get(url, headers=headers)
    print(r.status_code)  # 200 means no error
    # Extra safeguard against error
    r.raise_for_status()
    return r.json()


# Takes date in yyyy-mm-dd format and converts to yyyymmdd integer
def date_to_int(full_date=""):
    return int(full_date.replace("-", ""))


def int_to_date(num=0):
    year = num // 10000
    month = (num // 100) % 100
    day = num % 100
    return f"{month}-{day}-{year}"


def amount_won(reg_num=0, mega=False, cash_value=None):
    if reg_num == 0 and mega:
        return cash_value[-1]
    elif reg_num == 1 and mega:
        return cash_value[-2]
    elif (reg_num == 2 and mega):
        return cash_value[-3]
    elif (reg_num == 3 and not mega):
        return cash_value[-4]
    elif reg_num == 3 and mega:
        return cash_value[-5]
    elif reg_num == 4 and not mega:
        return cash_value[-6]
    elif reg_num == 4 and mega:
        return cash_value[-7]
    elif reg_num == 5 and not mega:
        return cash_value[-8]
    elif reg_num == 5 and mega:
        return cash_value[-9]
    else:
        return 0


# Sorts through the syntax of the json file to output the date followed by the winning numbers
def find_winning_numbers_and_amounts(json_list):
    winning_numbers = []
    for drawing in json_list["PreviousDraws"]:

        current_winning_numbers = [date_to_int(drawing["DrawDate"][:10])]

        for numbers_drawn in drawing["WinningNumbers"]:
            current_winning_numbers.append(
                int(drawing["WinningNumbers"][numbers_drawn]["Number"]))

        for amount_per_win in drawing["Prizes"]:
            current_winning_numbers.append(
                drawing["Prizes"][amount_per_win]["Amount"])
        winning_numbers.append(current_winning_numbers)

    return winning_numbers


# Adds the winning number list (goes in pages of 20) till start date is included and then trims list to match start and end date inclusive
# Only needs start date to be entered and will default end date to today, but can enter custom end date if desired
def list_by_date(start_year=current_date.year, start_month=current_date.month, start_day=current_date.day, end_year=current_date.year, end_month=current_date.month, end_day=current_date.day):
    start_date = (start_year * 10000) + (start_month * 100) + (start_day)
    end_date = (end_year * 10000) + (end_month * 100) + (end_day)
    in_range_numbers = find_winning_numbers_and_amounts(fetch_json(
        "https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/8/1/20"))
    i = 1

    # Emergency termination to not waste resources
    if start_date < 20000000 or end_date < 20000000 or start_date > end_date:
        print("Entered out of bounds value")
        quit()

    # Gets all of the pages of winning numbers
    while in_range_numbers[-1][0] > start_date:
        i += 1
        in_range_numbers.extend(find_winning_numbers_and_amounts(fetch_json(
            f"https://www.calottery.com/api/DrawGameApi/DrawGamePastDrawResults/8/{i}/20")))

    # Trims all of the excess dates before start
    while in_range_numbers[-1][0] < start_date:
        in_range_numbers.pop()

    # Trims all of the excess dates after end
    while in_range_numbers[0][0] > end_date:
        in_range_numbers.pop(0)
    return (in_range_numbers)


# Takes in a list of winning numbers in [[date, #1, #2, #3, #4, #5, mega#], [...], ...] and another list of lists of just the numbers to be checked format and returns a string summarizing the results
def analize_list(winning, chosen):
    # info_list = []
    winnings = 0
    # print(winning)
    for number_set in chosen:
        # last_win = ""
        # wins = 0
        # print(number_set)
        for lucky in winning:
            reg_num = 0
            mega = number_set[5] == lucky[6]
            for i in range(5):
                for j in range(5):
                    if number_set[i] == lucky[j + 1]:
                        reg_num += 1
            # print(lucky, "                ", amount_won(reg_num, mega, lucky))
            winnings += amount_won(reg_num, mega, lucky)
    return winnings


# Make changes to the input in list by date to run what program you want
print(analize_list(list_by_date(2024), chosen_numbers))
