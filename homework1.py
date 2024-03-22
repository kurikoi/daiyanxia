#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_greetings(language, times):
    """
    Print greetings based on the specified language and number of times.

    :param language: Language for greetings (English, Chinese, Russian)
    :param times: Number of times to print the greeting
    """
    while True:
        if language.lower() in ['english', 'chinese', 'russian']:
            break
        language = input('Invalid input! Please choose language from English, Chinese, or Russian: ')

    for _ in range(times):
        if language.lower() == 'english':
            print('hello')
        elif language.lower() == 'chinese':
            print('ni hao')
        elif language.lower() == 'russian':
            print('privet')


if __name__ == '__main__':
    language = input('Please choose language from English, Chinese, or Russian: ')
    times = int(input('Please type the number of times to repeat the greeting: '))
    print_greetings(language, times)


# In[ ]:




