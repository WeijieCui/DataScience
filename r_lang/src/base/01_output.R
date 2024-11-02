# 1 standard output without using a print function

# 1.1 output strings
"output a string with double quotes"
'output a string with single quote'

# 1.2 output numbers
1

# 1.3 output variables
name <- "Mars"
name

# 2 standard output with a print function

# 2.1 print a string
print("output a string with a print function")

# 2.2 print multi strings
age <- 4
print(paste0("My name is ", name, " and I am ", age, "."))

# 3 standard output with c-sytle formatting options
sprintf("My name is %s and I am %d.", name, age)
sprintf("%.2f", 1 / 3)
sprintf("Capital %s,", c("A", "B", "C"))

# 4 output to a file
# 4.1 output one-line text to a file
sentence <- "This is a hello world file"
writeLines(sentence, "one_line.txt")
# 4.2 output multi-line text to a file - 1
sentence <- "This is a hello world file\nThis is the content"
writeLines(sentence, "multi_lines1.txt")
# 4.3 output multi-line text to a file - 2
multi_sentences <- "headline
First line
Second Line"
writeLines(multi_sentences, "multi_lines2.txt")
# 4.4 output data to a csv file
# Create a data frame
kids <- data.frame (
  Name = c("Mars", "Max"),
  Age = c(4, 2),
  Favor = c("Apple", "Blueberry"))
# write kids into kids csv file
write.csv(kids, "kids.csv")
