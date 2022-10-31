#------------------------------------------------------
#-- INCLUDE YOUR OWN TESTS IN THIS FILE
#------------------------------------------------------
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.prog_languages = {
            "CptS121" : ["C", "E-"],
            "CptS122" : ["C++", "E++"],
            "CptS131" : ["Java"],
            "CptS132" : ["Java"],
            "CptS223" : ["C++"],
            "CptS233" : ["Java"],
            "CptS321" : ["C#"],
            "CptS322" : ["Python"],
            "CptS355" : ["Haskell", "Python", "PostScript", "Java"],
            "CptS451" : ["Python", "C#", "SQL"],     
            "CptS360" : ["C", "Suffering"],
            "CptS370" : ["Java"],
            "CptS315" : ["Python"],
            "CptS411" : ["C", "C++"],
            "CptS475" : ["Python", "R"],
            "CptS423" : []
        }
    def sort_values(self,d):
        return dict(map(lambda t: (t[0],list(sorted(t[1]))), d.items()))
    
    #--- Problem 1----------------------------------
    def test_create_lang_dict(self):
        output = {'C': ['CptS121', 'CptS360', 'CptS411'],
                 'E-': ['CptS121'],
                'C++': ['CptS122', 'CptS223', 'CptS411'],
                'E++': ['CptS122'], 
               'Java': ['CptS131', 'CptS132', 'CptS233', 'CptS355', 'CptS370'], 
                 'C#': ['CptS321', 'CptS451'], 
             'Python': ['CptS315', 'CptS322', 'CptS355', 'CptS451', 'CptS475'],
            'Haskell': ['CptS355'], 
                'SQL': ['CptS451'], 
         'PostScript': ['CptS355'],
          'Suffering': ['CptS360'],                 
                  'R': ['CptS475'],}
        self.assertDictEqual(self.sort_values(create_lang_dict(self.prog_languages)),self.sort_values(output))
    
    #--- Problem 2----------------------------------
    def test_find_courses(self):
        output = sorted(['CptS360'])
        self.assertListEqual(sorted(find_courses(self.prog_languages,'Suffering')),output)


    #--- Problem 3 ----------------------------------
    def test_get_by_level(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test .
        # You can re-use the data dictionary you created for problem-1.

    #--- Problem 4----------------------------------
    def test_all_prerequisites(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test 
            
    #--- Problem 5 ----------------------------------
    def test_roll(self):
        pass
        # Provide your own test here. 

    #--- Problem 6----------------------------------
    def test_split_at_parenthesis(self):
        pass
        # Provide your own test here.  

    #--- Problem 7----------------------------------
    def test_state_machine(self):
        pass
        # Provide your own test here. Initialize the iterator with your own input.
    
if __name__ == '__main__':
    unittest.main()

