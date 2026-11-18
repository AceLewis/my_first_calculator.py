# test_times_12.py
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


class TestTimes12(unittest.TestCase):

    def test_12_times_0(self):
        self.assertEqual(run_calculator('12', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_1(self):
        self.assertEqual(run_calculator('12', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*1 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_2(self):
        self.assertEqual(run_calculator('12', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*2 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_3(self):
        self.assertEqual(run_calculator('12', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*3 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_4(self):
        self.assertEqual(run_calculator('12', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*4 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_5(self):
        self.assertEqual(run_calculator('12', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*5 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_6(self):
        self.assertEqual(run_calculator('12', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*6 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_7(self):
        self.assertEqual(run_calculator('12', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*7 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_8(self):
        self.assertEqual(run_calculator('12', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*8 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_9(self):
        self.assertEqual(run_calculator('12', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*9 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_10(self):
        self.assertEqual(run_calculator('12', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*10 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_11(self):
        self.assertEqual(run_calculator('12', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*11 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_12(self):
        self.assertEqual(run_calculator('12', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*12 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_13(self):
        self.assertEqual(run_calculator('12', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*13 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_14(self):
        self.assertEqual(run_calculator('12', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*14 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_15(self):
        self.assertEqual(run_calculator('12', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*15 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_16(self):
        self.assertEqual(run_calculator('12', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*16 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_17(self):
        self.assertEqual(run_calculator('12', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*17 = 204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_18(self):
        self.assertEqual(run_calculator('12', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*18 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_19(self):
        self.assertEqual(run_calculator('12', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*19 = 228',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_20(self):
        self.assertEqual(run_calculator('12', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*20 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_21(self):
        self.assertEqual(run_calculator('12', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*21 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_22(self):
        self.assertEqual(run_calculator('12', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*22 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_23(self):
        self.assertEqual(run_calculator('12', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*23 = 276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_24(self):
        self.assertEqual(run_calculator('12', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*24 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_25(self):
        self.assertEqual(run_calculator('12', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*25 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_26(self):
        self.assertEqual(run_calculator('12', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*26 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_27(self):
        self.assertEqual(run_calculator('12', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*27 = 324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_28(self):
        self.assertEqual(run_calculator('12', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*28 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_29(self):
        self.assertEqual(run_calculator('12', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*29 = 348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_30(self):
        self.assertEqual(run_calculator('12', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*30 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_31(self):
        self.assertEqual(run_calculator('12', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*31 = 372',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_32(self):
        self.assertEqual(run_calculator('12', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*32 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_33(self):
        self.assertEqual(run_calculator('12', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*33 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_34(self):
        self.assertEqual(run_calculator('12', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*34 = 408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_35(self):
        self.assertEqual(run_calculator('12', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*35 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_36(self):
        self.assertEqual(run_calculator('12', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*36 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_37(self):
        self.assertEqual(run_calculator('12', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*37 = 444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_38(self):
        self.assertEqual(run_calculator('12', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*38 = 456',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_39(self):
        self.assertEqual(run_calculator('12', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*39 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_40(self):
        self.assertEqual(run_calculator('12', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*40 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_41(self):
        self.assertEqual(run_calculator('12', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*41 = 492',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_42(self):
        self.assertEqual(run_calculator('12', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*42 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_43(self):
        self.assertEqual(run_calculator('12', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*43 = 516',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_44(self):
        self.assertEqual(run_calculator('12', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*44 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_45(self):
        self.assertEqual(run_calculator('12', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*45 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_46(self):
        self.assertEqual(run_calculator('12', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*46 = 552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_47(self):
        self.assertEqual(run_calculator('12', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*47 = 564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_48(self):
        self.assertEqual(run_calculator('12', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*48 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_49(self):
        self.assertEqual(run_calculator('12', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*49 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_times_50(self):
        self.assertEqual(run_calculator('12', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12*50 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
