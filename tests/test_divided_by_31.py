# test_divided_by_31.py
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


class TestDividedBy31(unittest.TestCase):

    def test_31_divided_by_0(self):
        self.assertEqual(run_calculator('31', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_1(self):
        self.assertEqual(run_calculator('31', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/1 = 31',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_2(self):
        self.assertEqual(run_calculator('31', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/2 = 15.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_3(self):
        self.assertEqual(run_calculator('31', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/3 = 10.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_4(self):
        self.assertEqual(run_calculator('31', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/4 = 7.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_5(self):
        self.assertEqual(run_calculator('31', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/5 = 6.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_6(self):
        self.assertEqual(run_calculator('31', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/6 = 5.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_7(self):
        self.assertEqual(run_calculator('31', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/7 = 4.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_8(self):
        self.assertEqual(run_calculator('31', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/8 = 3.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_9(self):
        self.assertEqual(run_calculator('31', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/9 = 3.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_10(self):
        self.assertEqual(run_calculator('31', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/10 = 3.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_11(self):
        self.assertEqual(run_calculator('31', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/11 = 2.818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_12(self):
        self.assertEqual(run_calculator('31', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/12 = 2.583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_13(self):
        self.assertEqual(run_calculator('31', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/13 = 2.384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_14(self):
        self.assertEqual(run_calculator('31', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/14 = 2.214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_15(self):
        self.assertEqual(run_calculator('31', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/15 = 2.066666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_16(self):
        self.assertEqual(run_calculator('31', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/16 = 1.9375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_17(self):
        self.assertEqual(run_calculator('31', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/17 = 1.823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_18(self):
        self.assertEqual(run_calculator('31', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/18 = 1.722222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_19(self):
        self.assertEqual(run_calculator('31', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/19 = 1.631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_20(self):
        self.assertEqual(run_calculator('31', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/20 = 1.55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_21(self):
        self.assertEqual(run_calculator('31', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/21 = 1.476190476190476190476190476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_22(self):
        self.assertEqual(run_calculator('31', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/22 = 1.409090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_23(self):
        self.assertEqual(run_calculator('31', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/23 = 1.347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_24(self):
        self.assertEqual(run_calculator('31', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/24 = 1.291666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_25(self):
        self.assertEqual(run_calculator('31', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/25 = 1.24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_26(self):
        self.assertEqual(run_calculator('31', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/26 = 1.192307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_27(self):
        self.assertEqual(run_calculator('31', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/27 = 1.148148148148148148148148148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_28(self):
        self.assertEqual(run_calculator('31', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/28 = 1.107142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_29(self):
        self.assertEqual(run_calculator('31', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/29 = 1.068965517241379310344827586',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_30(self):
        self.assertEqual(run_calculator('31', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/30 = 1.033333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_31(self):
        self.assertEqual(run_calculator('31', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/31 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_32(self):
        self.assertEqual(run_calculator('31', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/32 = 0.96875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_33(self):
        self.assertEqual(run_calculator('31', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/33 = 0.9393939393939393939393939394',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_34(self):
        self.assertEqual(run_calculator('31', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/34 = 0.9117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_35(self):
        self.assertEqual(run_calculator('31', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/35 = 0.8857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_36(self):
        self.assertEqual(run_calculator('31', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/36 = 0.8611111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_37(self):
        self.assertEqual(run_calculator('31', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/37 = 0.8378378378378378378378378378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_38(self):
        self.assertEqual(run_calculator('31', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/38 = 0.8157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_39(self):
        self.assertEqual(run_calculator('31', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/39 = 0.7948717948717948717948717949',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_40(self):
        self.assertEqual(run_calculator('31', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/40 = 0.775',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_41(self):
        self.assertEqual(run_calculator('31', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/41 = 0.7560975609756097560975609756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_42(self):
        self.assertEqual(run_calculator('31', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/42 = 0.7380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_43(self):
        self.assertEqual(run_calculator('31', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/43 = 0.7209302325581395348837209302',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_44(self):
        self.assertEqual(run_calculator('31', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/44 = 0.7045454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_45(self):
        self.assertEqual(run_calculator('31', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/45 = 0.6888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_46(self):
        self.assertEqual(run_calculator('31', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/46 = 0.6739130434782608695652173913',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_47(self):
        self.assertEqual(run_calculator('31', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/47 = 0.6595744680851063829787234043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_48(self):
        self.assertEqual(run_calculator('31', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/48 = 0.6458333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_49(self):
        self.assertEqual(run_calculator('31', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/49 = 0.6326530612244897959183673469',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_31_divided_by_50(self):
        self.assertEqual(run_calculator('31', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '31/50 = 0.62',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
