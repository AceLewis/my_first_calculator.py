# test_divided_by_41.py
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


class TestDividedBy41(unittest.TestCase):

    def test_41_divided_by_0(self):
        self.assertEqual(run_calculator('41', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_1(self):
        self.assertEqual(run_calculator('41', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/1 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_2(self):
        self.assertEqual(run_calculator('41', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/2 = 20.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_3(self):
        self.assertEqual(run_calculator('41', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/3 = 13.66666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_4(self):
        self.assertEqual(run_calculator('41', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/4 = 10.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_5(self):
        self.assertEqual(run_calculator('41', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/5 = 8.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_6(self):
        self.assertEqual(run_calculator('41', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/6 = 6.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_7(self):
        self.assertEqual(run_calculator('41', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/7 = 5.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_8(self):
        self.assertEqual(run_calculator('41', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/8 = 5.125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_9(self):
        self.assertEqual(run_calculator('41', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/9 = 4.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_10(self):
        self.assertEqual(run_calculator('41', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/10 = 4.1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_11(self):
        self.assertEqual(run_calculator('41', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/11 = 3.727272727272727272727272727',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_12(self):
        self.assertEqual(run_calculator('41', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/12 = 3.416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_13(self):
        self.assertEqual(run_calculator('41', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/13 = 3.153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_14(self):
        self.assertEqual(run_calculator('41', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/14 = 2.928571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_15(self):
        self.assertEqual(run_calculator('41', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/15 = 2.733333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_16(self):
        self.assertEqual(run_calculator('41', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/16 = 2.5625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_17(self):
        self.assertEqual(run_calculator('41', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/17 = 2.411764705882352941176470588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_18(self):
        self.assertEqual(run_calculator('41', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/18 = 2.277777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_19(self):
        self.assertEqual(run_calculator('41', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/19 = 2.157894736842105263157894737',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_20(self):
        self.assertEqual(run_calculator('41', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/20 = 2.05',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_21(self):
        self.assertEqual(run_calculator('41', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/21 = 1.952380952380952380952380952',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_22(self):
        self.assertEqual(run_calculator('41', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/22 = 1.863636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_23(self):
        self.assertEqual(run_calculator('41', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/23 = 1.782608695652173913043478261',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_24(self):
        self.assertEqual(run_calculator('41', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/24 = 1.708333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_25(self):
        self.assertEqual(run_calculator('41', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/25 = 1.64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_26(self):
        self.assertEqual(run_calculator('41', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/26 = 1.576923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_27(self):
        self.assertEqual(run_calculator('41', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/27 = 1.518518518518518518518518519',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_28(self):
        self.assertEqual(run_calculator('41', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/28 = 1.464285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_29(self):
        self.assertEqual(run_calculator('41', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/29 = 1.413793103448275862068965517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_30(self):
        self.assertEqual(run_calculator('41', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/30 = 1.366666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_31(self):
        self.assertEqual(run_calculator('41', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/31 = 1.322580645161290322580645161',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_32(self):
        self.assertEqual(run_calculator('41', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/32 = 1.28125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_33(self):
        self.assertEqual(run_calculator('41', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/33 = 1.242424242424242424242424242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_34(self):
        self.assertEqual(run_calculator('41', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/34 = 1.205882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_35(self):
        self.assertEqual(run_calculator('41', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/35 = 1.171428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_36(self):
        self.assertEqual(run_calculator('41', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/36 = 1.138888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_37(self):
        self.assertEqual(run_calculator('41', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/37 = 1.108108108108108108108108108',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_38(self):
        self.assertEqual(run_calculator('41', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/38 = 1.078947368421052631578947368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_39(self):
        self.assertEqual(run_calculator('41', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/39 = 1.051282051282051282051282051',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_40(self):
        self.assertEqual(run_calculator('41', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/40 = 1.025',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_41(self):
        self.assertEqual(run_calculator('41', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/41 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_42(self):
        self.assertEqual(run_calculator('41', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/42 = 0.9761904761904761904761904762',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_43(self):
        self.assertEqual(run_calculator('41', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/43 = 0.9534883720930232558139534884',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_44(self):
        self.assertEqual(run_calculator('41', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/44 = 0.9318181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_45(self):
        self.assertEqual(run_calculator('41', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/45 = 0.9111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_46(self):
        self.assertEqual(run_calculator('41', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/46 = 0.8913043478260869565217391304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_47(self):
        self.assertEqual(run_calculator('41', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/47 = 0.8723404255319148936170212766',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_48(self):
        self.assertEqual(run_calculator('41', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/48 = 0.8541666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_49(self):
        self.assertEqual(run_calculator('41', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/49 = 0.8367346938775510204081632653',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_divided_by_50(self):
        self.assertEqual(run_calculator('41', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41/50 = 0.82',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
