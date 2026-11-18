# test_times_43.py
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


class TestTimes43(unittest.TestCase):

    def test_43_times_0(self):
        self.assertEqual(run_calculator('43', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_1(self):
        self.assertEqual(run_calculator('43', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*1 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_2(self):
        self.assertEqual(run_calculator('43', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*2 = 86',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_3(self):
        self.assertEqual(run_calculator('43', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*3 = 129',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_4(self):
        self.assertEqual(run_calculator('43', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*4 = 172',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_5(self):
        self.assertEqual(run_calculator('43', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*5 = 215',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_6(self):
        self.assertEqual(run_calculator('43', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*6 = 258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_7(self):
        self.assertEqual(run_calculator('43', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*7 = 301',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_8(self):
        self.assertEqual(run_calculator('43', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*8 = 344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_9(self):
        self.assertEqual(run_calculator('43', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*9 = 387',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_10(self):
        self.assertEqual(run_calculator('43', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*10 = 430',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_11(self):
        self.assertEqual(run_calculator('43', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*11 = 473',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_12(self):
        self.assertEqual(run_calculator('43', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*12 = 516',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_13(self):
        self.assertEqual(run_calculator('43', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*13 = 559',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_14(self):
        self.assertEqual(run_calculator('43', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*14 = 602',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_15(self):
        self.assertEqual(run_calculator('43', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*15 = 645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_16(self):
        self.assertEqual(run_calculator('43', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*16 = 688',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_17(self):
        self.assertEqual(run_calculator('43', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*17 = 731',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_18(self):
        self.assertEqual(run_calculator('43', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*18 = 774',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_19(self):
        self.assertEqual(run_calculator('43', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*19 = 817',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_20(self):
        self.assertEqual(run_calculator('43', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*20 = 860',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_21(self):
        self.assertEqual(run_calculator('43', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*21 = 903',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_22(self):
        self.assertEqual(run_calculator('43', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*22 = 946',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_23(self):
        self.assertEqual(run_calculator('43', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*23 = 989',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_24(self):
        self.assertEqual(run_calculator('43', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*24 = 1032',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_25(self):
        self.assertEqual(run_calculator('43', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*25 = 1075',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_26(self):
        self.assertEqual(run_calculator('43', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*26 = 1118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_27(self):
        self.assertEqual(run_calculator('43', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*27 = 1161',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_28(self):
        self.assertEqual(run_calculator('43', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*28 = 1204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_29(self):
        self.assertEqual(run_calculator('43', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*29 = 1247',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_30(self):
        self.assertEqual(run_calculator('43', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*30 = 1290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_31(self):
        self.assertEqual(run_calculator('43', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*31 = 1333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_32(self):
        self.assertEqual(run_calculator('43', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*32 = 1376',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_33(self):
        self.assertEqual(run_calculator('43', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*33 = 1419',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_34(self):
        self.assertEqual(run_calculator('43', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*34 = 1462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_35(self):
        self.assertEqual(run_calculator('43', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*35 = 1505',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_36(self):
        self.assertEqual(run_calculator('43', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*36 = 1548',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_37(self):
        self.assertEqual(run_calculator('43', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*37 = 1591',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_38(self):
        self.assertEqual(run_calculator('43', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*38 = 1634',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_39(self):
        self.assertEqual(run_calculator('43', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*39 = 1677',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_40(self):
        self.assertEqual(run_calculator('43', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*40 = 1720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_41(self):
        self.assertEqual(run_calculator('43', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*41 = 1763',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_42(self):
        self.assertEqual(run_calculator('43', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*42 = 1806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_43(self):
        self.assertEqual(run_calculator('43', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*43 = 1849',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_44(self):
        self.assertEqual(run_calculator('43', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*44 = 1892',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_45(self):
        self.assertEqual(run_calculator('43', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*45 = 1935',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_46(self):
        self.assertEqual(run_calculator('43', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*46 = 1978',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_47(self):
        self.assertEqual(run_calculator('43', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*47 = 2021',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_48(self):
        self.assertEqual(run_calculator('43', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*48 = 2064',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_49(self):
        self.assertEqual(run_calculator('43', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*49 = 2107',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_times_50(self):
        self.assertEqual(run_calculator('43', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43*50 = 2150',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
