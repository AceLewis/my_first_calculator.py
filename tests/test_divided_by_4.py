# test_divided_by_4.py
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


class TestDividedBy4(unittest.TestCase):

    def test_4_divided_by_0(self):
        self.assertEqual(run_calculator('4', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_1(self):
        self.assertEqual(run_calculator('4', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/1 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_2(self):
        self.assertEqual(run_calculator('4', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/2 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_3(self):
        self.assertEqual(run_calculator('4', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/3 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_4(self):
        self.assertEqual(run_calculator('4', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/4 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_5(self):
        self.assertEqual(run_calculator('4', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/5 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_6(self):
        self.assertEqual(run_calculator('4', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/6 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_7(self):
        self.assertEqual(run_calculator('4', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/7 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_8(self):
        self.assertEqual(run_calculator('4', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/8 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_9(self):
        self.assertEqual(run_calculator('4', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/9 = 0.4444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_10(self):
        self.assertEqual(run_calculator('4', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/10 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_11(self):
        self.assertEqual(run_calculator('4', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/11 = 0.3636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_12(self):
        self.assertEqual(run_calculator('4', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/12 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_13(self):
        self.assertEqual(run_calculator('4', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/13 = 0.3076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_14(self):
        self.assertEqual(run_calculator('4', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/14 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_15(self):
        self.assertEqual(run_calculator('4', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/15 = 0.2666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_16(self):
        self.assertEqual(run_calculator('4', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/16 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_17(self):
        self.assertEqual(run_calculator('4', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/17 = 0.2352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_18(self):
        self.assertEqual(run_calculator('4', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/18 = 0.2222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_19(self):
        self.assertEqual(run_calculator('4', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/19 = 0.2105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_20(self):
        self.assertEqual(run_calculator('4', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/20 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_21(self):
        self.assertEqual(run_calculator('4', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/21 = 0.1904761904761904761904761905',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_22(self):
        self.assertEqual(run_calculator('4', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/22 = 0.1818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_23(self):
        self.assertEqual(run_calculator('4', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/23 = 0.1739130434782608695652173913',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_24(self):
        self.assertEqual(run_calculator('4', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/24 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_25(self):
        self.assertEqual(run_calculator('4', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/25 = 0.16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_26(self):
        self.assertEqual(run_calculator('4', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/26 = 0.1538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_27(self):
        self.assertEqual(run_calculator('4', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/27 = 0.1481481481481481481481481481',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_28(self):
        self.assertEqual(run_calculator('4', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/28 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_29(self):
        self.assertEqual(run_calculator('4', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/29 = 0.1379310344827586206896551724',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_30(self):
        self.assertEqual(run_calculator('4', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/30 = 0.1333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_31(self):
        self.assertEqual(run_calculator('4', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/31 = 0.1290322580645161290322580645',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_32(self):
        self.assertEqual(run_calculator('4', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/32 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_33(self):
        self.assertEqual(run_calculator('4', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/33 = 0.1212121212121212121212121212',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_34(self):
        self.assertEqual(run_calculator('4', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/34 = 0.1176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_35(self):
        self.assertEqual(run_calculator('4', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/35 = 0.1142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_36(self):
        self.assertEqual(run_calculator('4', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/36 = 0.1111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_37(self):
        self.assertEqual(run_calculator('4', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/37 = 0.1081081081081081081081081081',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_38(self):
        self.assertEqual(run_calculator('4', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/38 = 0.1052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_39(self):
        self.assertEqual(run_calculator('4', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/39 = 0.1025641025641025641025641026',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_40(self):
        self.assertEqual(run_calculator('4', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/40 = 0.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_41(self):
        self.assertEqual(run_calculator('4', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/41 = 0.09756097560975609756097560976',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_42(self):
        self.assertEqual(run_calculator('4', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/42 = 0.09523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_43(self):
        self.assertEqual(run_calculator('4', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/43 = 0.09302325581395348837209302326',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_44(self):
        self.assertEqual(run_calculator('4', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/44 = 0.09090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_45(self):
        self.assertEqual(run_calculator('4', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/45 = 0.08888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_46(self):
        self.assertEqual(run_calculator('4', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/46 = 0.08695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_47(self):
        self.assertEqual(run_calculator('4', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/47 = 0.08510638297872340425531914894',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_48(self):
        self.assertEqual(run_calculator('4', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/48 = 0.08333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_49(self):
        self.assertEqual(run_calculator('4', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/49 = 0.08163265306122448979591836735',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_4_divided_by_50(self):
        self.assertEqual(run_calculator('4', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '4/50 = 0.08',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
