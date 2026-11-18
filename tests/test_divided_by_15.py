# test_divided_by_15.py
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


class TestDividedBy15(unittest.TestCase):

    def test_15_divided_by_0(self):
        self.assertEqual(run_calculator('15', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_1(self):
        self.assertEqual(run_calculator('15', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/1 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_2(self):
        self.assertEqual(run_calculator('15', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/2 = 7.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_3(self):
        self.assertEqual(run_calculator('15', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/3 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_4(self):
        self.assertEqual(run_calculator('15', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/4 = 3.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_5(self):
        self.assertEqual(run_calculator('15', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/5 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_6(self):
        self.assertEqual(run_calculator('15', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/6 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_7(self):
        self.assertEqual(run_calculator('15', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/7 = 2.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_8(self):
        self.assertEqual(run_calculator('15', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/8 = 1.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_9(self):
        self.assertEqual(run_calculator('15', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/9 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_10(self):
        self.assertEqual(run_calculator('15', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/10 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_11(self):
        self.assertEqual(run_calculator('15', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/11 = 1.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_12(self):
        self.assertEqual(run_calculator('15', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/12 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_13(self):
        self.assertEqual(run_calculator('15', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/13 = 1.153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_14(self):
        self.assertEqual(run_calculator('15', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/14 = 1.071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_15(self):
        self.assertEqual(run_calculator('15', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/15 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_16(self):
        self.assertEqual(run_calculator('15', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/16 = 0.9375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_17(self):
        self.assertEqual(run_calculator('15', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/17 = 0.8823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_18(self):
        self.assertEqual(run_calculator('15', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/18 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_19(self):
        self.assertEqual(run_calculator('15', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/19 = 0.7894736842105263157894736842',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_20(self):
        self.assertEqual(run_calculator('15', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/20 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_21(self):
        self.assertEqual(run_calculator('15', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/21 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_22(self):
        self.assertEqual(run_calculator('15', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/22 = 0.6818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_23(self):
        self.assertEqual(run_calculator('15', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/23 = 0.6521739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_24(self):
        self.assertEqual(run_calculator('15', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/24 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_25(self):
        self.assertEqual(run_calculator('15', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/25 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_26(self):
        self.assertEqual(run_calculator('15', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/26 = 0.5769230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_27(self):
        self.assertEqual(run_calculator('15', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/27 = 0.5555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_28(self):
        self.assertEqual(run_calculator('15', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/28 = 0.5357142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_29(self):
        self.assertEqual(run_calculator('15', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/29 = 0.5172413793103448275862068966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_30(self):
        self.assertEqual(run_calculator('15', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/30 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_31(self):
        self.assertEqual(run_calculator('15', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/31 = 0.4838709677419354838709677419',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_32(self):
        self.assertEqual(run_calculator('15', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/32 = 0.46875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_33(self):
        self.assertEqual(run_calculator('15', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/33 = 0.4545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_34(self):
        self.assertEqual(run_calculator('15', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/34 = 0.4411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_35(self):
        self.assertEqual(run_calculator('15', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/35 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_36(self):
        self.assertEqual(run_calculator('15', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/36 = 0.4166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_37(self):
        self.assertEqual(run_calculator('15', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/37 = 0.4054054054054054054054054054',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_38(self):
        self.assertEqual(run_calculator('15', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/38 = 0.3947368421052631578947368421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_39(self):
        self.assertEqual(run_calculator('15', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/39 = 0.3846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_40(self):
        self.assertEqual(run_calculator('15', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/40 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_41(self):
        self.assertEqual(run_calculator('15', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/41 = 0.3658536585365853658536585366',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_42(self):
        self.assertEqual(run_calculator('15', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/42 = 0.3571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_43(self):
        self.assertEqual(run_calculator('15', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/43 = 0.3488372093023255813953488372',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_44(self):
        self.assertEqual(run_calculator('15', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/44 = 0.3409090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_45(self):
        self.assertEqual(run_calculator('15', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/45 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_46(self):
        self.assertEqual(run_calculator('15', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/46 = 0.3260869565217391304347826087',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_47(self):
        self.assertEqual(run_calculator('15', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/47 = 0.3191489361702127659574468085',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_48(self):
        self.assertEqual(run_calculator('15', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/48 = 0.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_49(self):
        self.assertEqual(run_calculator('15', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/49 = 0.3061224489795918367346938776',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_15_divided_by_50(self):
        self.assertEqual(run_calculator('15', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '15/50 = 0.3',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
