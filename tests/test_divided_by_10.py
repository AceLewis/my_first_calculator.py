# test_divided_by_10.py
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


class TestDividedBy10(unittest.TestCase):

    def test_10_divided_by_0(self):
        self.assertEqual(run_calculator('10', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_1(self):
        self.assertEqual(run_calculator('10', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/1 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_2(self):
        self.assertEqual(run_calculator('10', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/2 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_3(self):
        self.assertEqual(run_calculator('10', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/3 = 3.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_4(self):
        self.assertEqual(run_calculator('10', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/4 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_5(self):
        self.assertEqual(run_calculator('10', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/5 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_6(self):
        self.assertEqual(run_calculator('10', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/6 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_7(self):
        self.assertEqual(run_calculator('10', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/7 = 1.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_8(self):
        self.assertEqual(run_calculator('10', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/8 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_9(self):
        self.assertEqual(run_calculator('10', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/9 = 1.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_10(self):
        self.assertEqual(run_calculator('10', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/10 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_11(self):
        self.assertEqual(run_calculator('10', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/11 = 0.9090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_12(self):
        self.assertEqual(run_calculator('10', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/12 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_13(self):
        self.assertEqual(run_calculator('10', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/13 = 0.7692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_14(self):
        self.assertEqual(run_calculator('10', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/14 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_15(self):
        self.assertEqual(run_calculator('10', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/15 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_16(self):
        self.assertEqual(run_calculator('10', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/16 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_17(self):
        self.assertEqual(run_calculator('10', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/17 = 0.5882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_18(self):
        self.assertEqual(run_calculator('10', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/18 = 0.5555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_19(self):
        self.assertEqual(run_calculator('10', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/19 = 0.5263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_20(self):
        self.assertEqual(run_calculator('10', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/20 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_21(self):
        self.assertEqual(run_calculator('10', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/21 = 0.4761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_22(self):
        self.assertEqual(run_calculator('10', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/22 = 0.4545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_23(self):
        self.assertEqual(run_calculator('10', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/23 = 0.4347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_24(self):
        self.assertEqual(run_calculator('10', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/24 = 0.4166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_25(self):
        self.assertEqual(run_calculator('10', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/25 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_26(self):
        self.assertEqual(run_calculator('10', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/26 = 0.3846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_27(self):
        self.assertEqual(run_calculator('10', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/27 = 0.3703703703703703703703703704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_28(self):
        self.assertEqual(run_calculator('10', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/28 = 0.3571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_29(self):
        self.assertEqual(run_calculator('10', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/29 = 0.3448275862068965517241379310',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_30(self):
        self.assertEqual(run_calculator('10', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/30 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_31(self):
        self.assertEqual(run_calculator('10', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/31 = 0.3225806451612903225806451613',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_32(self):
        self.assertEqual(run_calculator('10', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/32 = 0.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_33(self):
        self.assertEqual(run_calculator('10', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/33 = 0.3030303030303030303030303030',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_34(self):
        self.assertEqual(run_calculator('10', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/34 = 0.2941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_35(self):
        self.assertEqual(run_calculator('10', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/35 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_36(self):
        self.assertEqual(run_calculator('10', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/36 = 0.2777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_37(self):
        self.assertEqual(run_calculator('10', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/37 = 0.2702702702702702702702702703',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_38(self):
        self.assertEqual(run_calculator('10', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/38 = 0.2631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_39(self):
        self.assertEqual(run_calculator('10', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/39 = 0.2564102564102564102564102564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_40(self):
        self.assertEqual(run_calculator('10', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/40 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_41(self):
        self.assertEqual(run_calculator('10', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/41 = 0.2439024390243902439024390244',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_42(self):
        self.assertEqual(run_calculator('10', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/42 = 0.2380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_43(self):
        self.assertEqual(run_calculator('10', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/43 = 0.2325581395348837209302325581',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_44(self):
        self.assertEqual(run_calculator('10', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/44 = 0.2272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_45(self):
        self.assertEqual(run_calculator('10', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/45 = 0.2222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_46(self):
        self.assertEqual(run_calculator('10', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/46 = 0.2173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_47(self):
        self.assertEqual(run_calculator('10', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/47 = 0.2127659574468085106382978723',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_48(self):
        self.assertEqual(run_calculator('10', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/48 = 0.2083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_49(self):
        self.assertEqual(run_calculator('10', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/49 = 0.2040816326530612244897959184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_10_divided_by_50(self):
        self.assertEqual(run_calculator('10', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '10/50 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
