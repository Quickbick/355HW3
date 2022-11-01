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
        self.prerequisites = {
            "CptS121" : "Ability to Google",
            "CptS122" : "CptS121",
            "CptS132" : "CptS131",
            "CptS223" : "CptS122",
            "CptS233" : "CptS132",
            "CptS260" : "CptS121",
            "CptS317" : "CptS223",
            "CptS321" : "CptS223",
            "CptS322" : "CptS223",
            "CptS355" : "CptS223",
            "CptS360" : "CptS317",
            "CptS370" : "CptS233",
            "CptS315" : "CptS233",
            "CptS460" : "CptS360",
            "CptS451" : "CptS223",
            "CptS475" : "CptS122",
            "CptS423" : "CptS322"
        }
        self.rollinput = list("SEND ELPH")
        self.parInput = "I(hate(THIS))"
        self.machine1 = {'S1':{'0':('S2','0'), '1':('S2','1')},
                         'S2':{'0':('S1','-'), '1':('S1','+')}}
        self.input1 = '00001'
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
        output = sorted(['C', 'C++', 'E-', 'E++', 'Java', 'Java'])
        self.assertListEqual(sorted(get_by_level(self.prog_languages,1)),output)

    #--- Problem 4----------------------------------
    def test_all_prerequisites(self):
        output = sorted(['Ability to Google', 'CptS121', 'CptS122', 'CptS223', 'CptS317'])
        self.assertListEqual(all_prerequisites(self.prerequisites,'CptS360'),output) 
            
    #--- Problem 5 ----------------------------------
    def test_roll(self):
        output = list("SEND HELP")
        self.assertListEqual( roll(self.rollinput,4,1),output )

    #--- Problem 6----------------------------------
    def test_split_at_parenthesis(self):
        output = ['I', ['h', 'a', 't', 'e', ['T', 'H', 'I', 'S']]]
        self.assertListEqual(split_at_parenthesis(self.parInput),output ) 

    #--- Problem 7----------------------------------
    def test_state_machine(self):
        out = []
        program = state_machine(self.machine1,iter(self.input1), ('S1',None))
        self.assertEqual(program.__next__(), ('S1', None))  # skip over first output
        for t in program:  
            out.append(t)
        state_output = [('S2', '0'), ('S1', '-'), ('S2', '0'), ('S1', '-'), ('S2', '1')]
        str_output = "0-0-1"
        self.assertListEqual(out,state_output)
        self.assertEqual(''.join(list(map(lambda t: t[1],out))),str_output)
    
if __name__ == '__main__':
    unittest.main()

