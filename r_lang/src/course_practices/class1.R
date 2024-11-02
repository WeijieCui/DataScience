# R functions
abs(-123)

# 1. sin(45)
sin(90*pi/180)
a <- rep(3, 5)
a <- c(1,2,3)
a
length(a)
a[1]
a <- c(1,2,3,4,5)
a[-1]
a[-2]
a[-2,-4]
a[-1, -2]
a[-1: -2]
a[-1: -3]
a[-1: -1]
m1 <- matrix(c(1,2,3,4), ncol=2, byrow=TRUE); m1
m2 <- cbind(c(1,2,3), c(4,5,6)); m2
m3 <- rbind(c(1,2,3), c(4,5,6)); m3
is.matrix(m1)
as.matrix(c(1,2,5))
a <- c(1,2,5); a
as.matrix(a); a
a <- c(c(1,2), c(3,4))
a
s <- c('abc', 'efg')
s
s[1] <- 1
s
s[1] <- c(1,2)
s
# matrix
m1 <- matrix(c(1,2,3,4,5,6), ncol=3, byrow=TRUE); m1
m1[2]
m1[2,]
m1[2,3]
m1[2,1]
m1[m1>=3]
m1[m1>3]<-0
m1

list()
c(c(1,2,3), c(4,5,6))
# 4
x <- seq(0:30); x
help(seq)
ns <- seq(from=0, to=360, by=(360-0)/179); ns
length(ns)
sin(ns*pi/180)

# Matrix product
A <- matrix(c(2,1,3,2,4,4), nrow=2, byrow=TRUE); A
A1 <- matrix(c(2,1,3,2,4,4), nrow=3, byrow=TRUE); A2
b <- c(4, -1); b
b1 <- c(4, -1, 0)
b2 <- matrix(c(4, -1, 0), nrow=1); b2
A * b
A * b1
A1 * b2
A %*% b
A %*% as.matrix(b)
# Determinant
A <- matrix(c(5,3,1,0,2,1,3,1,2), nrow=3, byrow=TRUE); A
det(A)
rank(A)
qr(A)

# QR decomposition
A <- matrix(c(2,-2,18,2,1,0,1,2,0), nrow=3, byrow=TRUE); A
a1 <- A[,1]; a1
a2 <- A[,2]; a2
a3 <- A[,3]; a3
# normalised vector
n1 <- sqrt(sum(a1 ^ 2)); n1
e1 <- a1 / n1; e1
n2 <- sqrt(sum(a2 ^ 2)); n2
e2 <- a2 / n2; e2
n3 <- sqrt(sum(a3 ^ 2)); n3
e3 <- a3 / n3; e3
Q <- matrix(c(e1,e2,e3), nrow=3, byrow=FALSE); Q
R <- matrix(c(sum(a1*e1),sum(a2*e1),sum(a3*e1),
             0, sum(a2*e2),sum(a3*e2),
             0,0,sum(a3*e3)), nrow=3, byrow=TRUE); R
Q %*% R
Q
R
qr(A)
# 8
a <- c(3,2,1); a
b <- c(-2, 3, 2); b
c <- c(0,1,2); c
# angle of a and b
angle <- acos(sum(a * b) / (sqrt(sum(a1 ^ 2) * sqrt(sum(a2 ^ 2))))); angle

# function
inner_prod <- function(a,b) {
  temp <- sum(a * b)
  return(temp)
}
inner_prod(c(1,2,3),c(3,4,5))
ang <- function(a,b) {acos(sum(a*b)/(sqrt(sum(a^2)) * sqrt(sum(b^2))))}              
ang(c(1,1),c(0,1)) * 180 / pi

a <- matrix(c(1,2,3,4,5,6), nrow=2, byrow=TRUE); a
dim(a)
# function excercise
# 1 columns sum
colSums <- function(m) {
  c <- dim(m)[2]
  s <- rep(0, c)
  for(i in 1:c) {
    s[i] <- sum(m[,i])
  }
  return(s)
}
colSums(a)

# check fac
fac <- function(n) {
  f <- 1
  t <- n
  repeat {
    if (t < 2) break
    f <- f * t
    t <- t - 1
  }
  f
}
fac(3)

fibonacci <- function(n) {
  a <- 1
  b <- 1
  while (n > 1) {
    c <- a + b
    a <- b
    b <- c
    n <- n - 1
  }
  b
}
for (i in 1: 10) {
  print(fibonacci(i))
}

a <- matrix(c(1,0,0,1),nrow=2,byrow = TRUE); a

a ^ 2
2 * a
(2 * a) ^ 5
del(a)
det(a)
a <- matrix(c(1,2,3,4), nrow=2,byrow=TRUE); a
det(a)
a <- matrix(c(1,2,3,4,5,6), nrow=2,byrow=T); a
det(a)
a <- matrix(c(5,3,1,0,2,1,3,1,2), nrow=3, byrow=T); a
det(a)
5 * (2 * 2 - 1 * 1) - 3 * (0 * 2 - 1 * 3) + 1 * (0 * 1 - 3 * 2)

names <- c('a', 'b', 'c')
ages <- c(10,12,11)
df <- data.frame(names,ages)
df
arr <- array(1:24,dim=c(2,3,4)); arr

arr
arr[1,1,3]
arr[,1,]
arr[,,3]
arr[1,2,]
arr[1,3,1]
arr[2,2,1]
arr[2,3,4]
a <- arr[1][1][1][1]
arr4 <- array(1:24, dim=c(2,3,2,2)); arr4
arr4[,,2,1]
mp <- hashtable()
sethash(mp,'a', 1)
sethash(mp,'b', 2)
sethash(mp,'c', 3)
gethash(mp,'c')
sethash(mp, 'c', 4)
mp[[2]] <- 20
mp[[1]]
mp[[2]]
