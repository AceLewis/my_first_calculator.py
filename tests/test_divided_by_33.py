# test_divided_by_33.py
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


class TestDividedBy33(unittest.TestCase):

    def test_33_divided_by_0(self):
        self.assertEqual(run_calculator('33', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_1(self):
        self.assertEqual(run_calculator('33', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/1 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_2(self):
        self.assertEqual(run_calculator('33', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/2 = 16.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_3(self):
        self.assertEqual(run_calculator('33', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/3 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_4(self):
        self.assertEqual(run_calculator('33', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/4 = 8.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_5(self):
        self.assertEqual(run_calculator('33', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/5 = 6.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_6(self):
        self.assertEqual(run_calculator('33', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/6 = 5.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_7(self):
        self.assertEqual(run_calculator('33', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/7 = 4.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_8(self):
        self.assertEqual(run_calculator('33', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/8 = 4.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_9(self):
        self.assertEqual(run_calculator('33', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/9 = 3.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_10(self):
        self.assertEqual(run_calculator('33', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/10 = 3.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_11(self):
        self.assertEqual(run_calculator('33', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/11 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_12(self):
        self.assertEqual(run_calculator('33', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/12 = 2.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_13(self):
        self.assertEqual(run_calculator('33', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/13 = 2.538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_14(self):
        self.assertEqual(run_calculator('33', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/14 = 2.357142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_15(self):
        self.assertEqual(run_calculator('33', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/15 = 2.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_16(self):
        self.assertEqual(run_calculator('33', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/16 = 2.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_17(self):
        self.assertEqual(run_calculator('33', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/17 = 1.941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_18(self):
        self.assertEqual(run_calculator('33', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/18 = 1.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_19(self):
        self.assertEqual(run_calculator('33', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/19 = 1.736842105263157894736842105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_20(self):
        self.assertEqual(run_calculator('33', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/20 = 1.65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_21(self):
        self.assertEqual(run_calculator('33', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/21 = 1.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_22(self):
        self.assertEqual(run_calculator('33', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/22 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_23(self):
        self.assertEqual(run_calculator('33', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/23 = 1.434782608695652173913043478',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_24(self):
        self.assertEqual(run_calculator('33', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/24 = 1.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_25(self):
        self.assertEqual(run_calculator('33', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/25 = 1.32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_26(self):
        self.assertEqual(run_calculator('33', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/26 = 1.269230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_27(self):
        self.assertEqual(run_calculator('33', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/27 = 1.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_28(self):
        self.assertEqual(run_calculator('33', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/28 = 1.178571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_29(self):
        self.assertEqual(run_calculator('33', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/29 = 1.137931034482758620689655172',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_30(self):
        self.assertEqual(run_calculator('33', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/30 = 1.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_31(self):
        self.assertEqual(run_calculator('33', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/31 = 1.064516129032258064516129032',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_32(self):
        self.assertEqual(run_calculator('33', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/32 = 1.03125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_33(self):
        self.assertEqual(run_calculator('33', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/33 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_34(self):
        self.assertEqual(run_calculator('33', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/34 = 0.9705882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_35(self):
        self.assertEqual(run_calculator('33', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/35 = 0.9428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_36(self):
        self.assertEqual(run_calculator('33', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/36 = 0.9166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_37(self):
        self.assertEqual(run_calculator('33', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/37 = 0.8918918918918918918918918919',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_38(self):
        self.assertEqual(run_calculator('33', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/38 = 0.8684210526315789473684210526',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_39(self):
        self.assertEqual(run_calculator('33', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/39 = 0.8461538461538461538461538462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_40(self):
        self.assertEqual(run_calculator('33', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/40 = 0.825',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_41(self):
        self.assertEqual(run_calculator('33', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/41 = 0.8048780487804878048780487805',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_42(self):
        self.assertEqual(run_calculator('33', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/42 = 0.7857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_43(self):
        self.assertEqual(run_calculator('33', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/43 = 0.7674418604651162790697674419',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_44(self):
        self.assertEqual(run_calculator('33', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/44 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_45(self):
        self.assertEqual(run_calculator('33', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/45 = 0.7333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_46(self):
        self.assertEqual(run_calculator('33', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/46 = 0.7173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_47(self):
        self.assertEqual(run_calculator('33', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/47 = 0.7021276595744680851063829787',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_48(self):
        self.assertEqual(run_calculator('33', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/48 = 0.6875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_49(self):
        self.assertEqual(run_calculator('33', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/49 = 0.6734693877551020408163265306',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_divided_by_50(self):
        self.assertEqual(run_calculator('33', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33/50 = 0.66',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
