# test_times_50.py
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


class TestTimes50(unittest.TestCase):

    def test_50_times_0(self):
        self.assertEqual(run_calculator('50', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_1(self):
        self.assertEqual(run_calculator('50', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*1 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_2(self):
        self.assertEqual(run_calculator('50', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*2 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_3(self):
        self.assertEqual(run_calculator('50', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*3 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_4(self):
        self.assertEqual(run_calculator('50', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*4 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_5(self):
        self.assertEqual(run_calculator('50', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*5 = 250',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_6(self):
        self.assertEqual(run_calculator('50', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*6 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_7(self):
        self.assertEqual(run_calculator('50', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*7 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_8(self):
        self.assertEqual(run_calculator('50', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*8 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_9(self):
        self.assertEqual(run_calculator('50', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*9 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_10(self):
        self.assertEqual(run_calculator('50', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*10 = 500',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_11(self):
        self.assertEqual(run_calculator('50', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*11 = 550',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_12(self):
        self.assertEqual(run_calculator('50', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*12 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_13(self):
        self.assertEqual(run_calculator('50', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*13 = 650',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_14(self):
        self.assertEqual(run_calculator('50', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*14 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_15(self):
        self.assertEqual(run_calculator('50', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*15 = 750',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_16(self):
        self.assertEqual(run_calculator('50', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*16 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_17(self):
        self.assertEqual(run_calculator('50', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*17 = 850',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_18(self):
        self.assertEqual(run_calculator('50', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*18 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_19(self):
        self.assertEqual(run_calculator('50', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*19 = 950',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_20(self):
        self.assertEqual(run_calculator('50', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*20 = 1000',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_21(self):
        self.assertEqual(run_calculator('50', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*21 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_22(self):
        self.assertEqual(run_calculator('50', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*22 = 1100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_23(self):
        self.assertEqual(run_calculator('50', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*23 = 1150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_24(self):
        self.assertEqual(run_calculator('50', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*24 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_25(self):
        self.assertEqual(run_calculator('50', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*25 = 1250',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_26(self):
        self.assertEqual(run_calculator('50', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*26 = 1300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_27(self):
        self.assertEqual(run_calculator('50', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*27 = 1350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_28(self):
        self.assertEqual(run_calculator('50', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*28 = 1400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_29(self):
        self.assertEqual(run_calculator('50', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*29 = 1450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_30(self):
        self.assertEqual(run_calculator('50', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*30 = 1500',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_31(self):
        self.assertEqual(run_calculator('50', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*31 = 1550',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_32(self):
        self.assertEqual(run_calculator('50', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*32 = 1600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_33(self):
        self.assertEqual(run_calculator('50', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*33 = 1650',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_34(self):
        self.assertEqual(run_calculator('50', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*34 = 1700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_35(self):
        self.assertEqual(run_calculator('50', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*35 = 1750',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_36(self):
        self.assertEqual(run_calculator('50', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*36 = 1800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_37(self):
        self.assertEqual(run_calculator('50', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*37 = 1850',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_38(self):
        self.assertEqual(run_calculator('50', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*38 = 1900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_39(self):
        self.assertEqual(run_calculator('50', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*39 = 1950',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_40(self):
        self.assertEqual(run_calculator('50', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*40 = 2000',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_41(self):
        self.assertEqual(run_calculator('50', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*41 = 2050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_42(self):
        self.assertEqual(run_calculator('50', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*42 = 2100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_43(self):
        self.assertEqual(run_calculator('50', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*43 = 2150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_44(self):
        self.assertEqual(run_calculator('50', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*44 = 2200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_45(self):
        self.assertEqual(run_calculator('50', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*45 = 2250',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_46(self):
        self.assertEqual(run_calculator('50', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*46 = 2300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_47(self):
        self.assertEqual(run_calculator('50', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*47 = 2350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_48(self):
        self.assertEqual(run_calculator('50', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*48 = 2400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_49(self):
        self.assertEqual(run_calculator('50', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*49 = 2450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_times_50(self):
        self.assertEqual(run_calculator('50', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50*50 = 2500',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
