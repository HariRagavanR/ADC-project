import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.fft import fft
import sounddevice as sd
from scipy.signal import square, sawtooth, butter, lfilter
from matplotlib.ticker import ScalarFormatter

while True:
    choices = int(input(
        "1. Spectrum Analyser\n2. Noisy Detector\n3. Live Signal\n4. Filters\n5. Waveforms\n6. Exit\nEnter the option to Perform: "
    ))

    if choices == 1:  # Spectrum Analyzer
        print("Opening Real-Time Spectrum Analyzer!")
        sample_rate = 44100
        duration = 0.1
        n_samples = int(sample_rate * duration)

        plt.ion()
        fig, ax = plt.subplots()
        x = np.linspace(0, sample_rate / 2, n_samples // 2)
        line, = ax.plot(x, np.zeros(n_samples // 2))
        ax.set_ylim(0, 250)
        ax.set_xlim(0, sample_rate / 100)
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Real-Time Spectrum Analyzer')
        print("Press ctrl + c to Exit...")

        try:
            while True:
                audio_data = sd.rec(n_samples, samplerate=sample_rate, channels=1, dtype='float64')
                sd.wait()
                fft_result = fft(audio_data.flatten())
                magnitude = np.abs(fft_result[:n_samples // 2])
                line.set_ydata(magnitude)
                plt.pause(0.1)
        except KeyboardInterrupt:
            print("Exiting the spectrum analyzer.")
        finally:
            plt.close(fig)

    elif choices == 2:  # Noisy Level Detector
        print("Opening Noisy Level Detector!")
        samplerate = 44100
        duration = int(input("Enter the Duration in seconds of your Signal: "))
        noise_level = 0.1

        def capture_audio():
            print("Recording... Start to Speak....")
            audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float64')
            sd.wait()
            return audio.flatten()

        def add_noise(signal, noise_level):
            noise = np.random.normal(0, noise_level, signal.shape)
            noisy_signal = signal + noise
            return noisy_signal, noise

        original_signal = capture_audio()
        noisy_signal, noise = add_noise(original_signal, noise_level)
        difference_signal = noisy_signal - original_signal
        time = np.linspace(0, duration, len(original_signal))

        plt.figure(figsize=(12, 8))
        plt.subplot(3, 1, 1)
        plt.plot(time, original_signal, color='green', label='Original Signal')
        plt.title('Original Audio Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.subplot(3, 1, 2)
        plt.plot(time, noisy_signal, color='yellow', label='Noisy Signal')
        plt.title('Noisy Audio Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.subplot(3, 1, 3)
        plt.plot(time, difference_signal, color='red', label='Difference Signal')
        plt.title('Difference Between Original and Noisy Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif choices == 3:  # Live Signal
        print("Opening Live Signal!")
        fs = 1000
        t = np.arange(0, 1.0, 1 / fs)
        f1, f2 = 50, 120
        signal = 10 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.sin(2 * np.pi * f2 * t)
        fft_result = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(fft_result), 1 / fs)

        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(t, signal)
        plt.title("Time Domain Signal")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.subplot(2, 1, 2)
        plt.plot(frequencies[:len(frequencies) // 2], np.abs(fft_result)[:len(fft_result) // 2])
        plt.title("Frequency Domain Signal (FFT)")
        plt.xlabel("Frequency [Hz]")
        plt.ylabel("Magnitude")
        plt.tight_layout()
        plt.show()

    elif choices == 4:  # Filters
        print("Opening Filters!")
        samplerate = 44100
        duration = int(input("Enter the Duration (seconds): "))
        low_cutoff_freq = 500
        high_cutoff_freq = 1500
        order = 6

        def butter_filter(filter_type, data, cutoff, fs, order=5):
            nyq = 0.5 * fs
            if filter_type == 'band':
                normal_cutoff = [c / nyq for c in cutoff]
            else:
                normal_cutoff = cutoff / nyq
            b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
            y = lfilter(b, a, data)
            return y

        def capture_audio():
            print("Recording... Start to Speak.")
            audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float64')
            sd.wait()
            return audio.flatten()

        original_signal = capture_audio()
        low_passed_signal = butter_filter('low', original_signal, 1000, samplerate, order)
        high_passed_signal = butter_filter('high', original_signal, 1000, samplerate, order)
        band_passed_signal = butter_filter('band', original_signal, [low_cutoff_freq, high_cutoff_freq], samplerate, order)

        plt.figure(figsize=(12, 8))
        plt.subplot(4, 1, 1)
        plt.plot(original_signal, color='blue', label='Original Signal')
        plt.title('Original Audio Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.subplot(4, 1, 2)
        plt.plot(low_passed_signal, color='green', label='Low-Pass Filtered Signal')
        plt.title('Low-Pass Filtered Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.subplot(4, 1, 3)
        plt.plot(high_passed_signal, color='red', label='High-Pass Filtered Signal')
        plt.title('High-Pass Filtered Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.subplot(4, 1, 4)
        plt.plot(band_passed_signal, color='purple', label='Band-Pass Filtered Signal')
        plt.title('Band-Pass Filtered Signal')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif choices == 5:  # Waveforms
        print("Opening Waveforms!")
        samp_freq = 44100
        duration = 0.1
        t = np.linspace(0, duration, int(samp_freq * duration), endpoint=False)
        amplitude = 10
        frequency = 440
        sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)
        square_wave = amplitude * square(2 * np.pi * frequency * t)
        sawtooth_wave = amplitude * sawtooth(2 * np.pi * frequency * t)

        while True:
            wave_choice = int(input("1.SINE Wave\n2.SQUARE Wave\n3.SAWTOOTH Wave\n4.All waves\n5.Exit\nEnter the Wave: "))
            if wave_choice == 1:
                plt.title('Sine Wave')
                plt.plot(t, sine_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
            elif wave_choice == 2:
                plt.title('Square Wave')
                plt.plot(t, square_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
            elif wave_choice == 3:
                plt.title('Sawtooth Wave')
                plt.plot(t, sawtooth_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
            elif wave_choice == 4:
                plt.figure(figsize=(12, 8))
                plt.subplot(3, 1, 1)
                plt.title('Sine Wave')
                plt.plot(t, sine_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
                plt.subplot(3, 1, 2)
                plt.title('Square Wave')
                plt.plot(t, square_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
                plt.subplot(3, 1, 3)
                plt.title('Sawtooth Wave')
                plt.plot(t, sawtooth_wave)
                plt.xlabel('Time [s]')
                plt.ylabel('Amplitude')
            elif wave_choice == 5:
                break
            plt.tight_layout()
            plt.show()

    elif choices == 6:
        break
    else:
        print("Invalid choice. Exiting.")
