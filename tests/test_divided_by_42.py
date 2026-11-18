# test_divided_by_42.py
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


class TestDividedBy42(unittest.TestCase):

    def test_42_divided_by_0(self):
        self.assertEqual(run_calculator('42', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_1(self):
        self.assertEqual(run_calculator('42', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/1 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_2(self):
        self.assertEqual(run_calculator('42', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/2 = 21',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_3(self):
        self.assertEqual(run_calculator('42', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/3 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_4(self):
        self.assertEqual(run_calculator('42', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/4 = 10.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_5(self):
        self.assertEqual(run_calculator('42', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/5 = 8.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_6(self):
        self.assertEqual(run_calculator('42', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/6 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_7(self):
        self.assertEqual(run_calculator('42', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/7 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_8(self):
        self.assertEqual(run_calculator('42', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/8 = 5.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_9(self):
        self.assertEqual(run_calculator('42', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/9 = 4.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_10(self):
        self.assertEqual(run_calculator('42', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/10 = 4.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_11(self):
        self.assertEqual(run_calculator('42', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/11 = 3.818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_12(self):
        self.assertEqual(run_calculator('42', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/12 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_13(self):
        self.assertEqual(run_calculator('42', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/13 = 3.230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_14(self):
        self.assertEqual(run_calculator('42', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/14 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_15(self):
        self.assertEqual(run_calculator('42', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/15 = 2.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_16(self):
        self.assertEqual(run_calculator('42', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/16 = 2.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_17(self):
        self.assertEqual(run_calculator('42', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/17 = 2.470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_18(self):
        self.assertEqual(run_calculator('42', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/18 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_19(self):
        self.assertEqual(run_calculator('42', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/19 = 2.210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_20(self):
        self.assertEqual(run_calculator('42', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/20 = 2.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_21(self):
        self.assertEqual(run_calculator('42', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/21 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_22(self):
        self.assertEqual(run_calculator('42', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/22 = 1.909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_23(self):
        self.assertEqual(run_calculator('42', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/23 = 1.826086956521739130434782609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_24(self):
        self.assertEqual(run_calculator('42', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/24 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_25(self):
        self.assertEqual(run_calculator('42', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/25 = 1.68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_26(self):
        self.assertEqual(run_calculator('42', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/26 = 1.615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_27(self):
        self.assertEqual(run_calculator('42', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/27 = 1.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_28(self):
        self.assertEqual(run_calculator('42', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/28 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_29(self):
        self.assertEqual(run_calculator('42', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/29 = 1.448275862068965517241379310',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_30(self):
        self.assertEqual(run_calculator('42', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/30 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_31(self):
        self.assertEqual(run_calculator('42', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/31 = 1.354838709677419354838709677',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_32(self):
        self.assertEqual(run_calculator('42', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/32 = 1.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_33(self):
        self.assertEqual(run_calculator('42', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/33 = 1.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_34(self):
        self.assertEqual(run_calculator('42', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/34 = 1.235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_35(self):
        self.assertEqual(run_calculator('42', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/35 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_36(self):
        self.assertEqual(run_calculator('42', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/36 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_37(self):
        self.assertEqual(run_calculator('42', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/37 = 1.135135135135135135135135135',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_38(self):
        self.assertEqual(run_calculator('42', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/38 = 1.105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_39(self):
        self.assertEqual(run_calculator('42', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/39 = 1.076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_40(self):
        self.assertEqual(run_calculator('42', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/40 = 1.05',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_41(self):
        self.assertEqual(run_calculator('42', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/41 = 1.024390243902439024390243902',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_42(self):
        self.assertEqual(run_calculator('42', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/42 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_43(self):
        self.assertEqual(run_calculator('42', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/43 = 0.9767441860465116279069767442',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_44(self):
        self.assertEqual(run_calculator('42', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/44 = 0.9545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_45(self):
        self.assertEqual(run_calculator('42', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/45 = 0.9333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_46(self):
        self.assertEqual(run_calculator('42', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/46 = 0.9130434782608695652173913043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_47(self):
        self.assertEqual(run_calculator('42', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/47 = 0.8936170212765957446808510638',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_48(self):
        self.assertEqual(run_calculator('42', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/48 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_49(self):
        self.assertEqual(run_calculator('42', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/49 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_42_divided_by_50(self):
        self.assertEqual(run_calculator('42', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '42/50 = 0.84',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
