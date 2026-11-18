# test_times_4.py
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


class TestTimes4(unittest.TestCase):

    def test_4_times_0(self):
        self.assertEqual(run_calculator('4', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_1(self):
        self.assertEqual(run_calculator('4', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*1 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_2(self):
        self.assertEqual(run_calculator('4', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*2 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_3(self):
        self.assertEqual(run_calculator('4', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*3 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_4(self):
        self.assertEqual(run_calculator('4', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*4 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_5(self):
        self.assertEqual(run_calculator('4', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*5 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_6(self):
        self.assertEqual(run_calculator('4', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*6 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_7(self):
        self.assertEqual(run_calculator('4', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*7 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_8(self):
        self.assertEqual(run_calculator('4', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*8 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_9(self):
        self.assertEqual(run_calculator('4', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*9 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_10(self):
        self.assertEqual(run_calculator('4', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*10 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_11(self):
        self.assertEqual(run_calculator('4', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*11 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_12(self):
        self.assertEqual(run_calculator('4', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*12 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_13(self):
        self.assertEqual(run_calculator('4', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*13 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_14(self):
        self.assertEqual(run_calculator('4', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*14 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_15(self):
        self.assertEqual(run_calculator('4', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*15 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_16(self):
        self.assertEqual(run_calculator('4', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*16 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_17(self):
        self.assertEqual(run_calculator('4', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*17 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_18(self):
        self.assertEqual(run_calculator('4', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*18 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_19(self):
        self.assertEqual(run_calculator('4', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*19 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_20(self):
        self.assertEqual(run_calculator('4', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*20 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_21(self):
        self.assertEqual(run_calculator('4', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*21 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_22(self):
        self.assertEqual(run_calculator('4', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*22 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_23(self):
        self.assertEqual(run_calculator('4', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*23 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_24(self):
        self.assertEqual(run_calculator('4', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*24 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_25(self):
        self.assertEqual(run_calculator('4', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*25 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_26(self):
        self.assertEqual(run_calculator('4', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*26 = 104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_27(self):
        self.assertEqual(run_calculator('4', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*27 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_28(self):
        self.assertEqual(run_calculator('4', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*28 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_29(self):
        self.assertEqual(run_calculator('4', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*29 = 116',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_30(self):
        self.assertEqual(run_calculator('4', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*30 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_31(self):
        self.assertEqual(run_calculator('4', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*31 = 124',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_32(self):
        self.assertEqual(run_calculator('4', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*32 = 128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_33(self):
        self.assertEqual(run_calculator('4', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*33 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_34(self):
        self.assertEqual(run_calculator('4', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*34 = 136',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_35(self):
        self.assertEqual(run_calculator('4', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*35 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_36(self):
        self.assertEqual(run_calculator('4', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*36 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_37(self):
        self.assertEqual(run_calculator('4', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*37 = 148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_38(self):
        self.assertEqual(run_calculator('4', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*38 = 152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_39(self):
        self.assertEqual(run_calculator('4', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*39 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_40(self):
        self.assertEqual(run_calculator('4', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*40 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_41(self):
        self.assertEqual(run_calculator('4', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*41 = 164',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_42(self):
        self.assertEqual(run_calculator('4', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*42 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_43(self):
        self.assertEqual(run_calculator('4', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*43 = 172',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_44(self):
        self.assertEqual(run_calculator('4', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*44 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_45(self):
        self.assertEqual(run_calculator('4', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*45 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_46(self):
        self.assertEqual(run_calculator('4', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*46 = 184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_47(self):
        self.assertEqual(run_calculator('4', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*47 = 188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_48(self):
        self.assertEqual(run_calculator('4', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*48 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_49(self):
        self.assertEqual(run_calculator('4', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*49 = 196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_times_50(self):
        self.assertEqual(run_calculator('4', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4*50 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
