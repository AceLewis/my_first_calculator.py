# test_divided_by_28.py
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


class TestDividedBy28(unittest.TestCase):

    def test_28_divided_by_0(self):
        self.assertEqual(run_calculator('28', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_1(self):
        self.assertEqual(run_calculator('28', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/1 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_2(self):
        self.assertEqual(run_calculator('28', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/2 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_3(self):
        self.assertEqual(run_calculator('28', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/3 = 9.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_4(self):
        self.assertEqual(run_calculator('28', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/4 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_5(self):
        self.assertEqual(run_calculator('28', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/5 = 5.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_6(self):
        self.assertEqual(run_calculator('28', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/6 = 4.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_7(self):
        self.assertEqual(run_calculator('28', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/7 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_8(self):
        self.assertEqual(run_calculator('28', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/8 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_9(self):
        self.assertEqual(run_calculator('28', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/9 = 3.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_10(self):
        self.assertEqual(run_calculator('28', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/10 = 2.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_11(self):
        self.assertEqual(run_calculator('28', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/11 = 2.545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_12(self):
        self.assertEqual(run_calculator('28', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/12 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_13(self):
        self.assertEqual(run_calculator('28', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/13 = 2.153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_14(self):
        self.assertEqual(run_calculator('28', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/14 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_15(self):
        self.assertEqual(run_calculator('28', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/15 = 1.866666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_16(self):
        self.assertEqual(run_calculator('28', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/16 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_17(self):
        self.assertEqual(run_calculator('28', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/17 = 1.647058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_18(self):
        self.assertEqual(run_calculator('28', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/18 = 1.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_19(self):
        self.assertEqual(run_calculator('28', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/19 = 1.473684210526315789473684211',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_20(self):
        self.assertEqual(run_calculator('28', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/20 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_21(self):
        self.assertEqual(run_calculator('28', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/21 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_22(self):
        self.assertEqual(run_calculator('28', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/22 = 1.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_23(self):
        self.assertEqual(run_calculator('28', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/23 = 1.217391304347826086956521739',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_24(self):
        self.assertEqual(run_calculator('28', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/24 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_25(self):
        self.assertEqual(run_calculator('28', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/25 = 1.12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_26(self):
        self.assertEqual(run_calculator('28', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/26 = 1.076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_27(self):
        self.assertEqual(run_calculator('28', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/27 = 1.037037037037037037037037037',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_28(self):
        self.assertEqual(run_calculator('28', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/28 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_29(self):
        self.assertEqual(run_calculator('28', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/29 = 0.9655172413793103448275862069',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_30(self):
        self.assertEqual(run_calculator('28', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/30 = 0.9333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_31(self):
        self.assertEqual(run_calculator('28', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/31 = 0.9032258064516129032258064516',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_32(self):
        self.assertEqual(run_calculator('28', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/32 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_33(self):
        self.assertEqual(run_calculator('28', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/33 = 0.8484848484848484848484848485',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_34(self):
        self.assertEqual(run_calculator('28', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/34 = 0.8235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_35(self):
        self.assertEqual(run_calculator('28', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/35 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_36(self):
        self.assertEqual(run_calculator('28', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/36 = 0.7777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_37(self):
        self.assertEqual(run_calculator('28', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/37 = 0.7567567567567567567567567568',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_38(self):
        self.assertEqual(run_calculator('28', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/38 = 0.7368421052631578947368421053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_39(self):
        self.assertEqual(run_calculator('28', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/39 = 0.7179487179487179487179487179',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_40(self):
        self.assertEqual(run_calculator('28', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/40 = 0.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_41(self):
        self.assertEqual(run_calculator('28', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/41 = 0.6829268292682926829268292683',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_42(self):
        self.assertEqual(run_calculator('28', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/42 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_43(self):
        self.assertEqual(run_calculator('28', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/43 = 0.6511627906976744186046511628',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_44(self):
        self.assertEqual(run_calculator('28', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/44 = 0.6363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_45(self):
        self.assertEqual(run_calculator('28', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/45 = 0.6222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_46(self):
        self.assertEqual(run_calculator('28', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/46 = 0.6086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_47(self):
        self.assertEqual(run_calculator('28', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/47 = 0.5957446808510638297872340426',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_48(self):
        self.assertEqual(run_calculator('28', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/48 = 0.5833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_49(self):
        self.assertEqual(run_calculator('28', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/49 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_divided_by_50(self):
        self.assertEqual(run_calculator('28', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28/50 = 0.56',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
