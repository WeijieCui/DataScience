# R does not have a command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# 1 A simple variable
name <- "Mars"
age <- 4
var_1 <- var_2 <- var_3 <- "same values"

# 2 A iterative variable
for (i in 1:3) {
  print(i)
}

# 3 Variable names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname).
# Rules for R variables are:
# - A variable name must start with a letter or a period(.), and can be a combination of letters, digits, period(.)
#   and underscore(_). If it starts with period(.), it cannot be followed by a digit.
# - Variable names are case-sensitive
# - Reserved words cannot be used as variables:
#   if else repeat while function for in next break
#   TRUE FALSE NULL Inf NaN NA NA_integer_ NA_real_ NA_complex_ NA_character_
.a.1_ <- 1
print(.a.1_)
help(reserved)

# 4 Object naming convention
# Use only lowercase letters and numbers.
# Use underscores (_) (so called snake case) to separate words within a name.
# Use names that are concise and meaningful (this is not easy!).
# Generally, variable names should be nouns and function names should be verbs.
# Where possible, avoid re-using names of common functions and variables. This will cause confusion for the readers of your code.
# If you find yourself attempting to cram data into variable names (e.g. model_2018, model_2019, model_2020), consider using a list or data frame instead.
# good naming
first_name <- "Mars"
day_1 <- 1
# bad naming
firstName <- "Mars"
day1 <- 1

# 5 Variable scope
# A variable's scope is the context in which the variable can be referenced/used.
# In R, variables can have local or global scope.
# - A variable declared inside a function is local to that function.
func <- function() {
  local_var <- "local"
  print(local_var)
}

# local_var # Error: object 'local_var' not found
# - A variable declared outside a function is global.
global_var <- "global"
global_var

func2 <- function() {
  # global_var is accessible inside the function
  print(global_var)
}

func2()