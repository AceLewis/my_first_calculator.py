# test_times_5.py
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


class TestTimes5(unittest.TestCase):

    def test_5_times_0(self):
        self.assertEqual(run_calculator('5', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_1(self):
        self.assertEqual(run_calculator('5', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*1 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_2(self):
        self.assertEqual(run_calculator('5', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*2 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_3(self):
        self.assertEqual(run_calculator('5', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*3 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_4(self):
        self.assertEqual(run_calculator('5', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*4 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_5(self):
        self.assertEqual(run_calculator('5', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*5 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_6(self):
        self.assertEqual(run_calculator('5', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*6 = 30',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_7(self):
        self.assertEqual(run_calculator('5', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*7 = 35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_8(self):
        self.assertEqual(run_calculator('5', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*8 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_9(self):
        self.assertEqual(run_calculator('5', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*9 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_10(self):
        self.assertEqual(run_calculator('5', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*10 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_11(self):
        self.assertEqual(run_calculator('5', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*11 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_12(self):
        self.assertEqual(run_calculator('5', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*12 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_13(self):
        self.assertEqual(run_calculator('5', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*13 = 65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_14(self):
        self.assertEqual(run_calculator('5', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*14 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_15(self):
        self.assertEqual(run_calculator('5', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*15 = 75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_16(self):
        self.assertEqual(run_calculator('5', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*16 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_17(self):
        self.assertEqual(run_calculator('5', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*17 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_18(self):
        self.assertEqual(run_calculator('5', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*18 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_19(self):
        self.assertEqual(run_calculator('5', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*19 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_20(self):
        self.assertEqual(run_calculator('5', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*20 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_21(self):
        self.assertEqual(run_calculator('5', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*21 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_22(self):
        self.assertEqual(run_calculator('5', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*22 = 110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_23(self):
        self.assertEqual(run_calculator('5', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*23 = 115',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_24(self):
        self.assertEqual(run_calculator('5', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*24 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_25(self):
        self.assertEqual(run_calculator('5', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*25 = 125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_26(self):
        self.assertEqual(run_calculator('5', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*26 = 130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_27(self):
        self.assertEqual(run_calculator('5', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*27 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_28(self):
        self.assertEqual(run_calculator('5', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*28 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_29(self):
        self.assertEqual(run_calculator('5', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*29 = 145',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_30(self):
        self.assertEqual(run_calculator('5', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*30 = 150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_31(self):
        self.assertEqual(run_calculator('5', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*31 = 155',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_32(self):
        self.assertEqual(run_calculator('5', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*32 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_33(self):
        self.assertEqual(run_calculator('5', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*33 = 165',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_34(self):
        self.assertEqual(run_calculator('5', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*34 = 170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_35(self):
        self.assertEqual(run_calculator('5', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*35 = 175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_36(self):
        self.assertEqual(run_calculator('5', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*36 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_37(self):
        self.assertEqual(run_calculator('5', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*37 = 185',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_38(self):
        self.assertEqual(run_calculator('5', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*38 = 190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_39(self):
        self.assertEqual(run_calculator('5', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*39 = 195',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_40(self):
        self.assertEqual(run_calculator('5', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*40 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_41(self):
        self.assertEqual(run_calculator('5', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*41 = 205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_42(self):
        self.assertEqual(run_calculator('5', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*42 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_43(self):
        self.assertEqual(run_calculator('5', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*43 = 215',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_44(self):
        self.assertEqual(run_calculator('5', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*44 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_45(self):
        self.assertEqual(run_calculator('5', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*45 = 225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_46(self):
        self.assertEqual(run_calculator('5', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*46 = 230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_47(self):
        self.assertEqual(run_calculator('5', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*47 = 235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_48(self):
        self.assertEqual(run_calculator('5', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*48 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_49(self):
        self.assertEqual(run_calculator('5', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*49 = 245',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_times_50(self):
        self.assertEqual(run_calculator('5', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5*50 = 250',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
