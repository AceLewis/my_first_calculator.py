# test_divided_by_44.py
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


class TestDividedBy44(unittest.TestCase):

    def test_44_divided_by_0(self):
        self.assertEqual(run_calculator('44', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_1(self):
        self.assertEqual(run_calculator('44', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/1 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_2(self):
        self.assertEqual(run_calculator('44', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/2 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_3(self):
        self.assertEqual(run_calculator('44', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/3 = 14.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_4(self):
        self.assertEqual(run_calculator('44', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/4 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_5(self):
        self.assertEqual(run_calculator('44', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/5 = 8.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_6(self):
        self.assertEqual(run_calculator('44', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/6 = 7.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_7(self):
        self.assertEqual(run_calculator('44', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/7 = 6.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_8(self):
        self.assertEqual(run_calculator('44', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/8 = 5.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_9(self):
        self.assertEqual(run_calculator('44', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/9 = 4.888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_10(self):
        self.assertEqual(run_calculator('44', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/10 = 4.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_11(self):
        self.assertEqual(run_calculator('44', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/11 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_12(self):
        self.assertEqual(run_calculator('44', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/12 = 3.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_13(self):
        self.assertEqual(run_calculator('44', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/13 = 3.384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_14(self):
        self.assertEqual(run_calculator('44', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/14 = 3.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_15(self):
        self.assertEqual(run_calculator('44', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/15 = 2.933333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_16(self):
        self.assertEqual(run_calculator('44', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/16 = 2.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_17(self):
        self.assertEqual(run_calculator('44', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/17 = 2.588235294117647058823529412',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_18(self):
        self.assertEqual(run_calculator('44', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/18 = 2.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_19(self):
        self.assertEqual(run_calculator('44', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/19 = 2.315789473684210526315789474',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_20(self):
        self.assertEqual(run_calculator('44', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/20 = 2.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_21(self):
        self.assertEqual(run_calculator('44', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/21 = 2.095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_22(self):
        self.assertEqual(run_calculator('44', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/22 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_23(self):
        self.assertEqual(run_calculator('44', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/23 = 1.913043478260869565217391304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_24(self):
        self.assertEqual(run_calculator('44', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/24 = 1.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_25(self):
        self.assertEqual(run_calculator('44', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/25 = 1.76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_26(self):
        self.assertEqual(run_calculator('44', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/26 = 1.692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_27(self):
        self.assertEqual(run_calculator('44', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/27 = 1.629629629629629629629629630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_28(self):
        self.assertEqual(run_calculator('44', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/28 = 1.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_29(self):
        self.assertEqual(run_calculator('44', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/29 = 1.517241379310344827586206897',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_30(self):
        self.assertEqual(run_calculator('44', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/30 = 1.466666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_31(self):
        self.assertEqual(run_calculator('44', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/31 = 1.419354838709677419354838710',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_32(self):
        self.assertEqual(run_calculator('44', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/32 = 1.375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_33(self):
        self.assertEqual(run_calculator('44', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/33 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_34(self):
        self.assertEqual(run_calculator('44', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/34 = 1.294117647058823529411764706',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_35(self):
        self.assertEqual(run_calculator('44', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/35 = 1.257142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_36(self):
        self.assertEqual(run_calculator('44', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/36 = 1.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_37(self):
        self.assertEqual(run_calculator('44', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/37 = 1.189189189189189189189189189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_38(self):
        self.assertEqual(run_calculator('44', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/38 = 1.157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_39(self):
        self.assertEqual(run_calculator('44', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/39 = 1.128205128205128205128205128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_40(self):
        self.assertEqual(run_calculator('44', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/40 = 1.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_41(self):
        self.assertEqual(run_calculator('44', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/41 = 1.073170731707317073170731707',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_42(self):
        self.assertEqual(run_calculator('44', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/42 = 1.047619047619047619047619048',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_43(self):
        self.assertEqual(run_calculator('44', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/43 = 1.023255813953488372093023256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_44(self):
        self.assertEqual(run_calculator('44', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/44 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_45(self):
        self.assertEqual(run_calculator('44', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/45 = 0.9777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_46(self):
        self.assertEqual(run_calculator('44', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/46 = 0.9565217391304347826086956522',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_47(self):
        self.assertEqual(run_calculator('44', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/47 = 0.9361702127659574468085106383',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_48(self):
        self.assertEqual(run_calculator('44', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/48 = 0.9166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_49(self):
        self.assertEqual(run_calculator('44', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/49 = 0.8979591836734693877551020408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_44_divided_by_50(self):
        self.assertEqual(run_calculator('44', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '44/50 = 0.88',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
