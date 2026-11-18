# test_times_29.py
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


class TestTimes29(unittest.TestCase):

    def test_29_times_0(self):
        self.assertEqual(run_calculator('29', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_1(self):
        self.assertEqual(run_calculator('29', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*1 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_2(self):
        self.assertEqual(run_calculator('29', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*2 = 58',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_3(self):
        self.assertEqual(run_calculator('29', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*3 = 87',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_4(self):
        self.assertEqual(run_calculator('29', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*4 = 116',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_5(self):
        self.assertEqual(run_calculator('29', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*5 = 145',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_6(self):
        self.assertEqual(run_calculator('29', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*6 = 174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_7(self):
        self.assertEqual(run_calculator('29', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*7 = 203',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_8(self):
        self.assertEqual(run_calculator('29', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*8 = 232',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_9(self):
        self.assertEqual(run_calculator('29', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*9 = 261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_10(self):
        self.assertEqual(run_calculator('29', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*10 = 290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_11(self):
        self.assertEqual(run_calculator('29', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*11 = 319',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_12(self):
        self.assertEqual(run_calculator('29', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*12 = 348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_13(self):
        self.assertEqual(run_calculator('29', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*13 = 377',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_14(self):
        self.assertEqual(run_calculator('29', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*14 = 406',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_15(self):
        self.assertEqual(run_calculator('29', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*15 = 435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_16(self):
        self.assertEqual(run_calculator('29', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*16 = 464',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_17(self):
        self.assertEqual(run_calculator('29', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*17 = 493',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_18(self):
        self.assertEqual(run_calculator('29', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*18 = 522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_19(self):
        self.assertEqual(run_calculator('29', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*19 = 551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_20(self):
        self.assertEqual(run_calculator('29', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*20 = 580',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_21(self):
        self.assertEqual(run_calculator('29', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*21 = 609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_22(self):
        self.assertEqual(run_calculator('29', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*22 = 638',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_23(self):
        self.assertEqual(run_calculator('29', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*23 = 667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_24(self):
        self.assertEqual(run_calculator('29', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*24 = 696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_25(self):
        self.assertEqual(run_calculator('29', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*25 = 725',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_26(self):
        self.assertEqual(run_calculator('29', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*26 = 754',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_27(self):
        self.assertEqual(run_calculator('29', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*27 = 783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_28(self):
        self.assertEqual(run_calculator('29', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*28 = 812',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_29(self):
        self.assertEqual(run_calculator('29', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*29 = 841',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_30(self):
        self.assertEqual(run_calculator('29', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*30 = 870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_31(self):
        self.assertEqual(run_calculator('29', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*31 = 899',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_32(self):
        self.assertEqual(run_calculator('29', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*32 = 928',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_33(self):
        self.assertEqual(run_calculator('29', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*33 = 957',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_34(self):
        self.assertEqual(run_calculator('29', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*34 = 986',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_35(self):
        self.assertEqual(run_calculator('29', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*35 = 1015',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_36(self):
        self.assertEqual(run_calculator('29', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*36 = 1044',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_37(self):
        self.assertEqual(run_calculator('29', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*37 = 1073',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_38(self):
        self.assertEqual(run_calculator('29', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*38 = 1102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_39(self):
        self.assertEqual(run_calculator('29', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*39 = 1131',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_40(self):
        self.assertEqual(run_calculator('29', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*40 = 1160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_41(self):
        self.assertEqual(run_calculator('29', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*41 = 1189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_42(self):
        self.assertEqual(run_calculator('29', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*42 = 1218',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_43(self):
        self.assertEqual(run_calculator('29', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*43 = 1247',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_44(self):
        self.assertEqual(run_calculator('29', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*44 = 1276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_45(self):
        self.assertEqual(run_calculator('29', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*45 = 1305',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_46(self):
        self.assertEqual(run_calculator('29', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*46 = 1334',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_47(self):
        self.assertEqual(run_calculator('29', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*47 = 1363',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_48(self):
        self.assertEqual(run_calculator('29', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*48 = 1392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_49(self):
        self.assertEqual(run_calculator('29', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*49 = 1421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_times_50(self):
        self.assertEqual(run_calculator('29', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29*50 = 1450',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
