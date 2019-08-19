


def list_entry():
    user_inut = input('Enter Some Noobs You Know Separated By Commas Please:-')
    user_ho = [person.strip(',').lower() for person in user_inut]
    return user_inut
def answer():
    
    idk = list_entry()
    noob = input('Enter A Person:-')
    if noob in idk:
        print('You Know Stupid')

answer()