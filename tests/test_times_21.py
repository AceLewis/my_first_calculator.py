# test_times_21.py
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


class TestTimes21(unittest.TestCase):

    def test_21_times_0(self):
        self.assertEqual(run_calculator('21', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_1(self):
        self.assertEqual(run_calculator('21', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*1 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_2(self):
        self.assertEqual(run_calculator('21', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*2 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_3(self):
        self.assertEqual(run_calculator('21', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*3 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_4(self):
        self.assertEqual(run_calculator('21', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*4 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_5(self):
        self.assertEqual(run_calculator('21', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*5 = 105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_6(self):
        self.assertEqual(run_calculator('21', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*6 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_7(self):
        self.assertEqual(run_calculator('21', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*7 = 147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_8(self):
        self.assertEqual(run_calculator('21', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*8 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_9(self):
        self.assertEqual(run_calculator('21', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*9 = 189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_10(self):
        self.assertEqual(run_calculator('21', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*10 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_11(self):
        self.assertEqual(run_calculator('21', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*11 = 231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_12(self):
        self.assertEqual(run_calculator('21', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*12 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_13(self):
        self.assertEqual(run_calculator('21', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*13 = 273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_14(self):
        self.assertEqual(run_calculator('21', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*14 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_15(self):
        self.assertEqual(run_calculator('21', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*15 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_16(self):
        self.assertEqual(run_calculator('21', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*16 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_17(self):
        self.assertEqual(run_calculator('21', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*17 = 357',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_18(self):
        self.assertEqual(run_calculator('21', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*18 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_19(self):
        self.assertEqual(run_calculator('21', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*19 = 399',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_20(self):
        self.assertEqual(run_calculator('21', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*20 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_21(self):
        self.assertEqual(run_calculator('21', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*21 = 441',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_22(self):
        self.assertEqual(run_calculator('21', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*22 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_23(self):
        self.assertEqual(run_calculator('21', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*23 = 483',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_24(self):
        self.assertEqual(run_calculator('21', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*24 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_25(self):
        self.assertEqual(run_calculator('21', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*25 = 525',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_26(self):
        self.assertEqual(run_calculator('21', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*26 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_27(self):
        self.assertEqual(run_calculator('21', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*27 = 567',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_28(self):
        self.assertEqual(run_calculator('21', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*28 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_29(self):
        self.assertEqual(run_calculator('21', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*29 = 609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_30(self):
        self.assertEqual(run_calculator('21', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*30 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_31(self):
        self.assertEqual(run_calculator('21', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*31 = 651',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_32(self):
        self.assertEqual(run_calculator('21', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*32 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_33(self):
        self.assertEqual(run_calculator('21', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*33 = 693',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_34(self):
        self.assertEqual(run_calculator('21', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*34 = 714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_35(self):
        self.assertEqual(run_calculator('21', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*35 = 735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_36(self):
        self.assertEqual(run_calculator('21', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*36 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_37(self):
        self.assertEqual(run_calculator('21', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*37 = 777',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_38(self):
        self.assertEqual(run_calculator('21', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*38 = 798',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_39(self):
        self.assertEqual(run_calculator('21', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*39 = 819',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_40(self):
        self.assertEqual(run_calculator('21', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*40 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_41(self):
        self.assertEqual(run_calculator('21', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*41 = 861',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_42(self):
        self.assertEqual(run_calculator('21', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*42 = 882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_43(self):
        self.assertEqual(run_calculator('21', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*43 = 903',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_44(self):
        self.assertEqual(run_calculator('21', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*44 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_45(self):
        self.assertEqual(run_calculator('21', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*45 = 945',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_46(self):
        self.assertEqual(run_calculator('21', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*46 = 966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_47(self):
        self.assertEqual(run_calculator('21', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*47 = 987',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_48(self):
        self.assertEqual(run_calculator('21', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*48 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_49(self):
        self.assertEqual(run_calculator('21', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*49 = 1029',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_times_50(self):
        self.assertEqual(run_calculator('21', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21*50 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
