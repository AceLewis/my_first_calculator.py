# test_divided_by_1.py
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


class TestDividedBy1(unittest.TestCase):

    def test_1_divided_by_0(self):
        self.assertEqual(run_calculator('1', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_1(self):
        self.assertEqual(run_calculator('1', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/1 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_2(self):
        self.assertEqual(run_calculator('1', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/2 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_3(self):
        self.assertEqual(run_calculator('1', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/3 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_4(self):
        self.assertEqual(run_calculator('1', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/4 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_5(self):
        self.assertEqual(run_calculator('1', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/5 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_6(self):
        self.assertEqual(run_calculator('1', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/6 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_7(self):
        self.assertEqual(run_calculator('1', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/7 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_8(self):
        self.assertEqual(run_calculator('1', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/8 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_9(self):
        self.assertEqual(run_calculator('1', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/9 = 0.1111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_10(self):
        self.assertEqual(run_calculator('1', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/10 = 0.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_11(self):
        self.assertEqual(run_calculator('1', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/11 = 0.09090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_12(self):
        self.assertEqual(run_calculator('1', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/12 = 0.08333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_13(self):
        self.assertEqual(run_calculator('1', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/13 = 0.07692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_14(self):
        self.assertEqual(run_calculator('1', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/14 = 0.07142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_15(self):
        self.assertEqual(run_calculator('1', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/15 = 0.06666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_16(self):
        self.assertEqual(run_calculator('1', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/16 = 0.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_17(self):
        self.assertEqual(run_calculator('1', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/17 = 0.05882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_18(self):
        self.assertEqual(run_calculator('1', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/18 = 0.05555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_19(self):
        self.assertEqual(run_calculator('1', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/19 = 0.05263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_20(self):
        self.assertEqual(run_calculator('1', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/20 = 0.05',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_21(self):
        self.assertEqual(run_calculator('1', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/21 = 0.04761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_22(self):
        self.assertEqual(run_calculator('1', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/22 = 0.04545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_23(self):
        self.assertEqual(run_calculator('1', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/23 = 0.04347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_24(self):
        self.assertEqual(run_calculator('1', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/24 = 0.04166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_25(self):
        self.assertEqual(run_calculator('1', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/25 = 0.04',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_26(self):
        self.assertEqual(run_calculator('1', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/26 = 0.03846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_27(self):
        self.assertEqual(run_calculator('1', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/27 = 0.03703703703703703703703703704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_28(self):
        self.assertEqual(run_calculator('1', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/28 = 0.03571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_29(self):
        self.assertEqual(run_calculator('1', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/29 = 0.03448275862068965517241379310',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_30(self):
        self.assertEqual(run_calculator('1', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/30 = 0.03333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_31(self):
        self.assertEqual(run_calculator('1', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/31 = 0.03225806451612903225806451613',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_32(self):
        self.assertEqual(run_calculator('1', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/32 = 0.03125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_33(self):
        self.assertEqual(run_calculator('1', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/33 = 0.03030303030303030303030303030',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_34(self):
        self.assertEqual(run_calculator('1', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/34 = 0.02941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_35(self):
        self.assertEqual(run_calculator('1', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/35 = 0.02857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_36(self):
        self.assertEqual(run_calculator('1', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/36 = 0.02777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_37(self):
        self.assertEqual(run_calculator('1', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/37 = 0.02702702702702702702702702703',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_38(self):
        self.assertEqual(run_calculator('1', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/38 = 0.02631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_39(self):
        self.assertEqual(run_calculator('1', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/39 = 0.02564102564102564102564102564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_40(self):
        self.assertEqual(run_calculator('1', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/40 = 0.025',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_41(self):
        self.assertEqual(run_calculator('1', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/41 = 0.02439024390243902439024390244',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_42(self):
        self.assertEqual(run_calculator('1', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/42 = 0.02380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_43(self):
        self.assertEqual(run_calculator('1', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/43 = 0.02325581395348837209302325581',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_44(self):
        self.assertEqual(run_calculator('1', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/44 = 0.02272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_45(self):
        self.assertEqual(run_calculator('1', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/45 = 0.02222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_46(self):
        self.assertEqual(run_calculator('1', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/46 = 0.02173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_47(self):
        self.assertEqual(run_calculator('1', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/47 = 0.02127659574468085106382978723',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_48(self):
        self.assertEqual(run_calculator('1', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/48 = 0.02083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_49(self):
        self.assertEqual(run_calculator('1', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/49 = 0.02040816326530612244897959184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_1_divided_by_50(self):
        self.assertEqual(run_calculator('1', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '1/50 = 0.02',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
