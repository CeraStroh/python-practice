seconds = 14926

hours = seconds // 3600
left_over_minutes = seconds % 3600
minutes = left_over_minutes // 60

final_seconds = left_over_minutes % 60

print(str(seconds) , "seconds is the same as")
print(str(hours) , "hours," , minutes  , "minutes, and" , final_seconds , "seconds")