from datetime import datetime, timedelta

# Subtract five days from current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago was:", five_days_ago)

# Print yesterday, today, tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)

# Drop microseconds from datetime
current_date = datetime.now()
current_date = current_date.replace(microsecond=0)
print("Datetime without microseconds:", current_date)

# Calculate two date difference in seconds
date1 = datetime(2024, 3, 20, 12, 0, 0)
date2 = datetime(2024, 3, 21, 12, 0, 0)
difference = date2 - date1
difference_seconds = difference.total_seconds()
print("Difference in seconds between two dates:", difference_seconds)
