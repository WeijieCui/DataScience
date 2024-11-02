# 1 Read content from a file
# 1.1 Read text from a txt file
text <- readLines('one_line.txt')
text

# 1.2 Read text from a multi-line file
lines <- readLines('multi_lines1.txt')
for (line in lines) {
  print(line)
}

# 2 Read data from command line
var_1 <- readline(prompt = "Enter number one: ");
var_2 <- readline(prompt = "Enter number two: ");
print(sprintf("the sum of numbers is: %d", as.integer(var_1) + as.integer(var_2)))