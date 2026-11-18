# test_divided_by_20.py
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


class TestDividedBy20(unittest.TestCase):

    def test_20_divided_by_0(self):
        self.assertEqual(run_calculator('20', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_1(self):
        self.assertEqual(run_calculator('20', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/1 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_2(self):
        self.assertEqual(run_calculator('20', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/2 = 10',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_3(self):
        self.assertEqual(run_calculator('20', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/3 = 6.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_4(self):
        self.assertEqual(run_calculator('20', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/4 = 5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_5(self):
        self.assertEqual(run_calculator('20', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/5 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_6(self):
        self.assertEqual(run_calculator('20', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/6 = 3.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_7(self):
        self.assertEqual(run_calculator('20', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/7 = 2.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_8(self):
        self.assertEqual(run_calculator('20', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/8 = 2.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_9(self):
        self.assertEqual(run_calculator('20', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/9 = 2.222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_10(self):
        self.assertEqual(run_calculator('20', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/10 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_11(self):
        self.assertEqual(run_calculator('20', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/11 = 1.818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_12(self):
        self.assertEqual(run_calculator('20', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/12 = 1.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_13(self):
        self.assertEqual(run_calculator('20', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/13 = 1.538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_14(self):
        self.assertEqual(run_calculator('20', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/14 = 1.428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_15(self):
        self.assertEqual(run_calculator('20', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/15 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_16(self):
        self.assertEqual(run_calculator('20', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/16 = 1.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_17(self):
        self.assertEqual(run_calculator('20', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/17 = 1.176470588235294117647058824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_18(self):
        self.assertEqual(run_calculator('20', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/18 = 1.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_19(self):
        self.assertEqual(run_calculator('20', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/19 = 1.052631578947368421052631579',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_20(self):
        self.assertEqual(run_calculator('20', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/20 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_21(self):
        self.assertEqual(run_calculator('20', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/21 = 0.9523809523809523809523809524',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_22(self):
        self.assertEqual(run_calculator('20', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/22 = 0.9090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_23(self):
        self.assertEqual(run_calculator('20', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/23 = 0.8695652173913043478260869565',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_24(self):
        self.assertEqual(run_calculator('20', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/24 = 0.8333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_25(self):
        self.assertEqual(run_calculator('20', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/25 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_26(self):
        self.assertEqual(run_calculator('20', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/26 = 0.7692307692307692307692307692',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_27(self):
        self.assertEqual(run_calculator('20', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/27 = 0.7407407407407407407407407407',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_28(self):
        self.assertEqual(run_calculator('20', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/28 = 0.7142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_29(self):
        self.assertEqual(run_calculator('20', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/29 = 0.6896551724137931034482758621',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_30(self):
        self.assertEqual(run_calculator('20', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/30 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_31(self):
        self.assertEqual(run_calculator('20', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/31 = 0.6451612903225806451612903226',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_32(self):
        self.assertEqual(run_calculator('20', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/32 = 0.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_33(self):
        self.assertEqual(run_calculator('20', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/33 = 0.6060606060606060606060606061',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_34(self):
        self.assertEqual(run_calculator('20', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/34 = 0.5882352941176470588235294118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_35(self):
        self.assertEqual(run_calculator('20', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/35 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_36(self):
        self.assertEqual(run_calculator('20', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/36 = 0.5555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_37(self):
        self.assertEqual(run_calculator('20', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/37 = 0.5405405405405405405405405405',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_38(self):
        self.assertEqual(run_calculator('20', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/38 = 0.5263157894736842105263157895',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_39(self):
        self.assertEqual(run_calculator('20', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/39 = 0.5128205128205128205128205128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_40(self):
        self.assertEqual(run_calculator('20', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/40 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_41(self):
        self.assertEqual(run_calculator('20', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/41 = 0.4878048780487804878048780488',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_42(self):
        self.assertEqual(run_calculator('20', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/42 = 0.4761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_43(self):
        self.assertEqual(run_calculator('20', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/43 = 0.4651162790697674418604651163',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_44(self):
        self.assertEqual(run_calculator('20', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/44 = 0.4545454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_45(self):
        self.assertEqual(run_calculator('20', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/45 = 0.4444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_46(self):
        self.assertEqual(run_calculator('20', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/46 = 0.4347826086956521739130434783',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_47(self):
        self.assertEqual(run_calculator('20', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/47 = 0.4255319148936170212765957447',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_48(self):
        self.assertEqual(run_calculator('20', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/48 = 0.4166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_49(self):
        self.assertEqual(run_calculator('20', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/49 = 0.4081632653061224489795918367',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_divided_by_50(self):
        self.assertEqual(run_calculator('20', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20/50 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
