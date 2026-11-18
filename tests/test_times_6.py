# test_times_6.py
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


class TestTimes6(unittest.TestCase):

    def test_6_times_0(self):
        self.assertEqual(run_calculator('6', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_1(self):
        self.assertEqual(run_calculator('6', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*1 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_2(self):
        self.assertEqual(run_calculator('6', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*2 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_3(self):
        self.assertEqual(run_calculator('6', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*3 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_4(self):
        self.assertEqual(run_calculator('6', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*4 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_5(self):
        self.assertEqual(run_calculator('6', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*5 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_6(self):
        self.assertEqual(run_calculator('6', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*6 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_7(self):
        self.assertEqual(run_calculator('6', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*7 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_8(self):
        self.assertEqual(run_calculator('6', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*8 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_9(self):
        self.assertEqual(run_calculator('6', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*9 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_10(self):
        self.assertEqual(run_calculator('6', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*10 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_11(self):
        self.assertEqual(run_calculator('6', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*11 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_12(self):
        self.assertEqual(run_calculator('6', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*12 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_13(self):
        self.assertEqual(run_calculator('6', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*13 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_14(self):
        self.assertEqual(run_calculator('6', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*14 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_15(self):
        self.assertEqual(run_calculator('6', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*15 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_16(self):
        self.assertEqual(run_calculator('6', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*16 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_17(self):
        self.assertEqual(run_calculator('6', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*17 = 102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_18(self):
        self.assertEqual(run_calculator('6', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*18 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_19(self):
        self.assertEqual(run_calculator('6', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*19 = 114',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_20(self):
        self.assertEqual(run_calculator('6', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*20 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_21(self):
        self.assertEqual(run_calculator('6', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*21 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_22(self):
        self.assertEqual(run_calculator('6', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*22 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_23(self):
        self.assertEqual(run_calculator('6', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*23 = 138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_24(self):
        self.assertEqual(run_calculator('6', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*24 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_25(self):
        self.assertEqual(run_calculator('6', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*25 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_26(self):
        self.assertEqual(run_calculator('6', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*26 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_27(self):
        self.assertEqual(run_calculator('6', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*27 = 162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_28(self):
        self.assertEqual(run_calculator('6', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*28 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_29(self):
        self.assertEqual(run_calculator('6', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*29 = 174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_30(self):
        self.assertEqual(run_calculator('6', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*30 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_31(self):
        self.assertEqual(run_calculator('6', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*31 = 186',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_32(self):
        self.assertEqual(run_calculator('6', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*32 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_33(self):
        self.assertEqual(run_calculator('6', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*33 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_34(self):
        self.assertEqual(run_calculator('6', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*34 = 204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_35(self):
        self.assertEqual(run_calculator('6', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*35 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_36(self):
        self.assertEqual(run_calculator('6', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*36 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_37(self):
        self.assertEqual(run_calculator('6', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*37 = 222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_38(self):
        self.assertEqual(run_calculator('6', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*38 = 228',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_39(self):
        self.assertEqual(run_calculator('6', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*39 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_40(self):
        self.assertEqual(run_calculator('6', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*40 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_41(self):
        self.assertEqual(run_calculator('6', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*41 = 246',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_42(self):
        self.assertEqual(run_calculator('6', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*42 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_43(self):
        self.assertEqual(run_calculator('6', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*43 = 258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_44(self):
        self.assertEqual(run_calculator('6', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*44 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_45(self):
        self.assertEqual(run_calculator('6', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*45 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_46(self):
        self.assertEqual(run_calculator('6', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*46 = 276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_47(self):
        self.assertEqual(run_calculator('6', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*47 = 282',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_48(self):
        self.assertEqual(run_calculator('6', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*48 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_49(self):
        self.assertEqual(run_calculator('6', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*49 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_6_times_50(self):
        self.assertEqual(run_calculator('6', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '6*50 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
