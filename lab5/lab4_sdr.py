#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: v3.8.2.0-56-gc7a096b8

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx

from gnuradio import qtgui

class lab4_sdr(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "lab4_sdr")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.fsk_deviation_hz = fsk_deviation_hz = 5000
        self.samples_per_second = samples_per_second = 200
        self.samp_rate = samp_rate = 4e5
        self.filter_transition = filter_transition = 250
        self.filter_cutoff = filter_cutoff = 1*fsk_deviation_hz
        self.carrier_freq = carrier_freq = 20000

        ##################################################
        # Blocks
        ##################################################
        self._fsk_deviation_hz_tool_bar = Qt.QToolBar(self)
        self._fsk_deviation_hz_tool_bar.addWidget(Qt.QLabel('fsk_deviation_hz' + ": "))
        self._fsk_deviation_hz_line_edit = Qt.QLineEdit(str(self.fsk_deviation_hz))
        self._fsk_deviation_hz_tool_bar.addWidget(self._fsk_deviation_hz_line_edit)
        self._fsk_deviation_hz_line_edit.returnPressed.connect(
            lambda: self.set_fsk_deviation_hz(int(str(self._fsk_deviation_hz_line_edit.text()))))
        self.top_grid_layout.addWidget(self._fsk_deviation_hz_tool_bar)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Demodulator Input', #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            4096, #size
            samp_rate, #samp_rate
            'Reciever Output', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Demodulator Output', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.low_pass(1, samp_rate, filter_cutoff, filter_transition), 0, samp_rate)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self._carrier_freq_tool_bar = Qt.QToolBar(self)
        self._carrier_freq_tool_bar.addWidget(Qt.QLabel('carrier_freq' + ": "))
        self._carrier_freq_line_edit = Qt.QLineEdit(str(self.carrier_freq))
        self._carrier_freq_tool_bar.addWidget(self._carrier_freq_line_edit)
        self._carrier_freq_line_edit.returnPressed.connect(
            lambda: self.set_carrier_freq(int(str(self._carrier_freq_line_edit.text()))))
        self.top_grid_layout.addWidget(self._carrier_freq_tool_bar)
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_char*1, samples_per_second)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/ad/eng/users/k/r/kremerme/Desktop/ec415/lab5/lab5_2fsk(1).iq', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/ad/eng/users/k/r/kremerme/Desktop/ec415/lab5/2fsk_out.bin', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_binary_slicer_fb_1, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab4_sdr")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.set_filter_cutoff(1*self.fsk_deviation_hz)
        Qt.QMetaObject.invokeMethod(self._fsk_deviation_hz_line_edit, "setText", Qt.Q_ARG("QString", str(self.fsk_deviation_hz)))
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))

    def get_samples_per_second(self):
        return self.samples_per_second

    def set_samples_per_second(self, samples_per_second):
        self.samples_per_second = samples_per_second
        self.blocks_keep_one_in_n_0.set_n(self.samples_per_second)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz))
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_filter_transition(self):
        return self.filter_transition

    def set_filter_transition(self, filter_transition):
        self.filter_transition = filter_transition
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition))

    def get_filter_cutoff(self):
        return self.filter_cutoff

    def set_filter_cutoff(self, filter_cutoff):
        self.filter_cutoff = filter_cutoff
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1, self.samp_rate, self.filter_cutoff, self.filter_transition))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        Qt.QMetaObject.invokeMethod(self._carrier_freq_line_edit, "setText", Qt.Q_ARG("QString", str(self.carrier_freq)))





def main(top_block_cls=lab4_sdr, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
