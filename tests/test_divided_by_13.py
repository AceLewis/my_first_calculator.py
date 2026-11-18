# test_divided_by_13.py
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


class TestDividedBy13(unittest.TestCase):

    def test_13_divided_by_0(self):
        self.assertEqual(run_calculator('13', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_1(self):
        self.assertEqual(run_calculator('13', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/1 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_2(self):
        self.assertEqual(run_calculator('13', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/2 = 6.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_3(self):
        self.assertEqual(run_calculator('13', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/3 = 4.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_4(self):
        self.assertEqual(run_calculator('13', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/4 = 3.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_5(self):
        self.assertEqual(run_calculator('13', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/5 = 2.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_6(self):
        self.assertEqual(run_calculator('13', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/6 = 2.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_7(self):
        self.assertEqual(run_calculator('13', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/7 = 1.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_8(self):
        self.assertEqual(run_calculator('13', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/8 = 1.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_9(self):
        self.assertEqual(run_calculator('13', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/9 = 1.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_10(self):
        self.assertEqual(run_calculator('13', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/10 = 1.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_11(self):
        self.assertEqual(run_calculator('13', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/11 = 1.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_12(self):
        self.assertEqual(run_calculator('13', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/12 = 1.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_13(self):
        self.assertEqual(run_calculator('13', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/13 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_14(self):
        self.assertEqual(run_calculator('13', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/14 = 0.9285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_15(self):
        self.assertEqual(run_calculator('13', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/15 = 0.8666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_16(self):
        self.assertEqual(run_calculator('13', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/16 = 0.8125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_17(self):
        self.assertEqual(run_calculator('13', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/17 = 0.7647058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_18(self):
        self.assertEqual(run_calculator('13', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/18 = 0.7222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_19(self):
        self.assertEqual(run_calculator('13', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/19 = 0.6842105263157894736842105263',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_20(self):
        self.assertEqual(run_calculator('13', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/20 = 0.65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_21(self):
        self.assertEqual(run_calculator('13', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/21 = 0.6190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_22(self):
        self.assertEqual(run_calculator('13', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/22 = 0.5909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_23(self):
        self.assertEqual(run_calculator('13', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/23 = 0.5652173913043478260869565217',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_24(self):
        self.assertEqual(run_calculator('13', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/24 = 0.5416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_25(self):
        self.assertEqual(run_calculator('13', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/25 = 0.52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_26(self):
        self.assertEqual(run_calculator('13', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/26 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_27(self):
        self.assertEqual(run_calculator('13', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/27 = 0.4814814814814814814814814815',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_28(self):
        self.assertEqual(run_calculator('13', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/28 = 0.4642857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_29(self):
        self.assertEqual(run_calculator('13', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/29 = 0.4482758620689655172413793103',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_30(self):
        self.assertEqual(run_calculator('13', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/30 = 0.4333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_31(self):
        self.assertEqual(run_calculator('13', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/31 = 0.4193548387096774193548387097',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_32(self):
        self.assertEqual(run_calculator('13', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/32 = 0.40625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_33(self):
        self.assertEqual(run_calculator('13', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/33 = 0.3939393939393939393939393939',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_34(self):
        self.assertEqual(run_calculator('13', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/34 = 0.3823529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_35(self):
        self.assertEqual(run_calculator('13', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/35 = 0.3714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_36(self):
        self.assertEqual(run_calculator('13', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/36 = 0.3611111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_37(self):
        self.assertEqual(run_calculator('13', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/37 = 0.3513513513513513513513513514',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_38(self):
        self.assertEqual(run_calculator('13', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/38 = 0.3421052631578947368421052632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_39(self):
        self.assertEqual(run_calculator('13', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/39 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_40(self):
        self.assertEqual(run_calculator('13', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/40 = 0.325',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_41(self):
        self.assertEqual(run_calculator('13', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/41 = 0.3170731707317073170731707317',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_42(self):
        self.assertEqual(run_calculator('13', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/42 = 0.3095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_43(self):
        self.assertEqual(run_calculator('13', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/43 = 0.3023255813953488372093023256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_44(self):
        self.assertEqual(run_calculator('13', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/44 = 0.2954545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_45(self):
        self.assertEqual(run_calculator('13', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/45 = 0.2888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_46(self):
        self.assertEqual(run_calculator('13', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/46 = 0.2826086956521739130434782609',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_47(self):
        self.assertEqual(run_calculator('13', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/47 = 0.2765957446808510638297872340',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_48(self):
        self.assertEqual(run_calculator('13', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/48 = 0.2708333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_49(self):
        self.assertEqual(run_calculator('13', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/49 = 0.2653061224489795918367346939',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_13_divided_by_50(self):
        self.assertEqual(run_calculator('13', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '13/50 = 0.26',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
