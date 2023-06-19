# data:14-June-2023, HR- Sakshi: 7014129682

# what tools you have used in networking
# how to optimize database queries
# mixins
# have you used cython
# caching
# Celery



# data:16-June-2023, HR- Sakshi: 7014129682 , Interview: Shubham

x = '{[]}{}' # correct
x = '{[}{}'  # incorrect
x = '{[}}'   # incorrect
x = '}}'   # incorrect


def paraCheck(x):
    if len(x)%2!=0:
        return False
    stak = []
    for ch in x:
        if ch=='(' or ch=='{' or ch=='[':
            stak.append(ch)

        if ch==')':
            if len(stak)>0:
                last_ele = stak.pop()
                if last_ele != '(':
                    return False
            else:
                return False

        if ch==']':
            if  len(stak)>0:
                last_ele = stak.pop()
                if last_ele != '[':
                    return False
            else:
                return False

        if ch=='}':
            if len(stak)>0:
                last_ele = stak.pop()
                if last_ele != '{':
                    return False
            else:
                return False

    if len(stak)==0:
        return True
    else:
        return False

print(paraCheck(x))



# how many aws services have you used
# how to stop a request if it is coming say 1000 times
# have you used url shortner services?
'''
# how to get data from employee and student table from django Candidate Model
class Candidate():

    name
    age


employee: name, age
student: name, age



Candidate.objects.using('employee').all()
Candidate.objects.using('student').all()


'''