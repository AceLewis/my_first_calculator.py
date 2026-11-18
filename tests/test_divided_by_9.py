# test_divided_by_9.py
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


class TestDividedBy9(unittest.TestCase):

    def test_9_divided_by_0(self):
        self.assertEqual(run_calculator('9', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_1(self):
        self.assertEqual(run_calculator('9', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/1 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_2(self):
        self.assertEqual(run_calculator('9', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/2 = 4.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_3(self):
        self.assertEqual(run_calculator('9', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/3 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_4(self):
        self.assertEqual(run_calculator('9', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/4 = 2.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_5(self):
        self.assertEqual(run_calculator('9', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/5 = 1.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_6(self):
        self.assertEqual(run_calculator('9', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/6 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_7(self):
        self.assertEqual(run_calculator('9', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/7 = 1.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_8(self):
        self.assertEqual(run_calculator('9', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/8 = 1.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_9(self):
        self.assertEqual(run_calculator('9', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/9 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_10(self):
        self.assertEqual(run_calculator('9', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/10 = 0.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_11(self):
        self.assertEqual(run_calculator('9', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/11 = 0.8181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_12(self):
        self.assertEqual(run_calculator('9', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/12 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_13(self):
        self.assertEqual(run_calculator('9', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/13 = 0.6923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_14(self):
        self.assertEqual(run_calculator('9', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/14 = 0.6428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_15(self):
        self.assertEqual(run_calculator('9', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/15 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_16(self):
        self.assertEqual(run_calculator('9', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/16 = 0.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_17(self):
        self.assertEqual(run_calculator('9', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/17 = 0.5294117647058823529411764706',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_18(self):
        self.assertEqual(run_calculator('9', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/18 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_19(self):
        self.assertEqual(run_calculator('9', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/19 = 0.4736842105263157894736842105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_20(self):
        self.assertEqual(run_calculator('9', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/20 = 0.45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_21(self):
        self.assertEqual(run_calculator('9', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/21 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_22(self):
        self.assertEqual(run_calculator('9', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/22 = 0.4090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_23(self):
        self.assertEqual(run_calculator('9', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/23 = 0.3913043478260869565217391304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_24(self):
        self.assertEqual(run_calculator('9', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/24 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_25(self):
        self.assertEqual(run_calculator('9', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/25 = 0.36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_26(self):
        self.assertEqual(run_calculator('9', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/26 = 0.3461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_27(self):
        self.assertEqual(run_calculator('9', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/27 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_28(self):
        self.assertEqual(run_calculator('9', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/28 = 0.3214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_29(self):
        self.assertEqual(run_calculator('9', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/29 = 0.3103448275862068965517241379',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_30(self):
        self.assertEqual(run_calculator('9', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/30 = 0.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_31(self):
        self.assertEqual(run_calculator('9', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/31 = 0.2903225806451612903225806452',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_32(self):
        self.assertEqual(run_calculator('9', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/32 = 0.28125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_33(self):
        self.assertEqual(run_calculator('9', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/33 = 0.2727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_34(self):
        self.assertEqual(run_calculator('9', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/34 = 0.2647058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_35(self):
        self.assertEqual(run_calculator('9', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/35 = 0.2571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_36(self):
        self.assertEqual(run_calculator('9', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/36 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_37(self):
        self.assertEqual(run_calculator('9', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/37 = 0.2432432432432432432432432432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_38(self):
        self.assertEqual(run_calculator('9', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/38 = 0.2368421052631578947368421053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_39(self):
        self.assertEqual(run_calculator('9', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/39 = 0.2307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_40(self):
        self.assertEqual(run_calculator('9', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/40 = 0.225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_41(self):
        self.assertEqual(run_calculator('9', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/41 = 0.2195121951219512195121951220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_42(self):
        self.assertEqual(run_calculator('9', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/42 = 0.2142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_43(self):
        self.assertEqual(run_calculator('9', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/43 = 0.2093023255813953488372093023',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_44(self):
        self.assertEqual(run_calculator('9', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/44 = 0.2045454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_45(self):
        self.assertEqual(run_calculator('9', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/45 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_46(self):
        self.assertEqual(run_calculator('9', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/46 = 0.1956521739130434782608695652',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_47(self):
        self.assertEqual(run_calculator('9', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/47 = 0.1914893617021276595744680851',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_48(self):
        self.assertEqual(run_calculator('9', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/48 = 0.1875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_49(self):
        self.assertEqual(run_calculator('9', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/49 = 0.1836734693877551020408163265',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_9_divided_by_50(self):
        self.assertEqual(run_calculator('9', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '9/50 = 0.18',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
