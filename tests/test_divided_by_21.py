# test_divided_by_21.py
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


class TestDividedBy21(unittest.TestCase):

    def test_21_divided_by_0(self):
        self.assertEqual(run_calculator('21', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_1(self):
        self.assertEqual(run_calculator('21', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/1 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_2(self):
        self.assertEqual(run_calculator('21', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/2 = 10.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_3(self):
        self.assertEqual(run_calculator('21', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/3 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_4(self):
        self.assertEqual(run_calculator('21', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/4 = 5.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_5(self):
        self.assertEqual(run_calculator('21', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/5 = 4.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_6(self):
        self.assertEqual(run_calculator('21', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/6 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_7(self):
        self.assertEqual(run_calculator('21', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/7 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_8(self):
        self.assertEqual(run_calculator('21', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/8 = 2.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_9(self):
        self.assertEqual(run_calculator('21', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/9 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_10(self):
        self.assertEqual(run_calculator('21', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/10 = 2.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_11(self):
        self.assertEqual(run_calculator('21', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/11 = 1.909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_12(self):
        self.assertEqual(run_calculator('21', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/12 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_13(self):
        self.assertEqual(run_calculator('21', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/13 = 1.615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_14(self):
        self.assertEqual(run_calculator('21', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/14 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_15(self):
        self.assertEqual(run_calculator('21', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/15 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_16(self):
        self.assertEqual(run_calculator('21', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/16 = 1.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_17(self):
        self.assertEqual(run_calculator('21', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/17 = 1.235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_18(self):
        self.assertEqual(run_calculator('21', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/18 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_19(self):
        self.assertEqual(run_calculator('21', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/19 = 1.105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_20(self):
        self.assertEqual(run_calculator('21', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/20 = 1.05',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_21(self):
        self.assertEqual(run_calculator('21', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/21 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_22(self):
        self.assertEqual(run_calculator('21', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/22 = 0.9545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_23(self):
        self.assertEqual(run_calculator('21', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/23 = 0.9130434782608695652173913043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_24(self):
        self.assertEqual(run_calculator('21', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/24 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_25(self):
        self.assertEqual(run_calculator('21', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/25 = 0.84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_26(self):
        self.assertEqual(run_calculator('21', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/26 = 0.8076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_27(self):
        self.assertEqual(run_calculator('21', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/27 = 0.7777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_28(self):
        self.assertEqual(run_calculator('21', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/28 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_29(self):
        self.assertEqual(run_calculator('21', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/29 = 0.7241379310344827586206896552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_30(self):
        self.assertEqual(run_calculator('21', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/30 = 0.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_31(self):
        self.assertEqual(run_calculator('21', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/31 = 0.6774193548387096774193548387',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_32(self):
        self.assertEqual(run_calculator('21', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/32 = 0.65625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_33(self):
        self.assertEqual(run_calculator('21', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/33 = 0.6363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_34(self):
        self.assertEqual(run_calculator('21', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/34 = 0.6176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_35(self):
        self.assertEqual(run_calculator('21', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/35 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_36(self):
        self.assertEqual(run_calculator('21', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/36 = 0.5833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_37(self):
        self.assertEqual(run_calculator('21', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/37 = 0.5675675675675675675675675676',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_38(self):
        self.assertEqual(run_calculator('21', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/38 = 0.5526315789473684210526315789',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_39(self):
        self.assertEqual(run_calculator('21', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/39 = 0.5384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_40(self):
        self.assertEqual(run_calculator('21', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/40 = 0.525',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_41(self):
        self.assertEqual(run_calculator('21', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/41 = 0.5121951219512195121951219512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_42(self):
        self.assertEqual(run_calculator('21', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/42 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_43(self):
        self.assertEqual(run_calculator('21', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/43 = 0.4883720930232558139534883721',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_44(self):
        self.assertEqual(run_calculator('21', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/44 = 0.4772727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_45(self):
        self.assertEqual(run_calculator('21', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/45 = 0.4666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_46(self):
        self.assertEqual(run_calculator('21', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/46 = 0.4565217391304347826086956522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_47(self):
        self.assertEqual(run_calculator('21', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/47 = 0.4468085106382978723404255319',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_48(self):
        self.assertEqual(run_calculator('21', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/48 = 0.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_49(self):
        self.assertEqual(run_calculator('21', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/49 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_21_divided_by_50(self):
        self.assertEqual(run_calculator('21', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '21/50 = 0.42',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
