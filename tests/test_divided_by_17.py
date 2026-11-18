# test_divided_by_17.py
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


class TestDividedBy17(unittest.TestCase):

    def test_17_divided_by_0(self):
        self.assertEqual(run_calculator('17', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_1(self):
        self.assertEqual(run_calculator('17', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/1 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_2(self):
        self.assertEqual(run_calculator('17', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/2 = 8.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_3(self):
        self.assertEqual(run_calculator('17', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/3 = 5.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_4(self):
        self.assertEqual(run_calculator('17', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/4 = 4.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_5(self):
        self.assertEqual(run_calculator('17', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/5 = 3.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_6(self):
        self.assertEqual(run_calculator('17', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/6 = 2.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_7(self):
        self.assertEqual(run_calculator('17', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/7 = 2.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_8(self):
        self.assertEqual(run_calculator('17', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/8 = 2.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_9(self):
        self.assertEqual(run_calculator('17', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/9 = 1.888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_10(self):
        self.assertEqual(run_calculator('17', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/10 = 1.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_11(self):
        self.assertEqual(run_calculator('17', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/11 = 1.545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_12(self):
        self.assertEqual(run_calculator('17', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/12 = 1.416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_13(self):
        self.assertEqual(run_calculator('17', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/13 = 1.307692307692307692307692308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_14(self):
        self.assertEqual(run_calculator('17', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/14 = 1.214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_15(self):
        self.assertEqual(run_calculator('17', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/15 = 1.133333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_16(self):
        self.assertEqual(run_calculator('17', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/16 = 1.0625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_17(self):
        self.assertEqual(run_calculator('17', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/17 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_18(self):
        self.assertEqual(run_calculator('17', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/18 = 0.9444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_19(self):
        self.assertEqual(run_calculator('17', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/19 = 0.8947368421052631578947368421',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_20(self):
        self.assertEqual(run_calculator('17', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/20 = 0.85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_21(self):
        self.assertEqual(run_calculator('17', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/21 = 0.8095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_22(self):
        self.assertEqual(run_calculator('17', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/22 = 0.7727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_23(self):
        self.assertEqual(run_calculator('17', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/23 = 0.7391304347826086956521739130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_24(self):
        self.assertEqual(run_calculator('17', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/24 = 0.7083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_25(self):
        self.assertEqual(run_calculator('17', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/25 = 0.68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_26(self):
        self.assertEqual(run_calculator('17', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/26 = 0.6538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_27(self):
        self.assertEqual(run_calculator('17', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/27 = 0.6296296296296296296296296296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_28(self):
        self.assertEqual(run_calculator('17', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/28 = 0.6071428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_29(self):
        self.assertEqual(run_calculator('17', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/29 = 0.5862068965517241379310344828',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_30(self):
        self.assertEqual(run_calculator('17', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/30 = 0.5666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_31(self):
        self.assertEqual(run_calculator('17', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/31 = 0.5483870967741935483870967742',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_32(self):
        self.assertEqual(run_calculator('17', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/32 = 0.53125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_33(self):
        self.assertEqual(run_calculator('17', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/33 = 0.5151515151515151515151515152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_34(self):
        self.assertEqual(run_calculator('17', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/34 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_35(self):
        self.assertEqual(run_calculator('17', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/35 = 0.4857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_36(self):
        self.assertEqual(run_calculator('17', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/36 = 0.4722222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_37(self):
        self.assertEqual(run_calculator('17', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/37 = 0.4594594594594594594594594595',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_38(self):
        self.assertEqual(run_calculator('17', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/38 = 0.4473684210526315789473684211',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_39(self):
        self.assertEqual(run_calculator('17', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/39 = 0.4358974358974358974358974359',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_40(self):
        self.assertEqual(run_calculator('17', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/40 = 0.425',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_41(self):
        self.assertEqual(run_calculator('17', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/41 = 0.4146341463414634146341463415',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_42(self):
        self.assertEqual(run_calculator('17', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/42 = 0.4047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_43(self):
        self.assertEqual(run_calculator('17', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/43 = 0.3953488372093023255813953488',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_44(self):
        self.assertEqual(run_calculator('17', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/44 = 0.3863636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_45(self):
        self.assertEqual(run_calculator('17', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/45 = 0.3777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_46(self):
        self.assertEqual(run_calculator('17', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/46 = 0.3695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_47(self):
        self.assertEqual(run_calculator('17', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/47 = 0.3617021276595744680851063830',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_48(self):
        self.assertEqual(run_calculator('17', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/48 = 0.3541666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_49(self):
        self.assertEqual(run_calculator('17', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/49 = 0.3469387755102040816326530612',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_divided_by_50(self):
        self.assertEqual(run_calculator('17', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17/50 = 0.34',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
