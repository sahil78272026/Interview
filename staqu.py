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


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        stack = []
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)

            if ch==')':
                if len(stack)>0:
                    last_ele = stack.pop()
                    if last_ele != '(':
                        return False
                else:
                    return False

            if ch==']':
                if  len(stack)>0:
                    last_ele = stack.pop()
                    if last_ele != '[':
                        return False
                else:
                    return False

            if ch=='}':
                if len(stack)>0:
                    last_ele = stack.pop()
                    if last_ele != '{':
                        return False
                else:
                    return False

        if len(stack)!=0:
            return False
        else:
            return True



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