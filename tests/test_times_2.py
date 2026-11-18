# test_times_2.py
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


class TestTimes2(unittest.TestCase):

    def test_2_times_0(self):
        self.assertEqual(run_calculator('2', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_1(self):
        self.assertEqual(run_calculator('2', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*1 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_2(self):
        self.assertEqual(run_calculator('2', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*2 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_3(self):
        self.assertEqual(run_calculator('2', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*3 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_4(self):
        self.assertEqual(run_calculator('2', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*4 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_5(self):
        self.assertEqual(run_calculator('2', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*5 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_6(self):
        self.assertEqual(run_calculator('2', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*6 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_7(self):
        self.assertEqual(run_calculator('2', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*7 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_8(self):
        self.assertEqual(run_calculator('2', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*8 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_9(self):
        self.assertEqual(run_calculator('2', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*9 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_10(self):
        self.assertEqual(run_calculator('2', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*10 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_11(self):
        self.assertEqual(run_calculator('2', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*11 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_12(self):
        self.assertEqual(run_calculator('2', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*12 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_13(self):
        self.assertEqual(run_calculator('2', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*13 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_14(self):
        self.assertEqual(run_calculator('2', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*14 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_15(self):
        self.assertEqual(run_calculator('2', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*15 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_16(self):
        self.assertEqual(run_calculator('2', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*16 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_17(self):
        self.assertEqual(run_calculator('2', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*17 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_18(self):
        self.assertEqual(run_calculator('2', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*18 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_19(self):
        self.assertEqual(run_calculator('2', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*19 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_20(self):
        self.assertEqual(run_calculator('2', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*20 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_21(self):
        self.assertEqual(run_calculator('2', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*21 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_22(self):
        self.assertEqual(run_calculator('2', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*22 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_23(self):
        self.assertEqual(run_calculator('2', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*23 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_24(self):
        self.assertEqual(run_calculator('2', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*24 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_25(self):
        self.assertEqual(run_calculator('2', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*25 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_26(self):
        self.assertEqual(run_calculator('2', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*26 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_27(self):
        self.assertEqual(run_calculator('2', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*27 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_28(self):
        self.assertEqual(run_calculator('2', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*28 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_29(self):
        self.assertEqual(run_calculator('2', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*29 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_30(self):
        self.assertEqual(run_calculator('2', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*30 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_31(self):
        self.assertEqual(run_calculator('2', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*31 = 62',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_32(self):
        self.assertEqual(run_calculator('2', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*32 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_33(self):
        self.assertEqual(run_calculator('2', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*33 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_34(self):
        self.assertEqual(run_calculator('2', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*34 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_35(self):
        self.assertEqual(run_calculator('2', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*35 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_36(self):
        self.assertEqual(run_calculator('2', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*36 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_37(self):
        self.assertEqual(run_calculator('2', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*37 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_38(self):
        self.assertEqual(run_calculator('2', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*38 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_39(self):
        self.assertEqual(run_calculator('2', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*39 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_40(self):
        self.assertEqual(run_calculator('2', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*40 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_41(self):
        self.assertEqual(run_calculator('2', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*41 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_42(self):
        self.assertEqual(run_calculator('2', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*42 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_43(self):
        self.assertEqual(run_calculator('2', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*43 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_44(self):
        self.assertEqual(run_calculator('2', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*44 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_45(self):
        self.assertEqual(run_calculator('2', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*45 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_46(self):
        self.assertEqual(run_calculator('2', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*46 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_47(self):
        self.assertEqual(run_calculator('2', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*47 = 94',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_48(self):
        self.assertEqual(run_calculator('2', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*48 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_49(self):
        self.assertEqual(run_calculator('2', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*49 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_2_times_50(self):
        self.assertEqual(run_calculator('2', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '2*50 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
