# test_divided_by_25.py
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


class TestDividedBy25(unittest.TestCase):

    def test_25_divided_by_0(self):
        self.assertEqual(run_calculator('25', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_1(self):
        self.assertEqual(run_calculator('25', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/1 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_2(self):
        self.assertEqual(run_calculator('25', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/2 = 12.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_3(self):
        self.assertEqual(run_calculator('25', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/3 = 8.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_4(self):
        self.assertEqual(run_calculator('25', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/4 = 6.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_5(self):
        self.assertEqual(run_calculator('25', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/5 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_6(self):
        self.assertEqual(run_calculator('25', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/6 = 4.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_7(self):
        self.assertEqual(run_calculator('25', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/7 = 3.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_8(self):
        self.assertEqual(run_calculator('25', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/8 = 3.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_9(self):
        self.assertEqual(run_calculator('25', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/9 = 2.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_10(self):
        self.assertEqual(run_calculator('25', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/10 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_11(self):
        self.assertEqual(run_calculator('25', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/11 = 2.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_12(self):
        self.assertEqual(run_calculator('25', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/12 = 2.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_13(self):
        self.assertEqual(run_calculator('25', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/13 = 1.923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_14(self):
        self.assertEqual(run_calculator('25', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/14 = 1.785714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_15(self):
        self.assertEqual(run_calculator('25', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/15 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_16(self):
        self.assertEqual(run_calculator('25', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/16 = 1.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_17(self):
        self.assertEqual(run_calculator('25', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/17 = 1.470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_18(self):
        self.assertEqual(run_calculator('25', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/18 = 1.388888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_19(self):
        self.assertEqual(run_calculator('25', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/19 = 1.315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_20(self):
        self.assertEqual(run_calculator('25', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/20 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_21(self):
        self.assertEqual(run_calculator('25', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/21 = 1.190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_22(self):
        self.assertEqual(run_calculator('25', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/22 = 1.136363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_23(self):
        self.assertEqual(run_calculator('25', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/23 = 1.086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_24(self):
        self.assertEqual(run_calculator('25', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/24 = 1.041666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_25(self):
        self.assertEqual(run_calculator('25', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/25 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_26(self):
        self.assertEqual(run_calculator('25', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/26 = 0.9615384615384615384615384615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_27(self):
        self.assertEqual(run_calculator('25', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/27 = 0.9259259259259259259259259259',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_28(self):
        self.assertEqual(run_calculator('25', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/28 = 0.8928571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_29(self):
        self.assertEqual(run_calculator('25', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/29 = 0.8620689655172413793103448276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_30(self):
        self.assertEqual(run_calculator('25', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/30 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_31(self):
        self.assertEqual(run_calculator('25', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/31 = 0.8064516129032258064516129032',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_32(self):
        self.assertEqual(run_calculator('25', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/32 = 0.78125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_33(self):
        self.assertEqual(run_calculator('25', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/33 = 0.7575757575757575757575757576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_34(self):
        self.assertEqual(run_calculator('25', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/34 = 0.7352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_35(self):
        self.assertEqual(run_calculator('25', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/35 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_36(self):
        self.assertEqual(run_calculator('25', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/36 = 0.6944444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_37(self):
        self.assertEqual(run_calculator('25', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/37 = 0.6756756756756756756756756757',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_38(self):
        self.assertEqual(run_calculator('25', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/38 = 0.6578947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_39(self):
        self.assertEqual(run_calculator('25', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/39 = 0.6410256410256410256410256410',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_40(self):
        self.assertEqual(run_calculator('25', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/40 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_41(self):
        self.assertEqual(run_calculator('25', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/41 = 0.6097560975609756097560975610',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_42(self):
        self.assertEqual(run_calculator('25', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/42 = 0.5952380952380952380952380952',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_43(self):
        self.assertEqual(run_calculator('25', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/43 = 0.5813953488372093023255813953',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_44(self):
        self.assertEqual(run_calculator('25', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/44 = 0.5681818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_45(self):
        self.assertEqual(run_calculator('25', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/45 = 0.5555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_46(self):
        self.assertEqual(run_calculator('25', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/46 = 0.5434782608695652173913043478',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_47(self):
        self.assertEqual(run_calculator('25', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/47 = 0.5319148936170212765957446809',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_48(self):
        self.assertEqual(run_calculator('25', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/48 = 0.5208333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_49(self):
        self.assertEqual(run_calculator('25', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/49 = 0.5102040816326530612244897959',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_25_divided_by_50(self):
        self.assertEqual(run_calculator('25', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '25/50 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
