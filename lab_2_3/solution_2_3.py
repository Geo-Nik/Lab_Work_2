'''
Write the code to do following:
1. Generate string with lowercase and uppercase alphabet plus numbers.
2. Print 1-st symbol of string.
3. Print last symbol.
4. Print 3rd from start and 3rd from the end.
5. Slice first 8 symbols.
6. Print only symbols with index, which divides on 3 without remaining.
7. Print the symbol of the middle of the string text.
8. Reverse text using slice.
'''

#Importing the module
import string as st
#1. Generate string with lowercase and uppercase alphabet plus numbers.
S=st.ascii_lowercase+st.ascii_uppercase+st.digits
print('#1. Generate string with lowercase and uppercase alphabet plus numbers.')
print('S={}'.format(S))

#2. Print 1-st symbol of string.
print('2. Print 1-st symbol of string.')
print('1-st symbol of string S[0]="{}"'.format(S[0]))

#3. Print last symbol.
print('3. Print last symbol.')
print('Last symbol S_last="{}"'.format(S[len(S)-1]))

#4. Print 3rd from start and 3rd from the end.
print('4. Print 3rd from start and 3rd from the end.')
print('3-rd symbol from start "{}", 3-rd symbol from end "{}" '.format(S[2],S[-3]))

# 5. Slice first 8 symbols.
print('# 5. Slice first 8 symbols.')
print('Slise first 8 symbols "{}"'.format(S[:8]))

#6. Print only symbols with index, which divides on 3 without remaining.
print('6. Print only symbols with index, which divides on 3 without remaining.')
print('Symbols with index, which divides on 3 without remaining:{}'.format([a for a in S if S.index(a)%3==0]))

#7. Print the symbol of the middle of the string text.
print('7. Print the symbol of the middle of the string text.')
print('Symbol of the middle of the string text:"{}"'.format(S[len(S)//2]))

#8. Reverse text using slice.
print('8. Reverse text using slice.')
print('Revers text:"{}"'.format(S[::-1]))