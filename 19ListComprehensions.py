

ppl_known = ['Rolf',' Jeff' , 'anna' , 'GREG']

test = [person.strip(',').lower() for person in ppl_known]
print(test)