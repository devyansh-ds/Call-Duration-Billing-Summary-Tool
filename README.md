# Call-Duration-Billing-Summary-Tool
## Project Description:
Python-based command-line tool that reads mobile call records from structured text files and generates a formatted billing summary based on the duration and type of each call. The tool parses input files containing #-separated values for each call, calculates the total talk time for STD (local long-distance), ISD (international), and Free call categories, and then applies predefined per-minute rates to compute a detailed user bill.
The program also handles file input errors gracefully and filters out incomplete or invalid entries, ensuring accurate and reliable billing. This project was designed to strengthen core programming fundamentals including file handling, string parsing, conditionals, user input handling, and formatted output presentation.

## Key Features:
- Reads and processes structured .txt call logs
- Supports calculation of call durations by type:
  - STD (charged at ₹1.20/min)
  - ISD (charged at ₹5.00/min)
  - Free (₹0.00)
- Converts talk time from seconds to minutes for billing
- Displays a clear, readable CLI billing summary
- Handles missing files or invalid lines gracefully
- Works by entering the user’s phone number to locate the respective call log file

## Input Format:
- Each input .txt file must follow this format, where fields are separated by #:
  - custid#fromcall#tocall#duration#status#time#type
  - 54321#9986019198#9110336344#637#complete#02:30#std
  - 54321#9986019198#8363738388#634#complete#02:30#isd
  - 54321#9986019198#8363346356#755#complete#02:30#free
- The script expects one file per user, named after the phone number (e.g., 9986019198.txt)
- These files are stored in a folder path defined at the top of the script

## Technologies Used:
- Python 3
- File I/O (open, readlines, split)
- Conditional logic (if-elif)
- String and list manipulation
- Basic error handling (try-except)
- CLI input/output

## How to Run:
- Place all input .txt files in the specified folder path.
- Open the script in any Python environment or terminal.
- Update the input_folder variable in the script if needed.
- Run the script and enter the desired phone number when prompted.
- View the generated billing summary in the terminal.

## What I Learned:
- Reading structured data from text files
- Filtering and validating user data
- Applying real-world billing logic with rates and conversions
- Gracefully handling user input errors and file-not-found issues
- Formatting output cleanly for terminal display
