# test_divided_by_46.py
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


class TestDividedBy46(unittest.TestCase):

    def test_46_divided_by_0(self):
        self.assertEqual(run_calculator('46', '/', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/0 = Inf',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_1(self):
        self.assertEqual(run_calculator('46', '/', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/1 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_2(self):
        self.assertEqual(run_calculator('46', '/', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/2 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_3(self):
        self.assertEqual(run_calculator('46', '/', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/3 = 15.33333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_4(self):
        self.assertEqual(run_calculator('46', '/', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/4 = 11.5',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_5(self):
        self.assertEqual(run_calculator('46', '/', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/5 = 9.2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_6(self):
        self.assertEqual(run_calculator('46', '/', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/6 = 7.666666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_7(self):
        self.assertEqual(run_calculator('46', '/', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/7 = 6.571428571428571428571428571',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_8(self):
        self.assertEqual(run_calculator('46', '/', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/8 = 5.75',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_9(self):
        self.assertEqual(run_calculator('46', '/', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/9 = 5.111111111111111111111111111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_10(self):
        self.assertEqual(run_calculator('46', '/', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/10 = 4.6',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_11(self):
        self.assertEqual(run_calculator('46', '/', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/11 = 4.181818181818181818181818182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_12(self):
        self.assertEqual(run_calculator('46', '/', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/12 = 3.833333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_13(self):
        self.assertEqual(run_calculator('46', '/', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/13 = 3.538461538461538461538461538',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_14(self):
        self.assertEqual(run_calculator('46', '/', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/14 = 3.285714285714285714285714286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_15(self):
        self.assertEqual(run_calculator('46', '/', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/15 = 3.066666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_16(self):
        self.assertEqual(run_calculator('46', '/', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/16 = 2.875',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_17(self):
        self.assertEqual(run_calculator('46', '/', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/17 = 2.705882352941176470588235294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_18(self):
        self.assertEqual(run_calculator('46', '/', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/18 = 2.555555555555555555555555556',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_19(self):
        self.assertEqual(run_calculator('46', '/', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/19 = 2.421052631578947368421052632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_20(self):
        self.assertEqual(run_calculator('46', '/', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/20 = 2.3',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_21(self):
        self.assertEqual(run_calculator('46', '/', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/21 = 2.190476190476190476190476190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_22(self):
        self.assertEqual(run_calculator('46', '/', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/22 = 2.090909090909090909090909091',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_23(self):
        self.assertEqual(run_calculator('46', '/', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/23 = 2',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_24(self):
        self.assertEqual(run_calculator('46', '/', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/24 = 1.916666666666666666666666667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_25(self):
        self.assertEqual(run_calculator('46', '/', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/25 = 1.84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_26(self):
        self.assertEqual(run_calculator('46', '/', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/26 = 1.769230769230769230769230769',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_27(self):
        self.assertEqual(run_calculator('46', '/', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/27 = 1.703703703703703703703703704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_28(self):
        self.assertEqual(run_calculator('46', '/', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/28 = 1.642857142857142857142857143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_29(self):
        self.assertEqual(run_calculator('46', '/', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/29 = 1.586206896551724137931034483',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_30(self):
        self.assertEqual(run_calculator('46', '/', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/30 = 1.533333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_31(self):
        self.assertEqual(run_calculator('46', '/', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/31 = 1.483870967741935483870967742',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_32(self):
        self.assertEqual(run_calculator('46', '/', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/32 = 1.4375',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_33(self):
        self.assertEqual(run_calculator('46', '/', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/33 = 1.393939393939393939393939394',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_34(self):
        self.assertEqual(run_calculator('46', '/', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/34 = 1.352941176470588235294117647',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_35(self):
        self.assertEqual(run_calculator('46', '/', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/35 = 1.314285714285714285714285714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_36(self):
        self.assertEqual(run_calculator('46', '/', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/36 = 1.277777777777777777777777778',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_37(self):
        self.assertEqual(run_calculator('46', '/', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/37 = 1.243243243243243243243243243',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_38(self):
        self.assertEqual(run_calculator('46', '/', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/38 = 1.210526315789473684210526316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_39(self):
        self.assertEqual(run_calculator('46', '/', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/39 = 1.179487179487179487179487179',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_40(self):
        self.assertEqual(run_calculator('46', '/', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/40 = 1.15',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_41(self):
        self.assertEqual(run_calculator('46', '/', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/41 = 1.121951219512195121951219512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_42(self):
        self.assertEqual(run_calculator('46', '/', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/42 = 1.095238095238095238095238095',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_43(self):
        self.assertEqual(run_calculator('46', '/', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/43 = 1.069767441860465116279069767',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_44(self):
        self.assertEqual(run_calculator('46', '/', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/44 = 1.045454545454545454545454545',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_45(self):
        self.assertEqual(run_calculator('46', '/', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/45 = 1.022222222222222222222222222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_46(self):
        self.assertEqual(run_calculator('46', '/', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/46 = 1',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_47(self):
        self.assertEqual(run_calculator('46', '/', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/47 = 0.9787234042553191489361702128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_48(self):
        self.assertEqual(run_calculator('46', '/', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/48 = 0.9583333333333333333333333333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_49(self):
        self.assertEqual(run_calculator('46', '/', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/49 = 0.9387755102040816326530612245',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_divided_by_50(self):
        self.assertEqual(run_calculator('46', '/', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46/50 = 0.92',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
