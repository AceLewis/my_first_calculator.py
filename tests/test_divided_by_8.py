# test_divided_by_8.py
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


class TestDividedBy8(unittest.TestCase):

    def test_8_divided_by_0(self):
        self.assertEqual(run_calculator('8', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_1(self):
        self.assertEqual(run_calculator('8', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/1 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_2(self):
        self.assertEqual(run_calculator('8', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/2 = 4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_3(self):
        self.assertEqual(run_calculator('8', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/3 = 2.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_4(self):
        self.assertEqual(run_calculator('8', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/4 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_5(self):
        self.assertEqual(run_calculator('8', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/5 = 1.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_6(self):
        self.assertEqual(run_calculator('8', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/6 = 1.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_7(self):
        self.assertEqual(run_calculator('8', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/7 = 1.142857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_8(self):
        self.assertEqual(run_calculator('8', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/8 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_9(self):
        self.assertEqual(run_calculator('8', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/9 = 0.8888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_10(self):
        self.assertEqual(run_calculator('8', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/10 = 0.8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_11(self):
        self.assertEqual(run_calculator('8', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/11 = 0.7272727272727272727272727273',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_12(self):
        self.assertEqual(run_calculator('8', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/12 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_13(self):
        self.assertEqual(run_calculator('8', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/13 = 0.6153846153846153846153846154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_14(self):
        self.assertEqual(run_calculator('8', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/14 = 0.5714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_15(self):
        self.assertEqual(run_calculator('8', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/15 = 0.5333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_16(self):
        self.assertEqual(run_calculator('8', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/16 = 0.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_17(self):
        self.assertEqual(run_calculator('8', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/17 = 0.4705882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_18(self):
        self.assertEqual(run_calculator('8', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/18 = 0.4444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_19(self):
        self.assertEqual(run_calculator('8', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/19 = 0.4210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_20(self):
        self.assertEqual(run_calculator('8', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/20 = 0.4',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_21(self):
        self.assertEqual(run_calculator('8', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/21 = 0.3809523809523809523809523810',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_22(self):
        self.assertEqual(run_calculator('8', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/22 = 0.3636363636363636363636363636',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_23(self):
        self.assertEqual(run_calculator('8', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/23 = 0.3478260869565217391304347826',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_24(self):
        self.assertEqual(run_calculator('8', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/24 = 0.3333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_25(self):
        self.assertEqual(run_calculator('8', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/25 = 0.32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_26(self):
        self.assertEqual(run_calculator('8', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/26 = 0.3076923076923076923076923077',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_27(self):
        self.assertEqual(run_calculator('8', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/27 = 0.2962962962962962962962962963',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_28(self):
        self.assertEqual(run_calculator('8', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/28 = 0.2857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_29(self):
        self.assertEqual(run_calculator('8', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/29 = 0.2758620689655172413793103448',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_30(self):
        self.assertEqual(run_calculator('8', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/30 = 0.2666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_31(self):
        self.assertEqual(run_calculator('8', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/31 = 0.2580645161290322580645161290',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_32(self):
        self.assertEqual(run_calculator('8', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/32 = 0.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_33(self):
        self.assertEqual(run_calculator('8', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/33 = 0.2424242424242424242424242424',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_34(self):
        self.assertEqual(run_calculator('8', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/34 = 0.2352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_35(self):
        self.assertEqual(run_calculator('8', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/35 = 0.2285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_36(self):
        self.assertEqual(run_calculator('8', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/36 = 0.2222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_37(self):
        self.assertEqual(run_calculator('8', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/37 = 0.2162162162162162162162162162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_38(self):
        self.assertEqual(run_calculator('8', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/38 = 0.2105263157894736842105263158',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_39(self):
        self.assertEqual(run_calculator('8', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/39 = 0.2051282051282051282051282051',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_40(self):
        self.assertEqual(run_calculator('8', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/40 = 0.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_41(self):
        self.assertEqual(run_calculator('8', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/41 = 0.1951219512195121951219512195',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_42(self):
        self.assertEqual(run_calculator('8', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/42 = 0.1904761904761904761904761905',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_43(self):
        self.assertEqual(run_calculator('8', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/43 = 0.1860465116279069767441860465',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_44(self):
        self.assertEqual(run_calculator('8', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/44 = 0.1818181818181818181818181818',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_45(self):
        self.assertEqual(run_calculator('8', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/45 = 0.1777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_46(self):
        self.assertEqual(run_calculator('8', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/46 = 0.1739130434782608695652173913',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_47(self):
        self.assertEqual(run_calculator('8', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/47 = 0.1702127659574468085106382979',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_48(self):
        self.assertEqual(run_calculator('8', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/48 = 0.1666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_49(self):
        self.assertEqual(run_calculator('8', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/49 = 0.1632653061224489795918367347',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_divided_by_50(self):
        self.assertEqual(run_calculator('8', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8/50 = 0.16',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
