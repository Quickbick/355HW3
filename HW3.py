# CptS 355 - Fall 2022 - Assignment 3 - Python

# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Name: Nathanael Ostheller

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

from functools import reduce

## problem 1 - create_lang_dict (courses)  - 8%
def create_lang_dict (courses):
     languages = {}
     for course in courses:
          for lang in courses[course]:
               if lang not in languages.keys():
                    languages[lang] = []
               languages[lang].append(course)
     return languages

## problem 2 - find_courses(lang_dict,language)– 10%
def isLang(item, language):
     if language in item:
          return True
     else:
          return False

def find_courses(lang_dict,language):
     results = dict(filter(lambda item: isLang(item[1], language), lang_dict.items()))
     return results.keys()

## problem 3 - get_by_level(lang_dict,level)– 15%
def isLevel(item, level):
     if str(item)[4] == str(level):
          return True
     else:
          return False

def get_by_level(lang_dict,level):
     results = dict(filter(lambda item: isLevel(item[0], level), lang_dict.items()))
     return reduce(lambda x, y: x + y, results.values())       

## problem 4 - all_prerequisites(course_dict,course)– 15%


## problem 5 - roll(lst,n,count)– 10% 


## problem 6 - split_at_parenthesis(str_input)– 14% 


## problem 7 - state_machine – 18% 