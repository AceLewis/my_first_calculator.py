# test_times_32.py
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


class TestTimes32(unittest.TestCase):

    def test_32_times_0(self):
        self.assertEqual(run_calculator('32', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_1(self):
        self.assertEqual(run_calculator('32', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*1 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_2(self):
        self.assertEqual(run_calculator('32', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*2 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_3(self):
        self.assertEqual(run_calculator('32', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*3 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_4(self):
        self.assertEqual(run_calculator('32', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*4 = 128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_5(self):
        self.assertEqual(run_calculator('32', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*5 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_6(self):
        self.assertEqual(run_calculator('32', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*6 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_7(self):
        self.assertEqual(run_calculator('32', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*7 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_8(self):
        self.assertEqual(run_calculator('32', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*8 = 256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_9(self):
        self.assertEqual(run_calculator('32', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*9 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_10(self):
        self.assertEqual(run_calculator('32', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*10 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_11(self):
        self.assertEqual(run_calculator('32', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*11 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_12(self):
        self.assertEqual(run_calculator('32', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*12 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_13(self):
        self.assertEqual(run_calculator('32', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*13 = 416',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_14(self):
        self.assertEqual(run_calculator('32', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*14 = 448',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_15(self):
        self.assertEqual(run_calculator('32', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*15 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_16(self):
        self.assertEqual(run_calculator('32', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*16 = 512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_17(self):
        self.assertEqual(run_calculator('32', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*17 = 544',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_18(self):
        self.assertEqual(run_calculator('32', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*18 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_19(self):
        self.assertEqual(run_calculator('32', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*19 = 608',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_20(self):
        self.assertEqual(run_calculator('32', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*20 = 640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_21(self):
        self.assertEqual(run_calculator('32', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*21 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_22(self):
        self.assertEqual(run_calculator('32', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*22 = 704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_23(self):
        self.assertEqual(run_calculator('32', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*23 = 736',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_24(self):
        self.assertEqual(run_calculator('32', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*24 = 768',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_25(self):
        self.assertEqual(run_calculator('32', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*25 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_26(self):
        self.assertEqual(run_calculator('32', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*26 = 832',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_27(self):
        self.assertEqual(run_calculator('32', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*27 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_28(self):
        self.assertEqual(run_calculator('32', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*28 = 896',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_29(self):
        self.assertEqual(run_calculator('32', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*29 = 928',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_30(self):
        self.assertEqual(run_calculator('32', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*30 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_31(self):
        self.assertEqual(run_calculator('32', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*31 = 992',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_32(self):
        self.assertEqual(run_calculator('32', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*32 = 1024',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_33(self):
        self.assertEqual(run_calculator('32', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*33 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_34(self):
        self.assertEqual(run_calculator('32', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*34 = 1088',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_35(self):
        self.assertEqual(run_calculator('32', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*35 = 1120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_36(self):
        self.assertEqual(run_calculator('32', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*36 = 1152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_37(self):
        self.assertEqual(run_calculator('32', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*37 = 1184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_38(self):
        self.assertEqual(run_calculator('32', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*38 = 1216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_39(self):
        self.assertEqual(run_calculator('32', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*39 = 1248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_40(self):
        self.assertEqual(run_calculator('32', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*40 = 1280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_41(self):
        self.assertEqual(run_calculator('32', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*41 = 1312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_42(self):
        self.assertEqual(run_calculator('32', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*42 = 1344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_43(self):
        self.assertEqual(run_calculator('32', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*43 = 1376',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_44(self):
        self.assertEqual(run_calculator('32', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*44 = 1408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_45(self):
        self.assertEqual(run_calculator('32', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*45 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_46(self):
        self.assertEqual(run_calculator('32', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*46 = 1472',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_47(self):
        self.assertEqual(run_calculator('32', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*47 = 1504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_48(self):
        self.assertEqual(run_calculator('32', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*48 = 1536',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_49(self):
        self.assertEqual(run_calculator('32', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*49 = 1568',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_times_50(self):
        self.assertEqual(run_calculator('32', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32*50 = 1600',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
