# test_divided_by_45.py
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


class TestDividedBy45(unittest.TestCase):

    def test_45_divided_by_0(self):
        self.assertEqual(run_calculator('45', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_1(self):
        self.assertEqual(run_calculator('45', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/1 = 45',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_2(self):
        self.assertEqual(run_calculator('45', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/2 = 22.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_3(self):
        self.assertEqual(run_calculator('45', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/3 = 15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_4(self):
        self.assertEqual(run_calculator('45', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/4 = 11.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_5(self):
        self.assertEqual(run_calculator('45', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/5 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_6(self):
        self.assertEqual(run_calculator('45', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/6 = 7.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_7(self):
        self.assertEqual(run_calculator('45', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/7 = 6.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_8(self):
        self.assertEqual(run_calculator('45', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/8 = 5.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_9(self):
        self.assertEqual(run_calculator('45', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/9 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_10(self):
        self.assertEqual(run_calculator('45', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/10 = 4.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_11(self):
        self.assertEqual(run_calculator('45', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/11 = 4.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_12(self):
        self.assertEqual(run_calculator('45', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/12 = 3.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_13(self):
        self.assertEqual(run_calculator('45', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/13 = 3.461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_14(self):
        self.assertEqual(run_calculator('45', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/14 = 3.214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_15(self):
        self.assertEqual(run_calculator('45', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/15 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_16(self):
        self.assertEqual(run_calculator('45', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/16 = 2.8125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_17(self):
        self.assertEqual(run_calculator('45', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/17 = 2.647058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_18(self):
        self.assertEqual(run_calculator('45', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/18 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_19(self):
        self.assertEqual(run_calculator('45', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/19 = 2.368421052631578947368421053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_20(self):
        self.assertEqual(run_calculator('45', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/20 = 2.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_21(self):
        self.assertEqual(run_calculator('45', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/21 = 2.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_22(self):
        self.assertEqual(run_calculator('45', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/22 = 2.045454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_23(self):
        self.assertEqual(run_calculator('45', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/23 = 1.956521739130434782608695652',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_24(self):
        self.assertEqual(run_calculator('45', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/24 = 1.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_25(self):
        self.assertEqual(run_calculator('45', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/25 = 1.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_26(self):
        self.assertEqual(run_calculator('45', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/26 = 1.730769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_27(self):
        self.assertEqual(run_calculator('45', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/27 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_28(self):
        self.assertEqual(run_calculator('45', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/28 = 1.607142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_29(self):
        self.assertEqual(run_calculator('45', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/29 = 1.551724137931034482758620690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_30(self):
        self.assertEqual(run_calculator('45', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/30 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_31(self):
        self.assertEqual(run_calculator('45', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/31 = 1.451612903225806451612903226',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_32(self):
        self.assertEqual(run_calculator('45', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/32 = 1.40625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_33(self):
        self.assertEqual(run_calculator('45', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/33 = 1.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_34(self):
        self.assertEqual(run_calculator('45', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/34 = 1.323529411764705882352941176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_35(self):
        self.assertEqual(run_calculator('45', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/35 = 1.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_36(self):
        self.assertEqual(run_calculator('45', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/36 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_37(self):
        self.assertEqual(run_calculator('45', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/37 = 1.216216216216216216216216216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_38(self):
        self.assertEqual(run_calculator('45', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/38 = 1.184210526315789473684210526',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_39(self):
        self.assertEqual(run_calculator('45', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/39 = 1.153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_40(self):
        self.assertEqual(run_calculator('45', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/40 = 1.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_41(self):
        self.assertEqual(run_calculator('45', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/41 = 1.097560975609756097560975610',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_42(self):
        self.assertEqual(run_calculator('45', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/42 = 1.071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_43(self):
        self.assertEqual(run_calculator('45', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/43 = 1.046511627906976744186046512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_44(self):
        self.assertEqual(run_calculator('45', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/44 = 1.022727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_45(self):
        self.assertEqual(run_calculator('45', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/45 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_46(self):
        self.assertEqual(run_calculator('45', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/46 = 0.9782608695652173913043478261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_47(self):
        self.assertEqual(run_calculator('45', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/47 = 0.9574468085106382978723404255',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_48(self):
        self.assertEqual(run_calculator('45', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/48 = 0.9375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_49(self):
        self.assertEqual(run_calculator('45', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/49 = 0.9183673469387755102040816327',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_45_divided_by_50(self):
        self.assertEqual(run_calculator('45', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '45/50 = 0.9',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
