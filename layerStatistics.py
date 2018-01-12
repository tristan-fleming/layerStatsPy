import pandas
from scipy.ndimage.interpolation import shift
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def load_excel(filename):
     buildData = pandas.read_excel(filename, skiprows = 2, parse_cols = 49)
     colIndex = buildData.columns
     numShapes = (len(colIndex) - 1)/ 4
     solidLayerThickness = []
     solidLayerThicknessErr = []
     powderLayerThickness = []
     powderLayerThicknessErr = []
     cubeCount = 1
     plt.style.use('ggplot')
     mpl.rcParams["font.family"] = "serif"
     mpl.rcParams["font.serif"] = "Times New Roman"
     mpl.rcParams["font.style"] = "normal"
     mpl.rcParams["font.weight"] = "light"
     mpl.rcParams["font.size"] = 14.0
     mpl.rcParams["xtick.color"] = "k"
     mpl.rcParams["ytick.color"] = "k"
     mpl.rcParams["ytick.major.right"] = False
     mpl.rcParams["xtick.major.top"] = False
     mpl.rcParams["grid.color"] = "lightgray"
     plt.rcParams["axes.facecolor"] = "w"
     #plt.rcParams["figure.edgecolor"] = "gray"
     mpl.rcParams["axes.edgecolor"] = "k"
     x = range(1, len(buildData.index))
     for colInd in range(1,len(colIndex)):
         if (colInd + 1) % 4 == 0:
            currSolidLayerThickness = shift(buildData[colIndex[colInd]].values, -1) - buildData[colIndex[colInd]].values + 50
            solidLayerThickness.append(currSolidLayerThickness[:-1])
            currSolidLayerThicknessErr = np.sqrt(shift(buildData[colIndex[colInd+1]].values, -1)**2 + buildData[colIndex[colInd+1]].values**2)
            solidLayerThicknessErr.append(currSolidLayerThicknessErr[:-1])
            plt.errorbar(x, currSolidLayerThickness[:-1], yerr = currSolidLayerThicknessErr[:-1], fmt = 'ko', capsize = 3, markersize = 5, elinewidth = 1)
            plt.ylim([-50, 150])
            plt.xlabel("Layer number", color = 'k')
            plt.ylabel("Solid layer thickness ($\mu m$)", color = 'k')
            plt.tight_layout()
            plt.savefig('solidLayerThickness_cube{0}.png'.format(cubeCount))
            plt.close()
            currPowderLayerThickness = shift(buildData[colIndex[colInd - 2]].values, -1) - buildData[colIndex[colInd]].values + 50
            powderLayerThickness.append(currPowderLayerThickness[:-1])
            currPowderLayerThicknessErr = np.sqrt(shift(buildData[colIndex[colInd - 1]].values, -1)**2 + buildData[colIndex[colInd + 1]].values**2)
            powderLayerThicknessErr.append(currPowderLayerThicknessErr[:-1])
            plt.errorbar(x, currPowderLayerThickness[:-1], yerr = currPowderLayerThicknessErr[:-1], fmt = 'ko', capsize = 3, markersize = 5, elinewidth = 1)
            plt.ylim([-75, 275])
            plt.xlabel("Layer number", color = 'k')
            plt.ylabel("Powder layer thickness ($\mu m$)", color = 'k')
            plt.tight_layout()
            plt.savefig('powderLayerThickness_cube{0}.png'.format(cubeCount))
            plt.close()
            cubeCount += 1
     return solidLayerThickness, solidLayerThicknessErr, powderLayerThickness, powderLayerThicknessErr
