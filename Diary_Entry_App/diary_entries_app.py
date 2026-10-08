import datetime, json

def print_diary(diary_entries):
    for date in diary_entries:
        year = date[0]+ date[1]+ date[2]+ date[3]
        month = date[4] + date[5]
        day = date[6]+date[7]
        output = year + "-" + month + "-" + day
        print(f"{output}: {diary_entries[date]}")
def sort_diary_by_date(diary_entries, sort_type):
    sorted_diary = {}
    if sort_type == "dsc":
        for date in sorted(diary_entries,reverse=True):
            sorted_diary[date] = diary_entries[date]
        return sorted_diary
    elif sort_type == "asc":
        for date in sorted(diary_entries,reverse=False):
            sorted_diary[date] = diary_entries[date]
        return sorted_diary
def filter_diary_by_date(diary_entries, desired_date, filter_type):
    search_list = []
    if(filter_type == "after"):
        for key in diary_entries.keys():
            # print(key)
            if key > desired_date:
                search_list.append((key, diary_entries.get(key)))
                # search_list.append(diary_entries.get(key))
        return search_list
    elif(filter_type == "before"):
        for key in diary_entries.keys():
            # print(key)
            if key < desired_date:
                search_list.append((key, diary_entries.get(key)))
                # search_list.append(diary_entries.get(key))
        return search_list
    
def save_diary_to_file(diary_entries, filename):
    with open(filename, "w") as f:
        json.dump(diary_entries, f, indent = 4)
def load_diary_from_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
   
def create_diary_dictionary():
    diary_dictionary = {}
    return diary_dictionary

def add_diary_entry(diary_entries, date, body):
    diary_entries[date] = body

def search_diary_entry_by_date(diary_entries, search_date):
    search_result = str(diary_entries.get(search_date))
    if search_result == "None":
        # print(f"An entry for {search_date} was not found")
        return "Not Found"
    return f"{search_date[0:4]}-{search_date[4:6]}-{search_date[6:8]}:{search_result}"

 
def prompt_user():
    print("WELCOME TO PYTHON ENTRIES APP\nWhat would you like to do?")
    user_choice = "yes"
    while user_choice == "yes":
        user_choice = input("[CREATE] DIARY FILE|[LOAD] DIARY FILE|\n")
        match user_choice:
            case "create":
                failure = True
                filename = ""
                while failure == True:
                    filename = input("Please enter a filename for diary. Must end in .json\n")
                    if ".json" in filename:
                        failure = False
                diary = create_diary_dictionary()
                save_diary_to_file(diary, filename)
            case "load":
                failure = True
                filename = ""
                diary = dict()
                while failure == True:
                    filename = input("Please enter a filename for diary. Must end in .json\n")
                    if ".json" in filename:
                        failure = False
                        try:
                            diary = load_diary_from_file(filename)
                            failure = False
                        except:
                            print("Error. File not found. Please create file first before loading or ensure filename is correct")
                            failure = True
                        
                print("Diary file has been loaded")
                print("Diary Options Menu")
                user_diary_menu_choice = "yes"
                while user_diary_menu_choice == "yes":
                    user_diary_menu_choice = input("[Add] Adds an Entry [Search] Searches for entry by date [Filter] Filter entries before or after a certain date[Save] Saves new entries to file [Print] Prints the entire diary\n")
                    match user_diary_menu_choice:
                        case "add":
                            date=""
                            body=""
                            while len(date) == 0 or len(body) == 0:
                                date = input("enter date for this entry in YYYYMMDD format. i.e 20261008")
                                body = input("Enter the text content for this entry")

                            add_diary_entry(diary,date,body)
                        case "save":
                            diary = sort_diary_by_date(diary,"asc")
                            save_diary_to_file(diary, filename)
                        case "search":
                            search_date = input("Enter search date in YYYYMMDD format. i.e 20200130")
                            print(search_diary_entry_by_date(diary,search_date))
                        case "filter":
                            filter_date = input("Enter search date in YYYYMMDD format. i.e 20200130\n")
                            filter_type = input(f"Are you search for diary entries before or after {filter_date}?\n")
                            filtered_result = filter_diary_by_date(diary,filter_date,filter_type)
                            if len(filtered_result) != 0:
                                for results in filtered_result:
                                    # print(results[0][0])
                                    year_formatted = results[0][0]+ results[0][1]+ results[0][2]+ results[0][3]
                                    month_formatted = results[0][4]+ results[0][5]
                                    days_formatted = results[0][6] + results[0][7]
                                    print(f"{year_formatted}-{month_formatted}-{days_formatted}: {results[1]}")
                            else:
                                print("Nothing found")
                        case "print":
                            print_diary(diary)
                        case _:
                            print("error. Please select add, load, search, print")
                    user_diary_menu_choice = input("Continue in user diary menu?\n")
                        
            case _:
                print("error. Please select create, load, or yes to continue. Type anything else to exit")

        user_choice = input("Continue in main menu?\n")

# prompt_user()


def main():
    prompt_user()

if __name__ == "__main__":
    main()
else:
    print(__name__, "has been imported")
