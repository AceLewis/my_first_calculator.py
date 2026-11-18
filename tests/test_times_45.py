# test_times_45.py
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


class TestTimes45(unittest.TestCase):

    def test_45_times_0(self):
        self.assertEqual(run_calculator('45', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_1(self):
        self.assertEqual(run_calculator('45', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*1 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_2(self):
        self.assertEqual(run_calculator('45', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*2 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_3(self):
        self.assertEqual(run_calculator('45', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*3 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_4(self):
        self.assertEqual(run_calculator('45', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*4 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_5(self):
        self.assertEqual(run_calculator('45', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*5 = 225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_6(self):
        self.assertEqual(run_calculator('45', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*6 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_7(self):
        self.assertEqual(run_calculator('45', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*7 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_8(self):
        self.assertEqual(run_calculator('45', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*8 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_9(self):
        self.assertEqual(run_calculator('45', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*9 = 405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_10(self):
        self.assertEqual(run_calculator('45', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*10 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_11(self):
        self.assertEqual(run_calculator('45', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*11 = 495',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_12(self):
        self.assertEqual(run_calculator('45', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*12 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_13(self):
        self.assertEqual(run_calculator('45', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*13 = 585',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_14(self):
        self.assertEqual(run_calculator('45', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*14 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_15(self):
        self.assertEqual(run_calculator('45', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*15 = 675',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_16(self):
        self.assertEqual(run_calculator('45', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*16 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_17(self):
        self.assertEqual(run_calculator('45', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*17 = 765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_18(self):
        self.assertEqual(run_calculator('45', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*18 = 810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_19(self):
        self.assertEqual(run_calculator('45', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*19 = 855',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_20(self):
        self.assertEqual(run_calculator('45', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*20 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_21(self):
        self.assertEqual(run_calculator('45', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*21 = 945',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_22(self):
        self.assertEqual(run_calculator('45', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*22 = 990',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_23(self):
        self.assertEqual(run_calculator('45', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*23 = 1035',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_24(self):
        self.assertEqual(run_calculator('45', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*24 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_25(self):
        self.assertEqual(run_calculator('45', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*25 = 1125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_26(self):
        self.assertEqual(run_calculator('45', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*26 = 1170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_27(self):
        self.assertEqual(run_calculator('45', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*27 = 1215',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_28(self):
        self.assertEqual(run_calculator('45', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*28 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_29(self):
        self.assertEqual(run_calculator('45', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*29 = 1305',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_30(self):
        self.assertEqual(run_calculator('45', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*30 = 1350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_31(self):
        self.assertEqual(run_calculator('45', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*31 = 1395',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_32(self):
        self.assertEqual(run_calculator('45', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*32 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_33(self):
        self.assertEqual(run_calculator('45', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*33 = 1485',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_34(self):
        self.assertEqual(run_calculator('45', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*34 = 1530',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_35(self):
        self.assertEqual(run_calculator('45', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*35 = 1575',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_36(self):
        self.assertEqual(run_calculator('45', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*36 = 1620',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_37(self):
        self.assertEqual(run_calculator('45', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*37 = 1665',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_38(self):
        self.assertEqual(run_calculator('45', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*38 = 1710',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_39(self):
        self.assertEqual(run_calculator('45', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*39 = 1755',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_40(self):
        self.assertEqual(run_calculator('45', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*40 = 1800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_41(self):
        self.assertEqual(run_calculator('45', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*41 = 1845',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_42(self):
        self.assertEqual(run_calculator('45', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*42 = 1890',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_43(self):
        self.assertEqual(run_calculator('45', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*43 = 1935',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_44(self):
        self.assertEqual(run_calculator('45', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*44 = 1980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_45(self):
        self.assertEqual(run_calculator('45', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*45 = 2025',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_46(self):
        self.assertEqual(run_calculator('45', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*46 = 2070',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_47(self):
        self.assertEqual(run_calculator('45', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*47 = 2115',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_48(self):
        self.assertEqual(run_calculator('45', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*48 = 2160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_49(self):
        self.assertEqual(run_calculator('45', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*49 = 2205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_times_50(self):
        self.assertEqual(run_calculator('45', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45*50 = 2250',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
