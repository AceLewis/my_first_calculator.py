# test_divided_by_29.py
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


class TestDividedBy29(unittest.TestCase):

    def test_29_divided_by_0(self):
        self.assertEqual(run_calculator('29', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_1(self):
        self.assertEqual(run_calculator('29', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/1 = 29',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_2(self):
        self.assertEqual(run_calculator('29', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/2 = 14.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_3(self):
        self.assertEqual(run_calculator('29', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/3 = 9.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_4(self):
        self.assertEqual(run_calculator('29', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/4 = 7.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_5(self):
        self.assertEqual(run_calculator('29', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/5 = 5.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_6(self):
        self.assertEqual(run_calculator('29', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/6 = 4.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_7(self):
        self.assertEqual(run_calculator('29', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/7 = 4.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_8(self):
        self.assertEqual(run_calculator('29', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/8 = 3.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_9(self):
        self.assertEqual(run_calculator('29', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/9 = 3.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_10(self):
        self.assertEqual(run_calculator('29', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/10 = 2.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_11(self):
        self.assertEqual(run_calculator('29', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/11 = 2.636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_12(self):
        self.assertEqual(run_calculator('29', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/12 = 2.416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_13(self):
        self.assertEqual(run_calculator('29', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/13 = 2.230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_14(self):
        self.assertEqual(run_calculator('29', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/14 = 2.071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_15(self):
        self.assertEqual(run_calculator('29', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/15 = 1.933333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_16(self):
        self.assertEqual(run_calculator('29', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/16 = 1.8125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_17(self):
        self.assertEqual(run_calculator('29', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/17 = 1.705882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_18(self):
        self.assertEqual(run_calculator('29', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/18 = 1.611111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_19(self):
        self.assertEqual(run_calculator('29', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/19 = 1.526315789473684210526315789',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_20(self):
        self.assertEqual(run_calculator('29', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/20 = 1.45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_21(self):
        self.assertEqual(run_calculator('29', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/21 = 1.380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_22(self):
        self.assertEqual(run_calculator('29', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/22 = 1.318181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_23(self):
        self.assertEqual(run_calculator('29', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/23 = 1.260869565217391304347826087',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_24(self):
        self.assertEqual(run_calculator('29', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/24 = 1.208333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_25(self):
        self.assertEqual(run_calculator('29', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/25 = 1.16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_26(self):
        self.assertEqual(run_calculator('29', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/26 = 1.115384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_27(self):
        self.assertEqual(run_calculator('29', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/27 = 1.074074074074074074074074074',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_28(self):
        self.assertEqual(run_calculator('29', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/28 = 1.035714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_29(self):
        self.assertEqual(run_calculator('29', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/29 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_30(self):
        self.assertEqual(run_calculator('29', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/30 = 0.9666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_31(self):
        self.assertEqual(run_calculator('29', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/31 = 0.9354838709677419354838709677',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_32(self):
        self.assertEqual(run_calculator('29', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/32 = 0.90625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_33(self):
        self.assertEqual(run_calculator('29', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/33 = 0.8787878787878787878787878788',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_34(self):
        self.assertEqual(run_calculator('29', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/34 = 0.8529411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_35(self):
        self.assertEqual(run_calculator('29', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/35 = 0.8285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_36(self):
        self.assertEqual(run_calculator('29', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/36 = 0.8055555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_37(self):
        self.assertEqual(run_calculator('29', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/37 = 0.7837837837837837837837837838',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_38(self):
        self.assertEqual(run_calculator('29', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/38 = 0.7631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_39(self):
        self.assertEqual(run_calculator('29', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/39 = 0.7435897435897435897435897436',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_40(self):
        self.assertEqual(run_calculator('29', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/40 = 0.725',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_41(self):
        self.assertEqual(run_calculator('29', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/41 = 0.7073170731707317073170731707',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_42(self):
        self.assertEqual(run_calculator('29', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/42 = 0.6904761904761904761904761905',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_43(self):
        self.assertEqual(run_calculator('29', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/43 = 0.6744186046511627906976744186',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_44(self):
        self.assertEqual(run_calculator('29', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/44 = 0.6590909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_45(self):
        self.assertEqual(run_calculator('29', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/45 = 0.6444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_46(self):
        self.assertEqual(run_calculator('29', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/46 = 0.6304347826086956521739130435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_47(self):
        self.assertEqual(run_calculator('29', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/47 = 0.6170212765957446808510638298',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_48(self):
        self.assertEqual(run_calculator('29', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/48 = 0.6041666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_49(self):
        self.assertEqual(run_calculator('29', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/49 = 0.5918367346938775510204081633',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_29_divided_by_50(self):
        self.assertEqual(run_calculator('29', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '29/50 = 0.58',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
