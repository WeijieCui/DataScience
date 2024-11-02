# Lists
# Lists are a collection of objects, which is ordered and changeable.
# 1 Lists Creation
# 1.1 Lists can be created using the list() function.
list_1 <- list("Apple", "Banana", "Cherry")
print(list_1)

# 2 List Operations
# 2.1 Access elements in a list
print(list_1[1]) # "Apple"
# 2.2 Update elements in a list
list_1[1] <- "Durian"
# 2.3 Add elements to a list
list_1[length(list_1) + 1] <- "Elderberry"
append(list_1, "Peach")
print(list_1)
# 2.4 Remove elements from a list
list_1[3] <- NULL
print(list_1)
nums <- list(1, 2, 3)
print(nums[-2]) # return the list without the second element: 1 3
# 2.5 Combine lists
list_2 <- list("Fig", "Grape")
list_3 <- c(list_1, list_2)
print(list_3)


# compare with vectors
# 3.1 Data types: Vectors can only store elements of the same data type, while lists can store elements of different data types.
# 3.2 Access elements: Vectors are accessed by index, while lists are accessed by name or index.
# 3.3 Length: Vectors have a fixed length, while lists can have a variable length.
# 3.4 Operations: Vectors support arithmetic operations, while lists do not.
nums <- list_1 <- list(1, 2, 3)
# nums * 2 # Error in nums * 2 : non-numeric argument to binary operator
# 3.5 Memory: Vectors are more memory efficient than lists.
# 3.6 Performance: Vectors are faster than lists.
# 3.7 Use cases: Vectors are used for mathematical operations, while lists are used for storing different types of data.
# 3.8 Conversion: Vectors can be converted to lists using the as.list() function, while lists can be converted to vectors using the unlist() function.