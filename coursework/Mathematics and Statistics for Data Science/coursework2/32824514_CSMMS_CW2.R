# CSMMS_assignment_2
# By Weijie Cui
# 7 famous film actors matching rate
# calculate the probabilities by 100,000 random experiments
cal_prop <- function(n) {
  r <- 100000
  count <- 0
  for (i in 1:r) {
    sp <- sample(1:n)
    is.matched <- 0
    for (i in seq_along(sp)) {
      if (i == sp[i]) {
        is.matched <- 1
        break
      }
    }
    count <- count + is.matched
  }
  count / r
}


ls <- list()
for (i in 2: 15) {
  ls[[i-1]] <- cal_prop(i)
}
plot(2: 15, unlist(ls), type='l',
     xlab='number of actors', ylab='probability')

# 8 Eigenfaces
# 8.a calculate the average of the 3 faces
library(bmp)
img8.1 <- read.bmp(choose.files())
img8.2 <- read.bmp(choose.files())
img8.3 <- read.bmp(choose.files())
img8.avg <- (img8.1 + img8.2 + img8.3)/3
rotate <- function(x) t(apply(x, 2, rev))
image(rotate(img8.avg),col = gray((0:256)/256), axes=F, asp=1)

# 8.b the difference of each face from the average face
img8.1.diff <- img8.1 - img8.avg
img8.2.diff <- img8.2 - img8.avg
img8.3.diff <- img8.3 - img8.avg
par(mfrow=c(1,3))
image(rotate(img8.1.diff + 128), col = gray((0:256)/256), axes=F, asp=1)
image(rotate(img8.2.diff + 128), col = gray((0:256)/256), axes=F, asp=1)
image(rotate(img8.3.diff + 128), col = gray((0:256)/256), axes=F, asp=1)

# 8.c eigenfaces
# convert images to vectors and combind them
img8.diff.vec <- cbind(as.vector(img8.1.diff),
                   as.vector(img8.2.diff),
                   as.vector(img8.3.diff))

# calculate the covariance matrix
cov8.matrix <- cov(t(img8.diff.vec))

# calculate eigenvectors
eigen8.vectors <- eigen(cov8.matrix)$vectors

# convert vectors to matrices
row8 <- nrow(img8.1)
img8.1.eigenface <- matrix(eigen8.vectors[,1], nrow = row8, byrow = F)
img8.2.eigenface <- matrix(eigen8.vectors[,2], nrow = row8, byrow = F)
img8.3.eigenface <- matrix(eigen8.vectors[,3], nrow = row8, byrow = F)

# plot eigenfaces
par(mfrow=c(1,3))
image(rotate(img8.1.eigenface), col = gray((0:256)/256), axes=F, asp=1)
image(rotate(img8.2.eigenface), col = gray((0:256)/256), axes=F, asp=1)
image(rotate(img8.3.eigenface), col = gray((0:256)/256), axes=F, asp=1)

# 9 Binomial Distribution
# define generating function
generate_binomial_samples <- function(m, n) {
  colMeans(matrix(rbinom(n=m * n, size=10, prob=0.01), ncol = m, byrow=T))
}
# generate means
means9.1 <- generate_binomial_samples(10000, 20)
means9.2 <- generate_binomial_samples(10000, 100)
# plot figures
par(mfrow=c(2,1))
hist(means9.1, main='Histogram of the Means (20 Numbers)', xlab='means')
hist(means9.2, main='Histogram of the Means  (100 Numbers)', xlab='means')

# 10 Normal Distribution
# generate normal distribution numbers
x10 <- rnorm(20, mean=100, sd=4)
# generate noises
noise10 <- rnorm(length(x10), mean = 0, sd=1)
# calculate y values
y10 <- 2 + x10 + noise10
# plot scattered points
plot(y10~x10, asp=1, xlab='x', ylab='y')
# add mean lines
abline(h=mean(y10), col='blue')
abline(v=mean(x10), col='red')
legend('topleft', legend = c('Mean Y', 'Mean X'), col = c("blue", "red"))

# two sample t test of X and Y
t.test(x10,y10,conf.level=0.05)

# matched pair t test
t.test(y10-x10, conf.level = 0.05)

# 11 Weighted ridge regression estimates
# 11.b function for the weighted ridge regression estimates
weighted_ridge_regression <- function(x, y, w, lambda) {
  w.sq <- sqrt(w)
  j <- ncol(x) + 1
  x.wr <- rbind(cbind(w.sq,x*w.sq), lambda*diag(j))
  y.wr <- matrix(c(y*w.sq, rep(0, j)), ncol=1, byrow=F)
  # t(x.wr) %*% x.wr %*% t(x.wr) %*% y.wr
  coef(lm(y.wr ~ x.wr))
}
# test the weighted ridge regression estimates
weighted_ridge_regression(
  x=matrix(c(1,2,3,4,8),nrow=5,byrow = T),
  y=c(1,2.1,3.05,3.95,8.9),
  w=c(1),
  lambda=1)
x11.1 <- c(1:100)
x11.2 <- sample(1:10, length(x11.1), replace = TRUE)
noise11 <- rnorm(length(x11.1), mean = 0, sd=0.05)
y11 <- 2 * x11.1 + 3 * x11.2 + noise11
weighted_ridge_regression(
  x=matrix(data = cbind(x1=x11.1, x2=x11.2), ncol = 2, byrow = F),
  y=y11,
  w=c(1,1),
  lambda=1)
# 12 Multiply Questions
# 12.B Climbing a staircase
ways12 <- function(n) {
  # for cases that n <= 3, return the results
  if (n <= 0) {
    return(0)
  }else if (n == 1) {
    return (1)
  }else if (n == 2) {
    return (2)
  }else if (n == 3) {
    return (4)
  }
  # for cases that n > 3, use a dynamic programming method
  # init a list to store the number of possible ways
  ways <- c(c(1,2,3),rep(0,n-3))
  # compute the values step by step
  for (i in 4:n){
    ways[[i]] <- ways[[i-3]] + ways[[i-2]] + ways[[i-1]]
  }
  print(ways)
  ways[[length(ways)]]
}
ways12(30)
# 12.C Defaultnew
# 12.C.a: compare average income of defaulted and normal students
customers <- read.csv(file.choose())
head(customers)
students <- customers[customers$student=='Yes',c('default', 'balance', 'income')]
avg_income_defaulted <- mean(students[students$default=='Yes',]$income)
avg_income_normal <- mean(students[students$default!='Yes',]$income)
sprintf("The average income of defaulted students is: %.2f", 
        avg_income_defaulted)
sprintf("The average income of normal students is: %.2f", 
        avg_income_normal)
if (avg_income_defaulted > avg_income_normal) {
  sprintf("The average income of defaulted students is %.2f%% higher than normal students", 
          (avg_income_defaulted-avg_income_normal)/avg_income_normal*100)
} else if (avg_income_defaulted == avg_income_normal){
  print("The average income of defaulted students is equal to the one of normal students")
} else {
  sprintf("The average income of normal students is %.2f%% higher than defaulted students", 
          (avg_income_normal-avg_income_defaulted)/avg_income_defaulted*100)
}
# 12.C.b: logistic regression
# Fit logistic regression model
customers$default <- ifelse(customers$default=='Yes', 1, 0)
customers$student <- ifelse(customers$student=='Yes', 1, 0)
# train the model
lr.model <- glm(default ~ student + balance + income,
                data = customers,
                family = binomial)
lr.model$coefficients
predict(lr.model,data.frame(student=1, income=17500, balance=970), type="response")
predict(lr.model,data.frame(student=1, income=17500, balance=970*1.04), type="response")
