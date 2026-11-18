# test_divided_by_47.py
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


class TestDividedBy47(unittest.TestCase):

    def test_47_divided_by_0(self):
        self.assertEqual(run_calculator('47', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_1(self):
        self.assertEqual(run_calculator('47', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/1 = 47',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_2(self):
        self.assertEqual(run_calculator('47', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/2 = 23.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_3(self):
        self.assertEqual(run_calculator('47', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/3 = 15.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_4(self):
        self.assertEqual(run_calculator('47', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/4 = 11.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_5(self):
        self.assertEqual(run_calculator('47', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/5 = 9.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_6(self):
        self.assertEqual(run_calculator('47', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/6 = 7.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_7(self):
        self.assertEqual(run_calculator('47', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/7 = 6.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_8(self):
        self.assertEqual(run_calculator('47', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/8 = 5.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_9(self):
        self.assertEqual(run_calculator('47', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/9 = 5.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_10(self):
        self.assertEqual(run_calculator('47', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/10 = 4.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_11(self):
        self.assertEqual(run_calculator('47', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/11 = 4.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_12(self):
        self.assertEqual(run_calculator('47', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/12 = 3.916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_13(self):
        self.assertEqual(run_calculator('47', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/13 = 3.615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_14(self):
        self.assertEqual(run_calculator('47', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/14 = 3.357142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_15(self):
        self.assertEqual(run_calculator('47', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/15 = 3.133333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_16(self):
        self.assertEqual(run_calculator('47', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/16 = 2.9375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_17(self):
        self.assertEqual(run_calculator('47', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/17 = 2.764705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_18(self):
        self.assertEqual(run_calculator('47', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/18 = 2.611111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_19(self):
        self.assertEqual(run_calculator('47', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/19 = 2.473684210526315789473684211',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_20(self):
        self.assertEqual(run_calculator('47', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/20 = 2.35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_21(self):
        self.assertEqual(run_calculator('47', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/21 = 2.238095238095238095238095238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_22(self):
        self.assertEqual(run_calculator('47', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/22 = 2.136363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_23(self):
        self.assertEqual(run_calculator('47', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/23 = 2.043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_24(self):
        self.assertEqual(run_calculator('47', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/24 = 1.958333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_25(self):
        self.assertEqual(run_calculator('47', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/25 = 1.88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_26(self):
        self.assertEqual(run_calculator('47', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/26 = 1.807692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_27(self):
        self.assertEqual(run_calculator('47', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/27 = 1.740740740740740740740740741',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_28(self):
        self.assertEqual(run_calculator('47', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/28 = 1.678571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_29(self):
        self.assertEqual(run_calculator('47', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/29 = 1.620689655172413793103448276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_30(self):
        self.assertEqual(run_calculator('47', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/30 = 1.566666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_31(self):
        self.assertEqual(run_calculator('47', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/31 = 1.516129032258064516129032258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_32(self):
        self.assertEqual(run_calculator('47', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/32 = 1.46875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_33(self):
        self.assertEqual(run_calculator('47', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/33 = 1.424242424242424242424242424',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_34(self):
        self.assertEqual(run_calculator('47', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/34 = 1.382352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_35(self):
        self.assertEqual(run_calculator('47', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/35 = 1.342857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_36(self):
        self.assertEqual(run_calculator('47', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/36 = 1.305555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_37(self):
        self.assertEqual(run_calculator('47', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/37 = 1.270270270270270270270270270',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_38(self):
        self.assertEqual(run_calculator('47', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/38 = 1.236842105263157894736842105',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_39(self):
        self.assertEqual(run_calculator('47', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/39 = 1.205128205128205128205128205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_40(self):
        self.assertEqual(run_calculator('47', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/40 = 1.175',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_41(self):
        self.assertEqual(run_calculator('47', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/41 = 1.146341463414634146341463415',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_42(self):
        self.assertEqual(run_calculator('47', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/42 = 1.119047619047619047619047619',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_43(self):
        self.assertEqual(run_calculator('47', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/43 = 1.093023255813953488372093023',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_44(self):
        self.assertEqual(run_calculator('47', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/44 = 1.068181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_45(self):
        self.assertEqual(run_calculator('47', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/45 = 1.044444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_46(self):
        self.assertEqual(run_calculator('47', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/46 = 1.021739130434782608695652174',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_47(self):
        self.assertEqual(run_calculator('47', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/47 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_48(self):
        self.assertEqual(run_calculator('47', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/48 = 0.9791666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_49(self):
        self.assertEqual(run_calculator('47', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/49 = 0.9591836734693877551020408163',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_47_divided_by_50(self):
        self.assertEqual(run_calculator('47', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '47/50 = 0.94',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
