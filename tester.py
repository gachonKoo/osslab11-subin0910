import geo.utils as utils

# Pythagoras example
a, b = 3, 4
c = utils.pythagoras(a, b)
print(f"c = {c:.1f}")  # 소수점 1자리까지 출력

# Circle area example
r = 10
area = utils.circle(r)
print(f"area = {area:.15f}")  # 소수점 15자리까지 출력
