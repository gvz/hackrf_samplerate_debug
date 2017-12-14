#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HackRF Software Channel
# Description: HackRF Software Channel
# Generated: Thu Dec 14 15:21:10 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
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
import sys
import time
from gnuradio import qtgui


class hackrf_software_channel(gr.top_block, Qt.QWidget):

    def __init__(self, channel_in_hackrf="hackrf=0000000000000000909864c8385824cf", channel_out_hackrf="hackrf=0000000000000000909864c8365e56cf", freq=2480e6):
        gr.top_block.__init__(self, "HackRF Software Channel")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HackRF Software Channel")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hackrf_software_channel")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.channel_in_hackrf = channel_in_hackrf
        self.channel_out_hackrf = channel_out_hackrf
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.tx_rf_gain = tx_rf_gain = 7
        self.tx_if_gain = tx_if_gain = 21
        self.tx_bb_gain = tx_bb_gain = 15
        self.shift = shift = 0
        self.samp_rate = samp_rate = 5e6
        self.rx_rf_gain = rx_rf_gain = 0
        self.rx_if_gain = rx_if_gain = 21
        self.rx_bb_gain = rx_bb_gain = 15

        ##################################################
        # Blocks
        ##################################################
        self._tx_rf_gain_range = Range(0, 10, 0.1, 7, 200)
        self._tx_rf_gain_win = RangeWidget(self._tx_rf_gain_range, self.set_tx_rf_gain, "tx_rf_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_rf_gain_win)
        self._tx_if_gain_range = Range(15, 30, 1, 21, 200)
        self._tx_if_gain_win = RangeWidget(self._tx_if_gain_range, self.set_tx_if_gain, "tx_if_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_if_gain_win)
        self._tx_bb_gain_range = Range(15, 30, 1, 15, 200)
        self._tx_bb_gain_win = RangeWidget(self._tx_bb_gain_range, self.set_tx_bb_gain, "tx_bb_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_bb_gain_win)
        self._samp_rate_range = Range(1e6, 10e6, 1e5, 5e6, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "samp_rate", "counter_slider", float)
        self.top_layout.addWidget(self._samp_rate_win)
        self._rx_rf_gain_range = Range(0, 10, 0.1, 0, 200)
        self._rx_rf_gain_win = RangeWidget(self._rx_rf_gain_range, self.set_rx_rf_gain, "rx_rf_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rx_rf_gain_win)
        self._rx_if_gain_range = Range(15, 30, 1, 21, 200)
        self._rx_if_gain_win = RangeWidget(self._rx_if_gain_range, self.set_rx_if_gain, "rx_if_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rx_if_gain_win)
        self._rx_bb_gain_range = Range(15, 30, 1, 15, 200)
        self._rx_bb_gain_win = RangeWidget(self._rx_bb_gain_range, self.set_rx_bb_gain, "rx_bb_gain", "counter_slider", float)
        self.top_layout.addWidget(self._rx_bb_gain_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + channel_in_hackrf )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq+shift, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(rx_rf_gain, 0)
        self.osmosdr_source_0.set_if_gain(rx_if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(rx_bb_gain, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + channel_out_hackrf )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(tx_rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(tx_if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(tx_bb_gain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._fosphor_qt_sink_c_0_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.osmosdr_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hackrf_software_channel")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_channel_in_hackrf(self):
        return self.channel_in_hackrf

    def set_channel_in_hackrf(self, channel_in_hackrf):
        self.channel_in_hackrf = channel_in_hackrf

    def get_channel_out_hackrf(self):
        return self.channel_out_hackrf

    def set_channel_out_hackrf(self, channel_out_hackrf):
        self.channel_out_hackrf = channel_out_hackrf

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_source_0.set_center_freq(self.freq+self.shift, 0)
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)

    def get_tx_rf_gain(self):
        return self.tx_rf_gain

    def set_tx_rf_gain(self, tx_rf_gain):
        self.tx_rf_gain = tx_rf_gain
        self.osmosdr_sink_0.set_gain(self.tx_rf_gain, 0)

    def get_tx_if_gain(self):
        return self.tx_if_gain

    def set_tx_if_gain(self, tx_if_gain):
        self.tx_if_gain = tx_if_gain
        self.osmosdr_sink_0.set_if_gain(self.tx_if_gain, 0)

    def get_tx_bb_gain(self):
        return self.tx_bb_gain

    def set_tx_bb_gain(self, tx_bb_gain):
        self.tx_bb_gain = tx_bb_gain
        self.osmosdr_sink_0.set_bb_gain(self.tx_bb_gain, 0)

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift
        self.osmosdr_source_0.set_center_freq(self.freq+self.shift, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate)

    def get_rx_rf_gain(self):
        return self.rx_rf_gain

    def set_rx_rf_gain(self, rx_rf_gain):
        self.rx_rf_gain = rx_rf_gain
        self.osmosdr_source_0.set_gain(self.rx_rf_gain, 0)

    def get_rx_if_gain(self):
        return self.rx_if_gain

    def set_rx_if_gain(self, rx_if_gain):
        self.rx_if_gain = rx_if_gain
        self.osmosdr_source_0.set_if_gain(self.rx_if_gain, 0)

    def get_rx_bb_gain(self):
        return self.rx_bb_gain

    def set_rx_bb_gain(self, rx_bb_gain):
        self.rx_bb_gain = rx_bb_gain
        self.osmosdr_source_0.set_bb_gain(self.rx_bb_gain, 0)


def argument_parser():
    description = 'HackRF Software Channel'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    return parser


def main(top_block_cls=hackrf_software_channel, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
