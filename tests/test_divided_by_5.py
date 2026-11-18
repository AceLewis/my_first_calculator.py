# test_divided_by_5.py
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


class TestDividedBy5(unittest.TestCase):

    def test_5_divided_by_0(self):
        self.assertEqual(run_calculator('5', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_1(self):
        self.assertEqual(run_calculator('5', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/1 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_2(self):
        self.assertEqual(run_calculator('5', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/2 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_3(self):
        self.assertEqual(run_calculator('5', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/3 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_4(self):
        self.assertEqual(run_calculator('5', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/4 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_5(self):
        self.assertEqual(run_calculator('5', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/5 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_6(self):
        self.assertEqual(run_calculator('5', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/6 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_7(self):
        self.assertEqual(run_calculator('5', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/7 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_8(self):
        self.assertEqual(run_calculator('5', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/8 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_9(self):
        self.assertEqual(run_calculator('5', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/9 = 0.5555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_10(self):
        self.assertEqual(run_calculator('5', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/10 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_11(self):
        self.assertEqual(run_calculator('5', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/11 = 0.4545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_12(self):
        self.assertEqual(run_calculator('5', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/12 = 0.4166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_13(self):
        self.assertEqual(run_calculator('5', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/13 = 0.3846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_14(self):
        self.assertEqual(run_calculator('5', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/14 = 0.3571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_15(self):
        self.assertEqual(run_calculator('5', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/15 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_16(self):
        self.assertEqual(run_calculator('5', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/16 = 0.3125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_17(self):
        self.assertEqual(run_calculator('5', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/17 = 0.2941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_18(self):
        self.assertEqual(run_calculator('5', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/18 = 0.2777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_19(self):
        self.assertEqual(run_calculator('5', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/19 = 0.2631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_20(self):
        self.assertEqual(run_calculator('5', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/20 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_21(self):
        self.assertEqual(run_calculator('5', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/21 = 0.2380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_22(self):
        self.assertEqual(run_calculator('5', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/22 = 0.2272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_23(self):
        self.assertEqual(run_calculator('5', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/23 = 0.2173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_24(self):
        self.assertEqual(run_calculator('5', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/24 = 0.2083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_25(self):
        self.assertEqual(run_calculator('5', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/25 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_26(self):
        self.assertEqual(run_calculator('5', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/26 = 0.1923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_27(self):
        self.assertEqual(run_calculator('5', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/27 = 0.1851851851851851851851851852',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_28(self):
        self.assertEqual(run_calculator('5', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/28 = 0.1785714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_29(self):
        self.assertEqual(run_calculator('5', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/29 = 0.1724137931034482758620689655',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_30(self):
        self.assertEqual(run_calculator('5', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/30 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_31(self):
        self.assertEqual(run_calculator('5', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/31 = 0.1612903225806451612903225806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_32(self):
        self.assertEqual(run_calculator('5', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/32 = 0.15625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_33(self):
        self.assertEqual(run_calculator('5', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/33 = 0.1515151515151515151515151515',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_34(self):
        self.assertEqual(run_calculator('5', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/34 = 0.1470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_35(self):
        self.assertEqual(run_calculator('5', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/35 = 0.1428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_36(self):
        self.assertEqual(run_calculator('5', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/36 = 0.1388888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_37(self):
        self.assertEqual(run_calculator('5', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/37 = 0.1351351351351351351351351351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_38(self):
        self.assertEqual(run_calculator('5', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/38 = 0.1315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_39(self):
        self.assertEqual(run_calculator('5', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/39 = 0.1282051282051282051282051282',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_40(self):
        self.assertEqual(run_calculator('5', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/40 = 0.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_41(self):
        self.assertEqual(run_calculator('5', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/41 = 0.1219512195121951219512195122',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_42(self):
        self.assertEqual(run_calculator('5', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/42 = 0.1190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_43(self):
        self.assertEqual(run_calculator('5', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/43 = 0.1162790697674418604651162791',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_44(self):
        self.assertEqual(run_calculator('5', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/44 = 0.1136363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_45(self):
        self.assertEqual(run_calculator('5', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/45 = 0.1111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_46(self):
        self.assertEqual(run_calculator('5', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/46 = 0.1086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_47(self):
        self.assertEqual(run_calculator('5', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/47 = 0.1063829787234042553191489362',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_48(self):
        self.assertEqual(run_calculator('5', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/48 = 0.1041666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_49(self):
        self.assertEqual(run_calculator('5', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/49 = 0.1020408163265306122448979592',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_5_divided_by_50(self):
        self.assertEqual(run_calculator('5', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '5/50 = 0.1',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
