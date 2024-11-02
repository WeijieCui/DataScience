# 1 for loop
for (i in 0:6) {
  print(i * 2 + 1)
}

# 2 while loop
count <- 10
while (count >= 0) {
  if (count %% 5 == 0) {
    print(count)
    count <- count - 1
    next # skip the rest of the loop
  }
  print(sprintf("count: %d", count))
  if (count == 3) {
    print(sprintf("end at: %d", count))
    break
  }
  count <- count - 1
}
