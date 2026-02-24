#1
from datetime import datetime, timedelta

# Get current date and time
current_date = datetime.now()

# Subtract 5 days from current date
five_days_ago = current_date - timedelta(days=5)

# Print results
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))



#2
from datetime import datetime, timedelta

# Get today's date
today = datetime.now().date()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



#3
from datetime import datetime

# Get current time with microseconds
current_with_micro = datetime.now()
print("With microseconds:", current_with_micro)

# Remove microseconds
without_micro = current_with_micro.replace(microsecond=0)
print("Without microseconds:", without_micro)


#4
from datetime import datetime

# Format: YYYY-MM-DD HH:MM:SS
date_str1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

# Calculate difference in seconds
difference = abs((date2 - date1).total_seconds())

print(f"Difference in seconds: {difference}")