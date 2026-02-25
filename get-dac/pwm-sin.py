import time
import pwm_dac as pwm
import signal_generator as sg

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = None
    try:
        dac = pwm.PWMDAC(12, 500, 3.290, verbose=False)

        start = time.time()
        while True:
            t = time.time() - start
            norm = sg.get_sin_wave_amplitude(signal_frequency, t)
            voltage = amplitude * norm                             

            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        if dac is not None:
            dac.deinit()
