from mkt.core.fragment import Fragment

f1 = Fragment('tep1', 5, 'atgcatgcatgcatgc', 'deneme dizisi', 10)
f2 = Fragment('tep1', 3, 'atgcatgcatgcatgc', 'deneme dizisi', 10)
for i in f1:
    print(i)

print('SLICE [1:5] = ', f1[1:5])


print(f1 == f2)
f2.start = 5
print(f1 == f2)

print(f1)
f1.complementary()
print(f1)

