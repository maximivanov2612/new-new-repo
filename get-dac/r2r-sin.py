import time
import r2r_dac as r2r
import signal_generator as sg

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, verbose=False)

        start = time.time()
        while True:
            t = time.time() - start
            norm = sg.get_sin_wave_amplitude(signal_frequency, t)  # 0..1
            voltage = amplitude * norm                             # 0..amplitude

            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        if dac is not None:
            dac.deinit()
