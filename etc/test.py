def get_divisors_sum(num):
  s = 0
  i = 1
  while i <= num:
    if num % i == 0:
      s += i
    i += 1
  return s

def is_prime_number(num):
  if num == 1:
    return False

  i = 2
  while i < num:
    if num % i == 0:
      return False
    i += 1
    
  return True

def is_prime_number_v2(num):
  return get_divisors_sum(num) == num + 1

print("3은 소수입니다 : {}".format(is_prime_number_v2(3)))
print("4는 소수입니다 : {}".format(is_prime_number(4)))
print("1000은 소수입니다 : {}".format(is_prime_number(1000)))