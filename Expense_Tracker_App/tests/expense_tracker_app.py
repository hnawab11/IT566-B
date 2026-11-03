from datetime import datetime
import json


d1 = datetime(2026,12,30,13,30)
d2 = datetime(2026,12,30,6,0)
d3 = datetime(2026,12,29,14,0)
d4 = datetime(2026,12,29,16,0)
d5 = datetime(2026,12,30)

# print(d5.date() == d4.date())


d1s = d1.strftime("%Y-%m-%d %I:%M%p")
d2s = d2.strftime("%Y-%m-%d %I:%M%p")
d3s = d3.strftime("%Y-%m-%d %I:%M%p")
d4s = d4.strftime("%Y-%m-%d %I:%M%p")

def parse_datetime_dictionary_to_string_dictionary(datetime_dictionary):
    expense_dictionary_string_format = {}
    for line in datetime_dictionary:
        expense_dictionary_string_format[line.strftime("%Y-%m-%d %I:%M%p")] = datetime_dictionary[line]
    return expense_dictionary_string_format


def sort_datetime_dictionary(datetime_dictionary):
    sorted_dictionary = dict(sorted(datetime_dictionary.items()))
    return sorted_dictionary

expenses_dict = {d1:1.92,d2:7.95,d3:15,d4:40.55}
expenses_dict = sort_datetime_dictionary(expenses_dict)
# print(expenses_dict)
expenses_dict_string = parse_datetime_dictionary_to_string_dictionary(expenses_dict)


# print(expenses_dict_string)
def print_expense_dict_string(expenses_dict_string):
    output = ""
    for line in expenses_dict_string:
        output += f'{line} ${expenses_dict_string[line]}\n'
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
    

print(search_datetime_dictionry(expenses_dict, d5))


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
