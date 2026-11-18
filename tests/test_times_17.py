# test_times_17.py
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


class TestTimes17(unittest.TestCase):

    def test_17_times_0(self):
        self.assertEqual(run_calculator('17', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_1(self):
        self.assertEqual(run_calculator('17', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*1 = 17',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_2(self):
        self.assertEqual(run_calculator('17', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*2 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_3(self):
        self.assertEqual(run_calculator('17', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*3 = 51',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_4(self):
        self.assertEqual(run_calculator('17', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*4 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_5(self):
        self.assertEqual(run_calculator('17', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*5 = 85',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_6(self):
        self.assertEqual(run_calculator('17', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*6 = 102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_7(self):
        self.assertEqual(run_calculator('17', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*7 = 119',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_8(self):
        self.assertEqual(run_calculator('17', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*8 = 136',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_9(self):
        self.assertEqual(run_calculator('17', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*9 = 153',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_10(self):
        self.assertEqual(run_calculator('17', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*10 = 170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_11(self):
        self.assertEqual(run_calculator('17', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*11 = 187',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_12(self):
        self.assertEqual(run_calculator('17', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*12 = 204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_13(self):
        self.assertEqual(run_calculator('17', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*13 = 221',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_14(self):
        self.assertEqual(run_calculator('17', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*14 = 238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_15(self):
        self.assertEqual(run_calculator('17', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*15 = 255',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_16(self):
        self.assertEqual(run_calculator('17', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*16 = 272',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_17(self):
        self.assertEqual(run_calculator('17', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*17 = 289',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_18(self):
        self.assertEqual(run_calculator('17', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*18 = 306',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_19(self):
        self.assertEqual(run_calculator('17', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*19 = 323',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_20(self):
        self.assertEqual(run_calculator('17', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*20 = 340',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_21(self):
        self.assertEqual(run_calculator('17', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*21 = 357',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_22(self):
        self.assertEqual(run_calculator('17', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*22 = 374',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_23(self):
        self.assertEqual(run_calculator('17', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*23 = 391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_24(self):
        self.assertEqual(run_calculator('17', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*24 = 408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_25(self):
        self.assertEqual(run_calculator('17', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*25 = 425',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_26(self):
        self.assertEqual(run_calculator('17', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*26 = 442',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_27(self):
        self.assertEqual(run_calculator('17', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*27 = 459',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_28(self):
        self.assertEqual(run_calculator('17', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*28 = 476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_29(self):
        self.assertEqual(run_calculator('17', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*29 = 493',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_30(self):
        self.assertEqual(run_calculator('17', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*30 = 510',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_31(self):
        self.assertEqual(run_calculator('17', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*31 = 527',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_32(self):
        self.assertEqual(run_calculator('17', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*32 = 544',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_33(self):
        self.assertEqual(run_calculator('17', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*33 = 561',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_34(self):
        self.assertEqual(run_calculator('17', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*34 = 578',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_35(self):
        self.assertEqual(run_calculator('17', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*35 = 595',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_36(self):
        self.assertEqual(run_calculator('17', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*36 = 612',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_37(self):
        self.assertEqual(run_calculator('17', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*37 = 629',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_38(self):
        self.assertEqual(run_calculator('17', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*38 = 646',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_39(self):
        self.assertEqual(run_calculator('17', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*39 = 663',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_40(self):
        self.assertEqual(run_calculator('17', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*40 = 680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_41(self):
        self.assertEqual(run_calculator('17', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*41 = 697',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_42(self):
        self.assertEqual(run_calculator('17', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*42 = 714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_43(self):
        self.assertEqual(run_calculator('17', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*43 = 731',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_44(self):
        self.assertEqual(run_calculator('17', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*44 = 748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_45(self):
        self.assertEqual(run_calculator('17', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*45 = 765',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_46(self):
        self.assertEqual(run_calculator('17', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*46 = 782',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_47(self):
        self.assertEqual(run_calculator('17', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*47 = 799',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_48(self):
        self.assertEqual(run_calculator('17', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*48 = 816',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_49(self):
        self.assertEqual(run_calculator('17', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*49 = 833',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_17_times_50(self):
        self.assertEqual(run_calculator('17', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '17*50 = 850',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
