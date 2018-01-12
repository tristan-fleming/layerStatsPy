import matplotlib.pyplot as plt
from scipy import io as sio
import numpy as np


def load_mat(matFile, varName):
    '''Loads the histogram trend Matlab file outputted by HistogramTrend.m found
    at https://github.com/FraserGroup/MicroICI '''
    data_dict = sio.loadmat(matFile)
    data_arr = data_dict[varName][0]
    return data_arr

def plot_hists(hist_data, numBins, labels):
    plt.style.use('ggplot')
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams["font.style"] = "normal"
    plt.rcParams["font.weight"] = "light"
    plt.rcParams["font.size"] = 16.0
    plt.rcParams["xtick.color"] = "k"
    plt.rcParams["ytick.color"] = "k"
    plt.rcParams["ytick.major.right"] = False
    plt.rcParams["xtick.major.top"] = False
    bins = np.append([0], np.linspace(8, 60, numBins))
    hist_data_num = np.asarray([np.nan_to_num(x) for x in hist_data])[:,:,0]

    plt.figure(1)
    plt.hist(hist_data_num.transpose(), bins = bins, label = labels)
    plt.xlabel("Backscattered Intensity (dB)", color = 'k')
    plt.ylabel("Number of A-lines", color = 'k')
    plt.legend()
    plt.tight_layout()

    plt.figure(2)
    [plt.hist(shape_data, bins = bins, histtype = 'bar', alpha = 0.75, label = labels[i]) for i, shape_data in enumerate(hist_data_num)]
    plt.xlabel("Backscattered Intensity (dB)", color = 'k')
    plt.ylabel("Number of A-lines", color = 'k')
    plt.legend()
    plt.tight_layout()
    plt.show()
