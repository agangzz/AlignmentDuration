
# coding: utf-8

'''
open results in praat

visualizes errors for different as graph. matplotlib
'''
import sys
import os
from Phonetizer import Phonetizer
from matplotlib.axes import Axes
parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]) ), os.path.pardir)) 

#  evaluation  
pathEvaluation = os.path.join(parentDir, 'AlignmentEvaluation')
if not pathEvaluation in sys.path:
    sys.path.append(pathEvaluation)

# 
# from PraatVisualiser import addAlignmentResultToTextGrid, openTextGridInPraat, addAlignmentResultToTextGridFIle, \
#   _alignmentResult2TextGrid

# from tab2PraatAndOpenWithPRaat import tab2PraatAndOpenWithPRaat 

# from TextGrid_Parsing import tier_names


import matplotlib.pylab as plt
import matplotlib
import numpy as np
ANNOTATION_EXT = '.TextGrid'  


def visualizeBMap(b_Map): 

            matplotlib.interactive(False)

#             plt.figure(figsize=(16,8))
            fig, ax = plt.subplots()
#             ax.imshow(self.B_map, extent=[0, 200, 0, 100], interpolation='none')
            plt.imshow(b_Map, interpolation='none')

#             plt.colorbar()
#             fig.colorbar()
            ax.autoscale(False)
            plt.title('B_map')
            plt.show(block=True)
            return ax


def visualizeMatrix(psi,  titleName):
        psi = np.rot90(psi)
        psi = np.flipud(psi)
#         plt.figure(1)
        fig, ax1 = plt.subplots()
        ax  = plt.imshow(psi, interpolation='none')
        plt.colorbar(ax)
        plt.grid(True)
        plt.title(titleName)
#         plt.tight_layout()
        
        plt.show() 
        return ax1 
        

def visualizePath( ax, path, B_map):
    ''' print path on top of existing plot
    '''
            
    if B_map.shape[1] != len(path):
        sys.exit("obs features are {}, but path has duration {}".format(B_map.shape[1], len(path)))
    
    plt.plot(path, marker='x', color='k', markersize=5)
    
    plt.show()





    

def plotStuff():
    # In[14]:
    
    #x - alpha
    alphas = np.arange(0.81,1,0.01)
    
    
    
    #errors for olmaz ilaç
    errorMeans = [ 2.13, 2.13, 2.03, 1.65, 1.44,1.34, 1.3, 1.07, 1.07, 1.06, 1.07, 0.9, 0.9, 0.89, 0.63, 0.13, 0.13, 0.13, 0.12 ]
    errorStDev = [2.18,  2.18, 2.22, 2.13, 2.09, 2.12, 2.14, 1.86, 1.86, 1.86, 1.87, 1.86, 1.85,1.85,  1.75, 0.17, 0.16, 0.17, 0.15]
    
    
    
    # In[15]:
    
    len(alphas)
    
    
    # In[ ]:
    
    
    plt.plot(alphas,errorMeans, 'r^', alphas, errorStDev, 'bs' )
    plt.show()

