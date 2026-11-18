# test_divided_by_12.py
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


class TestDividedBy12(unittest.TestCase):

    def test_12_divided_by_0(self):
        self.assertEqual(run_calculator('12', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_1(self):
        self.assertEqual(run_calculator('12', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/1 = 12',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_2(self):
        self.assertEqual(run_calculator('12', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/2 = 6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_3(self):
        self.assertEqual(run_calculator('12', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/3 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_4(self):
        self.assertEqual(run_calculator('12', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/4 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_5(self):
        self.assertEqual(run_calculator('12', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/5 = 2.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_6(self):
        self.assertEqual(run_calculator('12', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/6 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_7(self):
        self.assertEqual(run_calculator('12', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/7 = 1.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_8(self):
        self.assertEqual(run_calculator('12', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/8 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_9(self):
        self.assertEqual(run_calculator('12', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/9 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_10(self):
        self.assertEqual(run_calculator('12', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/10 = 1.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_11(self):
        self.assertEqual(run_calculator('12', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/11 = 1.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_12(self):
        self.assertEqual(run_calculator('12', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/12 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_13(self):
        self.assertEqual(run_calculator('12', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/13 = 0.9230769230769230769230769231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_14(self):
        self.assertEqual(run_calculator('12', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/14 = 0.8571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_15(self):
        self.assertEqual(run_calculator('12', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/15 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_16(self):
        self.assertEqual(run_calculator('12', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/16 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_17(self):
        self.assertEqual(run_calculator('12', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/17 = 0.7058823529411764705882352941',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_18(self):
        self.assertEqual(run_calculator('12', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/18 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_19(self):
        self.assertEqual(run_calculator('12', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/19 = 0.6315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_20(self):
        self.assertEqual(run_calculator('12', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/20 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_21(self):
        self.assertEqual(run_calculator('12', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/21 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_22(self):
        self.assertEqual(run_calculator('12', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/22 = 0.5454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_23(self):
        self.assertEqual(run_calculator('12', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/23 = 0.5217391304347826086956521739',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_24(self):
        self.assertEqual(run_calculator('12', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/24 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_25(self):
        self.assertEqual(run_calculator('12', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/25 = 0.48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_26(self):
        self.assertEqual(run_calculator('12', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/26 = 0.4615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_27(self):
        self.assertEqual(run_calculator('12', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/27 = 0.4444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_28(self):
        self.assertEqual(run_calculator('12', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/28 = 0.4285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_29(self):
        self.assertEqual(run_calculator('12', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/29 = 0.4137931034482758620689655172',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_30(self):
        self.assertEqual(run_calculator('12', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/30 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_31(self):
        self.assertEqual(run_calculator('12', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/31 = 0.3870967741935483870967741935',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_32(self):
        self.assertEqual(run_calculator('12', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/32 = 0.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_33(self):
        self.assertEqual(run_calculator('12', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/33 = 0.3636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_34(self):
        self.assertEqual(run_calculator('12', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/34 = 0.3529411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_35(self):
        self.assertEqual(run_calculator('12', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/35 = 0.3428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_36(self):
        self.assertEqual(run_calculator('12', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/36 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_37(self):
        self.assertEqual(run_calculator('12', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/37 = 0.3243243243243243243243243243',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_38(self):
        self.assertEqual(run_calculator('12', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/38 = 0.3157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_39(self):
        self.assertEqual(run_calculator('12', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/39 = 0.3076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_40(self):
        self.assertEqual(run_calculator('12', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/40 = 0.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_41(self):
        self.assertEqual(run_calculator('12', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/41 = 0.2926829268292682926829268293',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_42(self):
        self.assertEqual(run_calculator('12', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/42 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_43(self):
        self.assertEqual(run_calculator('12', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/43 = 0.2790697674418604651162790698',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_44(self):
        self.assertEqual(run_calculator('12', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/44 = 0.2727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_45(self):
        self.assertEqual(run_calculator('12', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/45 = 0.2666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_46(self):
        self.assertEqual(run_calculator('12', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/46 = 0.2608695652173913043478260870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_47(self):
        self.assertEqual(run_calculator('12', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/47 = 0.2553191489361702127659574468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_48(self):
        self.assertEqual(run_calculator('12', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/48 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_49(self):
        self.assertEqual(run_calculator('12', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/49 = 0.2448979591836734693877551020',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_12_divided_by_50(self):
        self.assertEqual(run_calculator('12', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '12/50 = 0.24',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
