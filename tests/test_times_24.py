# test_times_24.py
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


class TestTimes24(unittest.TestCase):

    def test_24_times_0(self):
        self.assertEqual(run_calculator('24', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_1(self):
        self.assertEqual(run_calculator('24', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*1 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_2(self):
        self.assertEqual(run_calculator('24', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*2 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_3(self):
        self.assertEqual(run_calculator('24', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*3 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_4(self):
        self.assertEqual(run_calculator('24', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*4 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_5(self):
        self.assertEqual(run_calculator('24', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*5 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_6(self):
        self.assertEqual(run_calculator('24', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*6 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_7(self):
        self.assertEqual(run_calculator('24', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*7 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_8(self):
        self.assertEqual(run_calculator('24', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*8 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_9(self):
        self.assertEqual(run_calculator('24', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*9 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_10(self):
        self.assertEqual(run_calculator('24', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*10 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_11(self):
        self.assertEqual(run_calculator('24', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*11 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_12(self):
        self.assertEqual(run_calculator('24', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*12 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_13(self):
        self.assertEqual(run_calculator('24', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*13 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_14(self):
        self.assertEqual(run_calculator('24', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*14 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_15(self):
        self.assertEqual(run_calculator('24', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*15 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_16(self):
        self.assertEqual(run_calculator('24', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*16 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_17(self):
        self.assertEqual(run_calculator('24', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*17 = 408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_18(self):
        self.assertEqual(run_calculator('24', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*18 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_19(self):
        self.assertEqual(run_calculator('24', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*19 = 456',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_20(self):
        self.assertEqual(run_calculator('24', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*20 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_21(self):
        self.assertEqual(run_calculator('24', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*21 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_22(self):
        self.assertEqual(run_calculator('24', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*22 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_23(self):
        self.assertEqual(run_calculator('24', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*23 = 552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_24(self):
        self.assertEqual(run_calculator('24', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*24 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_25(self):
        self.assertEqual(run_calculator('24', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*25 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_26(self):
        self.assertEqual(run_calculator('24', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*26 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_27(self):
        self.assertEqual(run_calculator('24', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*27 = 648',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_28(self):
        self.assertEqual(run_calculator('24', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*28 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_29(self):
        self.assertEqual(run_calculator('24', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*29 = 696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_30(self):
        self.assertEqual(run_calculator('24', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*30 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_31(self):
        self.assertEqual(run_calculator('24', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*31 = 744',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_32(self):
        self.assertEqual(run_calculator('24', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*32 = 768',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_33(self):
        self.assertEqual(run_calculator('24', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*33 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_34(self):
        self.assertEqual(run_calculator('24', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*34 = 816',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_35(self):
        self.assertEqual(run_calculator('24', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*35 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_36(self):
        self.assertEqual(run_calculator('24', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*36 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_37(self):
        self.assertEqual(run_calculator('24', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*37 = 888',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_38(self):
        self.assertEqual(run_calculator('24', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*38 = 912',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_39(self):
        self.assertEqual(run_calculator('24', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*39 = 936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_40(self):
        self.assertEqual(run_calculator('24', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*40 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_41(self):
        self.assertEqual(run_calculator('24', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*41 = 984',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_42(self):
        self.assertEqual(run_calculator('24', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*42 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_43(self):
        self.assertEqual(run_calculator('24', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*43 = 1032',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_44(self):
        self.assertEqual(run_calculator('24', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*44 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_45(self):
        self.assertEqual(run_calculator('24', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*45 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_46(self):
        self.assertEqual(run_calculator('24', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*46 = 1104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_47(self):
        self.assertEqual(run_calculator('24', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*47 = 1128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_48(self):
        self.assertEqual(run_calculator('24', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*48 = 1152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_49(self):
        self.assertEqual(run_calculator('24', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*49 = 1176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_times_50(self):
        self.assertEqual(run_calculator('24', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24*50 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
