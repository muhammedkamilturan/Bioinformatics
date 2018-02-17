from mkt.core.direction import Direction

d1 = Direction(5)
d2 = Direction(3)
d3 = Direction(10)

print(d1)
print(d2)
print(d3)

d1.complementary()
print(d1 == d2)
print(d2 == d3)
