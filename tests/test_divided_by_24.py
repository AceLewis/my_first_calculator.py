# test_divided_by_24.py
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


class TestDividedBy24(unittest.TestCase):

    def test_24_divided_by_0(self):
        self.assertEqual(run_calculator('24', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_1(self):
        self.assertEqual(run_calculator('24', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/1 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_2(self):
        self.assertEqual(run_calculator('24', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/2 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_3(self):
        self.assertEqual(run_calculator('24', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/3 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_4(self):
        self.assertEqual(run_calculator('24', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/4 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_5(self):
        self.assertEqual(run_calculator('24', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/5 = 4.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_6(self):
        self.assertEqual(run_calculator('24', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/6 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_7(self):
        self.assertEqual(run_calculator('24', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/7 = 3.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_8(self):
        self.assertEqual(run_calculator('24', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/8 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_9(self):
        self.assertEqual(run_calculator('24', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/9 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_10(self):
        self.assertEqual(run_calculator('24', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/10 = 2.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_11(self):
        self.assertEqual(run_calculator('24', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/11 = 2.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_12(self):
        self.assertEqual(run_calculator('24', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/12 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_13(self):
        self.assertEqual(run_calculator('24', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/13 = 1.846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_14(self):
        self.assertEqual(run_calculator('24', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/14 = 1.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_15(self):
        self.assertEqual(run_calculator('24', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/15 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_16(self):
        self.assertEqual(run_calculator('24', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/16 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_17(self):
        self.assertEqual(run_calculator('24', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/17 = 1.411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_18(self):
        self.assertEqual(run_calculator('24', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/18 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_19(self):
        self.assertEqual(run_calculator('24', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/19 = 1.263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_20(self):
        self.assertEqual(run_calculator('24', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/20 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_21(self):
        self.assertEqual(run_calculator('24', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/21 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_22(self):
        self.assertEqual(run_calculator('24', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/22 = 1.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_23(self):
        self.assertEqual(run_calculator('24', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/23 = 1.043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_24(self):
        self.assertEqual(run_calculator('24', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/24 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_25(self):
        self.assertEqual(run_calculator('24', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/25 = 0.96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_26(self):
        self.assertEqual(run_calculator('24', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/26 = 0.9230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_27(self):
        self.assertEqual(run_calculator('24', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/27 = 0.8888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_28(self):
        self.assertEqual(run_calculator('24', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/28 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_29(self):
        self.assertEqual(run_calculator('24', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/29 = 0.8275862068965517241379310345',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_30(self):
        self.assertEqual(run_calculator('24', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/30 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_31(self):
        self.assertEqual(run_calculator('24', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/31 = 0.7741935483870967741935483871',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_32(self):
        self.assertEqual(run_calculator('24', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/32 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_33(self):
        self.assertEqual(run_calculator('24', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/33 = 0.7272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_34(self):
        self.assertEqual(run_calculator('24', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/34 = 0.7058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_35(self):
        self.assertEqual(run_calculator('24', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/35 = 0.6857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_36(self):
        self.assertEqual(run_calculator('24', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/36 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_37(self):
        self.assertEqual(run_calculator('24', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/37 = 0.6486486486486486486486486486',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_38(self):
        self.assertEqual(run_calculator('24', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/38 = 0.6315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_39(self):
        self.assertEqual(run_calculator('24', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/39 = 0.6153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_40(self):
        self.assertEqual(run_calculator('24', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/40 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_41(self):
        self.assertEqual(run_calculator('24', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/41 = 0.5853658536585365853658536585',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_42(self):
        self.assertEqual(run_calculator('24', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/42 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_43(self):
        self.assertEqual(run_calculator('24', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/43 = 0.5581395348837209302325581395',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_44(self):
        self.assertEqual(run_calculator('24', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/44 = 0.5454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_45(self):
        self.assertEqual(run_calculator('24', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/45 = 0.5333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_46(self):
        self.assertEqual(run_calculator('24', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/46 = 0.5217391304347826086956521739',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_47(self):
        self.assertEqual(run_calculator('24', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/47 = 0.5106382978723404255319148936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_48(self):
        self.assertEqual(run_calculator('24', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/48 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_49(self):
        self.assertEqual(run_calculator('24', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/49 = 0.4897959183673469387755102041',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_24_divided_by_50(self):
        self.assertEqual(run_calculator('24', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '24/50 = 0.48',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
