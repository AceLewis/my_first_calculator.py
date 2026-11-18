# test_divided_by_37.py
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


class TestDividedBy37(unittest.TestCase):

    def test_37_divided_by_0(self):
        self.assertEqual(run_calculator('37', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_1(self):
        self.assertEqual(run_calculator('37', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/1 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_2(self):
        self.assertEqual(run_calculator('37', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/2 = 18.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_3(self):
        self.assertEqual(run_calculator('37', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/3 = 12.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_4(self):
        self.assertEqual(run_calculator('37', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/4 = 9.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_5(self):
        self.assertEqual(run_calculator('37', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/5 = 7.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_6(self):
        self.assertEqual(run_calculator('37', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/6 = 6.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_7(self):
        self.assertEqual(run_calculator('37', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/7 = 5.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_8(self):
        self.assertEqual(run_calculator('37', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/8 = 4.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_9(self):
        self.assertEqual(run_calculator('37', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/9 = 4.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_10(self):
        self.assertEqual(run_calculator('37', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/10 = 3.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_11(self):
        self.assertEqual(run_calculator('37', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/11 = 3.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_12(self):
        self.assertEqual(run_calculator('37', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/12 = 3.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_13(self):
        self.assertEqual(run_calculator('37', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/13 = 2.846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_14(self):
        self.assertEqual(run_calculator('37', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/14 = 2.642857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_15(self):
        self.assertEqual(run_calculator('37', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/15 = 2.466666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_16(self):
        self.assertEqual(run_calculator('37', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/16 = 2.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_17(self):
        self.assertEqual(run_calculator('37', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/17 = 2.176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_18(self):
        self.assertEqual(run_calculator('37', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/18 = 2.055555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_19(self):
        self.assertEqual(run_calculator('37', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/19 = 1.947368421052631578947368421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_20(self):
        self.assertEqual(run_calculator('37', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/20 = 1.85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_21(self):
        self.assertEqual(run_calculator('37', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/21 = 1.761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_22(self):
        self.assertEqual(run_calculator('37', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/22 = 1.681818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_23(self):
        self.assertEqual(run_calculator('37', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/23 = 1.608695652173913043478260870',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_24(self):
        self.assertEqual(run_calculator('37', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/24 = 1.541666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_25(self):
        self.assertEqual(run_calculator('37', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/25 = 1.48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_26(self):
        self.assertEqual(run_calculator('37', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/26 = 1.423076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_27(self):
        self.assertEqual(run_calculator('37', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/27 = 1.370370370370370370370370370',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_28(self):
        self.assertEqual(run_calculator('37', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/28 = 1.321428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_29(self):
        self.assertEqual(run_calculator('37', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/29 = 1.275862068965517241379310345',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_30(self):
        self.assertEqual(run_calculator('37', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/30 = 1.233333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_31(self):
        self.assertEqual(run_calculator('37', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/31 = 1.193548387096774193548387097',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_32(self):
        self.assertEqual(run_calculator('37', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/32 = 1.15625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_33(self):
        self.assertEqual(run_calculator('37', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/33 = 1.121212121212121212121212121',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_34(self):
        self.assertEqual(run_calculator('37', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/34 = 1.088235294117647058823529412',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_35(self):
        self.assertEqual(run_calculator('37', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/35 = 1.057142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_36(self):
        self.assertEqual(run_calculator('37', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/36 = 1.027777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_37(self):
        self.assertEqual(run_calculator('37', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/37 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_38(self):
        self.assertEqual(run_calculator('37', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/38 = 0.9736842105263157894736842105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_39(self):
        self.assertEqual(run_calculator('37', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/39 = 0.9487179487179487179487179487',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_40(self):
        self.assertEqual(run_calculator('37', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/40 = 0.925',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_41(self):
        self.assertEqual(run_calculator('37', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/41 = 0.9024390243902439024390243902',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_42(self):
        self.assertEqual(run_calculator('37', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/42 = 0.8809523809523809523809523810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_43(self):
        self.assertEqual(run_calculator('37', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/43 = 0.8604651162790697674418604651',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_44(self):
        self.assertEqual(run_calculator('37', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/44 = 0.8409090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_45(self):
        self.assertEqual(run_calculator('37', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/45 = 0.8222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_46(self):
        self.assertEqual(run_calculator('37', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/46 = 0.8043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_47(self):
        self.assertEqual(run_calculator('37', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/47 = 0.7872340425531914893617021277',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_48(self):
        self.assertEqual(run_calculator('37', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/48 = 0.7708333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_49(self):
        self.assertEqual(run_calculator('37', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/49 = 0.7551020408163265306122448980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_divided_by_50(self):
        self.assertEqual(run_calculator('37', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37/50 = 0.74',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
