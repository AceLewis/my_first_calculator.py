# test_divided_by_11.py
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


class TestDividedBy11(unittest.TestCase):

    def test_11_divided_by_0(self):
        self.assertEqual(run_calculator('11', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_1(self):
        self.assertEqual(run_calculator('11', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/1 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_2(self):
        self.assertEqual(run_calculator('11', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/2 = 5.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_3(self):
        self.assertEqual(run_calculator('11', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/3 = 3.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_4(self):
        self.assertEqual(run_calculator('11', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/4 = 2.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_5(self):
        self.assertEqual(run_calculator('11', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/5 = 2.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_6(self):
        self.assertEqual(run_calculator('11', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/6 = 1.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_7(self):
        self.assertEqual(run_calculator('11', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/7 = 1.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_8(self):
        self.assertEqual(run_calculator('11', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/8 = 1.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_9(self):
        self.assertEqual(run_calculator('11', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/9 = 1.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_10(self):
        self.assertEqual(run_calculator('11', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/10 = 1.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_11(self):
        self.assertEqual(run_calculator('11', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/11 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_12(self):
        self.assertEqual(run_calculator('11', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/12 = 0.9166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_13(self):
        self.assertEqual(run_calculator('11', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/13 = 0.8461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_14(self):
        self.assertEqual(run_calculator('11', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/14 = 0.7857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_15(self):
        self.assertEqual(run_calculator('11', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/15 = 0.7333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_16(self):
        self.assertEqual(run_calculator('11', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/16 = 0.6875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_17(self):
        self.assertEqual(run_calculator('11', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/17 = 0.6470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_18(self):
        self.assertEqual(run_calculator('11', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/18 = 0.6111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_19(self):
        self.assertEqual(run_calculator('11', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/19 = 0.5789473684210526315789473684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_20(self):
        self.assertEqual(run_calculator('11', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/20 = 0.55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_21(self):
        self.assertEqual(run_calculator('11', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/21 = 0.5238095238095238095238095238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_22(self):
        self.assertEqual(run_calculator('11', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/22 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_23(self):
        self.assertEqual(run_calculator('11', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/23 = 0.4782608695652173913043478261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_24(self):
        self.assertEqual(run_calculator('11', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/24 = 0.4583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_25(self):
        self.assertEqual(run_calculator('11', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/25 = 0.44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_26(self):
        self.assertEqual(run_calculator('11', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/26 = 0.4230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_27(self):
        self.assertEqual(run_calculator('11', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/27 = 0.4074074074074074074074074074',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_28(self):
        self.assertEqual(run_calculator('11', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/28 = 0.3928571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_29(self):
        self.assertEqual(run_calculator('11', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/29 = 0.3793103448275862068965517241',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_30(self):
        self.assertEqual(run_calculator('11', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/30 = 0.3666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_31(self):
        self.assertEqual(run_calculator('11', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/31 = 0.3548387096774193548387096774',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_32(self):
        self.assertEqual(run_calculator('11', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/32 = 0.34375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_33(self):
        self.assertEqual(run_calculator('11', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/33 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_34(self):
        self.assertEqual(run_calculator('11', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/34 = 0.3235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_35(self):
        self.assertEqual(run_calculator('11', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/35 = 0.3142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_36(self):
        self.assertEqual(run_calculator('11', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/36 = 0.3055555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_37(self):
        self.assertEqual(run_calculator('11', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/37 = 0.2972972972972972972972972973',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_38(self):
        self.assertEqual(run_calculator('11', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/38 = 0.2894736842105263157894736842',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_39(self):
        self.assertEqual(run_calculator('11', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/39 = 0.2820512820512820512820512821',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_40(self):
        self.assertEqual(run_calculator('11', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/40 = 0.275',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_41(self):
        self.assertEqual(run_calculator('11', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/41 = 0.2682926829268292682926829268',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_42(self):
        self.assertEqual(run_calculator('11', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/42 = 0.2619047619047619047619047619',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_43(self):
        self.assertEqual(run_calculator('11', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/43 = 0.2558139534883720930232558140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_44(self):
        self.assertEqual(run_calculator('11', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/44 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_45(self):
        self.assertEqual(run_calculator('11', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/45 = 0.2444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_46(self):
        self.assertEqual(run_calculator('11', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/46 = 0.2391304347826086956521739130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_47(self):
        self.assertEqual(run_calculator('11', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/47 = 0.2340425531914893617021276596',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_48(self):
        self.assertEqual(run_calculator('11', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/48 = 0.2291666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_49(self):
        self.assertEqual(run_calculator('11', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/49 = 0.2244897959183673469387755102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_divided_by_50(self):
        self.assertEqual(run_calculator('11', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11/50 = 0.22',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
