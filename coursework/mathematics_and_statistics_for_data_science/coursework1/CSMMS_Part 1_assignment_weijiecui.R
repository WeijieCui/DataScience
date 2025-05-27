# CSMMS_assignment_1
# By Weijie Cui
# 1.b Cholesky Decomposition
# 1.b.1 import required libraries
library(Matrix)
require(Matrix)
# 1.b.2 define CholeskyDecomposition function
CholeskyDecomposition <- function(A) {
  if (!isSymmetric.matrix(A)) {
    print('[ERROR] parameter A should be a n*n symmetric matrix')
    return()
  }
  n <- nrow(A)
  for (i in 1:n) {
    if (A[i, i] < 0) {
      print(sprintf('[ERROR] the leading minor of order %d is not positive', i))
      return()
    }
  }
  L <- Matrix(0, n, n)
  for (i in 1:n) {
    square <- A[i, i]
    if (1 <= i) {
      for (j in 1:i) {
        square <- square - (L[i, j]^2)
      }
    }
    if (square < 0) {
      print(sprintf('[ERROR] the leading minor of order %d is not positive', i))
      return()
    }
    L[i, i] <- sqrt(square)
    if ((i + 1) <= n) {
      for (j in (i + 1):n) {
        product <- A[i, j]
        if (1 <= (j - 1)) {
          for (k in 1:(j - 1)) {
            product <- product - L[i, k] * L[j, k]
          }
        }
        if ((L[i, i] == 0) & product != 0) {
          print(sprintf('[ERROR] the leading minor of order %d is not positive', i))
          return()
        }
        L[j, i] <- product / L[i, i]
      }
    }
  }
  L
}

# 1.b.3 test answers in part(a)
CholeskyDecomposition(matrix(c(3, -1, 0, -1, 0,
                               -1, 3, -1, 3, -1,
                               0, -1, 3, 1, 0,
                               -1, 3, 1, 5, -1,
                               0, -1, 0, -1, 1), nrow = 5, byrow = TRUE))

# 5 x 5 sparse Matrix of class "dtCMatrix"

# [1,]  1.7320508  .          .        .         .        
# [2,] -0.5773503  1.6329932  .        .         .        
# [3,]  .         -0.6123724  1.620185 .         .        
# [4,] -0.5773503  1.6329932  1.234427 0.6900656 .        
# [5,]  .         -0.6123724 -0.231455 0.4140393 0.6324555

# 1.b.4 test CholeskyDecomposition function
CholeskyDecompositionTest <- function() {
  error.count <- 0
  # test case
  for (mtx in list(
    matrix(1,1,1),
    matrix(2,2,2),
    matrix(c(2, -1,0,
             -1, 3,-1,
             0,-1,3), nrow = 3, byrow = TRUE),
    matrix(c(2, -1, 0, -1,
             -1, 3, -1, 3,
             0, -1, 3, 1,
             -1, 3, 1, 6), nrow = 4, byrow = TRUE)
  )) {
    L <- CholeskyDecomposition(mtx)
    print(L)
    mtx.new <- L %*% t(L)
    bias <- 0.1^6
    n <- ncol(mtx)
    if (sum(abs(mtx.new - mtx) > bias)) {
      print('[FAILED] different results:')
      print(mtx)
      print(mtx.new)
      error.count <- error.count + 1
    }
  }
  if (error.count) {
    print(sprintf('[FAILED] CholeskyDecomposition function test failed: %d testcase.', error.count))
  }else {
    print('[PASSED] CholeskyDecomposition function test passed.')
  }
}

CholeskyDecompositionTest()

# Question 2: Singular Value Decomposition
# 2.b Singular Value Decomposition
# 2.b.1 import required libraries
library(Matrix)
require(Matrix)
# 2.b.2 compare 
A2 <- matrix(c(1,2,
               1,0,
               1,0,
               1,0), nrow=4,byrow=TRUE)
svd(A2)
# $d
# [1] 2.449490 1.414214

# $u
# [,1] [,2]
# [1,] -0.8660254  0.5
# [2,] -0.2886751 -0.5
# [3,] -0.2886751 -0.5
# [4,] -0.2886751 -0.5
# $v
# [,1]       [,2]
# [1,] -0.7071068 -0.7071068
# [2,] -0.7071068  0.7071068

# Question 3: Differential Equations
# 3.b Differential Equations
# 3.b.1 import required libraries
library(deSolve)
# 3.b.2 define initial conditions
initial.3 <- c(y=0, v=1, u=-2.5)
# 3.b.3 define differential equations
derivs.3 <- function (t,Ov,parms){
  with(as.list(c(Ov,parms)), {
    dy <- v
    dv <- u
    du <- exp(-t) + y + v - u
    list(c(dy, dv, du))
  })
}
# 3.b.4 define time interval
times <- seq(from = 0, to = 5, by = 0.001)
# 3.b.5 call ode function and get output
ode.out3 <- ode(y = initial.3, times = times, func = derivs.3, parms = NULL)
# 3.b.6 plot a curve for ode results
plot(ode.out3[,"time"], ode.out3[,"y"], type = "l", col="green", lwd=2,
     main="Trends of Y by Time", xlab="time", ylab="y")
# 3.b.7 Analytic solution
y3<-function(t) (t - 0.25 * t^2)*exp(-t)
curve(y3, 0, 5, lty=2, add=T, col="red")

# Question 4: Fish and Humans
# 4.a solve the system of equations
# 4.b Differential Equations
# 4.b.1 import required libraries
library(deSolve)
# 4.b.2 define initial conditions
initial.4 <- c(x=10000, y=60)
# 4.b.3 define parameters
parameters.4 <- c(a=5, b=0.01, c=100, d=0.01, g=0.0001)
# 4.b.4 define differential equations
derivs.4 <- function (t, Ov, params){
  with(as.list(c(Ov,params)), {
    dx <- a*x - g*x^2 - b*x*y
    dy <- -c*y + d*x*y
    list(c(dx, dy))
  })
}
# 4.b.6 call ode function and get output
ode.out4 <- ode(y=initial.4, times=NULL, func=derivs.4, parms=NULL)
# 4.b Differential Equations
# 4.b.1 import required libraries
library(deSolve)
# 4.b.2 define initial conditions
initial.4 <- c(x=10000, y=60)
# 4.b.3 define parameters
parameters.4 <- c(a=5, b=0.01, c=100, d=0.01, g=0.0001)
# 4.b.4 define differential equations
derivs.4 <- function (t, Ov, params){
  with(as.list(c(Ov,params)), {
    dx <- a*x - g*x^2 - b*x*y
    dy <- -c*y + d*x*y
    list(c(dx, dy))
  })
}
# 4.b.5 define time interval
times.4 <- seq(from=0, to=5, by=0.001)
# 4.b.6 call ode function and get output
ode.out4 <- ode(y=initial.4, times=times.4, func=derivs.4, parms=parameters.4)
# 4.b.7 plot a curve for ode results
par(mfrow = c(1, 3))
plot(ode.out4[,"x"], ode.out4[,"y"], type="l",col="red",
     main='Trends of Fish and Humans', xlab="Number of Fish", ylab="Number of Humans")
plot(ode.out4[,"time"], ode.out4[,"x"], type="l", col="green",
     main='Trends of Fish', xlab="Time", ylab="Number of Fish")
plot(ode.out4[,"time"], ode.out4[,"y"], type="l", col="blue",
     main='Trends of Humans', xlab="Time", ylab="Number of Humans")
# 4.d find the minimum value of b, at which the human population dies out 
# 4.d.1 iterate values of b to find the minimum
for (b.x in seq(from=0.2, to=0.4, by=0.001)) {
  # update parameters
  parameters.4 <- c(a=5, b=b.x, c=100, d=0.01, g=0.0001)
  # call ode function and get output
  ode.out4 <- ode(y=initial.4, times=times.4, func=derivs.4, parms=parameters.4)
  # find the minimum value of y
  my.4 <- min(ode.out4[,"y"])
  if (as.integer(b.x*1000) %% 10 == 0) {
    print(sprintf('b: %.3f -> min y: %f', b.x, my.4))
  }
  # if the minimum value of y less than 1, print result and break the loop
  if (my.4 < 1) {
    print(ode.out4[ode.out4[,'y']<=1, c('x','y')])
    plot(ode.out4[,"x"], ode.out4[,"y"], type="l",col="red",
         main='Trends of Fish and Humans', xlab="Number of Fish", ylab="Number of Humans")
    print(sprintf('The minimum value of b is %.3f.', b.x))
    break
  }
}
# 5 Question 5: Multivariate Optimization
# 5.a Part A: plot f(x, y)
# 5.a.1 define function f and expression f
f.5 <- function(x, y) {
  (x^2 + y - 11)^2 + (x + y^2 - 7)^2
}
f.5.exp <- expression(f(x, y) == (x^2 + y - 11)^2 + (x + y^2 - 7)^2)
# 5.a.2 define ranges of variables and calculate function results -4.5 <= x,y <= 4.5
x.5 <- seq(-4.5, 4.5, length.out = 50)
y.5 <- seq(-4.5, 4.5, length.out = 50)
out.5 <- outer(x.5, y.5, f.5)
# 5.a.3 plot
persp(x.5, y.5, out.5, theta = 30, phi = 30, expand = 0.5,
      col = 'lightblue', ltheta = 120, shade = 0.5,
      ticktype = 'detailed', xlab = 'x',
      ylab = 'y', zlab = 'f(x,y)', main='Graph of f(x,y)', sub=f5.exp)

# 5.b To approximate f(x, y) by Newton Raphson method
# 5.b.1 define a multivariate differentiation function
MDeriv<-function(expr, x.name){
  #Get 1st partial derivatives 
  deriv1<-lapply(x.name, function(x,f) D(f,x), f=expr)
  #Construct vector labels
  temp<-paste0("d",x.name)
  names(deriv1)<-temp
  #Initialize a list to store 2nd partial derivatives
  deriv2<-list()
  #Get 2nd partial derivatives
  for (i in 1:length(x.name)) {
    deriv2[[i]]<-lapply(x.name, function(x,f) D(f,x), f=deriv1[[i]])
  }
  #Construct vector of labels for 2nd partial derivatives
  names2<-c(sapply(temp, paste0, x.name))
  deriv2<-unlist(deriv2)
  names(deriv2)<-names2
  c(deriv1,deriv2)
}

# 5.b.2 define a Newton Raphson function
optim.NewtonRaphson<-function(expr,name,start){
  # Get partial derivatives
  mderiv <- MDeriv(expr, name)
  # first derivative vector
  grad <- function(xp) {
    data <- as.list(c(x <- xp[1], y <- xp[2]))
    c(with(data, eval(mderiv$dx)), with(data, eval(mderiv$dy)))
  }
  # the reverse of the second derivative matrix
  hess.rev <- function(xp) {
    data <- as.list(c(x<-xp[1],y<-xp[2]))
    with(data, eval(mderiv$dxx))
    hess <- Matrix(c(with(data, eval(mderiv$dxx)),
                    with(data, eval(mderiv$dxy)),
                    with(data, eval(mderiv$dyx)),
                    with(data, eval(mderiv$dyy))),
                  nrow = 2, byrow = T)
    solve(hess)
  }
  # Newton-Raphson, Want to find x satisfying grad(x)=0
  x.old<-start # starting value for x
  n.iter <- 1 # count the number of iterations
  while(n.iter <= 50){
    x.new <- x.old - hess.rev(x.old) %*% grad(x.old)
    tol<-sqrt(sum((x.new-x.old)^2))
    # convergence criteria
    if (tol <= 10^-10) {
      break
    }
    # footprints
    # if (n.iter%%5==0) print(x.new)
    x.old <- x.new
    n.iter <- n.iter + 1
  }
  c(value=with(as.list(c(x<-x.new[1],y<-x.new[2])), eval(expr)),
    optimum=x.new,
    gradient=grad(x.new),
    n.iterations=n.iter)
}
# Iterate several points to search critical points
for (start.5 in list(
  c(-4,-4),
  c(-4,4), 
  c(4,-4),
  c(4,4)
  )){
  opt.out.5 <- optim.NewtonRaphson(expression((x^2 + y - 11)^2 + (x + y^2 - 7)^2),
                      c('x','y'), 
                      start.5)
  print('-----------------------solutition---------------------------')
  print(c(value=opt.out.5$val, optimum=opt.out.5$optimum))
}
# 5.c Find all the critical points
# 5.c.1 Write the function with parameters in a vector
f.vec.5 <- function(vec) (vec[1]^2+vec[2]-11)^2 + (vec[1]+vec[2]^2-7)^2
# 5.c.2 To get the second derivative matrix
mderiv <- MDeriv(expression((x^2 + y - 11)^2 + (x + y^2 - 7)^2),c('x', 'y'))
# 5.c.3 Iterate start points to find the critical points
for (start.5 in list(
  c(-4, -4),
  c(-4, 4), 
  c(4, -4),
  c(4, 4)
  )){
  # call optim function and get a Optimal solution
  opt.out.5 <- optim(start.5,f.vec.5)
  data <- as.list(c(x=opt.out.5$par[1],y=opt.out.5$par[2]))
  # wrap and calculate hess matrix
  hess <- Matrix(c(with(data, eval(mderiv$dxx)),
                  with(data, eval(mderiv$dxy)),
                  with(data, eval(mderiv$dyx)),
                  with(data, eval(mderiv$dyy))),
                nrow = 2, byrow = T)
  print(c(value=opt.out.5$val, point=opt.out.5$par, eigen.values=eigen(hess)$values))
}
# Question 6: Back Propagation
