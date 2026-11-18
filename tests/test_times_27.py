# test_times_27.py
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


class TestTimes27(unittest.TestCase):

    def test_27_times_0(self):
        self.assertEqual(run_calculator('27', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_1(self):
        self.assertEqual(run_calculator('27', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*1 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_2(self):
        self.assertEqual(run_calculator('27', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*2 = 54',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_3(self):
        self.assertEqual(run_calculator('27', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*3 = 81',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_4(self):
        self.assertEqual(run_calculator('27', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*4 = 108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_5(self):
        self.assertEqual(run_calculator('27', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*5 = 135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_6(self):
        self.assertEqual(run_calculator('27', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*6 = 162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_7(self):
        self.assertEqual(run_calculator('27', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*7 = 189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_8(self):
        self.assertEqual(run_calculator('27', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*8 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_9(self):
        self.assertEqual(run_calculator('27', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*9 = 243',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_10(self):
        self.assertEqual(run_calculator('27', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*10 = 270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_11(self):
        self.assertEqual(run_calculator('27', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*11 = 297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_12(self):
        self.assertEqual(run_calculator('27', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*12 = 324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_13(self):
        self.assertEqual(run_calculator('27', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*13 = 351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_14(self):
        self.assertEqual(run_calculator('27', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*14 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_15(self):
        self.assertEqual(run_calculator('27', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*15 = 405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_16(self):
        self.assertEqual(run_calculator('27', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*16 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_17(self):
        self.assertEqual(run_calculator('27', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*17 = 459',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_18(self):
        self.assertEqual(run_calculator('27', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*18 = 486',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_19(self):
        self.assertEqual(run_calculator('27', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*19 = 513',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_20(self):
        self.assertEqual(run_calculator('27', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*20 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_21(self):
        self.assertEqual(run_calculator('27', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*21 = 567',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_22(self):
        self.assertEqual(run_calculator('27', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*22 = 594',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_23(self):
        self.assertEqual(run_calculator('27', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*23 = 621',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_24(self):
        self.assertEqual(run_calculator('27', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*24 = 648',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_25(self):
        self.assertEqual(run_calculator('27', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*25 = 675',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_26(self):
        self.assertEqual(run_calculator('27', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*26 = 702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_27(self):
        self.assertEqual(run_calculator('27', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*27 = 729',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_28(self):
        self.assertEqual(run_calculator('27', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*28 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_29(self):
        self.assertEqual(run_calculator('27', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*29 = 783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_30(self):
        self.assertEqual(run_calculator('27', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*30 = 810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_31(self):
        self.assertEqual(run_calculator('27', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*31 = 837',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_32(self):
        self.assertEqual(run_calculator('27', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*32 = 864',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_33(self):
        self.assertEqual(run_calculator('27', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*33 = 891',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_34(self):
        self.assertEqual(run_calculator('27', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*34 = 918',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_35(self):
        self.assertEqual(run_calculator('27', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*35 = 945',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_36(self):
        self.assertEqual(run_calculator('27', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*36 = 972',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_37(self):
        self.assertEqual(run_calculator('27', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*37 = 999',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_38(self):
        self.assertEqual(run_calculator('27', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*38 = 1026',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_39(self):
        self.assertEqual(run_calculator('27', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*39 = 1053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_40(self):
        self.assertEqual(run_calculator('27', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*40 = 1080',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_41(self):
        self.assertEqual(run_calculator('27', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*41 = 1107',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_42(self):
        self.assertEqual(run_calculator('27', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*42 = 1134',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_43(self):
        self.assertEqual(run_calculator('27', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*43 = 1161',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_44(self):
        self.assertEqual(run_calculator('27', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*44 = 1188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_45(self):
        self.assertEqual(run_calculator('27', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*45 = 1215',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_46(self):
        self.assertEqual(run_calculator('27', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*46 = 1242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_47(self):
        self.assertEqual(run_calculator('27', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*47 = 1269',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_48(self):
        self.assertEqual(run_calculator('27', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*48 = 1296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_49(self):
        self.assertEqual(run_calculator('27', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*49 = 1323',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_times_50(self):
        self.assertEqual(run_calculator('27', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27*50 = 1350',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
