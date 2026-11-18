# test_times_7.py
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


class TestTimes7(unittest.TestCase):

    def test_7_times_0(self):
        self.assertEqual(run_calculator('7', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_1(self):
        self.assertEqual(run_calculator('7', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*1 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_2(self):
        self.assertEqual(run_calculator('7', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*2 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_3(self):
        self.assertEqual(run_calculator('7', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*3 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_4(self):
        self.assertEqual(run_calculator('7', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*4 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_5(self):
        self.assertEqual(run_calculator('7', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*5 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_6(self):
        self.assertEqual(run_calculator('7', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*6 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_7(self):
        self.assertEqual(run_calculator('7', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*7 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_8(self):
        self.assertEqual(run_calculator('7', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*8 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_9(self):
        self.assertEqual(run_calculator('7', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*9 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_10(self):
        self.assertEqual(run_calculator('7', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*10 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_11(self):
        self.assertEqual(run_calculator('7', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*11 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_12(self):
        self.assertEqual(run_calculator('7', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*12 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_13(self):
        self.assertEqual(run_calculator('7', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*13 = 91',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_14(self):
        self.assertEqual(run_calculator('7', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*14 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_15(self):
        self.assertEqual(run_calculator('7', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*15 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_16(self):
        self.assertEqual(run_calculator('7', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*16 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_17(self):
        self.assertEqual(run_calculator('7', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*17 = 119',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_18(self):
        self.assertEqual(run_calculator('7', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*18 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_19(self):
        self.assertEqual(run_calculator('7', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*19 = 133',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_20(self):
        self.assertEqual(run_calculator('7', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*20 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_21(self):
        self.assertEqual(run_calculator('7', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*21 = 147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_22(self):
        self.assertEqual(run_calculator('7', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*22 = 154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_23(self):
        self.assertEqual(run_calculator('7', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*23 = 161',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_24(self):
        self.assertEqual(run_calculator('7', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*24 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_25(self):
        self.assertEqual(run_calculator('7', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*25 = 175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_26(self):
        self.assertEqual(run_calculator('7', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*26 = 182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_27(self):
        self.assertEqual(run_calculator('7', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*27 = 189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_28(self):
        self.assertEqual(run_calculator('7', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*28 = 196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_29(self):
        self.assertEqual(run_calculator('7', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*29 = 203',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_30(self):
        self.assertEqual(run_calculator('7', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*30 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_31(self):
        self.assertEqual(run_calculator('7', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*31 = 217',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_32(self):
        self.assertEqual(run_calculator('7', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*32 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_33(self):
        self.assertEqual(run_calculator('7', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*33 = 231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_34(self):
        self.assertEqual(run_calculator('7', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*34 = 238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_35(self):
        self.assertEqual(run_calculator('7', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*35 = 245',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_36(self):
        self.assertEqual(run_calculator('7', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*36 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_37(self):
        self.assertEqual(run_calculator('7', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*37 = 259',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_38(self):
        self.assertEqual(run_calculator('7', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*38 = 266',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_39(self):
        self.assertEqual(run_calculator('7', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*39 = 273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_40(self):
        self.assertEqual(run_calculator('7', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*40 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_41(self):
        self.assertEqual(run_calculator('7', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*41 = 287',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_42(self):
        self.assertEqual(run_calculator('7', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*42 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_43(self):
        self.assertEqual(run_calculator('7', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*43 = 301',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_44(self):
        self.assertEqual(run_calculator('7', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*44 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_45(self):
        self.assertEqual(run_calculator('7', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*45 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_46(self):
        self.assertEqual(run_calculator('7', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*46 = 322',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_47(self):
        self.assertEqual(run_calculator('7', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*47 = 329',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_48(self):
        self.assertEqual(run_calculator('7', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*48 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_49(self):
        self.assertEqual(run_calculator('7', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*49 = 343',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_times_50(self):
        self.assertEqual(run_calculator('7', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7*50 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
