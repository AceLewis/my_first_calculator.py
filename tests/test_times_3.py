# test_times_3.py
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


class TestTimes3(unittest.TestCase):

    def test_3_times_0(self):
        self.assertEqual(run_calculator('3', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_1(self):
        self.assertEqual(run_calculator('3', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*1 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_2(self):
        self.assertEqual(run_calculator('3', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*2 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_3(self):
        self.assertEqual(run_calculator('3', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*3 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_4(self):
        self.assertEqual(run_calculator('3', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*4 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_5(self):
        self.assertEqual(run_calculator('3', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*5 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_6(self):
        self.assertEqual(run_calculator('3', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*6 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_7(self):
        self.assertEqual(run_calculator('3', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*7 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_8(self):
        self.assertEqual(run_calculator('3', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*8 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_9(self):
        self.assertEqual(run_calculator('3', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*9 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_10(self):
        self.assertEqual(run_calculator('3', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*10 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_11(self):
        self.assertEqual(run_calculator('3', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*11 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_12(self):
        self.assertEqual(run_calculator('3', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*12 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_13(self):
        self.assertEqual(run_calculator('3', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*13 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_14(self):
        self.assertEqual(run_calculator('3', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*14 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_15(self):
        self.assertEqual(run_calculator('3', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*15 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_16(self):
        self.assertEqual(run_calculator('3', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*16 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_17(self):
        self.assertEqual(run_calculator('3', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*17 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_18(self):
        self.assertEqual(run_calculator('3', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*18 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_19(self):
        self.assertEqual(run_calculator('3', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*19 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_20(self):
        self.assertEqual(run_calculator('3', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*20 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_21(self):
        self.assertEqual(run_calculator('3', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*21 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_22(self):
        self.assertEqual(run_calculator('3', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*22 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_23(self):
        self.assertEqual(run_calculator('3', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*23 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_24(self):
        self.assertEqual(run_calculator('3', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*24 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_25(self):
        self.assertEqual(run_calculator('3', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*25 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_26(self):
        self.assertEqual(run_calculator('3', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*26 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_27(self):
        self.assertEqual(run_calculator('3', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*27 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_28(self):
        self.assertEqual(run_calculator('3', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*28 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_29(self):
        self.assertEqual(run_calculator('3', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*29 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_30(self):
        self.assertEqual(run_calculator('3', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*30 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_31(self):
        self.assertEqual(run_calculator('3', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*31 = 93',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_32(self):
        self.assertEqual(run_calculator('3', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*32 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_33(self):
        self.assertEqual(run_calculator('3', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*33 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_34(self):
        self.assertEqual(run_calculator('3', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*34 = 102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_35(self):
        self.assertEqual(run_calculator('3', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*35 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_36(self):
        self.assertEqual(run_calculator('3', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*36 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_37(self):
        self.assertEqual(run_calculator('3', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*37 = 111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_38(self):
        self.assertEqual(run_calculator('3', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*38 = 114',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_39(self):
        self.assertEqual(run_calculator('3', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*39 = 117',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_40(self):
        self.assertEqual(run_calculator('3', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*40 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_41(self):
        self.assertEqual(run_calculator('3', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*41 = 123',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_42(self):
        self.assertEqual(run_calculator('3', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*42 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_43(self):
        self.assertEqual(run_calculator('3', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*43 = 129',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_44(self):
        self.assertEqual(run_calculator('3', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*44 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_45(self):
        self.assertEqual(run_calculator('3', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*45 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_46(self):
        self.assertEqual(run_calculator('3', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*46 = 138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_47(self):
        self.assertEqual(run_calculator('3', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*47 = 141',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_48(self):
        self.assertEqual(run_calculator('3', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*48 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_49(self):
        self.assertEqual(run_calculator('3', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*49 = 147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_3_times_50(self):
        self.assertEqual(run_calculator('3', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '3*50 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
