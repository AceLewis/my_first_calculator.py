# test_divided_by_14.py
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


class TestDividedBy14(unittest.TestCase):

    def test_14_divided_by_0(self):
        self.assertEqual(run_calculator('14', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_1(self):
        self.assertEqual(run_calculator('14', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/1 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_2(self):
        self.assertEqual(run_calculator('14', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/2 = 7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_3(self):
        self.assertEqual(run_calculator('14', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/3 = 4.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_4(self):
        self.assertEqual(run_calculator('14', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/4 = 3.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_5(self):
        self.assertEqual(run_calculator('14', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/5 = 2.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_6(self):
        self.assertEqual(run_calculator('14', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/6 = 2.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_7(self):
        self.assertEqual(run_calculator('14', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/7 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_8(self):
        self.assertEqual(run_calculator('14', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/8 = 1.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_9(self):
        self.assertEqual(run_calculator('14', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/9 = 1.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_10(self):
        self.assertEqual(run_calculator('14', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/10 = 1.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_11(self):
        self.assertEqual(run_calculator('14', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/11 = 1.272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_12(self):
        self.assertEqual(run_calculator('14', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/12 = 1.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_13(self):
        self.assertEqual(run_calculator('14', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/13 = 1.076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_14(self):
        self.assertEqual(run_calculator('14', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/14 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_15(self):
        self.assertEqual(run_calculator('14', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/15 = 0.9333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_16(self):
        self.assertEqual(run_calculator('14', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/16 = 0.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_17(self):
        self.assertEqual(run_calculator('14', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/17 = 0.8235294117647058823529411765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_18(self):
        self.assertEqual(run_calculator('14', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/18 = 0.7777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_19(self):
        self.assertEqual(run_calculator('14', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/19 = 0.7368421052631578947368421053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_20(self):
        self.assertEqual(run_calculator('14', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/20 = 0.7',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_21(self):
        self.assertEqual(run_calculator('14', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/21 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_22(self):
        self.assertEqual(run_calculator('14', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/22 = 0.6363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_23(self):
        self.assertEqual(run_calculator('14', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/23 = 0.6086956521739130434782608696',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_24(self):
        self.assertEqual(run_calculator('14', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/24 = 0.5833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_25(self):
        self.assertEqual(run_calculator('14', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/25 = 0.56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_26(self):
        self.assertEqual(run_calculator('14', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/26 = 0.5384615384615384615384615385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_27(self):
        self.assertEqual(run_calculator('14', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/27 = 0.5185185185185185185185185185',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_28(self):
        self.assertEqual(run_calculator('14', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/28 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_29(self):
        self.assertEqual(run_calculator('14', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/29 = 0.4827586206896551724137931034',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_30(self):
        self.assertEqual(run_calculator('14', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/30 = 0.4666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_31(self):
        self.assertEqual(run_calculator('14', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/31 = 0.4516129032258064516129032258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_32(self):
        self.assertEqual(run_calculator('14', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/32 = 0.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_33(self):
        self.assertEqual(run_calculator('14', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/33 = 0.4242424242424242424242424242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_34(self):
        self.assertEqual(run_calculator('14', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/34 = 0.4117647058823529411764705882',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_35(self):
        self.assertEqual(run_calculator('14', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/35 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_36(self):
        self.assertEqual(run_calculator('14', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/36 = 0.3888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_37(self):
        self.assertEqual(run_calculator('14', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/37 = 0.3783783783783783783783783784',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_38(self):
        self.assertEqual(run_calculator('14', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/38 = 0.3684210526315789473684210526',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_39(self):
        self.assertEqual(run_calculator('14', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/39 = 0.3589743589743589743589743590',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_40(self):
        self.assertEqual(run_calculator('14', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/40 = 0.35',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_41(self):
        self.assertEqual(run_calculator('14', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/41 = 0.3414634146341463414634146341',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_42(self):
        self.assertEqual(run_calculator('14', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/42 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_43(self):
        self.assertEqual(run_calculator('14', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/43 = 0.3255813953488372093023255814',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_44(self):
        self.assertEqual(run_calculator('14', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/44 = 0.3181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_45(self):
        self.assertEqual(run_calculator('14', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/45 = 0.3111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_46(self):
        self.assertEqual(run_calculator('14', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/46 = 0.3043478260869565217391304348',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_47(self):
        self.assertEqual(run_calculator('14', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/47 = 0.2978723404255319148936170213',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_48(self):
        self.assertEqual(run_calculator('14', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/48 = 0.2916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_49(self):
        self.assertEqual(run_calculator('14', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/49 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_divided_by_50(self):
        self.assertEqual(run_calculator('14', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14/50 = 0.28',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
