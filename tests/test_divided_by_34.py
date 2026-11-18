# test_divided_by_34.py
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


class TestDividedBy34(unittest.TestCase):

    def test_34_divided_by_0(self):
        self.assertEqual(run_calculator('34', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_1(self):
        self.assertEqual(run_calculator('34', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/1 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_2(self):
        self.assertEqual(run_calculator('34', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/2 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_3(self):
        self.assertEqual(run_calculator('34', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/3 = 11.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_4(self):
        self.assertEqual(run_calculator('34', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/4 = 8.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_5(self):
        self.assertEqual(run_calculator('34', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/5 = 6.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_6(self):
        self.assertEqual(run_calculator('34', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/6 = 5.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_7(self):
        self.assertEqual(run_calculator('34', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/7 = 4.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_8(self):
        self.assertEqual(run_calculator('34', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/8 = 4.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_9(self):
        self.assertEqual(run_calculator('34', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/9 = 3.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_10(self):
        self.assertEqual(run_calculator('34', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/10 = 3.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_11(self):
        self.assertEqual(run_calculator('34', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/11 = 3.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_12(self):
        self.assertEqual(run_calculator('34', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/12 = 2.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_13(self):
        self.assertEqual(run_calculator('34', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/13 = 2.615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_14(self):
        self.assertEqual(run_calculator('34', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/14 = 2.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_15(self):
        self.assertEqual(run_calculator('34', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/15 = 2.266666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_16(self):
        self.assertEqual(run_calculator('34', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/16 = 2.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_17(self):
        self.assertEqual(run_calculator('34', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/17 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_18(self):
        self.assertEqual(run_calculator('34', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/18 = 1.888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_19(self):
        self.assertEqual(run_calculator('34', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/19 = 1.789473684210526315789473684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_20(self):
        self.assertEqual(run_calculator('34', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/20 = 1.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_21(self):
        self.assertEqual(run_calculator('34', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/21 = 1.619047619047619047619047619',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_22(self):
        self.assertEqual(run_calculator('34', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/22 = 1.545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_23(self):
        self.assertEqual(run_calculator('34', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/23 = 1.478260869565217391304347826',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_24(self):
        self.assertEqual(run_calculator('34', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/24 = 1.416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_25(self):
        self.assertEqual(run_calculator('34', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/25 = 1.36',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_26(self):
        self.assertEqual(run_calculator('34', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/26 = 1.307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_27(self):
        self.assertEqual(run_calculator('34', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/27 = 1.259259259259259259259259259',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_28(self):
        self.assertEqual(run_calculator('34', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/28 = 1.214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_29(self):
        self.assertEqual(run_calculator('34', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/29 = 1.172413793103448275862068966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_30(self):
        self.assertEqual(run_calculator('34', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/30 = 1.133333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_31(self):
        self.assertEqual(run_calculator('34', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/31 = 1.096774193548387096774193548',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_32(self):
        self.assertEqual(run_calculator('34', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/32 = 1.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_33(self):
        self.assertEqual(run_calculator('34', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/33 = 1.030303030303030303030303030',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_34(self):
        self.assertEqual(run_calculator('34', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/34 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_35(self):
        self.assertEqual(run_calculator('34', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/35 = 0.9714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_36(self):
        self.assertEqual(run_calculator('34', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/36 = 0.9444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_37(self):
        self.assertEqual(run_calculator('34', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/37 = 0.9189189189189189189189189189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_38(self):
        self.assertEqual(run_calculator('34', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/38 = 0.8947368421052631578947368421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_39(self):
        self.assertEqual(run_calculator('34', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/39 = 0.8717948717948717948717948718',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_40(self):
        self.assertEqual(run_calculator('34', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/40 = 0.85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_41(self):
        self.assertEqual(run_calculator('34', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/41 = 0.8292682926829268292682926829',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_42(self):
        self.assertEqual(run_calculator('34', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/42 = 0.8095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_43(self):
        self.assertEqual(run_calculator('34', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/43 = 0.7906976744186046511627906977',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_44(self):
        self.assertEqual(run_calculator('34', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/44 = 0.7727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_45(self):
        self.assertEqual(run_calculator('34', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/45 = 0.7555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_46(self):
        self.assertEqual(run_calculator('34', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/46 = 0.7391304347826086956521739130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_47(self):
        self.assertEqual(run_calculator('34', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/47 = 0.7234042553191489361702127660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_48(self):
        self.assertEqual(run_calculator('34', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/48 = 0.7083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_49(self):
        self.assertEqual(run_calculator('34', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/49 = 0.6938775510204081632653061224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_divided_by_50(self):
        self.assertEqual(run_calculator('34', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34/50 = 0.68',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
