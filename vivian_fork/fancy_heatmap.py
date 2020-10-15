import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
        
def fancy_heatmap(df):
    '''
    Creates a much more organized looking heatmap
    This script was created by someone online and shared in my dsir-824 class
    I did not make this, but i am implementing it here
    '''
    mask = np.zeros_like(df.corr())
    mask[np.triu_indices_from(mask)] = True

    plt.figure(figsize=(20, 10))
    sns.heatmap(
        df.corr(),
        #cmap='coolwarm',
        annot=True,
        mask = mask
    )