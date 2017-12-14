#!/usr/bin/env python2

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from concurrent_transmission import concurrent_transmission  # grc-generated hier_block
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import correctiq
import osmosdr
import sip
import time
from gnuradio import qtgui
import hackrf_software_channel

def argument_parser():
    description = 'HackRF Software Channel'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    return parser

def main(options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = hackrf_software_channel.hackrf_software_channel()
    tb.start()
    tb.show()

    while True:
        for rate in range(10000000,5000000,-50000):
            time.sleep(1)
            tb.set_samp_rate(rate)
            print(rate)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("My pid in case you need more violent termination: %d"%(os.getpid(),))
        os.kill(os.getpid(), signal.SIGTERM)
