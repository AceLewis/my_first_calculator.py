# test_divided_by_40.py
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


class TestDividedBy40(unittest.TestCase):

    def test_40_divided_by_0(self):
        self.assertEqual(run_calculator('40', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_1(self):
        self.assertEqual(run_calculator('40', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/1 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_2(self):
        self.assertEqual(run_calculator('40', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/2 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_3(self):
        self.assertEqual(run_calculator('40', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/3 = 13.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_4(self):
        self.assertEqual(run_calculator('40', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/4 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_5(self):
        self.assertEqual(run_calculator('40', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/5 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_6(self):
        self.assertEqual(run_calculator('40', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/6 = 6.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_7(self):
        self.assertEqual(run_calculator('40', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/7 = 5.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_8(self):
        self.assertEqual(run_calculator('40', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/8 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_9(self):
        self.assertEqual(run_calculator('40', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/9 = 4.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_10(self):
        self.assertEqual(run_calculator('40', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/10 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_11(self):
        self.assertEqual(run_calculator('40', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/11 = 3.636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_12(self):
        self.assertEqual(run_calculator('40', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/12 = 3.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_13(self):
        self.assertEqual(run_calculator('40', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/13 = 3.076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_14(self):
        self.assertEqual(run_calculator('40', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/14 = 2.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_15(self):
        self.assertEqual(run_calculator('40', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/15 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_16(self):
        self.assertEqual(run_calculator('40', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/16 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_17(self):
        self.assertEqual(run_calculator('40', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/17 = 2.352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_18(self):
        self.assertEqual(run_calculator('40', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/18 = 2.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_19(self):
        self.assertEqual(run_calculator('40', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/19 = 2.105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_20(self):
        self.assertEqual(run_calculator('40', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/20 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_21(self):
        self.assertEqual(run_calculator('40', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/21 = 1.904761904761904761904761905',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_22(self):
        self.assertEqual(run_calculator('40', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/22 = 1.818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_23(self):
        self.assertEqual(run_calculator('40', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/23 = 1.739130434782608695652173913',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_24(self):
        self.assertEqual(run_calculator('40', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/24 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_25(self):
        self.assertEqual(run_calculator('40', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/25 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_26(self):
        self.assertEqual(run_calculator('40', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/26 = 1.538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_27(self):
        self.assertEqual(run_calculator('40', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/27 = 1.481481481481481481481481481',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_28(self):
        self.assertEqual(run_calculator('40', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/28 = 1.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_29(self):
        self.assertEqual(run_calculator('40', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/29 = 1.379310344827586206896551724',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_30(self):
        self.assertEqual(run_calculator('40', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/30 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_31(self):
        self.assertEqual(run_calculator('40', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/31 = 1.290322580645161290322580645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_32(self):
        self.assertEqual(run_calculator('40', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/32 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_33(self):
        self.assertEqual(run_calculator('40', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/33 = 1.212121212121212121212121212',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_34(self):
        self.assertEqual(run_calculator('40', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/34 = 1.176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_35(self):
        self.assertEqual(run_calculator('40', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/35 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_36(self):
        self.assertEqual(run_calculator('40', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/36 = 1.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_37(self):
        self.assertEqual(run_calculator('40', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/37 = 1.081081081081081081081081081',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_38(self):
        self.assertEqual(run_calculator('40', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/38 = 1.052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_39(self):
        self.assertEqual(run_calculator('40', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/39 = 1.025641025641025641025641026',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_40(self):
        self.assertEqual(run_calculator('40', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/40 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_41(self):
        self.assertEqual(run_calculator('40', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/41 = 0.9756097560975609756097560976',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_42(self):
        self.assertEqual(run_calculator('40', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/42 = 0.9523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_43(self):
        self.assertEqual(run_calculator('40', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/43 = 0.9302325581395348837209302326',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_44(self):
        self.assertEqual(run_calculator('40', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/44 = 0.9090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_45(self):
        self.assertEqual(run_calculator('40', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/45 = 0.8888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_46(self):
        self.assertEqual(run_calculator('40', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/46 = 0.8695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_47(self):
        self.assertEqual(run_calculator('40', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/47 = 0.8510638297872340425531914894',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_48(self):
        self.assertEqual(run_calculator('40', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/48 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_49(self):
        self.assertEqual(run_calculator('40', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/49 = 0.8163265306122448979591836735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_40_divided_by_50(self):
        self.assertEqual(run_calculator('40', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '40/50 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
