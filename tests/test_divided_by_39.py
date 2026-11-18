# test_divided_by_39.py
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


class TestDividedBy39(unittest.TestCase):

    def test_39_divided_by_0(self):
        self.assertEqual(run_calculator('39', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_1(self):
        self.assertEqual(run_calculator('39', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/1 = 39',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_2(self):
        self.assertEqual(run_calculator('39', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/2 = 19.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_3(self):
        self.assertEqual(run_calculator('39', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/3 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_4(self):
        self.assertEqual(run_calculator('39', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/4 = 9.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_5(self):
        self.assertEqual(run_calculator('39', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/5 = 7.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_6(self):
        self.assertEqual(run_calculator('39', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/6 = 6.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_7(self):
        self.assertEqual(run_calculator('39', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/7 = 5.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_8(self):
        self.assertEqual(run_calculator('39', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/8 = 4.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_9(self):
        self.assertEqual(run_calculator('39', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/9 = 4.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_10(self):
        self.assertEqual(run_calculator('39', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/10 = 3.9',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_11(self):
        self.assertEqual(run_calculator('39', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/11 = 3.545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_12(self):
        self.assertEqual(run_calculator('39', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/12 = 3.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_13(self):
        self.assertEqual(run_calculator('39', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/13 = 3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_14(self):
        self.assertEqual(run_calculator('39', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/14 = 2.785714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_15(self):
        self.assertEqual(run_calculator('39', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/15 = 2.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_16(self):
        self.assertEqual(run_calculator('39', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/16 = 2.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_17(self):
        self.assertEqual(run_calculator('39', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/17 = 2.294117647058823529411764706',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_18(self):
        self.assertEqual(run_calculator('39', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/18 = 2.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_19(self):
        self.assertEqual(run_calculator('39', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/19 = 2.052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_20(self):
        self.assertEqual(run_calculator('39', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/20 = 1.95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_21(self):
        self.assertEqual(run_calculator('39', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/21 = 1.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_22(self):
        self.assertEqual(run_calculator('39', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/22 = 1.772727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_23(self):
        self.assertEqual(run_calculator('39', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/23 = 1.695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_24(self):
        self.assertEqual(run_calculator('39', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/24 = 1.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_25(self):
        self.assertEqual(run_calculator('39', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/25 = 1.56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_26(self):
        self.assertEqual(run_calculator('39', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/26 = 1.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_27(self):
        self.assertEqual(run_calculator('39', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/27 = 1.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_28(self):
        self.assertEqual(run_calculator('39', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/28 = 1.392857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_29(self):
        self.assertEqual(run_calculator('39', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/29 = 1.344827586206896551724137931',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_30(self):
        self.assertEqual(run_calculator('39', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/30 = 1.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_31(self):
        self.assertEqual(run_calculator('39', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/31 = 1.258064516129032258064516129',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_32(self):
        self.assertEqual(run_calculator('39', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/32 = 1.21875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_33(self):
        self.assertEqual(run_calculator('39', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/33 = 1.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_34(self):
        self.assertEqual(run_calculator('39', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/34 = 1.147058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_35(self):
        self.assertEqual(run_calculator('39', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/35 = 1.114285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_36(self):
        self.assertEqual(run_calculator('39', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/36 = 1.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_37(self):
        self.assertEqual(run_calculator('39', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/37 = 1.054054054054054054054054054',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_38(self):
        self.assertEqual(run_calculator('39', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/38 = 1.026315789473684210526315789',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_39(self):
        self.assertEqual(run_calculator('39', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/39 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_40(self):
        self.assertEqual(run_calculator('39', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/40 = 0.975',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_41(self):
        self.assertEqual(run_calculator('39', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/41 = 0.9512195121951219512195121951',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_42(self):
        self.assertEqual(run_calculator('39', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/42 = 0.9285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_43(self):
        self.assertEqual(run_calculator('39', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/43 = 0.9069767441860465116279069767',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_44(self):
        self.assertEqual(run_calculator('39', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/44 = 0.8863636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_45(self):
        self.assertEqual(run_calculator('39', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/45 = 0.8666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_46(self):
        self.assertEqual(run_calculator('39', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/46 = 0.8478260869565217391304347826',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_47(self):
        self.assertEqual(run_calculator('39', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/47 = 0.8297872340425531914893617021',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_48(self):
        self.assertEqual(run_calculator('39', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/48 = 0.8125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_49(self):
        self.assertEqual(run_calculator('39', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/49 = 0.7959183673469387755102040816',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_39_divided_by_50(self):
        self.assertEqual(run_calculator('39', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '39/50 = 0.78',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
