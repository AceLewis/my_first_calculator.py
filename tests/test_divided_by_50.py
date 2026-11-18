# test_divided_by_50.py
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


class TestDividedBy50(unittest.TestCase):

    def test_50_divided_by_0(self):
        self.assertEqual(run_calculator('50', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_1(self):
        self.assertEqual(run_calculator('50', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/1 = 50',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_2(self):
        self.assertEqual(run_calculator('50', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/2 = 25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_3(self):
        self.assertEqual(run_calculator('50', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/3 = 16.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_4(self):
        self.assertEqual(run_calculator('50', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/4 = 12.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_5(self):
        self.assertEqual(run_calculator('50', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/5 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_6(self):
        self.assertEqual(run_calculator('50', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/6 = 8.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_7(self):
        self.assertEqual(run_calculator('50', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/7 = 7.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_8(self):
        self.assertEqual(run_calculator('50', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/8 = 6.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_9(self):
        self.assertEqual(run_calculator('50', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/9 = 5.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_10(self):
        self.assertEqual(run_calculator('50', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/10 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_11(self):
        self.assertEqual(run_calculator('50', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/11 = 4.545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_12(self):
        self.assertEqual(run_calculator('50', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/12 = 4.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_13(self):
        self.assertEqual(run_calculator('50', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/13 = 3.846153846153846153846153846',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_14(self):
        self.assertEqual(run_calculator('50', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/14 = 3.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_15(self):
        self.assertEqual(run_calculator('50', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/15 = 3.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_16(self):
        self.assertEqual(run_calculator('50', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/16 = 3.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_17(self):
        self.assertEqual(run_calculator('50', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/17 = 2.941176470588235294117647059',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_18(self):
        self.assertEqual(run_calculator('50', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/18 = 2.777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_19(self):
        self.assertEqual(run_calculator('50', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/19 = 2.631578947368421052631578947',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_20(self):
        self.assertEqual(run_calculator('50', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/20 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_21(self):
        self.assertEqual(run_calculator('50', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/21 = 2.380952380952380952380952381',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_22(self):
        self.assertEqual(run_calculator('50', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/22 = 2.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_23(self):
        self.assertEqual(run_calculator('50', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/23 = 2.173913043478260869565217391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_24(self):
        self.assertEqual(run_calculator('50', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/24 = 2.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_25(self):
        self.assertEqual(run_calculator('50', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/25 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_26(self):
        self.assertEqual(run_calculator('50', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/26 = 1.923076923076923076923076923',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_27(self):
        self.assertEqual(run_calculator('50', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/27 = 1.851851851851851851851851852',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_28(self):
        self.assertEqual(run_calculator('50', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/28 = 1.785714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_29(self):
        self.assertEqual(run_calculator('50', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/29 = 1.724137931034482758620689655',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_30(self):
        self.assertEqual(run_calculator('50', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/30 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_31(self):
        self.assertEqual(run_calculator('50', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/31 = 1.612903225806451612903225806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_32(self):
        self.assertEqual(run_calculator('50', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/32 = 1.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_33(self):
        self.assertEqual(run_calculator('50', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/33 = 1.515151515151515151515151515',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_34(self):
        self.assertEqual(run_calculator('50', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/34 = 1.470588235294117647058823529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_35(self):
        self.assertEqual(run_calculator('50', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/35 = 1.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_36(self):
        self.assertEqual(run_calculator('50', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/36 = 1.388888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_37(self):
        self.assertEqual(run_calculator('50', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/37 = 1.351351351351351351351351351',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_38(self):
        self.assertEqual(run_calculator('50', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/38 = 1.315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_39(self):
        self.assertEqual(run_calculator('50', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/39 = 1.282051282051282051282051282',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_40(self):
        self.assertEqual(run_calculator('50', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/40 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_41(self):
        self.assertEqual(run_calculator('50', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/41 = 1.219512195121951219512195122',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_42(self):
        self.assertEqual(run_calculator('50', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/42 = 1.190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_43(self):
        self.assertEqual(run_calculator('50', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/43 = 1.162790697674418604651162791',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_44(self):
        self.assertEqual(run_calculator('50', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/44 = 1.136363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_45(self):
        self.assertEqual(run_calculator('50', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/45 = 1.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_46(self):
        self.assertEqual(run_calculator('50', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/46 = 1.086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_47(self):
        self.assertEqual(run_calculator('50', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/47 = 1.063829787234042553191489362',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_48(self):
        self.assertEqual(run_calculator('50', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/48 = 1.041666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_49(self):
        self.assertEqual(run_calculator('50', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/49 = 1.020408163265306122448979592',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_50_divided_by_50(self):
        self.assertEqual(run_calculator('50', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '50/50 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
