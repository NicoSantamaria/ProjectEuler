# What is the largest prime factor of the number 600851475143?
number = 600851475143

isPrimeFac <- function(num) {
  if (number %% num == 0) {
    for (x in 2:round(num**0.5)) {
      if (num %% x == 0) {
        return(FALSE)
      }
    }
    return(TRUE)
  }
  return(FALSE)
}

i <- round(number**0.5)
while (isPrimeFac(i) == FALSE){
  i <- i - 1
}

print(i)
# 6857