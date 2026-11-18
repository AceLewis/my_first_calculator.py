# test_divided_by_49.py
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


class TestDividedBy49(unittest.TestCase):

    def test_49_divided_by_0(self):
        self.assertEqual(run_calculator('49', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_1(self):
        self.assertEqual(run_calculator('49', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/1 = 49',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_2(self):
        self.assertEqual(run_calculator('49', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/2 = 24.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_3(self):
        self.assertEqual(run_calculator('49', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/3 = 16.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_4(self):
        self.assertEqual(run_calculator('49', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/4 = 12.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_5(self):
        self.assertEqual(run_calculator('49', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/5 = 9.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_6(self):
        self.assertEqual(run_calculator('49', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/6 = 8.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_7(self):
        self.assertEqual(run_calculator('49', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/7 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_8(self):
        self.assertEqual(run_calculator('49', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/8 = 6.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_9(self):
        self.assertEqual(run_calculator('49', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/9 = 5.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_10(self):
        self.assertEqual(run_calculator('49', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/10 = 4.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_11(self):
        self.assertEqual(run_calculator('49', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/11 = 4.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_12(self):
        self.assertEqual(run_calculator('49', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/12 = 4.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_13(self):
        self.assertEqual(run_calculator('49', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/13 = 3.769230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_14(self):
        self.assertEqual(run_calculator('49', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/14 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_15(self):
        self.assertEqual(run_calculator('49', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/15 = 3.266666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_16(self):
        self.assertEqual(run_calculator('49', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/16 = 3.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_17(self):
        self.assertEqual(run_calculator('49', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/17 = 2.882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_18(self):
        self.assertEqual(run_calculator('49', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/18 = 2.722222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_19(self):
        self.assertEqual(run_calculator('49', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/19 = 2.578947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_20(self):
        self.assertEqual(run_calculator('49', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/20 = 2.45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_21(self):
        self.assertEqual(run_calculator('49', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/21 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_22(self):
        self.assertEqual(run_calculator('49', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/22 = 2.227272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_23(self):
        self.assertEqual(run_calculator('49', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/23 = 2.130434782608695652173913043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_24(self):
        self.assertEqual(run_calculator('49', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/24 = 2.041666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_25(self):
        self.assertEqual(run_calculator('49', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/25 = 1.96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_26(self):
        self.assertEqual(run_calculator('49', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/26 = 1.884615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_27(self):
        self.assertEqual(run_calculator('49', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/27 = 1.814814814814814814814814815',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_28(self):
        self.assertEqual(run_calculator('49', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/28 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_29(self):
        self.assertEqual(run_calculator('49', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/29 = 1.689655172413793103448275862',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_30(self):
        self.assertEqual(run_calculator('49', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/30 = 1.633333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_31(self):
        self.assertEqual(run_calculator('49', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/31 = 1.580645161290322580645161290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_32(self):
        self.assertEqual(run_calculator('49', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/32 = 1.53125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_33(self):
        self.assertEqual(run_calculator('49', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/33 = 1.484848484848484848484848485',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_34(self):
        self.assertEqual(run_calculator('49', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/34 = 1.441176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_35(self):
        self.assertEqual(run_calculator('49', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/35 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_36(self):
        self.assertEqual(run_calculator('49', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/36 = 1.361111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_37(self):
        self.assertEqual(run_calculator('49', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/37 = 1.324324324324324324324324324',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_38(self):
        self.assertEqual(run_calculator('49', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/38 = 1.289473684210526315789473684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_39(self):
        self.assertEqual(run_calculator('49', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/39 = 1.256410256410256410256410256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_40(self):
        self.assertEqual(run_calculator('49', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/40 = 1.225',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_41(self):
        self.assertEqual(run_calculator('49', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/41 = 1.195121951219512195121951220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_42(self):
        self.assertEqual(run_calculator('49', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/42 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_43(self):
        self.assertEqual(run_calculator('49', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/43 = 1.139534883720930232558139535',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_44(self):
        self.assertEqual(run_calculator('49', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/44 = 1.113636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_45(self):
        self.assertEqual(run_calculator('49', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/45 = 1.088888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_46(self):
        self.assertEqual(run_calculator('49', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/46 = 1.065217391304347826086956522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_47(self):
        self.assertEqual(run_calculator('49', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/47 = 1.042553191489361702127659574',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_48(self):
        self.assertEqual(run_calculator('49', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/48 = 1.020833333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_49(self):
        self.assertEqual(run_calculator('49', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/49 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_49_divided_by_50(self):
        self.assertEqual(run_calculator('49', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '49/50 = 0.98',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
