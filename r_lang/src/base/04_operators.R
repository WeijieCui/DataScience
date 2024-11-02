# 1 add
x <- 5L
y <- 3L
x + y
# 2 subtract
x - y
# 3 multiply
x * y
# 4 divide
x / y
class(x / y) # [1] "numeric"
typeof(x / y) # [1] "double"

# 5 exponent
x ^ y
typeof(x ^ y) # [1] "numeric"

# 6 modulus
x %% y
class(x %% y) # [1] "numeric"

# 7 Numerical Comparison
x > y # TRUE
x >= y # TRUE
x < y # FALSE
x == y # FALSE