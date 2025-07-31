Here's a README file for your Python audio processing application, formatted for clarity and ease of understanding.

-----

# Audio Signal Processing Toolkit

This Python application provides a suite of tools for real-time and simulated audio signal processing, including a spectrum analyzer, a noisy signal detector, live signal visualization, various audio filters, and waveform generation.

## Features

  * **Spectrum Analyzer:** Visualize the frequency spectrum of live audio input in real-time.
  * **Noisy Detector:** Record audio, add simulated noise, and analyze the difference between the original and noisy signals.
  * **Live Signal:** Generate and visualize a synthetic signal in both time and frequency domains.
  * **Filters:** Apply low-pass, high-pass, and band-pass Butterworth filters to live audio input.
  * **Waveforms:** Generate and display common waveforms (sine, square, sawtooth).

## Prerequisites

Before running the application, ensure you have the following Python libraries installed:

  * `numpy`
  * `matplotlib`
  * `scipy`
  * `sounddevice`

You can install them using pip:

```bash
pip install numpy matplotlib scipy sounddevice
```

**Note for `sounddevice`:**
On some systems, you might need to install additional audio backend libraries for `sounddevice` to function correctly. For example:

  * **Windows:** No extra steps usually needed.
  * **macOS:** Install PortAudio: `brew install portaudio`
  * **Linux:** Install PortAudio and development headers: `sudo apt-get install portaudio19-dev python3-pyaudio` (for Debian/Ubuntu) or equivalent for your distribution.

## How to Run

1.  Save the provided code as a Python file (e.g., `audio_toolkit.py`).

2.  Open a terminal or command prompt.

3.  Navigate to the directory where you saved the file.

4.  Run the script using Python:

    ```bash
    python audio_toolkit.py
    ```

## Usage

Upon running the script, a menu will appear in your console:

```
1. Spectrum Analyser
2. Noisy Detector
3. Live Signal
4. Filters
5. Waveforms
6. Exit
Enter the option to Perform:
```

Enter the number corresponding to the function you wish to use and press Enter.

### 1\. Spectrum Analyzer

  * Displays a real-time frequency spectrum of audio captured from your default input device (microphone).
  * **To exit:** Press `Ctrl + C` in the console.

### 2\. Noisy Detector

  * Prompts you to enter a duration for recording.
  * Records audio from your microphone for the specified duration.
  * Adds simulated random noise to the recorded signal.
  * Plots three graphs: the original signal, the noisy signal, and the difference between them.
  * **To close the plot:** Close the matplotlib window.

### 3\. Live Signal

  * Generates a synthetic signal composed of two sine waves.
  * Displays two plots: the signal in the time domain and its Fast Fourier Transform (FFT) in the frequency domain.
  * **To close the plot:** Close the matplotlib window.

### 4\. Filters

  * Prompts you to enter a duration for recording.
  * Records audio from your microphone.
  * Applies a **low-pass filter** (cutoff 1000 Hz), a **high-pass filter** (cutoff 1000 Hz), and a **band-pass filter** (500 Hz to 1500 Hz) to the recorded audio.
  * Plots four graphs: the original signal, the low-passed signal, the high-passed signal, and the band-passed signal.
  * **To close the plot:** Close the matplotlib window.

### 5\. Waveforms

  * Presents a sub-menu for generating and visualizing different basic waveforms:
    ```
    1. SINE Wave
    2. SQUARE Wave
    3. SAWTOOTH Wave
    4. All waves
    5. Exit
    Enter the Wave:
    ```
  * Select an option to view the corresponding waveform plot.
  * Choosing "4. All waves" will display sine, square, and sawtooth waves in separate subplots.
  * **To close the plot:** Close the matplotlib window.
  * **To exit the Waveforms section:** Choose option "5".

### 6\. Exit

  * Exits the application.

## Troubleshooting

  * **`sounddevice.PortAudioError: No devices available`**: This usually means `sounddevice` cannot find an audio input device or PortAudio is not correctly installed. Refer to the "Prerequisites" section for installation steps for PortAudio.
  * **Plots not appearing/freezing**: Ensure `matplotlib` is correctly installed. For real-time plots like the Spectrum Analyzer, `plt.ion()` is used, but issues might arise with certain backend configurations. If plots aren't interactive, try updating `matplotlib`.
  * **`KeyboardInterrupt` in Spectrum Analyzer**: This is the intended way to stop the Spectrum Analyzer. If it doesn't respond, ensure your terminal is active and you're pressing `Ctrl + C`.

-----
