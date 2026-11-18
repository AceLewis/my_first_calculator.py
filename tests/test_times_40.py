# test_times_40.py
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


class TestTimes40(unittest.TestCase):

    def test_40_times_0(self):
        self.assertEqual(run_calculator('40', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_1(self):
        self.assertEqual(run_calculator('40', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*1 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_2(self):
        self.assertEqual(run_calculator('40', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*2 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_3(self):
        self.assertEqual(run_calculator('40', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*3 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_4(self):
        self.assertEqual(run_calculator('40', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*4 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_5(self):
        self.assertEqual(run_calculator('40', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*5 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_6(self):
        self.assertEqual(run_calculator('40', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*6 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_7(self):
        self.assertEqual(run_calculator('40', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*7 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_8(self):
        self.assertEqual(run_calculator('40', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*8 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_9(self):
        self.assertEqual(run_calculator('40', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*9 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_10(self):
        self.assertEqual(run_calculator('40', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*10 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_11(self):
        self.assertEqual(run_calculator('40', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*11 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_12(self):
        self.assertEqual(run_calculator('40', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*12 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_13(self):
        self.assertEqual(run_calculator('40', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*13 = 520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_14(self):
        self.assertEqual(run_calculator('40', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*14 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_15(self):
        self.assertEqual(run_calculator('40', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*15 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_16(self):
        self.assertEqual(run_calculator('40', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*16 = 640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_17(self):
        self.assertEqual(run_calculator('40', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*17 = 680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_18(self):
        self.assertEqual(run_calculator('40', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*18 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_19(self):
        self.assertEqual(run_calculator('40', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*19 = 760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_20(self):
        self.assertEqual(run_calculator('40', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*20 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_21(self):
        self.assertEqual(run_calculator('40', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*21 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_22(self):
        self.assertEqual(run_calculator('40', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*22 = 880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_23(self):
        self.assertEqual(run_calculator('40', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*23 = 920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_24(self):
        self.assertEqual(run_calculator('40', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*24 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_25(self):
        self.assertEqual(run_calculator('40', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*25 = 1000',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_26(self):
        self.assertEqual(run_calculator('40', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*26 = 1040',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_27(self):
        self.assertEqual(run_calculator('40', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*27 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_28(self):
        self.assertEqual(run_calculator('40', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*28 = 1120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_29(self):
        self.assertEqual(run_calculator('40', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*29 = 1160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_30(self):
        self.assertEqual(run_calculator('40', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*30 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_31(self):
        self.assertEqual(run_calculator('40', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*31 = 1240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_32(self):
        self.assertEqual(run_calculator('40', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*32 = 1280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_33(self):
        self.assertEqual(run_calculator('40', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*33 = 1320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_34(self):
        self.assertEqual(run_calculator('40', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*34 = 1360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_35(self):
        self.assertEqual(run_calculator('40', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*35 = 1400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_36(self):
        self.assertEqual(run_calculator('40', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*36 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_37(self):
        self.assertEqual(run_calculator('40', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*37 = 1480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_38(self):
        self.assertEqual(run_calculator('40', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*38 = 1520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_39(self):
        self.assertEqual(run_calculator('40', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*39 = 1560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_40(self):
        self.assertEqual(run_calculator('40', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*40 = 1600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_41(self):
        self.assertEqual(run_calculator('40', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*41 = 1640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_42(self):
        self.assertEqual(run_calculator('40', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*42 = 1680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_43(self):
        self.assertEqual(run_calculator('40', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*43 = 1720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_44(self):
        self.assertEqual(run_calculator('40', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*44 = 1760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_45(self):
        self.assertEqual(run_calculator('40', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*45 = 1800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_46(self):
        self.assertEqual(run_calculator('40', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*46 = 1840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_47(self):
        self.assertEqual(run_calculator('40', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*47 = 1880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_48(self):
        self.assertEqual(run_calculator('40', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*48 = 1920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_49(self):
        self.assertEqual(run_calculator('40', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*49 = 1960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_times_50(self):
        self.assertEqual(run_calculator('40', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40*50 = 2000',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
