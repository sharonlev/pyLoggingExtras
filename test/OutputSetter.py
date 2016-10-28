__author__ = 'Sharon Lev'
__email__ = 'sharon_lev@yahoo.com'
__date__ = '10/25/16'

import sys
from StringIO import StringIO
from unittest import TestCase
from logging import root

class OutputSetter(TestCase):
    """
    """
    temp_stdout = None
    @classmethod
    def setUpClass(cls):
        for handler in root.handlers[:]:
            root.removeHandler(handler)
        cls.temp_stdout = sys.stdout
        sys.stdout = StringIO()

    def setUp(self):
        sys.stdout.truncate(0)

    def tearDown(self):
        content = sys.stdout.getvalue()
        sys.stderr.writelines(content)

    @classmethod
    def tearDownClass(cls):
        cls.tmp  = sys.stdout
        sys.stdout = cls.temp_stdout
        print 'done!'

    def get_log_lines_parts(self):
        """
        :return: list of logged lines separated by separator ":"
        """
        output = sys.stdout.getvalue().splitlines()
        return [line.split(":") for line in output]


    def validate_output(self, level, method, expected_output,  *wargs, **kwargs):
        """

        :param level:
        :param method:
        :param wargs:
        :param kwargs:
        :return:
        """
        output = self.get_log_lines_parts()
        self.assertEqual(len(output), 3, output)
        for line in [output[0]] + [output[2]]:
            self.assertEqual(line[0], level)
            self.assertEqual(line[1], method)
            self.assertIn(line[2].split()[0], ['entering', 'exiting'])

        if wargs:
            for arg in wargs:
                self.assertIn(str(arg), output[0][2])
                self.assertIn(str(arg), output[1][1])
        if kwargs:
            for key, value  in kwargs.iteritems():
                self.assertIn(str(key), ':'.join(output[0]))
                self.assertIn(str(value), ':'.join(output[0]))
                self.assertIn(str(value), output[1][1])

        if expected_output:
            self.assertIn("%s" % expected_output, ":".join(output[2]))

        return output