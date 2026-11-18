# test_divided_by_18.py
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


class TestDividedBy18(unittest.TestCase):

    def test_18_divided_by_0(self):
        self.assertEqual(run_calculator('18', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_1(self):
        self.assertEqual(run_calculator('18', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/1 = 18',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_2(self):
        self.assertEqual(run_calculator('18', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/2 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_3(self):
        self.assertEqual(run_calculator('18', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/3 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_4(self):
        self.assertEqual(run_calculator('18', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/4 = 4.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_5(self):
        self.assertEqual(run_calculator('18', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/5 = 3.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_6(self):
        self.assertEqual(run_calculator('18', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/6 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_7(self):
        self.assertEqual(run_calculator('18', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/7 = 2.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_8(self):
        self.assertEqual(run_calculator('18', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/8 = 2.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_9(self):
        self.assertEqual(run_calculator('18', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/9 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_10(self):
        self.assertEqual(run_calculator('18', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/10 = 1.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_11(self):
        self.assertEqual(run_calculator('18', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/11 = 1.636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_12(self):
        self.assertEqual(run_calculator('18', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/12 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_13(self):
        self.assertEqual(run_calculator('18', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/13 = 1.384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_14(self):
        self.assertEqual(run_calculator('18', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/14 = 1.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_15(self):
        self.assertEqual(run_calculator('18', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/15 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_16(self):
        self.assertEqual(run_calculator('18', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/16 = 1.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_17(self):
        self.assertEqual(run_calculator('18', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/17 = 1.058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_18(self):
        self.assertEqual(run_calculator('18', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/18 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_19(self):
        self.assertEqual(run_calculator('18', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/19 = 0.9473684210526315789473684211',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_20(self):
        self.assertEqual(run_calculator('18', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/20 = 0.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_21(self):
        self.assertEqual(run_calculator('18', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/21 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_22(self):
        self.assertEqual(run_calculator('18', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/22 = 0.8181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_23(self):
        self.assertEqual(run_calculator('18', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/23 = 0.7826086956521739130434782609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_24(self):
        self.assertEqual(run_calculator('18', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/24 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_25(self):
        self.assertEqual(run_calculator('18', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/25 = 0.72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_26(self):
        self.assertEqual(run_calculator('18', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/26 = 0.6923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_27(self):
        self.assertEqual(run_calculator('18', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/27 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_28(self):
        self.assertEqual(run_calculator('18', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/28 = 0.6428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_29(self):
        self.assertEqual(run_calculator('18', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/29 = 0.6206896551724137931034482759',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_30(self):
        self.assertEqual(run_calculator('18', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/30 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_31(self):
        self.assertEqual(run_calculator('18', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/31 = 0.5806451612903225806451612903',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_32(self):
        self.assertEqual(run_calculator('18', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/32 = 0.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_33(self):
        self.assertEqual(run_calculator('18', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/33 = 0.5454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_34(self):
        self.assertEqual(run_calculator('18', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/34 = 0.5294117647058823529411764706',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_35(self):
        self.assertEqual(run_calculator('18', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/35 = 0.5142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_36(self):
        self.assertEqual(run_calculator('18', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/36 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_37(self):
        self.assertEqual(run_calculator('18', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/37 = 0.4864864864864864864864864865',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_38(self):
        self.assertEqual(run_calculator('18', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/38 = 0.4736842105263157894736842105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_39(self):
        self.assertEqual(run_calculator('18', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/39 = 0.4615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_40(self):
        self.assertEqual(run_calculator('18', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/40 = 0.45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_41(self):
        self.assertEqual(run_calculator('18', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/41 = 0.4390243902439024390243902439',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_42(self):
        self.assertEqual(run_calculator('18', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/42 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_43(self):
        self.assertEqual(run_calculator('18', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/43 = 0.4186046511627906976744186047',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_44(self):
        self.assertEqual(run_calculator('18', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/44 = 0.4090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_45(self):
        self.assertEqual(run_calculator('18', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/45 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_46(self):
        self.assertEqual(run_calculator('18', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/46 = 0.3913043478260869565217391304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_47(self):
        self.assertEqual(run_calculator('18', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/47 = 0.3829787234042553191489361702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_48(self):
        self.assertEqual(run_calculator('18', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/48 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_49(self):
        self.assertEqual(run_calculator('18', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/49 = 0.3673469387755102040816326531',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_18_divided_by_50(self):
        self.assertEqual(run_calculator('18', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '18/50 = 0.36',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
