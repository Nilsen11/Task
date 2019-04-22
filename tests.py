from script import email_anonim, phone_anonim, skype_user_anomin
import unittest


class TestStringMethods(unittest.TestCase):

    def test_skype(self):
        self.assertEqual(skype_user_anomin("skype:loremipsum", '#'), 'skype:#')
        self.assertEqual(skype_user_anomin("Lorem ipsum <a href=”skype:loremipsum?call”>call</a>, dolor sit", 'X'),
                         "Lorem ipsum <a href=”skype:X?call”>call</a>, dolor sit")
        self.assertEqual(skype_user_anomin("Lorem ipsum", '#'), 'Lorem ipsum')
        self.assertEqual(
            skype_user_anomin("sit <a href=”skype:IPSUMLOREM?chat”>chat</a> amet. Lorem skype:ipsum sit", '*'),
            'sit <a href=”skype:*?chat”>chat</a> amet. Lorem skype:* sit')

        self.assertEqual(skype_user_anomin(' skype: ', '@'), ' skype: ')
        # etc...

    def test_email(self):
        self.assertEqual(email_anonim("john.doe@gmail.com", '#'), 'j######e@gmail.com')
        self.assertEqual(email_anonim("Lorem abc-abc@abc.edu.co.uk am", "#"), 'Lorem a#####c@abc.edu.co.uk am')
        self.assertEqual(email_anonim("Lorem ipsum", '#'), 'Lorem ipsum')
        self.assertEqual(email_anonim("Lorem ipsum --@--.--", "#"), "Lorem ipsum --@--.--")
        self.assertEqual(email_anonim("Lorem some@data ipsum", '#'), "Lorem some@data ipsum")

        # etc...

    def test_phone(self):
        self.assertEqual(phone_anonim("+48 845 546 546", 'X', 3), '+48 845 546 XXX')
        self.assertEqual(phone_anonim("Lorem +48 845 546 546 ipsum", 'X', 0),
                         'Lorem +48 845 546 546 ipsum')
        self.assertEqual(phone_anonim("Lorem ipsum", '#', 5), "Lorem ipsum")
        self.assertEqual(phone_anonim("Lorem +48 845 546 546, +48 777 777 777 sit 898 845 566 amet", "*", 4),
                         "Lorem +48 845 54* ***, +48 777 77* *** sit 898 845 566 amet")


if __name__ == '__main__':
    unittest.main()
