import numpy as np
import csv
import time

def write_to_file(data_set, start_time):
    # Write results to a csv file
    F3 = data_set['F3']
    FC5 = data_set['FC5']
    AF3 = data_set['AF3']
    F7 = data_set['F7']
    T7 = data_set['T7']
    P7 = data_set['P7']
    O1 = data_set['O1']
    O2 = data_set['O2']
    P8 = data_set['P8']
    T8 = data_set['T8']
    F8 = data_set['F8']
    AF4 = data_set['AF4']
    FC6 = data_set['FC6']
    F4 = data_set['F4']

    cur_time = time.time() - start_time

    with open('fft_power_spectrum.csv', 'a') as f:
        writer = csv.writer(f)
        data = [str(cur_time)]

        for i in range(0, len(F3)):
            data.append(str(F3[i]))
            data.append(str(FC5[i]))
            data.append(str(AF3[i]))
            data.append(str(F7[i]))
            data.append(str(T7[i]))
            data.append(str(P7[i]))
            data.append(str(O1[i]))
            data.append(str(O2[i]))
            data.append(str(P8[i]))
            data.append(str(T8[i]))
            data.append(str(F8[i]))
            data.append(str(AF4[i]))
            data.append(str(FC6[i]))
            data.append(str(F4[i]))

        writer.writerow(data)

def compute_fft(data):
    # Compute fft amplitude spectrum
    y = np.fft.fft(data)
    length_y = len(y)
    y_normalized = (y / float(length_y)) * 2.0
    y_shifted = np.fft.fftshift(y_normalized)

    # Return the positive frequency components
    return np.absolute(y_shifted[0:(length_y // 2) + 1])
