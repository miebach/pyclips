# test_00.py
# initial (hence the name '00') definitions for testing purposes


"""\
TESTS:

CurrentEnvironment
Environment
"""


import clips, unittest
import gc


class ctestcase(unittest.TestCase):
    """base class for pyclips unit test cases"""

    def setUp(self):
        """set up testing environment"""
        e1 = clips.Environment()
        self.envdict = {
            'clips': clips,
            'env': e1,
            }
        clips.DebugConfig.WatchAll()
        e1.DebugConfig.WatchAll()

    def tearDown(self):
        clips.DebugConfig.UnwatchAll()
        self.envdict['env'].DebugConfig.UnwatchAll()
        s = clips.TraceStream.Read()
        with open("trace.out", 'a') as fc:
            fc.write("=" * 78 + "\n")
            fc.write("--> %s\n" % self.__class__.__name__)
            fc.write("-" * 78 + "\n")
            fc.write("%s" % s)
            fc.write("\n\n\n")
        s = clips.ErrorStream.Read()
        with open("error.out", 'a') as fc:
            fc.write("=" * 78 + "\n")
            fc.write("--> %s\n" % self.__class__.__name__)
            fc.write("-" * 78 + "\n")
            fc.write("%s" % s)
            fc.write("\n\n\n")
        o = gc.collect()
        with open("garbage.out", 'a') as fc:
            fc.write("%s --> %s unreached objects\n" % (
                self.__class__.__name__, o))


# end.
