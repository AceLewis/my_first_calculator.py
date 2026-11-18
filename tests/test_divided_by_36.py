# test_divided_by_36.py
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


class TestDividedBy36(unittest.TestCase):

    def test_36_divided_by_0(self):
        self.assertEqual(run_calculator('36', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_1(self):
        self.assertEqual(run_calculator('36', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/1 = 36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_2(self):
        self.assertEqual(run_calculator('36', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/2 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_3(self):
        self.assertEqual(run_calculator('36', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/3 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_4(self):
        self.assertEqual(run_calculator('36', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/4 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_5(self):
        self.assertEqual(run_calculator('36', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/5 = 7.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_6(self):
        self.assertEqual(run_calculator('36', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/6 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_7(self):
        self.assertEqual(run_calculator('36', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/7 = 5.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_8(self):
        self.assertEqual(run_calculator('36', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/8 = 4.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_9(self):
        self.assertEqual(run_calculator('36', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/9 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_10(self):
        self.assertEqual(run_calculator('36', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/10 = 3.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_11(self):
        self.assertEqual(run_calculator('36', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/11 = 3.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_12(self):
        self.assertEqual(run_calculator('36', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/12 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_13(self):
        self.assertEqual(run_calculator('36', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/13 = 2.769230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_14(self):
        self.assertEqual(run_calculator('36', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/14 = 2.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_15(self):
        self.assertEqual(run_calculator('36', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/15 = 2.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_16(self):
        self.assertEqual(run_calculator('36', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/16 = 2.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_17(self):
        self.assertEqual(run_calculator('36', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/17 = 2.117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_18(self):
        self.assertEqual(run_calculator('36', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/18 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_19(self):
        self.assertEqual(run_calculator('36', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/19 = 1.894736842105263157894736842',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_20(self):
        self.assertEqual(run_calculator('36', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/20 = 1.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_21(self):
        self.assertEqual(run_calculator('36', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/21 = 1.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_22(self):
        self.assertEqual(run_calculator('36', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/22 = 1.636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_23(self):
        self.assertEqual(run_calculator('36', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/23 = 1.565217391304347826086956522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_24(self):
        self.assertEqual(run_calculator('36', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/24 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_25(self):
        self.assertEqual(run_calculator('36', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/25 = 1.44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_26(self):
        self.assertEqual(run_calculator('36', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/26 = 1.384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_27(self):
        self.assertEqual(run_calculator('36', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/27 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_28(self):
        self.assertEqual(run_calculator('36', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/28 = 1.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_29(self):
        self.assertEqual(run_calculator('36', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/29 = 1.241379310344827586206896552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_30(self):
        self.assertEqual(run_calculator('36', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/30 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_31(self):
        self.assertEqual(run_calculator('36', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/31 = 1.161290322580645161290322581',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_32(self):
        self.assertEqual(run_calculator('36', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/32 = 1.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_33(self):
        self.assertEqual(run_calculator('36', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/33 = 1.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_34(self):
        self.assertEqual(run_calculator('36', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/34 = 1.058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_35(self):
        self.assertEqual(run_calculator('36', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/35 = 1.028571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_36(self):
        self.assertEqual(run_calculator('36', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/36 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_37(self):
        self.assertEqual(run_calculator('36', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/37 = 0.9729729729729729729729729730',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_38(self):
        self.assertEqual(run_calculator('36', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/38 = 0.9473684210526315789473684211',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_39(self):
        self.assertEqual(run_calculator('36', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/39 = 0.9230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_40(self):
        self.assertEqual(run_calculator('36', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/40 = 0.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_41(self):
        self.assertEqual(run_calculator('36', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/41 = 0.8780487804878048780487804878',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_42(self):
        self.assertEqual(run_calculator('36', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/42 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_43(self):
        self.assertEqual(run_calculator('36', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/43 = 0.8372093023255813953488372093',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_44(self):
        self.assertEqual(run_calculator('36', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/44 = 0.8181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_45(self):
        self.assertEqual(run_calculator('36', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/45 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_46(self):
        self.assertEqual(run_calculator('36', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/46 = 0.7826086956521739130434782609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_47(self):
        self.assertEqual(run_calculator('36', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/47 = 0.7659574468085106382978723404',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_48(self):
        self.assertEqual(run_calculator('36', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/48 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_49(self):
        self.assertEqual(run_calculator('36', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/49 = 0.7346938775510204081632653061',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_36_divided_by_50(self):
        self.assertEqual(run_calculator('36', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '36/50 = 0.72',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
