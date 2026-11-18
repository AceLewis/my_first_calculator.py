# test_times_48.py
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


class TestTimes48(unittest.TestCase):

    def test_48_times_0(self):
        self.assertEqual(run_calculator('48', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_1(self):
        self.assertEqual(run_calculator('48', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*1 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_2(self):
        self.assertEqual(run_calculator('48', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*2 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_3(self):
        self.assertEqual(run_calculator('48', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*3 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_4(self):
        self.assertEqual(run_calculator('48', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*4 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_5(self):
        self.assertEqual(run_calculator('48', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*5 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_6(self):
        self.assertEqual(run_calculator('48', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*6 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_7(self):
        self.assertEqual(run_calculator('48', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*7 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_8(self):
        self.assertEqual(run_calculator('48', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*8 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_9(self):
        self.assertEqual(run_calculator('48', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*9 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_10(self):
        self.assertEqual(run_calculator('48', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*10 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_11(self):
        self.assertEqual(run_calculator('48', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*11 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_12(self):
        self.assertEqual(run_calculator('48', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*12 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_13(self):
        self.assertEqual(run_calculator('48', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*13 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_14(self):
        self.assertEqual(run_calculator('48', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*14 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_15(self):
        self.assertEqual(run_calculator('48', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*15 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_16(self):
        self.assertEqual(run_calculator('48', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*16 = 768',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_17(self):
        self.assertEqual(run_calculator('48', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*17 = 816',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_18(self):
        self.assertEqual(run_calculator('48', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*18 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_19(self):
        self.assertEqual(run_calculator('48', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*19 = 912',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_20(self):
        self.assertEqual(run_calculator('48', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*20 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_21(self):
        self.assertEqual(run_calculator('48', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*21 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_22(self):
        self.assertEqual(run_calculator('48', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*22 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_23(self):
        self.assertEqual(run_calculator('48', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*23 = 1104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_24(self):
        self.assertEqual(run_calculator('48', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*24 = 1152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_25(self):
        self.assertEqual(run_calculator('48', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*25 = 1200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_26(self):
        self.assertEqual(run_calculator('48', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*26 = 1248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_27(self):
        self.assertEqual(run_calculator('48', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*27 = 1296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_28(self):
        self.assertEqual(run_calculator('48', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*28 = 1344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_29(self):
        self.assertEqual(run_calculator('48', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*29 = 1392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_30(self):
        self.assertEqual(run_calculator('48', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*30 = 1440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_31(self):
        self.assertEqual(run_calculator('48', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*31 = 1488',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_32(self):
        self.assertEqual(run_calculator('48', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*32 = 1536',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_33(self):
        self.assertEqual(run_calculator('48', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*33 = 1584',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_34(self):
        self.assertEqual(run_calculator('48', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*34 = 1632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_35(self):
        self.assertEqual(run_calculator('48', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*35 = 1680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_36(self):
        self.assertEqual(run_calculator('48', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*36 = 1728',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_37(self):
        self.assertEqual(run_calculator('48', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*37 = 1776',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_38(self):
        self.assertEqual(run_calculator('48', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*38 = 1824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_39(self):
        self.assertEqual(run_calculator('48', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*39 = 1872',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_40(self):
        self.assertEqual(run_calculator('48', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*40 = 1920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_41(self):
        self.assertEqual(run_calculator('48', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*41 = 1968',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_42(self):
        self.assertEqual(run_calculator('48', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*42 = 2016',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_43(self):
        self.assertEqual(run_calculator('48', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*43 = 2064',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_44(self):
        self.assertEqual(run_calculator('48', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*44 = 2112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_45(self):
        self.assertEqual(run_calculator('48', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*45 = 2160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_46(self):
        self.assertEqual(run_calculator('48', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*46 = 2208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_47(self):
        self.assertEqual(run_calculator('48', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*47 = 2256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_48(self):
        self.assertEqual(run_calculator('48', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*48 = 2304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_49(self):
        self.assertEqual(run_calculator('48', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*49 = 2352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_times_50(self):
        self.assertEqual(run_calculator('48', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48*50 = 2400',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
