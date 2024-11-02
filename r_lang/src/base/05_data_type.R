# 1 numeric
num <- 30 # num is type of numeric
class(num) # [1] "numeric"

# 2 integer
int_num <- 30L # integer number
class(int_num) # [1] "integer"
num <- as.integer(num) # convert to integer
class(num) # [1] "integer"

# 3 complex
complex_num <- 3 + 4i # complex number
class(complex_num) # [1] "complex"
complex_num <- complex_num - 4i # subtract complex number
class(complex_num) # [1] "complex"
complex_num <- as.integer(complex_num) # convert to double
class(complex_num) # [1] "interger"

# 4 character
char <- "Hello, World!" # character
class(char) # [1] "character"
# 4.1 quotes
# good practice to use single quote
char_0 <- "Hello, World" # prefer to use double quote
char_1 <- 'Hello, "World"!' # use single quote only if double quote is used
# bad practice to use double quote
char_2 <- "Hello, 'World'!" # single quote in double quote
char_3 <- "Hello, \"World\"!" # escape double quote
char_4 <- 'Hello, \'World\'!' # escape single quote

# 5 logical
b <- TRUE # boolean
class(b) # [1] "logical"
b <- 1 # reassign b to type of double
class(b) # [1] "numeric"
# 6 differences between class and typeof
n <- 1L
# "class(1): integer, typeof(1): integer"
print(sprintf("class(%s): %s, typeof(%s): %s", n, class(n), n, typeof(n)))
n <- 1.1
# "class(1.1): numeric, typeof(1.1): double"
print(sprintf("class(%s): %s, typeof(%s): %s", n, class(n), n, typeof(n)))
