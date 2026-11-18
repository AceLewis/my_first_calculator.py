# test_divided_by_7.py
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


class TestDividedBy7(unittest.TestCase):

    def test_7_divided_by_0(self):
        self.assertEqual(run_calculator('7', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_1(self):
        self.assertEqual(run_calculator('7', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/1 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_2(self):
        self.assertEqual(run_calculator('7', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/2 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_3(self):
        self.assertEqual(run_calculator('7', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/3 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_4(self):
        self.assertEqual(run_calculator('7', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/4 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_5(self):
        self.assertEqual(run_calculator('7', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/5 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_6(self):
        self.assertEqual(run_calculator('7', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/6 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_7(self):
        self.assertEqual(run_calculator('7', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/7 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_8(self):
        self.assertEqual(run_calculator('7', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/8 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_9(self):
        self.assertEqual(run_calculator('7', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/9 = 0.7777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_10(self):
        self.assertEqual(run_calculator('7', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/10 = 0.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_11(self):
        self.assertEqual(run_calculator('7', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/11 = 0.6363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_12(self):
        self.assertEqual(run_calculator('7', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/12 = 0.5833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_13(self):
        self.assertEqual(run_calculator('7', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/13 = 0.5384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_14(self):
        self.assertEqual(run_calculator('7', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/14 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_15(self):
        self.assertEqual(run_calculator('7', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/15 = 0.4666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_16(self):
        self.assertEqual(run_calculator('7', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/16 = 0.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_17(self):
        self.assertEqual(run_calculator('7', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/17 = 0.4117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_18(self):
        self.assertEqual(run_calculator('7', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/18 = 0.3888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_19(self):
        self.assertEqual(run_calculator('7', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/19 = 0.3684210526315789473684210526',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_20(self):
        self.assertEqual(run_calculator('7', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/20 = 0.35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_21(self):
        self.assertEqual(run_calculator('7', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/21 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_22(self):
        self.assertEqual(run_calculator('7', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/22 = 0.3181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_23(self):
        self.assertEqual(run_calculator('7', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/23 = 0.3043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_24(self):
        self.assertEqual(run_calculator('7', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/24 = 0.2916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_25(self):
        self.assertEqual(run_calculator('7', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/25 = 0.28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_26(self):
        self.assertEqual(run_calculator('7', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/26 = 0.2692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_27(self):
        self.assertEqual(run_calculator('7', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/27 = 0.2592592592592592592592592593',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_28(self):
        self.assertEqual(run_calculator('7', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/28 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_29(self):
        self.assertEqual(run_calculator('7', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/29 = 0.2413793103448275862068965517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_30(self):
        self.assertEqual(run_calculator('7', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/30 = 0.2333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_31(self):
        self.assertEqual(run_calculator('7', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/31 = 0.2258064516129032258064516129',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_32(self):
        self.assertEqual(run_calculator('7', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/32 = 0.21875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_33(self):
        self.assertEqual(run_calculator('7', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/33 = 0.2121212121212121212121212121',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_34(self):
        self.assertEqual(run_calculator('7', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/34 = 0.2058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_35(self):
        self.assertEqual(run_calculator('7', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/35 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_36(self):
        self.assertEqual(run_calculator('7', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/36 = 0.1944444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_37(self):
        self.assertEqual(run_calculator('7', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/37 = 0.1891891891891891891891891892',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_38(self):
        self.assertEqual(run_calculator('7', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/38 = 0.1842105263157894736842105263',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_39(self):
        self.assertEqual(run_calculator('7', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/39 = 0.1794871794871794871794871795',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_40(self):
        self.assertEqual(run_calculator('7', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/40 = 0.175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_41(self):
        self.assertEqual(run_calculator('7', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/41 = 0.1707317073170731707317073171',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_42(self):
        self.assertEqual(run_calculator('7', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/42 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_43(self):
        self.assertEqual(run_calculator('7', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/43 = 0.1627906976744186046511627907',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_44(self):
        self.assertEqual(run_calculator('7', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/44 = 0.1590909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_45(self):
        self.assertEqual(run_calculator('7', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/45 = 0.1555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_46(self):
        self.assertEqual(run_calculator('7', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/46 = 0.1521739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_47(self):
        self.assertEqual(run_calculator('7', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/47 = 0.1489361702127659574468085106',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_48(self):
        self.assertEqual(run_calculator('7', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/48 = 0.1458333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_49(self):
        self.assertEqual(run_calculator('7', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/49 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_7_divided_by_50(self):
        self.assertEqual(run_calculator('7', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '7/50 = 0.14',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
