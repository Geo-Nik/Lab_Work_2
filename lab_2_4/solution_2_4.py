'''
Write the code to do following:
1. Generate list with lowercase and uppercase alphabet plus numbers
2. Print 1-st symbol of list
3. Print last symbol
4. Print 3rd from start and 3rd from the end
5. Slice first 10 symbols
6. Print only symbols with index, which divides on 2 without remaining
7. Print only integer values from list
8. Reverse list using slice
9. Convert base list into string
'''
import string as st
# 1. Generate list with lowercase and uppercase alphabet plus numbers
print('1. Generate list with lowercase and uppercase alphabet plus numbers')
S=st.ascii_lowercase+st.ascii_uppercase+st.digits
L=list(S)
print('list from string:{}'.format(L))

# 2. Print 1st symbol of list
print('2. Print 1st symbol of list')
print('1-st symbol of list:"{}"'.format(L[0]))

# 3. Print last symbol
print('3. Print last symbol')
print('Last symbol:"{}"'.format(L[-1]))

#4. Print 3rd from start and 3rd from the end
print('4. Print 3rd from start and 3rd from the end')
print('3rd symbol from start:"{}", 3rd symbol from end:"{}" '.format(L[2],L[-3]))

#5. Slice first 10 symbols
print('5. Slice first 10 symbols')
print('Slice first 10 symbols:{}'.format(L[:10]))

# 6. Print only symbols with index, which divides on 2 without remaining
print('6. Print only symbols with index, which divides on 2 without remaining')
print('symbols with index, which divides on 2 without remaining:{}'.format([a for a in L if L.index(a)%2==0 ]))

#7. Print only integer values from list
print('Only integer values from list:{}'.format([a for a in L if a.isdigit()==True]))

#8. Reverse list using slice
print('8. Reverse list using slice')
print('8. Reversed list:{}'.format(L[::-1]))

#9. Convert base list into string
print('9. Convert base list into string')
print('list2str:{}'.format(''.join(L)))
