"""
Referencing this answer on StackOverflow: 
    https://stackoverflow.com/questions/45157521/insert-an-item-into-a-specific-location-in-a-dict-in-a-single-statement/45157612#45157612

    Original question: How to insert a dict object at the beginning of a dict in python3.6 where dicts are now ordered in the 
    fewest lines possible.

    Solution: I didn't know anything about this, since I'm not using Python 3.6, but I installed it and ran a couple test 
    functions and created a dict comprehension that could do it in 1 line. Then, I guess as a challenge, he asked me how I 
    would insert it into position 1 and I provided another one line solution. Then I created a one line function that could 
    do it for any dict. Because I'm that cool...yea...
"""


# Our provided variables
original_dict = {'a':1,'b':2}

# His solution which took 3 lines
temp_dict = {}
temp_dict.update({'c':3})
new_dict = {**temp_dict,**original_dict}
print(new_dict, end='\n')

# My original solution to insert it at the beginning
new_dict = {k: v for k, v in ([('c', 3)] + list(original_dict.items()))}
print(new_dict, end='\n')

# My solution to insert it into the first position
new_dict = {k: v for k, v in (list(original_dict.items())[:1] + [('c', 3)] + list(original_dict.items())[1:])}
print(new_dict, end='\n')

# Finally as a function to insert the dict into any position in any dict
insert = lambda _dict, obj, pos: {k: v for k, v in (list(_dict.items())[:pos] + list(obj.items()) + list(_dict.items())[pos:])}

new_dict = insert(original_dict, {'c': 3}, 1)
print(new_dict, end='\n')

