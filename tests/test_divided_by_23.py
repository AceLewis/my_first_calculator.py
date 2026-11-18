# test_divided_by_23.py
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


class TestDividedBy23(unittest.TestCase):

    def test_23_divided_by_0(self):
        self.assertEqual(run_calculator('23', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_1(self):
        self.assertEqual(run_calculator('23', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/1 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_2(self):
        self.assertEqual(run_calculator('23', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/2 = 11.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_3(self):
        self.assertEqual(run_calculator('23', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/3 = 7.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_4(self):
        self.assertEqual(run_calculator('23', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/4 = 5.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_5(self):
        self.assertEqual(run_calculator('23', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/5 = 4.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_6(self):
        self.assertEqual(run_calculator('23', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/6 = 3.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_7(self):
        self.assertEqual(run_calculator('23', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/7 = 3.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_8(self):
        self.assertEqual(run_calculator('23', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/8 = 2.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_9(self):
        self.assertEqual(run_calculator('23', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/9 = 2.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_10(self):
        self.assertEqual(run_calculator('23', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/10 = 2.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_11(self):
        self.assertEqual(run_calculator('23', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/11 = 2.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_12(self):
        self.assertEqual(run_calculator('23', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/12 = 1.916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_13(self):
        self.assertEqual(run_calculator('23', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/13 = 1.769230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_14(self):
        self.assertEqual(run_calculator('23', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/14 = 1.642857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_15(self):
        self.assertEqual(run_calculator('23', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/15 = 1.533333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_16(self):
        self.assertEqual(run_calculator('23', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/16 = 1.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_17(self):
        self.assertEqual(run_calculator('23', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/17 = 1.352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_18(self):
        self.assertEqual(run_calculator('23', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/18 = 1.277777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_19(self):
        self.assertEqual(run_calculator('23', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/19 = 1.210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_20(self):
        self.assertEqual(run_calculator('23', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/20 = 1.15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_21(self):
        self.assertEqual(run_calculator('23', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/21 = 1.095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_22(self):
        self.assertEqual(run_calculator('23', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/22 = 1.045454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_23(self):
        self.assertEqual(run_calculator('23', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/23 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_24(self):
        self.assertEqual(run_calculator('23', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/24 = 0.9583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_25(self):
        self.assertEqual(run_calculator('23', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/25 = 0.92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_26(self):
        self.assertEqual(run_calculator('23', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/26 = 0.8846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_27(self):
        self.assertEqual(run_calculator('23', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/27 = 0.8518518518518518518518518519',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_28(self):
        self.assertEqual(run_calculator('23', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/28 = 0.8214285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_29(self):
        self.assertEqual(run_calculator('23', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/29 = 0.7931034482758620689655172414',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_30(self):
        self.assertEqual(run_calculator('23', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/30 = 0.7666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_31(self):
        self.assertEqual(run_calculator('23', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/31 = 0.7419354838709677419354838710',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_32(self):
        self.assertEqual(run_calculator('23', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/32 = 0.71875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_33(self):
        self.assertEqual(run_calculator('23', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/33 = 0.6969696969696969696969696970',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_34(self):
        self.assertEqual(run_calculator('23', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/34 = 0.6764705882352941176470588235',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_35(self):
        self.assertEqual(run_calculator('23', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/35 = 0.6571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_36(self):
        self.assertEqual(run_calculator('23', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/36 = 0.6388888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_37(self):
        self.assertEqual(run_calculator('23', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/37 = 0.6216216216216216216216216216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_38(self):
        self.assertEqual(run_calculator('23', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/38 = 0.6052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_39(self):
        self.assertEqual(run_calculator('23', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/39 = 0.5897435897435897435897435897',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_40(self):
        self.assertEqual(run_calculator('23', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/40 = 0.575',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_41(self):
        self.assertEqual(run_calculator('23', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/41 = 0.5609756097560975609756097561',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_42(self):
        self.assertEqual(run_calculator('23', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/42 = 0.5476190476190476190476190476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_43(self):
        self.assertEqual(run_calculator('23', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/43 = 0.5348837209302325581395348837',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_44(self):
        self.assertEqual(run_calculator('23', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/44 = 0.5227272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_45(self):
        self.assertEqual(run_calculator('23', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/45 = 0.5111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_46(self):
        self.assertEqual(run_calculator('23', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/46 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_47(self):
        self.assertEqual(run_calculator('23', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/47 = 0.4893617021276595744680851064',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_48(self):
        self.assertEqual(run_calculator('23', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/48 = 0.4791666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_49(self):
        self.assertEqual(run_calculator('23', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/49 = 0.4693877551020408163265306122',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_divided_by_50(self):
        self.assertEqual(run_calculator('23', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23/50 = 0.46',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
