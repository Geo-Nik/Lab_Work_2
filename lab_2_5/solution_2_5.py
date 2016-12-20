'''
Write the code to do following:
1. Create dict with 5 items, where keys will be country name and value -
domain name, i.e. {Ukraine:UA}
2. Create another dict with 5 items, where values of countries will be keys,
and values will be the capitals i.e. {'UA': 'Kiev'}
3. Add one more element to each dict above
4. Print sentence "Domain for COUNTRY is DOMAIN." for each record in
countries with the replace from dicts
5. Print sentence "The capital of COUNTRY is CAPITAL" for each record in
capitals with the replace from dicts
6. Merge sentences above together with one cycle
7. Add to each value of first dict another two domains: COM and GOV
'''
# 1. Create dict with 5 items, where keys will be country name and value
print('Create dict with 5 items, where keys will be country name and value')
D={'Ukraine':'UA','Poland':'PL','Spaine':'Es','Germany':'DE', 'Belgium':'BE'}
print('dict country:',D)


#2. Create another dict with 5 items, where values of countries will be keys,
#and values will be the capitals i.e. {'UA': 'Kiev'}
print('2. Create another dict with 5 items, where values of countries will be keys and values will be the capitals')
D1={'Ukraine':'Kyiv','Poland':'Warsaw','Spaine':'Madrid','Germany':'Berlin', 'Belgium':'Brussels'}
print('dict capitals:',D1)

# 3. Add one more element to each dict above
print('3. Add one more element to each dict above')
D.update({'Georgia':'GE'})
print('dict country:',D)
D1.update({'Georgia':'Tbilisi'})
print('dict capitals:',D1)

#4. Print sentence "Domain for COUNTRY is DOMAIN." for each record in
#countries with the replace from dicts
print('Domain for COUNTRY is DOMAIN')
for country in D:
    print('Domain for {} is {}'.format(country,D[country]))
print('*******************************************************')
print('The capital of COUNTRY is CAPITAL')
#5. Print sentence "The capital of COUNTRY is CAPITAL" for each record in
#capitals with the replace from dicts
for country in D1:
    print('The capital of {} is {}'.format(country, D1[country]))

print('*******************************************************')
#6. Merge sentences above together with one cycle
print('#6. Merge sentences above together with one cycle')
for country  in D:
    print('Domain for {} is {}'.format(country, D[country]))
    print('The capital of {} is {}'.format(country, D1[country]))
    print('-----------------------------------------------------')

#7. Add to each value of first dict another two domains: COM and GOV
print('#7. Add to each value of first dict another two domains: COM and GOV')
DOM={'com':'comercial', 'gov':'goverment'}
DOM['gov']=D
DOM['com']=D
print('DOM',DOM)
