library(Matrix)
require(Matrix)

A1 <- matrix(c(2, -1, 0, -1, 0,
               -1, 3, -1, 3, -1,
               0, -1, 3, 1, 0,
               -1, 3, 1, 6, -1,
               0, -1, 0, -1, 1), nrow = 5, byrow = TRUE)
t(chol(A1))
A2 <- matrix(c(2, -1, 0, -1,
               -1, 3, -1, 3,
               0, -1, 3, 1,
               -1, 3, 1, 6), nrow = 4, byrow = TRUE)
t(chol(A2))

cholesky_decomposition <- function(A) {
  if (!isSymmetric.matrix(A)) {
    print('error: parameter A should be a n*n symmetric matrix')
    return()
  }
  n <- nrow(A)
  for (i in 1:n) {
    if (A[i, i] < 0) {
      print(sprintf('error: the leading minor of order %d is not positive', i))
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
      print(sprintf('error: the leading minor of order %d is not positive', i))
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
          print(sprintf('error: the leading minor of order %d is not positive', i))
          return()
        }
        L[j, i] <- product / L[i, i]
      }
    }
  }
  L
}

L <- cholesky_decomposition(A2); L
L %*% t(L)

CholeskyDecompositionTest <- function() {
  error.count <- 0
  for (mtx in list(
    matrix(c(2, -1, 0, -1,
             -1, 3, -1, 3,
             0, -1, 3, 1,
             -1, 3, 1, 6), nrow = 4, byrow = TRUE),
    matrix(c(2, -1, 0, -1, 0,
             -1, 3, -1, 3, -1,
             0, -1, 3, 1, 0,
             -1, 3, 1, 6, -1,
             0, -1, 0, -1, 1), nrow = 5, byrow = TRUE)
  )) {
    L <- cholesky_decomposition(mtx)
    mtx.new <- L %*% t(L)
    bias <- 0.1^6
    n <- ncol(mtx)
    if (sum(abs(mtx.new - mtx) > bias)) {
      print('different results:')
      print(mtx)
      print(mtx.new)
      error.count <- error.count + 1
    }
  }
  if (error.count) {
    print(sprintf('CholeskyDecomposition function test failed: %d testcase.', error.count))
  }else {
    print('CholeskyDecomposition function test passed.')
  }
}

CholeskyDecompositionTest()