print('Hello,Welcome to Quiz:')
ans=input('You Want to play (yes/no):')
score=0
total_q=4
if ans.lower() == 'yes':
    ans=input('1.What is Best Programming language:Option=[java],[python] ')
    if ans=='python':
        score +=1
        print('correct Answer')
    else:
        print('incorrect Answer')

    ans = input('2.Who is india Prime Minister:Option=[Modi],[rahul] ')
    if ans.lower()== 'narendra Modi' or ans=='modi':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')

    ans = input('3.What is 3+6+3 ? :Option=[12],[11] ')
    if ans == '12':
        score += 1
        print(' correct Answer')
    else:
        print('incorrect Answer')

    ans = input('4.which Year corona virus war introduce:Option=[2020],[2019] ')
    if ans == '2020':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')

    print('Thank for playing this game , You got',score,"question correct")
    mark=(score/total_q) * 100
    print("mark",mark)

print("good bye")

