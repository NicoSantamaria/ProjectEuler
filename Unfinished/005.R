# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
prime_base <- 2*3*5*7*11*13*17*19
num_vec = rep(c(prime_base), times = 20)
divisors = c(1:20)
zero.v = rep(c(0), times = 20) 
truth.v = rep(c(TRUE), times = 20) 
# while () {
#   num_vec = num_vec + rep(c(prime_base), times = 20)
#   print(num_vec)
# }
#
repeat {
  if ((num_vec %% divisors == zero.v) == truth.v) {
    print(num_vec)
    break
  }
  num_vec = num_vec + rep(c(prime_base), times = 20)
}