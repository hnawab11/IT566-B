from datetime import datetime
import json


d1 = datetime(2026,12,30,13,30)
d2 = datetime(2026,12,30,6,0)
d3 = datetime(2026,12,29,14,0)
d4 = datetime(2026,12,29,16,0)
d5 = datetime(2026,12,30)

# year = input("enter YYYYMMDD")
# d6 = datetime(int(year[0:4]),int(year[4:6]),int(year[6:9]))
# print(d6.strftime("%Y-%B-%d %I:%M%p"))
# print(d5.date() == d4.date())


d1s = d1.strftime("%Y-%m-%d %I:%M%p")
d2s = d2.strftime("%Y-%m-%d %I:%M%p")
d3s = d3.strftime("%Y-%m-%d %I:%M%p")
d4s = d4.strftime("%Y-%m-%d %I:%M%p")
def add_expense_entry(datetime_dictionary,datetime_object,expense):
    datetime_dictionary[datetime_object] = expense

def parse_datetime_dictionary_to_string_dictionary(datetime_dictionary):
    expense_dictionary_string_format = {}
    for line in datetime_dictionary:
        expense_dictionary_string_format[line.strftime("%Y-%m-%d %I:%M%p")] = datetime_dictionary[line]
    return expense_dictionary_string_format


def sort_datetime_dictionary(datetime_dictionary):
    sorted_dictionary = dict(sorted(datetime_dictionary.items(),reverse=False))
    return sorted_dictionary

expenses_dict = {d1:1.92,d2:7.95,d3:15,d4:40.55}
expenses_dict = sort_datetime_dictionary(expenses_dict)
# print("debug:", expenses_dict[d2])
expenses_dict_string = parse_datetime_dictionary_to_string_dictionary(expenses_dict)


# print(expenses_dict_string)
def print_expense_dict_string(expenses_dict_string):
    output = "|   Date  |  Time | Expense\n"
    total = 0
    for line in expenses_dict_string:
        output += f'{line.strftime("%Y-%m-%d %I:%M%p")} ${expenses_dict_string[line]}\n'
        total += expenses_dict_string[line]
    output += f'Total: ${round(total,2)}'
    return output
    

# print(print_expense_dict_string(expenses_dict_string))

def search_datetime_dictionry(datetime_dictionary,search_datetime_date):
    search_results = {}
    for dates in datetime_dictionary:
        if dates.date() == search_datetime_date.date():
            search_results[dates] = datetime_dictionary[dates]
            # search_results.append(dates)
    if len(search_results) == 0:
        return "Not found"
    return search_results
    

# print(search_datetime_dictionry(expenses_dict, d5))


def save_expenses_to_file(expense_entries, filename):
     with open(filename, "w") as f:
        json.dump(expense_entries, f, indent = 4)

save_expenses_to_file(expenses_dict_string, "expenses.json")


def load_expenses_from_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
    
def parse_dictionary_into_datetime_dictionary(unparsed_expense_dictionary):
    datetime_dictionary = {}
    for line in unparsed_expense_dictionary:
        parsed_datetime_key = datetime.strptime(line, "%Y-%m-%d %I:%M%p")
        datetime_dictionary[parsed_datetime_key] = unparsed_expense_dictionary[line]
    return datetime_dictionary

expenses_entries_dictionary = load_expenses_from_file("expenses.json")
parsed_expenses_entries_dictionary = parse_dictionary_into_datetime_dictionary(expenses_entries_dictionary)
# print(parsed_expenses_entries_dictionary)

def create_expense_dictionary():
    expense_dictionary = {}
    return expense_dictionary


def prompt_user():
    print("WELCOME TO PYTHON EXPENSE TRACKER APP\nWhat would you like to do?")
    user_choice = "yes"
    while user_choice == "yes":
        user_choice = input("[CREATE] EXPENSE FILE|[LOAD] EXPENSE FILE|\n")
        match user_choice:
            case "create":
                failure = True
                filename = ""
                while failure == True:
                    filename = input("Please enter a filename for expense tracker. Must end in .json\n")
                    if ".json" in filename:
                        failure = False
                expenses = create_expense_dictionary()
                save_expenses_to_file(expenses, filename)
            case "load":
                failure = True
                filename = ""
                expenses = dict()
                # nofileexists = True
                while failure == True:
                    filename = input("Please enter a filename for expense tracker. Must end in .json. Or type [quit] to exit\n")
                    if filename == "quit":
                        failure = False
                    if ".json" in filename:
                        failure = False
                        try:
                            expenses = parse_dictionary_into_datetime_dictionary(load_expenses_from_file(filename))
                            print(f"Expense tracker file has been loaded\nExpense Tracker Options Menu")
                            failure = False
                        except:
                            print("Error. File not found. Please create file first before loading or ensure filename is correct")
                            # nofileexists = True
                            failure = True
                            break
                            # failure = True
                    

                         
                # print(f"Diary file has been loaded\nDiary Options Menu")
                # print("Diary Options Menu")
                user_expense_tracker_menu_choice = "yes"
                while user_expense_tracker_menu_choice == "yes" and (failure == False and filename != "quit"):
                    # print(f"Diary file has been loaded\nDiary Options Menu")
                    user_expense_tracker_menu_choice = input("[Add] Adds an Expense [Search] Searches for expenses by date [Filter] Filter expenses before or after a certain date[Save] Saves new expenses to file [Print] Prints the entire expense tracker list\n")
                    print("DEBUG: ", expenses) ##will this be datetime dict or datetime string dict
                    match user_expense_tracker_menu_choice:
                        case "add":
                            date_entry=""
                            time_entry=""
                            expense_entry=""
                            while len(date_entry) == 0 or len(time_entry) == 0 or len(expense_entry) == 0:
                                date_entry = input("enter date for this entry in YYYYMMDD format. i.e 20261008\n")
                                time_entry = input("enter time for this entry in HH:MM 24 hr format. i.e 16:30")
                                expense_entry = input("Enter the expense for this entry in dollars. i.e 8.99\n")
                                datetime_key_object = datetime(int(date_entry[0:4]),int(date_entry[4:6]),int(date_entry[6:9]),int(time_entry[0:2]),int(time_entry[3:5]))
                            add_expense_entry(expenses,datetime_key_object,float(expense_entry))
                        case "save":
                            expenses = sort_datetime_dictionary(expenses)
                            save_expenses_to_file(parse_datetime_dictionary_to_string_dictionary(expenses), filename)
                        case "search":
                            search_datetime = input("Enter search date in YYYYMMDD format. i.e 20200130\n")
                            datetime_search_object = datetime(int(search_datetime[0:4]),int(search_datetime[4:6]),int(search_datetime[6:9]))
                            search_results = search_datetime_dictionry(expenses,datetime_search_object)
                            if(search_results == "Not found"):
                                print(search_results)
                            else:
                                print(print_expense_dict_string(search_results))

                            # print(search_diary_entry_by_date(diary,search_date))
                        case "filter":
                            filter_date = input("Enter search date in YYYYMMDD format. i.e 20200130\n")
                            filter_year_formatted = filter_date[0]+ filter_date[1]+ filter_date[2]+ filter_date[3]
                            filter_month_formatted = filter_date[4]+ filter_date[5]
                            filter_days_formatted = filter_date[6] + filter_date[7]
                            filter_date_formatted = f"{filter_year_formatted}-{filter_month_formatted}-{filter_days_formatted}"
                            filter_type = input(f"Are you search for diary entries [BEFORE] or [AFTER] {filter_date_formatted}?\n")
                            filtered_result = filter_diary_by_date(diary,filter_date,filter_type)
                            if len(filtered_result) != 0:
                                for results in filtered_result:
                                    year_formatted = results[0][0]+ results[0][1]+ results[0][2]+ results[0][3]
                                    month_formatted = results[0][4]+ results[0][5]
                                    days_formatted = results[0][6] + results[0][7]
                                    print(f"{year_formatted}-{month_formatted}-{days_formatted}: {results[1]}")
                            else:
                                print("Nothing found")
                        case "print":
                            print(print_expense_dict_string(expenses))
                        case _:
                            print("error. Please select add, load, search, print")
                    user_expense_tracker_menu_choice= input("Continue in user diary menu? [YES] [NO] \n")
                        
            case _:
                print("Error. Please select create, load, or yes to continue. Type anything else to exit")

        user_choice = input("Continue in main menu? [YES] [NO]\n")

prompt_user()