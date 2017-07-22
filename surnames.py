"""
This isn't very interesting, but it was some code I did so why not add it.
The question was "how to check if a surname starts with a character in a range
and make write them to separate files" or something like that. I provided a couple different solutions. Question here:
    https://stackoverflow.com/questions/45256588/python-creating-a-range-over-a-set-of-letters/45256679#45256679

I really just enjoyed doing this task because it was an opportunity to discover that you can use a context manager on two different files at once.
"""
import re

surnames = ['Jacobson', 'Johnson', 'Williams', 'Abrahams', 'Putin', 'Trump', 'Obama', 'Nixon']


def read_names():
    a_to_l_pattern = r'^[a-lA-L]{1}'
    with open('a_to_l_names.txt', 'w') as a_to_l, open('m_to_z.txt', 'w') as m_to_z:
        for surname in surnames:
            if re.search(a_to_l_pattern, surname):
                a_to_l.write(surname + '\n')
            else: 
                m_to_z.write(surname + '\n')


if __name__ == '__main__':
    read_names()
