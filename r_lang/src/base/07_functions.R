# 1 function without return
hello <- function(name) {
  paste("Hello", name)
}

hello("world")

# 2 function with return
fullName <- function(fname, lname) {
  fname <- paste(fname, lname)
  return(fname)
}

fullName("John", "Doe")

add <- function(a, b) {
  return(a + b)
}

add(add(1, 2), add(3, 4))

# 3 function with default value
add <- function(a, b = 1) {
  return(a + b)
}

add(3)

# 4 function with variable number of arguments
add_all <- function(arg0, ...) {
  args <- list(...)
  sum <- arg0
  for (arg in args) {
    sum <- sum + arg
  }
  return(sum)
}

add_all(1, 2, 3, 4, 5)

# 5 nested function
accumulate <- function(a) {
  sum <- a

  inner <- function(b) {
    sum <<- sum + b
    return(sum)
  }

  return(inner)
}

acc <- accumulate(1)
acc(2)
acc(3)

# 6 Recursion
factorial <- function(n) {
  if (n < 0) {
    stop("n must be a non-negative integer")
  }else if (n == 0) {
    return(1)
  } else {
    return(n * factorial(n - 1))
  }
}

factorial(5)
