# test_times_9.py
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


class TestTimes9(unittest.TestCase):

    def test_9_times_0(self):
        self.assertEqual(run_calculator('9', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_1(self):
        self.assertEqual(run_calculator('9', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*1 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_2(self):
        self.assertEqual(run_calculator('9', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*2 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_3(self):
        self.assertEqual(run_calculator('9', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*3 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_4(self):
        self.assertEqual(run_calculator('9', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*4 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_5(self):
        self.assertEqual(run_calculator('9', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*5 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_6(self):
        self.assertEqual(run_calculator('9', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*6 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_7(self):
        self.assertEqual(run_calculator('9', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*7 = 63',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_8(self):
        self.assertEqual(run_calculator('9', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*8 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_9(self):
        self.assertEqual(run_calculator('9', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*9 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_10(self):
        self.assertEqual(run_calculator('9', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*10 = 90',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_11(self):
        self.assertEqual(run_calculator('9', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*11 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_12(self):
        self.assertEqual(run_calculator('9', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*12 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_13(self):
        self.assertEqual(run_calculator('9', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*13 = 117',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_14(self):
        self.assertEqual(run_calculator('9', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*14 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_15(self):
        self.assertEqual(run_calculator('9', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*15 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_16(self):
        self.assertEqual(run_calculator('9', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*16 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_17(self):
        self.assertEqual(run_calculator('9', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*17 = 153',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_18(self):
        self.assertEqual(run_calculator('9', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*18 = 162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_19(self):
        self.assertEqual(run_calculator('9', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*19 = 171',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_20(self):
        self.assertEqual(run_calculator('9', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*20 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_21(self):
        self.assertEqual(run_calculator('9', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*21 = 189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_22(self):
        self.assertEqual(run_calculator('9', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*22 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_23(self):
        self.assertEqual(run_calculator('9', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*23 = 207',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_24(self):
        self.assertEqual(run_calculator('9', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*24 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_25(self):
        self.assertEqual(run_calculator('9', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*25 = 225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_26(self):
        self.assertEqual(run_calculator('9', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*26 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_27(self):
        self.assertEqual(run_calculator('9', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*27 = 243',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_28(self):
        self.assertEqual(run_calculator('9', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*28 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_29(self):
        self.assertEqual(run_calculator('9', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*29 = 261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_30(self):
        self.assertEqual(run_calculator('9', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*30 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_31(self):
        self.assertEqual(run_calculator('9', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*31 = 279',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_32(self):
        self.assertEqual(run_calculator('9', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*32 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_33(self):
        self.assertEqual(run_calculator('9', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*33 = 297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_34(self):
        self.assertEqual(run_calculator('9', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*34 = 306',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_35(self):
        self.assertEqual(run_calculator('9', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*35 = 315',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_36(self):
        self.assertEqual(run_calculator('9', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*36 = 324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_37(self):
        self.assertEqual(run_calculator('9', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*37 = 333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_38(self):
        self.assertEqual(run_calculator('9', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*38 = 342',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_39(self):
        self.assertEqual(run_calculator('9', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*39 = 351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_40(self):
        self.assertEqual(run_calculator('9', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*40 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_41(self):
        self.assertEqual(run_calculator('9', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*41 = 369',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_42(self):
        self.assertEqual(run_calculator('9', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*42 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_43(self):
        self.assertEqual(run_calculator('9', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*43 = 387',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_44(self):
        self.assertEqual(run_calculator('9', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*44 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_45(self):
        self.assertEqual(run_calculator('9', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*45 = 405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_46(self):
        self.assertEqual(run_calculator('9', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*46 = 414',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_47(self):
        self.assertEqual(run_calculator('9', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*47 = 423',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_48(self):
        self.assertEqual(run_calculator('9', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*48 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_49(self):
        self.assertEqual(run_calculator('9', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*49 = 441',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_times_50(self):
        self.assertEqual(run_calculator('9', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9*50 = 450',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
