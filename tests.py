from script import email_anonim, phone_anonim, skype_user_anomin
import unittest


class TestStringMethods(unittest.TestCase):

    def test_error(self):
        # Skype
        with self.assertRaises(ValueError): skype_user_anomin('skype:nilsen11', '@@')
        with self.assertRaises(ValueError): skype_user_anomin('skype:nilsen11', '')
        # Email
        with self.assertRaises(ValueError): email_anonim("john.doe@gmail.com", '##')
        with self.assertRaises(ValueError): email_anonim("john.doe@gmail.com", '')
        # Phone
        with self.assertRaises(ValueError): phone_anonim("+48 845 546 546", 'X', 10)
        with self.assertRaises(ValueError): phone_anonim("+48 845 546 546", 'X', -1)
        with self.assertRaises(ValueError): phone_anonim("+48 845 546 546", 'XX', 3)
        with self.assertRaises(ValueError): phone_anonim("+48 845 546 546", '', 0)

    def test_skype(self):
        self.assertEqual(skype_user_anomin("skype:loremipsum", '#'), 'skype:#')
        self.assertEqual(skype_user_anomin("Lorem ipsum <a href=”skype:loremipsum?call”>call</a>, dolor sit", 'X'),
                         "Lorem ipsum <a href=”skype:X?call”>call</a>, dolor sit")
        self.assertEqual(skype_user_anomin("Lorem ipsum", '#'), 'Lorem ipsum')
        self.assertEqual(
            skype_user_anomin("sit <a href=”skype:IPSUMLOREM?chat”>chat</a> amet. Lorem skype:ipsum sit", '*'),
            'sit <a href=”skype:*?chat”>chat</a> amet. Lorem skype:* sit')

        # My tests
        self.assertEqual(skype_user_anomin(' skype: ', '@'), ' skype: ')
        self.assertEqual(skype_user_anomin('Sskype:nilsen11', '@'), 'Sskype:nilsen11')
        self.assertEqual(skype_user_anomin('skype:@nilsen11', '@'), 'skype:@nilsen11')
        # only 'skype:' records can be searched
        self.assertEqual(skype_user_anomin('Skype:@nilsen11', '@'), 'Skype:@nilsen11')

    def test_email(self):
        self.assertEqual(email_anonim("john.doe@gmail.com", '#'), 'j######e@gmail.com')
        self.assertEqual(email_anonim("Lorem abc-abc@abc.edu.co.uk am", "#"), 'Lorem a#####c@abc.edu.co.uk am')
        self.assertEqual(email_anonim("Lorem ipsum", '#'), 'Lorem ipsum')
        self.assertEqual(email_anonim("Lorem ipsum --@--.--", "#"), "Lorem ipsum --@--.--")
        self.assertEqual(email_anonim("Lorem some@data ipsum", '#'), "Lorem some@data ipsum")

        # My tests
        self.assertEqual(email_anonim("john..doe@gmail.com abc-abc@abc.edu.co.uk", '#'),
                         'john..doe@gmail.com a#####c@abc.edu.co.uk')
        self.assertEqual(email_anonim("john.d.oe@gmail.com", '#'), 'j#######e@gmail.com')
        self.assertEqual(email_anonim("john.d.oe@gmail.ua.com", '#'), 'j#######e@gmail.ua.com')
        self.assertEqual(email_anonim("jh@gmail.com", '#'), 'j#@gmail.com')
        self.assertEqual(email_anonim("j+h.ss@gmail.com", '#'), 'j####s@gmail.com')

    def test_phone(self):
        self.assertEqual(phone_anonim(" +48 845 546 546", 'X', 4), ' +48 845 54X XXX')
        self.assertEqual(phone_anonim("Lorem +48 845 546 546 ipsum", 'X', 0),
                         'Lorem +48 845 546 546 ipsum')
        self.assertEqual(phone_anonim("Lorem ipsum", '#', 5), "Lorem ipsum")
        self.assertEqual(phone_anonim("Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet", "*", 4),
                         "Lorem +48 845 54* ***, +48 777 77* *** sit 898 845 566 amet")
        # My tests
        self.assertEqual(phone_anonim("+48 845 546 546, +8 777 777 777 +380 777 777 777", '*', 9),
                         "+48 *** *** ***, +8 *** *** *** +380 *** *** ***")
        self.assertEqual(phone_anonim("+48 845 546546", '*', 1), "+48 845 546546")


if __name__ == '__main__':
    unittest.main()
