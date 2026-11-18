# test_divided_by_48.py
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


class TestDividedBy48(unittest.TestCase):

    def test_48_divided_by_0(self):
        self.assertEqual(run_calculator('48', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_1(self):
        self.assertEqual(run_calculator('48', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/1 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_2(self):
        self.assertEqual(run_calculator('48', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/2 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_3(self):
        self.assertEqual(run_calculator('48', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/3 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_4(self):
        self.assertEqual(run_calculator('48', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/4 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_5(self):
        self.assertEqual(run_calculator('48', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/5 = 9.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_6(self):
        self.assertEqual(run_calculator('48', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/6 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_7(self):
        self.assertEqual(run_calculator('48', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/7 = 6.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_8(self):
        self.assertEqual(run_calculator('48', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/8 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_9(self):
        self.assertEqual(run_calculator('48', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/9 = 5.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_10(self):
        self.assertEqual(run_calculator('48', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/10 = 4.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_11(self):
        self.assertEqual(run_calculator('48', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/11 = 4.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_12(self):
        self.assertEqual(run_calculator('48', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/12 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_13(self):
        self.assertEqual(run_calculator('48', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/13 = 3.692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_14(self):
        self.assertEqual(run_calculator('48', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/14 = 3.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_15(self):
        self.assertEqual(run_calculator('48', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/15 = 3.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_16(self):
        self.assertEqual(run_calculator('48', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/16 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_17(self):
        self.assertEqual(run_calculator('48', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/17 = 2.823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_18(self):
        self.assertEqual(run_calculator('48', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/18 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_19(self):
        self.assertEqual(run_calculator('48', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/19 = 2.526315789473684210526315789',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_20(self):
        self.assertEqual(run_calculator('48', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/20 = 2.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_21(self):
        self.assertEqual(run_calculator('48', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/21 = 2.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_22(self):
        self.assertEqual(run_calculator('48', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/22 = 2.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_23(self):
        self.assertEqual(run_calculator('48', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/23 = 2.086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_24(self):
        self.assertEqual(run_calculator('48', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/24 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_25(self):
        self.assertEqual(run_calculator('48', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/25 = 1.92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_26(self):
        self.assertEqual(run_calculator('48', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/26 = 1.846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_27(self):
        self.assertEqual(run_calculator('48', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/27 = 1.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_28(self):
        self.assertEqual(run_calculator('48', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/28 = 1.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_29(self):
        self.assertEqual(run_calculator('48', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/29 = 1.655172413793103448275862069',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_30(self):
        self.assertEqual(run_calculator('48', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/30 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_31(self):
        self.assertEqual(run_calculator('48', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/31 = 1.548387096774193548387096774',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_32(self):
        self.assertEqual(run_calculator('48', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/32 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_33(self):
        self.assertEqual(run_calculator('48', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/33 = 1.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_34(self):
        self.assertEqual(run_calculator('48', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/34 = 1.411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_35(self):
        self.assertEqual(run_calculator('48', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/35 = 1.371428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_36(self):
        self.assertEqual(run_calculator('48', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/36 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_37(self):
        self.assertEqual(run_calculator('48', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/37 = 1.297297297297297297297297297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_38(self):
        self.assertEqual(run_calculator('48', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/38 = 1.263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_39(self):
        self.assertEqual(run_calculator('48', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/39 = 1.230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_40(self):
        self.assertEqual(run_calculator('48', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/40 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_41(self):
        self.assertEqual(run_calculator('48', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/41 = 1.170731707317073170731707317',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_42(self):
        self.assertEqual(run_calculator('48', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/42 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_43(self):
        self.assertEqual(run_calculator('48', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/43 = 1.116279069767441860465116279',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_44(self):
        self.assertEqual(run_calculator('48', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/44 = 1.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_45(self):
        self.assertEqual(run_calculator('48', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/45 = 1.066666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_46(self):
        self.assertEqual(run_calculator('48', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/46 = 1.043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_47(self):
        self.assertEqual(run_calculator('48', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/47 = 1.021276595744680851063829787',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_48(self):
        self.assertEqual(run_calculator('48', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/48 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_49(self):
        self.assertEqual(run_calculator('48', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/49 = 0.9795918367346938775510204082',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_48_divided_by_50(self):
        self.assertEqual(run_calculator('48', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '48/50 = 0.96',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
