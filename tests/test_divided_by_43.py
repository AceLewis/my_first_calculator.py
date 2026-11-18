# test_divided_by_43.py
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


class TestDividedBy43(unittest.TestCase):

    def test_43_divided_by_0(self):
        self.assertEqual(run_calculator('43', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_1(self):
        self.assertEqual(run_calculator('43', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/1 = 43',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_2(self):
        self.assertEqual(run_calculator('43', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/2 = 21.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_3(self):
        self.assertEqual(run_calculator('43', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/3 = 14.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_4(self):
        self.assertEqual(run_calculator('43', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/4 = 10.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_5(self):
        self.assertEqual(run_calculator('43', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/5 = 8.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_6(self):
        self.assertEqual(run_calculator('43', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/6 = 7.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_7(self):
        self.assertEqual(run_calculator('43', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/7 = 6.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_8(self):
        self.assertEqual(run_calculator('43', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/8 = 5.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_9(self):
        self.assertEqual(run_calculator('43', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/9 = 4.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_10(self):
        self.assertEqual(run_calculator('43', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/10 = 4.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_11(self):
        self.assertEqual(run_calculator('43', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/11 = 3.909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_12(self):
        self.assertEqual(run_calculator('43', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/12 = 3.583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_13(self):
        self.assertEqual(run_calculator('43', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/13 = 3.307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_14(self):
        self.assertEqual(run_calculator('43', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/14 = 3.071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_15(self):
        self.assertEqual(run_calculator('43', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/15 = 2.866666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_16(self):
        self.assertEqual(run_calculator('43', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/16 = 2.6875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_17(self):
        self.assertEqual(run_calculator('43', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/17 = 2.529411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_18(self):
        self.assertEqual(run_calculator('43', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/18 = 2.388888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_19(self):
        self.assertEqual(run_calculator('43', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/19 = 2.263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_20(self):
        self.assertEqual(run_calculator('43', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/20 = 2.15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_21(self):
        self.assertEqual(run_calculator('43', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/21 = 2.047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_22(self):
        self.assertEqual(run_calculator('43', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/22 = 1.954545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_23(self):
        self.assertEqual(run_calculator('43', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/23 = 1.869565217391304347826086957',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_24(self):
        self.assertEqual(run_calculator('43', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/24 = 1.791666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_25(self):
        self.assertEqual(run_calculator('43', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/25 = 1.72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_26(self):
        self.assertEqual(run_calculator('43', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/26 = 1.653846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_27(self):
        self.assertEqual(run_calculator('43', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/27 = 1.592592592592592592592592593',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_28(self):
        self.assertEqual(run_calculator('43', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/28 = 1.535714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_29(self):
        self.assertEqual(run_calculator('43', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/29 = 1.482758620689655172413793103',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_30(self):
        self.assertEqual(run_calculator('43', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/30 = 1.433333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_31(self):
        self.assertEqual(run_calculator('43', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/31 = 1.387096774193548387096774194',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_32(self):
        self.assertEqual(run_calculator('43', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/32 = 1.34375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_33(self):
        self.assertEqual(run_calculator('43', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/33 = 1.303030303030303030303030303',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_34(self):
        self.assertEqual(run_calculator('43', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/34 = 1.264705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_35(self):
        self.assertEqual(run_calculator('43', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/35 = 1.228571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_36(self):
        self.assertEqual(run_calculator('43', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/36 = 1.194444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_37(self):
        self.assertEqual(run_calculator('43', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/37 = 1.162162162162162162162162162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_38(self):
        self.assertEqual(run_calculator('43', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/38 = 1.131578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_39(self):
        self.assertEqual(run_calculator('43', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/39 = 1.102564102564102564102564103',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_40(self):
        self.assertEqual(run_calculator('43', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/40 = 1.075',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_41(self):
        self.assertEqual(run_calculator('43', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/41 = 1.048780487804878048780487805',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_42(self):
        self.assertEqual(run_calculator('43', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/42 = 1.023809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_43(self):
        self.assertEqual(run_calculator('43', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/43 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_44(self):
        self.assertEqual(run_calculator('43', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/44 = 0.9772727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_45(self):
        self.assertEqual(run_calculator('43', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/45 = 0.9555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_46(self):
        self.assertEqual(run_calculator('43', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/46 = 0.9347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_47(self):
        self.assertEqual(run_calculator('43', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/47 = 0.9148936170212765957446808511',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_48(self):
        self.assertEqual(run_calculator('43', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/48 = 0.8958333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_49(self):
        self.assertEqual(run_calculator('43', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/49 = 0.8775510204081632653061224490',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_43_divided_by_50(self):
        self.assertEqual(run_calculator('43', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '43/50 = 0.86',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
