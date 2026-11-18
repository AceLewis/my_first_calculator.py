# test_divided_by_27.py
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


class TestDividedBy27(unittest.TestCase):

    def test_27_divided_by_0(self):
        self.assertEqual(run_calculator('27', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_1(self):
        self.assertEqual(run_calculator('27', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/1 = 27',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_2(self):
        self.assertEqual(run_calculator('27', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/2 = 13.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_3(self):
        self.assertEqual(run_calculator('27', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/3 = 9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_4(self):
        self.assertEqual(run_calculator('27', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/4 = 6.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_5(self):
        self.assertEqual(run_calculator('27', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/5 = 5.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_6(self):
        self.assertEqual(run_calculator('27', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/6 = 4.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_7(self):
        self.assertEqual(run_calculator('27', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/7 = 3.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_8(self):
        self.assertEqual(run_calculator('27', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/8 = 3.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_9(self):
        self.assertEqual(run_calculator('27', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/9 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_10(self):
        self.assertEqual(run_calculator('27', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/10 = 2.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_11(self):
        self.assertEqual(run_calculator('27', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/11 = 2.454545454545454545454545455',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_12(self):
        self.assertEqual(run_calculator('27', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/12 = 2.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_13(self):
        self.assertEqual(run_calculator('27', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/13 = 2.076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_14(self):
        self.assertEqual(run_calculator('27', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/14 = 1.928571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_15(self):
        self.assertEqual(run_calculator('27', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/15 = 1.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_16(self):
        self.assertEqual(run_calculator('27', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/16 = 1.6875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_17(self):
        self.assertEqual(run_calculator('27', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/17 = 1.588235294117647058823529412',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_18(self):
        self.assertEqual(run_calculator('27', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/18 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_19(self):
        self.assertEqual(run_calculator('27', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/19 = 1.421052631578947368421052632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_20(self):
        self.assertEqual(run_calculator('27', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/20 = 1.35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_21(self):
        self.assertEqual(run_calculator('27', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/21 = 1.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_22(self):
        self.assertEqual(run_calculator('27', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/22 = 1.227272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_23(self):
        self.assertEqual(run_calculator('27', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/23 = 1.173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_24(self):
        self.assertEqual(run_calculator('27', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/24 = 1.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_25(self):
        self.assertEqual(run_calculator('27', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/25 = 1.08',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_26(self):
        self.assertEqual(run_calculator('27', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/26 = 1.038461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_27(self):
        self.assertEqual(run_calculator('27', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/27 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_28(self):
        self.assertEqual(run_calculator('27', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/28 = 0.9642857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_29(self):
        self.assertEqual(run_calculator('27', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/29 = 0.9310344827586206896551724138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_30(self):
        self.assertEqual(run_calculator('27', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/30 = 0.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_31(self):
        self.assertEqual(run_calculator('27', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/31 = 0.8709677419354838709677419355',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_32(self):
        self.assertEqual(run_calculator('27', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/32 = 0.84375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_33(self):
        self.assertEqual(run_calculator('27', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/33 = 0.8181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_34(self):
        self.assertEqual(run_calculator('27', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/34 = 0.7941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_35(self):
        self.assertEqual(run_calculator('27', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/35 = 0.7714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_36(self):
        self.assertEqual(run_calculator('27', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/36 = 0.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_37(self):
        self.assertEqual(run_calculator('27', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/37 = 0.7297297297297297297297297297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_38(self):
        self.assertEqual(run_calculator('27', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/38 = 0.7105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_39(self):
        self.assertEqual(run_calculator('27', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/39 = 0.6923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_40(self):
        self.assertEqual(run_calculator('27', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/40 = 0.675',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_41(self):
        self.assertEqual(run_calculator('27', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/41 = 0.6585365853658536585365853659',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_42(self):
        self.assertEqual(run_calculator('27', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/42 = 0.6428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_43(self):
        self.assertEqual(run_calculator('27', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/43 = 0.6279069767441860465116279070',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_44(self):
        self.assertEqual(run_calculator('27', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/44 = 0.6136363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_45(self):
        self.assertEqual(run_calculator('27', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/45 = 0.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_46(self):
        self.assertEqual(run_calculator('27', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/46 = 0.5869565217391304347826086957',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_47(self):
        self.assertEqual(run_calculator('27', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/47 = 0.5744680851063829787234042553',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_48(self):
        self.assertEqual(run_calculator('27', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/48 = 0.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_49(self):
        self.assertEqual(run_calculator('27', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/49 = 0.5510204081632653061224489796',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_27_divided_by_50(self):
        self.assertEqual(run_calculator('27', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '27/50 = 0.54',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
