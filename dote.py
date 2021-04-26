old_file = open("new.csv", "r")
new_file = open("new1,csv", "w")
for line in old_file.readlines():
    cleaned_line =line.replace(',','.')
    new_file.write(cleaned_line)
old_file.close
new_file.close