# test_divided_by_26.py
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


class TestDividedBy26(unittest.TestCase):

    def test_26_divided_by_0(self):
        self.assertEqual(run_calculator('26', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_1(self):
        self.assertEqual(run_calculator('26', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/1 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_2(self):
        self.assertEqual(run_calculator('26', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/2 = 13',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_3(self):
        self.assertEqual(run_calculator('26', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/3 = 8.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_4(self):
        self.assertEqual(run_calculator('26', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/4 = 6.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_5(self):
        self.assertEqual(run_calculator('26', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/5 = 5.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_6(self):
        self.assertEqual(run_calculator('26', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/6 = 4.333333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_7(self):
        self.assertEqual(run_calculator('26', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/7 = 3.714285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_8(self):
        self.assertEqual(run_calculator('26', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/8 = 3.25',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_9(self):
        self.assertEqual(run_calculator('26', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/9 = 2.888888888888888888888888889',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_10(self):
        self.assertEqual(run_calculator('26', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/10 = 2.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_11(self):
        self.assertEqual(run_calculator('26', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/11 = 2.363636363636363636363636364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_12(self):
        self.assertEqual(run_calculator('26', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/12 = 2.166666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_13(self):
        self.assertEqual(run_calculator('26', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/13 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_14(self):
        self.assertEqual(run_calculator('26', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/14 = 1.857142857142857142857142857',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_15(self):
        self.assertEqual(run_calculator('26', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/15 = 1.733333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_16(self):
        self.assertEqual(run_calculator('26', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/16 = 1.625',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_17(self):
        self.assertEqual(run_calculator('26', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/17 = 1.529411764705882352941176471',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_18(self):
        self.assertEqual(run_calculator('26', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/18 = 1.444444444444444444444444444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_19(self):
        self.assertEqual(run_calculator('26', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/19 = 1.368421052631578947368421053',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_20(self):
        self.assertEqual(run_calculator('26', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/20 = 1.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_21(self):
        self.assertEqual(run_calculator('26', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/21 = 1.238095238095238095238095238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_22(self):
        self.assertEqual(run_calculator('26', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/22 = 1.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_23(self):
        self.assertEqual(run_calculator('26', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/23 = 1.130434782608695652173913043',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_24(self):
        self.assertEqual(run_calculator('26', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/24 = 1.083333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_25(self):
        self.assertEqual(run_calculator('26', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/25 = 1.04',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_26(self):
        self.assertEqual(run_calculator('26', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/26 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_27(self):
        self.assertEqual(run_calculator('26', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/27 = 0.9629629629629629629629629630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_28(self):
        self.assertEqual(run_calculator('26', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/28 = 0.9285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_29(self):
        self.assertEqual(run_calculator('26', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/29 = 0.8965517241379310344827586207',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_30(self):
        self.assertEqual(run_calculator('26', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/30 = 0.8666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_31(self):
        self.assertEqual(run_calculator('26', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/31 = 0.8387096774193548387096774194',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_32(self):
        self.assertEqual(run_calculator('26', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/32 = 0.8125',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_33(self):
        self.assertEqual(run_calculator('26', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/33 = 0.7878787878787878787878787879',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_34(self):
        self.assertEqual(run_calculator('26', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/34 = 0.7647058823529411764705882353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_35(self):
        self.assertEqual(run_calculator('26', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/35 = 0.7428571428571428571428571429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_36(self):
        self.assertEqual(run_calculator('26', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/36 = 0.7222222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_37(self):
        self.assertEqual(run_calculator('26', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/37 = 0.7027027027027027027027027027',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_38(self):
        self.assertEqual(run_calculator('26', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/38 = 0.6842105263157894736842105263',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_39(self):
        self.assertEqual(run_calculator('26', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/39 = 0.6666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_40(self):
        self.assertEqual(run_calculator('26', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/40 = 0.65',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_41(self):
        self.assertEqual(run_calculator('26', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/41 = 0.6341463414634146341463414634',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_42(self):
        self.assertEqual(run_calculator('26', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/42 = 0.6190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_43(self):
        self.assertEqual(run_calculator('26', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/43 = 0.6046511627906976744186046512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_44(self):
        self.assertEqual(run_calculator('26', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/44 = 0.5909090909090909090909090909',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_45(self):
        self.assertEqual(run_calculator('26', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/45 = 0.5777777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_46(self):
        self.assertEqual(run_calculator('26', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/46 = 0.5652173913043478260869565217',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_47(self):
        self.assertEqual(run_calculator('26', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/47 = 0.5531914893617021276595744681',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_48(self):
        self.assertEqual(run_calculator('26', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/48 = 0.5416666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_49(self):
        self.assertEqual(run_calculator('26', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/49 = 0.5306122448979591836734693878',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_divided_by_50(self):
        self.assertEqual(run_calculator('26', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26/50 = 0.52',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
