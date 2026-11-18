# test_times_18.py
# Every single case gets its own test, to be true to the story

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SOURCE = Path(__file__).parent.parent / 'my_first_calculator.py'
CODE = compile(SOURCE.read_text(), str(SOURCE), 'exec')


def run_calculator(num1, sign, num2):
    answers = iter([num1, sign, num2])
    out = io.StringIO()
    with mock.patch('builtins.input', lambda prompt='': next(answers)), redirect_stdout(out):
        exec(CODE, {'__name__': '__main__'})
    return out.getvalue().splitlines()


class TestTimes18(unittest.TestCase):

    def test_18_times_0(self):
        self.assertEqual(run_calculator('18', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_1(self):
        self.assertEqual(run_calculator('18', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*1 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_2(self):
        self.assertEqual(run_calculator('18', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*2 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_3(self):
        self.assertEqual(run_calculator('18', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*3 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_4(self):
        self.assertEqual(run_calculator('18', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*4 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_5(self):
        self.assertEqual(run_calculator('18', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*5 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_6(self):
        self.assertEqual(run_calculator('18', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*6 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_7(self):
        self.assertEqual(run_calculator('18', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*7 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_8(self):
        self.assertEqual(run_calculator('18', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*8 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_9(self):
        self.assertEqual(run_calculator('18', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*9 = 162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_10(self):
        self.assertEqual(run_calculator('18', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*10 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_11(self):
        self.assertEqual(run_calculator('18', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*11 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_12(self):
        self.assertEqual(run_calculator('18', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*12 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_13(self):
        self.assertEqual(run_calculator('18', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*13 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_14(self):
        self.assertEqual(run_calculator('18', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*14 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_15(self):
        self.assertEqual(run_calculator('18', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*15 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_16(self):
        self.assertEqual(run_calculator('18', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*16 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_17(self):
        self.assertEqual(run_calculator('18', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*17 = 306',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_18(self):
        self.assertEqual(run_calculator('18', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*18 = 324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_19(self):
        self.assertEqual(run_calculator('18', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*19 = 342',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_20(self):
        self.assertEqual(run_calculator('18', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*20 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_21(self):
        self.assertEqual(run_calculator('18', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*21 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_22(self):
        self.assertEqual(run_calculator('18', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*22 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_23(self):
        self.assertEqual(run_calculator('18', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*23 = 414',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_24(self):
        self.assertEqual(run_calculator('18', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*24 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_25(self):
        self.assertEqual(run_calculator('18', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*25 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_26(self):
        self.assertEqual(run_calculator('18', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*26 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_27(self):
        self.assertEqual(run_calculator('18', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*27 = 486',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_28(self):
        self.assertEqual(run_calculator('18', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*28 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_29(self):
        self.assertEqual(run_calculator('18', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*29 = 522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_30(self):
        self.assertEqual(run_calculator('18', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*30 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_31(self):
        self.assertEqual(run_calculator('18', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*31 = 558',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_32(self):
        self.assertEqual(run_calculator('18', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*32 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_33(self):
        self.assertEqual(run_calculator('18', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*33 = 594',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_34(self):
        self.assertEqual(run_calculator('18', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*34 = 612',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_35(self):
        self.assertEqual(run_calculator('18', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*35 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_36(self):
        self.assertEqual(run_calculator('18', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*36 = 648',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_37(self):
        self.assertEqual(run_calculator('18', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*37 = 666',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_38(self):
        self.assertEqual(run_calculator('18', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*38 = 684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_39(self):
        self.assertEqual(run_calculator('18', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*39 = 702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_40(self):
        self.assertEqual(run_calculator('18', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*40 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_41(self):
        self.assertEqual(run_calculator('18', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*41 = 738',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_42(self):
        self.assertEqual(run_calculator('18', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*42 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_43(self):
        self.assertEqual(run_calculator('18', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*43 = 774',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_44(self):
        self.assertEqual(run_calculator('18', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*44 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_45(self):
        self.assertEqual(run_calculator('18', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*45 = 810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_46(self):
        self.assertEqual(run_calculator('18', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*46 = 828',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_47(self):
        self.assertEqual(run_calculator('18', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*47 = 846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_48(self):
        self.assertEqual(run_calculator('18', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*48 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_49(self):
        self.assertEqual(run_calculator('18', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*49 = 882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_times_50(self):
        self.assertEqual(run_calculator('18', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18*50 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
