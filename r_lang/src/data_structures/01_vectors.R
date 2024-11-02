# Vectors
# Vectors are the most basic data structure in R. They are sequences of elements of the same type.
# 1 Vectors Creation
# 1.1 Vectors can be created using the c() function.
fruits <- c("Apple", "Banana", "Cherry")
class(fruits) # character
print(fruits)
fruits.length <- length(fruits)
print(fruits.length)
# Access elements in a vector
print(fruits[1]) # "Apple"
print(fruits[2]) # "Banana"
print(fruits[3]) # "Cherry"
# Access elements in a vector using negative index: returns all elements except the specified index.
print(fruits[-1]) # "Banana" "Cherry"
# Update elements in a vector
fruits[1] <- "Durian"
print(fruits) # "Durian" "Banana" "Cherry"

# 1.2 Vectors can be created using the seq() function.
seq_1 <- seq(1, 10)
print(seq_1) # 1 2 3 4 5 6 7 8 9 10
seq_2 <- seq(1, 10, by = 2)
print(seq_2) # 1 3 5 7 9

# 1.3 Vectors can be created using the : operator.
seq_3 <- 1:10
print(seq_3) # 1 2 3 4 5 6 7 8 9 10

# 1.3.1 float numbers can be created using the : operator.
seq_4 <- 1.5:5
print(seq_4) # 1.5 2.5 3.5 4.5

# 1.4 Vectors can be created using the rep() function.
rep_1 <- rep(1, 5)
print(rep_1) # 1 1 1 1 1

# 1.5 Vectors can be created using the vector() function.
vector_1 <- vector("numeric", 5)
print(vector_1) # 0 0 0 0 0

# 1.6 Vectors can be created using the character(), logical(), integer(), double(), complex() functions.
vector_2 <- character(5)
print(vector_2) # "" "" "" "" ""

# 1.7 Vectors can be repeated using the rep() function.
a <- c(1, 2, 3)
b <- rep(a, times = 3, length.out = 8)
print(b) # 1 2 3 1 2 3 1 2

# 2 Vector operations
# 2.1 Arithmetic operations
a <- c(1, 2, 3)
b <- c(4, 5, 6)
print(a + b) # 5 7 9
print(a - b) # -3 -3 -3
print(a * b) # 4 10 18
print(a / b) # 0.25 0.4 0.5

# 2.2 Comparison operations
print(a > b) # FALSE FALSE FALSE
print(a < b) # TRUE TRUE TRUE
print(a == b) # FALSE FALSE FALSE
print(a != b) # TRUE TRUE TRUE

# 2.3 Logical operations
print(a & b) # TRUE TRUE TRUE
print(a | b) # TRUE TRUE TRUE
print(!a) # FALSE FALSE FALSE

# 2.4 Vectorized operations
# Vectorized operations are operations that are applied element-wise to vectors.
# For example, the following code snippet adds 1 to each element in the vector.
a <- c(1, 2, 3)
print(a + 1) # 2 3 4
print(a - 1) # 0 1 2
print(a * 2) # 2 4 6
# Update values in a vector based on a condition
a[a > 1] <- 0
print(a) # 1 0 0
a[5] <- 4
print(a) # 1 0 0 NA 4