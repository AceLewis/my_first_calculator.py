# test_times_42.py
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


class TestTimes42(unittest.TestCase):

    def test_42_times_0(self):
        self.assertEqual(run_calculator('42', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_1(self):
        self.assertEqual(run_calculator('42', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*1 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_2(self):
        self.assertEqual(run_calculator('42', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*2 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_3(self):
        self.assertEqual(run_calculator('42', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*3 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_4(self):
        self.assertEqual(run_calculator('42', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*4 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_5(self):
        self.assertEqual(run_calculator('42', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*5 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_6(self):
        self.assertEqual(run_calculator('42', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*6 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_7(self):
        self.assertEqual(run_calculator('42', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*7 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_8(self):
        self.assertEqual(run_calculator('42', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*8 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_9(self):
        self.assertEqual(run_calculator('42', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*9 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_10(self):
        self.assertEqual(run_calculator('42', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*10 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_11(self):
        self.assertEqual(run_calculator('42', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*11 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_12(self):
        self.assertEqual(run_calculator('42', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*12 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_13(self):
        self.assertEqual(run_calculator('42', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*13 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_14(self):
        self.assertEqual(run_calculator('42', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*14 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_15(self):
        self.assertEqual(run_calculator('42', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*15 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_16(self):
        self.assertEqual(run_calculator('42', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*16 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_17(self):
        self.assertEqual(run_calculator('42', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*17 = 714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_18(self):
        self.assertEqual(run_calculator('42', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*18 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_19(self):
        self.assertEqual(run_calculator('42', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*19 = 798',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_20(self):
        self.assertEqual(run_calculator('42', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*20 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_21(self):
        self.assertEqual(run_calculator('42', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*21 = 882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_22(self):
        self.assertEqual(run_calculator('42', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*22 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_23(self):
        self.assertEqual(run_calculator('42', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*23 = 966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_24(self):
        self.assertEqual(run_calculator('42', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*24 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_25(self):
        self.assertEqual(run_calculator('42', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*25 = 1050',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_26(self):
        self.assertEqual(run_calculator('42', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*26 = 1092',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_27(self):
        self.assertEqual(run_calculator('42', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*27 = 1134',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_28(self):
        self.assertEqual(run_calculator('42', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*28 = 1176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_29(self):
        self.assertEqual(run_calculator('42', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*29 = 1218',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_30(self):
        self.assertEqual(run_calculator('42', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*30 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_31(self):
        self.assertEqual(run_calculator('42', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*31 = 1302',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_32(self):
        self.assertEqual(run_calculator('42', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*32 = 1344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_33(self):
        self.assertEqual(run_calculator('42', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*33 = 1386',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_34(self):
        self.assertEqual(run_calculator('42', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*34 = 1428',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_35(self):
        self.assertEqual(run_calculator('42', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*35 = 1470',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_36(self):
        self.assertEqual(run_calculator('42', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*36 = 1512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_37(self):
        self.assertEqual(run_calculator('42', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*37 = 1554',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_38(self):
        self.assertEqual(run_calculator('42', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*38 = 1596',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_39(self):
        self.assertEqual(run_calculator('42', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*39 = 1638',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_40(self):
        self.assertEqual(run_calculator('42', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*40 = 1680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_41(self):
        self.assertEqual(run_calculator('42', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*41 = 1722',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_42(self):
        self.assertEqual(run_calculator('42', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*42 = 1764',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_43(self):
        self.assertEqual(run_calculator('42', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*43 = 1806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_44(self):
        self.assertEqual(run_calculator('42', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*44 = 1848',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_45(self):
        self.assertEqual(run_calculator('42', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*45 = 1890',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_46(self):
        self.assertEqual(run_calculator('42', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*46 = 1932',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_47(self):
        self.assertEqual(run_calculator('42', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*47 = 1974',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_48(self):
        self.assertEqual(run_calculator('42', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*48 = 2016',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_49(self):
        self.assertEqual(run_calculator('42', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*49 = 2058',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_times_50(self):
        self.assertEqual(run_calculator('42', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42*50 = 2100',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
