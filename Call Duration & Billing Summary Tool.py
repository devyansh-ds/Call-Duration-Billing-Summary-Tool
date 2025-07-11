import os

all_calls = [] #List to store all call records

# Function to read call records from the given file
def read_calls(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:  #Skip the header line
                parts = line.strip().split('#')  #Split line into fields
                if len(parts) >= 7:
                    all_calls.append(parts)  #Add valid records to the list
                else:
                    print("Invalid line skipped:", line)  #Notify if the line is incomplete
            return all_calls  #Return the list of all call records
    except FileNotFoundError:
        print("File not found:", file_path)  #Handle case where file doesn't exist
    except Exception as e:
        print("Something went wrong while reading the file:", e)  #Handle other errors

# Function to calculate total durations by call type
def total_durations(records):
    total_std = 0
    total_isd = 0
    total_free = 0
    for record in records:
        call_type = record[-1].lower()
        duration = int(record[3])
        if call_type == 'std':
            total_std += duration
        elif call_type == 'isd':
            total_isd += duration
        elif call_type == 'free':
            total_free += duration
    return total_std, total_isd, total_free

#=== MAIN START ===
input_folder = r'C:\Users\Devyansh\Desktop\stuff\my Projects\Call Duration & Billing Summary Tool\Call inputs' #Folder containing input call files
phone_number = input("Enter phone number to generate bill: ").strip() #Ask user to input phone number
file_path = os.path.join(input_folder, phone_number + '.txt') #Build the full path to the corresponding file
all_calls.clear() #Clear the list in case it's reused
all_calls = read_calls(file_path) #Read the call records from the file

#If reading failed or file not found, exit the program
if all_calls is None:
    exit()
total_std, total_isd, total_free = total_durations(all_calls) #Get total durations for STD, ISD, and Free calls

#Billing Calculations
std_rate = 1.20
isd_rate = 5.00
free_rate = 0.00

#Calculate bills by converting seconds to minutes
std_bill = round(((total_std / 60) * std_rate), 2)
isd_bill = round(((total_isd / 60) * isd_rate), 2)
free_bill = 0.0

# Total of all call charges
total_bill = round((std_bill + isd_bill + free_bill), 2)

#Final Billing Summary
print("========== USER BILLING SUMMARY ==========")
print("Call Type | Talk Time (sec) | Bill (₹)")
print("---------------------------------------------------")
print("STD       |", total_std,   "|", std_bill)
print("ISD       |", total_isd,   "|", isd_bill)
print("Free      |", total_free,  "|", free_bill)
print("---------------------------------------------------")
print("TOTAL BILL: ₹", total_bill)