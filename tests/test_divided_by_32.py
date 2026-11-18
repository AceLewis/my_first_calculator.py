# test_divided_by_32.py
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


class TestDividedBy32(unittest.TestCase):

    def test_32_divided_by_0(self):
        self.assertEqual(run_calculator('32', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_1(self):
        self.assertEqual(run_calculator('32', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/1 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_2(self):
        self.assertEqual(run_calculator('32', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/2 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_3(self):
        self.assertEqual(run_calculator('32', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/3 = 10.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_4(self):
        self.assertEqual(run_calculator('32', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/4 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_5(self):
        self.assertEqual(run_calculator('32', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/5 = 6.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_6(self):
        self.assertEqual(run_calculator('32', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/6 = 5.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_7(self):
        self.assertEqual(run_calculator('32', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/7 = 4.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_8(self):
        self.assertEqual(run_calculator('32', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/8 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_9(self):
        self.assertEqual(run_calculator('32', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/9 = 3.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_10(self):
        self.assertEqual(run_calculator('32', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/10 = 3.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_11(self):
        self.assertEqual(run_calculator('32', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/11 = 2.909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_12(self):
        self.assertEqual(run_calculator('32', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/12 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_13(self):
        self.assertEqual(run_calculator('32', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/13 = 2.461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_14(self):
        self.assertEqual(run_calculator('32', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/14 = 2.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_15(self):
        self.assertEqual(run_calculator('32', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/15 = 2.133333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_16(self):
        self.assertEqual(run_calculator('32', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/16 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_17(self):
        self.assertEqual(run_calculator('32', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/17 = 1.882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_18(self):
        self.assertEqual(run_calculator('32', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/18 = 1.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_19(self):
        self.assertEqual(run_calculator('32', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/19 = 1.684210526315789473684210526',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_20(self):
        self.assertEqual(run_calculator('32', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/20 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_21(self):
        self.assertEqual(run_calculator('32', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/21 = 1.523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_22(self):
        self.assertEqual(run_calculator('32', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/22 = 1.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_23(self):
        self.assertEqual(run_calculator('32', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/23 = 1.391304347826086956521739130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_24(self):
        self.assertEqual(run_calculator('32', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/24 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_25(self):
        self.assertEqual(run_calculator('32', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/25 = 1.28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_26(self):
        self.assertEqual(run_calculator('32', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/26 = 1.230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_27(self):
        self.assertEqual(run_calculator('32', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/27 = 1.185185185185185185185185185',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_28(self):
        self.assertEqual(run_calculator('32', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/28 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_29(self):
        self.assertEqual(run_calculator('32', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/29 = 1.103448275862068965517241379',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_30(self):
        self.assertEqual(run_calculator('32', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/30 = 1.066666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_31(self):
        self.assertEqual(run_calculator('32', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/31 = 1.032258064516129032258064516',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_32(self):
        self.assertEqual(run_calculator('32', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/32 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_33(self):
        self.assertEqual(run_calculator('32', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/33 = 0.9696969696969696969696969697',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_34(self):
        self.assertEqual(run_calculator('32', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/34 = 0.9411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_35(self):
        self.assertEqual(run_calculator('32', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/35 = 0.9142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_36(self):
        self.assertEqual(run_calculator('32', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/36 = 0.8888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_37(self):
        self.assertEqual(run_calculator('32', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/37 = 0.8648648648648648648648648649',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_38(self):
        self.assertEqual(run_calculator('32', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/38 = 0.8421052631578947368421052632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_39(self):
        self.assertEqual(run_calculator('32', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/39 = 0.8205128205128205128205128205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_40(self):
        self.assertEqual(run_calculator('32', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/40 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_41(self):
        self.assertEqual(run_calculator('32', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/41 = 0.7804878048780487804878048780',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_42(self):
        self.assertEqual(run_calculator('32', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/42 = 0.7619047619047619047619047619',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_43(self):
        self.assertEqual(run_calculator('32', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/43 = 0.7441860465116279069767441860',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_44(self):
        self.assertEqual(run_calculator('32', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/44 = 0.7272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_45(self):
        self.assertEqual(run_calculator('32', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/45 = 0.7111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_46(self):
        self.assertEqual(run_calculator('32', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/46 = 0.6956521739130434782608695652',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_47(self):
        self.assertEqual(run_calculator('32', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/47 = 0.6808510638297872340425531915',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_48(self):
        self.assertEqual(run_calculator('32', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/48 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_49(self):
        self.assertEqual(run_calculator('32', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/49 = 0.6530612244897959183673469388',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_32_divided_by_50(self):
        self.assertEqual(run_calculator('32', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '32/50 = 0.64',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
