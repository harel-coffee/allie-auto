'''
               AAA               lllllll lllllll   iiii                      
              A:::A              l:::::l l:::::l  i::::i                     
             A:::::A             l:::::l l:::::l   iiii                      
            A:::::::A            l:::::l l:::::l                             
           A:::::::::A            l::::l  l::::l iiiiiii     eeeeeeeeeeee    
          A:::::A:::::A           l::::l  l::::l i:::::i   ee::::::::::::ee  
         A:::::A A:::::A          l::::l  l::::l  i::::i  e::::::eeeee:::::ee
        A:::::A   A:::::A         l::::l  l::::l  i::::i e::::::e     e:::::e
       A:::::A     A:::::A        l::::l  l::::l  i::::i e:::::::eeeee::::::e
      A:::::AAAAAAAAA:::::A       l::::l  l::::l  i::::i e:::::::::::::::::e 
     A:::::::::::::::::::::A      l::::l  l::::l  i::::i e::::::eeeeeeeeeee  
    A:::::AAAAAAAAAAAAA:::::A     l::::l  l::::l  i::::i e:::::::e           
   A:::::A             A:::::A   l::::::ll::::::li::::::ie::::::::e          
  A:::::A               A:::::A  l::::::ll::::::li::::::i e::::::::eeeeeeee  
 A:::::A                 A:::::A l::::::ll::::::li::::::i  ee:::::::::::::e  
AAAAAAA                   AAAAAAAlllllllllllllllliiiiiiii    eeeeeeeeeeeeee  


|  ___|       | |                        / _ \ | ___ \_   _|  _ 
| |_ ___  __ _| |_ _   _ _ __ ___  ___  / /_\ \| |_/ / | |   (_)
|  _/ _ \/ _` | __| | | | '__/ _ \/ __| |  _  ||  __/  | |      
| ||  __/ (_| | |_| |_| | | |  __/\__ \ | | | || |    _| |_   _ 
\_| \___|\__,_|\__|\__,_|_|  \___||___/ \_| |_/\_|    \___/  (_)
                                                                
                                                                
  ___            _ _       
 / _ \          | (_)      
/ /_\ \_   _  __| |_  ___  
|  _  | | | |/ _` | |/ _ \ 
| | | | |_| | (_| | | (_) |
\_| |_/\__,_|\__,_|_|\___/ 
                           
This will featurize folders of audio files if the default_audio_features = ['librosa_features']

Extracts acoustic features using the LibROSA library;
saves them as mean, standard devaition, amx, min, and median
in different classes: onset, rhythm, spectral, and power categories.

Note this is quite a powerful audio feature set that can be used
for a variety of purposes. 

For more information, check out libROSA's documentation: https://librosa.org/
'''
import os, pandas
import numpy as np 
import pandas as pd
import uuid, shutil

# https://github.com/novoic/surfboard 
def surfboard_featurize(wavfile, helpdir):
    # if categorize == True, output feature categories 
    
    # create a temporary folder 
    curdir=os.getcwd()
    wav_folder=str(uuid.uuid4())
    # copy one file over
    os.mkdir(wav_folder)
    shutil.copy(os.getcwd()+'/'+wavfile, os.getcwd()+'/'+wav_folder+'/'+wavfile)
    wav_folderpath=os.getcwd()+'/'+wav_folder

    # options are ['all_features.yaml', 'chroma_components.yaml', 'parkinsons_features.yaml','spectral_features.yaml']
    config='parkinsons_features.yaml'
    os.system('surfboard compute-features -i %s -o %s/surfboard_features.csv -F %s/surfboard/example_configs/%s -j 4'%(wav_folderpath, wav_folderpath, helpdir, config))
    os.chdir(wav_folderpath)
    g=pd.read_csv('surfboard_features.csv')
    features=list(g.iloc[0,:][0:-1])
    labels=['f0_contour_mean', 'f0_contour_std', 'f0_contour_skewness', 'f0_contour_kurtosis', 'f0_contour_first_derivative_mean', 'f0_contour_first_derivative_std', 'f0_contour_first_derivative_skewness', 'f0_contour_first_derivative_kurtosis', 'f0_contour_second_derivative_mean', 'f0_contour_second_derivative_std', 'f0_contour_second_derivative_skewness', 'f0_contour_second_derivative_kurtosis', 'f0_contour_first_quartile', 'f0_contour_second_quartile', 'f0_contour_third_quartile', 'f0_contour_q2_q1_range', 'f0_contour_q3_q2_range', 'f0_contour_q3_q1_range', 'f0_contour_percentile_1', 'f0_contour_percentile_99', 'f0_contour_percentile_1_99_range', 'f0_contour_linear_regression_offset', 'f0_contour_linear_regression_slope', 'f0_contour_linear_regression_mse', 'f0_mean', 'f0_std', 'log_energy', 'log_energy_slidingwindow_mean', 'log_energy_slidingwindow_std', 'log_energy_slidingwindow_skewness', 'log_energy_slidingwindow_kurtosis', 'log_energy_slidingwindow_first_derivative_mean', 'log_energy_slidingwindow_first_derivative_std', 'log_energy_slidingwindow_first_derivative_skewness', 'log_energy_slidingwindow_first_derivative_kurtosis', 'log_energy_slidingwindow_second_derivative_mean', 'log_energy_slidingwindow_second_derivative_std', 'log_energy_slidingwindow_second_derivative_skewness', 'log_energy_slidingwindow_second_derivative_kurtosis', 'log_energy_slidingwindow_first_quartile', 'log_energy_slidingwindow_second_quartile', 'log_energy_slidingwindow_third_quartile', 'log_energy_slidingwindow_q2_q1_range', 'log_energy_slidingwindow_q3_q2_range', 'log_energy_slidingwindow_q3_q1_range', 'log_energy_slidingwindow_percentile_1', 'log_energy_slidingwindow_percentile_99', 'log_energy_slidingwindow_percentile_1_99_range', 'log_energy_slidingwindow_linear_regression_offset', 'log_energy_slidingwindow_linear_regression_slope', 'log_energy_slidingwindow_linear_regression_mse', 'f1', 'f2', 'f3', 'f4', 'loudness', 'rms_mean', 'rms_std', 'rms_skewness', 'rms_kurtosis', 'rms_first_derivative_mean', 'rms_first_derivative_std', 'rms_first_derivative_skewness', 'rms_first_derivative_kurtosis', 'rms_second_derivative_mean', 'rms_second_derivative_std', 'rms_second_derivative_skewness', 'rms_second_derivative_kurtosis', 'rms_first_quartile', 'rms_second_quartile', 'rms_third_quartile', 'rms_q2_q1_range', 'rms_q3_q2_range', 'rms_q3_q1_range', 'rms_percentile_1', 'rms_percentile_99', 'rms_percentile_1_99_range', 'rms_linear_regression_offset', 'rms_linear_regression_slope', 'rms_linear_regression_mse', 'mfcc_mean_1', 'mfcc_mean_2', 'mfcc_mean_3', 'mfcc_mean_4', 'mfcc_mean_5', 'mfcc_mean_6', 'mfcc_mean_7', 'mfcc_mean_8', 'mfcc_mean_9', 'mfcc_mean_10', 'mfcc_mean_11', 'mfcc_mean_12', 'mfcc_mean_13', 'mfcc_std_1', 'mfcc_std_2', 'mfcc_std_3', 'mfcc_std_4', 'mfcc_std_5', 'mfcc_std_6', 'mfcc_std_7', 'mfcc_std_8', 'mfcc_std_9', 'mfcc_std_10', 'mfcc_std_11', 'mfcc_std_12', 'mfcc_std_13', 'mfcc_skewness_1', 'mfcc_skewness_2', 'mfcc_skewness_3', 'mfcc_skewness_4', 'mfcc_skewness_5', 'mfcc_skewness_6', 'mfcc_skewness_7', 'mfcc_skewness_8', 'mfcc_skewness_9', 'mfcc_skewness_10', 'mfcc_skewness_11', 'mfcc_skewness_12', 'mfcc_skewness_13', 'mfcc_kurtosis_1', 'mfcc_kurtosis_2', 'mfcc_kurtosis_3', 'mfcc_kurtosis_4', 'mfcc_kurtosis_5', 'mfcc_kurtosis_6', 'mfcc_kurtosis_7', 'mfcc_kurtosis_8', 'mfcc_kurtosis_9', 'mfcc_kurtosis_10', 'mfcc_kurtosis_11', 'mfcc_kurtosis_12', 'mfcc_kurtosis_13', 'mfcc_first_derivative_mean_1', 'mfcc_first_derivative_mean_2', 'mfcc_first_derivative_mean_3', 'mfcc_first_derivative_mean_4', 'mfcc_first_derivative_mean_5', 'mfcc_first_derivative_mean_6', 'mfcc_first_derivative_mean_7', 'mfcc_first_derivative_mean_8', 'mfcc_first_derivative_mean_9', 'mfcc_first_derivative_mean_10', 'mfcc_first_derivative_mean_11', 'mfcc_first_derivative_mean_12', 'mfcc_first_derivative_mean_13', 'mfcc_first_derivative_std_1', 'mfcc_first_derivative_std_2', 'mfcc_first_derivative_std_3', 'mfcc_first_derivative_std_4', 'mfcc_first_derivative_std_5', 'mfcc_first_derivative_std_6', 'mfcc_first_derivative_std_7', 'mfcc_first_derivative_std_8', 'mfcc_first_derivative_std_9', 'mfcc_first_derivative_std_10', 'mfcc_first_derivative_std_11', 'mfcc_first_derivative_std_12', 'mfcc_first_derivative_std_13', 'mfcc_first_derivative_skewness_1', 'mfcc_first_derivative_skewness_2', 'mfcc_first_derivative_skewness_3', 'mfcc_first_derivative_skewness_4', 'mfcc_first_derivative_skewness_5', 'mfcc_first_derivative_skewness_6', 'mfcc_first_derivative_skewness_7', 'mfcc_first_derivative_skewness_8', 'mfcc_first_derivative_skewness_9', 'mfcc_first_derivative_skewness_10', 'mfcc_first_derivative_skewness_11', 'mfcc_first_derivative_skewness_12', 'mfcc_first_derivative_skewness_13', 'mfcc_first_derivative_kurtosis_1', 'mfcc_first_derivative_kurtosis_2', 'mfcc_first_derivative_kurtosis_3', 'mfcc_first_derivative_kurtosis_4', 'mfcc_first_derivative_kurtosis_5', 'mfcc_first_derivative_kurtosis_6', 'mfcc_first_derivative_kurtosis_7', 'mfcc_first_derivative_kurtosis_8', 'mfcc_first_derivative_kurtosis_9', 'mfcc_first_derivative_kurtosis_10', 'mfcc_first_derivative_kurtosis_11', 'mfcc_first_derivative_kurtosis_12', 'mfcc_first_derivative_kurtosis_13', 'mfcc_second_derivative_mean_1', 'mfcc_second_derivative_mean_2', 'mfcc_second_derivative_mean_3', 'mfcc_second_derivative_mean_4', 'mfcc_second_derivative_mean_5', 'mfcc_second_derivative_mean_6', 'mfcc_second_derivative_mean_7', 'mfcc_second_derivative_mean_8', 'mfcc_second_derivative_mean_9', 'mfcc_second_derivative_mean_10', 'mfcc_second_derivative_mean_11', 'mfcc_second_derivative_mean_12', 'mfcc_second_derivative_mean_13', 'mfcc_second_derivative_std_1', 'mfcc_second_derivative_std_2', 'mfcc_second_derivative_std_3', 'mfcc_second_derivative_std_4', 'mfcc_second_derivative_std_5', 'mfcc_second_derivative_std_6', 'mfcc_second_derivative_std_7', 'mfcc_second_derivative_std_8', 'mfcc_second_derivative_std_9', 'mfcc_second_derivative_std_10', 'mfcc_second_derivative_std_11', 'mfcc_second_derivative_std_12', 'mfcc_second_derivative_std_13', 'mfcc_second_derivative_skewness_1', 'mfcc_second_derivative_skewness_2', 'mfcc_second_derivative_skewness_3', 'mfcc_second_derivative_skewness_4', 'mfcc_second_derivative_skewness_5', 'mfcc_second_derivative_skewness_6', 'mfcc_second_derivative_skewness_7', 'mfcc_second_derivative_skewness_8', 'mfcc_second_derivative_skewness_9', 'mfcc_second_derivative_skewness_10', 'mfcc_second_derivative_skewness_11', 'mfcc_second_derivative_skewness_12', 'mfcc_second_derivative_skewness_13', 'mfcc_second_derivative_kurtosis_1', 'mfcc_second_derivative_kurtosis_2', 'mfcc_second_derivative_kurtosis_3', 'mfcc_second_derivative_kurtosis_4', 'mfcc_second_derivative_kurtosis_5', 'mfcc_second_derivative_kurtosis_6', 'mfcc_second_derivative_kurtosis_7', 'mfcc_second_derivative_kurtosis_8', 'mfcc_second_derivative_kurtosis_9', 'mfcc_second_derivative_kurtosis_10', 'mfcc_second_derivative_kurtosis_11', 'mfcc_second_derivative_kurtosis_12', 'mfcc_second_derivative_kurtosis_13', 'mfcc_first_quartile_1', 'mfcc_first_quartile_2', 'mfcc_first_quartile_3', 'mfcc_first_quartile_4', 'mfcc_first_quartile_5', 'mfcc_first_quartile_6', 'mfcc_first_quartile_7', 'mfcc_first_quartile_8', 'mfcc_first_quartile_9', 'mfcc_first_quartile_10', 'mfcc_first_quartile_11', 'mfcc_first_quartile_12', 'mfcc_first_quartile_13', 'mfcc_second_quartile_1', 'mfcc_second_quartile_2', 'mfcc_second_quartile_3', 'mfcc_second_quartile_4', 'mfcc_second_quartile_5', 'mfcc_second_quartile_6', 'mfcc_second_quartile_7', 'mfcc_second_quartile_8', 'mfcc_second_quartile_9', 'mfcc_second_quartile_10', 'mfcc_second_quartile_11', 'mfcc_second_quartile_12', 'mfcc_second_quartile_13', 'mfcc_third_quartile_1', 'mfcc_third_quartile_2', 'mfcc_third_quartile_3', 'mfcc_third_quartile_4', 'mfcc_third_quartile_5', 'mfcc_third_quartile_6', 'mfcc_third_quartile_7', 'mfcc_third_quartile_8', 'mfcc_third_quartile_9', 'mfcc_third_quartile_10', 'mfcc_third_quartile_11', 'mfcc_third_quartile_12', 'mfcc_third_quartile_13', 'mfcc_q2_q1_range_1', 'mfcc_q2_q1_range_2', 'mfcc_q2_q1_range_3', 'mfcc_q2_q1_range_4', 'mfcc_q2_q1_range_5', 'mfcc_q2_q1_range_6', 'mfcc_q2_q1_range_7', 'mfcc_q2_q1_range_8', 'mfcc_q2_q1_range_9', 'mfcc_q2_q1_range_10', 'mfcc_q2_q1_range_11', 'mfcc_q2_q1_range_12', 'mfcc_q2_q1_range_13', 'mfcc_q3_q2_range_1', 'mfcc_q3_q2_range_2', 'mfcc_q3_q2_range_3', 'mfcc_q3_q2_range_4', 'mfcc_q3_q2_range_5', 'mfcc_q3_q2_range_6', 'mfcc_q3_q2_range_7', 'mfcc_q3_q2_range_8', 'mfcc_q3_q2_range_9', 'mfcc_q3_q2_range_10', 'mfcc_q3_q2_range_11', 'mfcc_q3_q2_range_12', 'mfcc_q3_q2_range_13', 'mfcc_q3_q1_range_1', 'mfcc_q3_q1_range_2', 'mfcc_q3_q1_range_3', 'mfcc_q3_q1_range_4', 'mfcc_q3_q1_range_5', 'mfcc_q3_q1_range_6', 'mfcc_q3_q1_range_7', 'mfcc_q3_q1_range_8', 'mfcc_q3_q1_range_9', 'mfcc_q3_q1_range_10', 'mfcc_q3_q1_range_11', 'mfcc_q3_q1_range_12', 'mfcc_q3_q1_range_13', 'mfcc_percentile_1_1', 'mfcc_percentile_1_2', 'mfcc_percentile_1_3', 'mfcc_percentile_1_4', 'mfcc_percentile_1_5', 'mfcc_percentile_1_6', 'mfcc_percentile_1_7', 'mfcc_percentile_1_8', 'mfcc_percentile_1_9', 'mfcc_percentile_1_10', 'mfcc_percentile_1_11', 'mfcc_percentile_1_12', 'mfcc_percentile_1_13', 'mfcc_percentile_99_1', 'mfcc_percentile_99_2', 'mfcc_percentile_99_3', 'mfcc_percentile_99_4', 'mfcc_percentile_99_5', 'mfcc_percentile_99_6', 'mfcc_percentile_99_7', 'mfcc_percentile_99_8', 'mfcc_percentile_99_9', 'mfcc_percentile_99_10', 'mfcc_percentile_99_11', 'mfcc_percentile_99_12', 'mfcc_percentile_99_13', 'mfcc_percentile_1_99_range_1', 'mfcc_percentile_1_99_range_2', 'mfcc_percentile_1_99_range_3', 'mfcc_percentile_1_99_range_4', 'mfcc_percentile_1_99_range_5', 'mfcc_percentile_1_99_range_6', 'mfcc_percentile_1_99_range_7', 'mfcc_percentile_1_99_range_8', 'mfcc_percentile_1_99_range_9', 'mfcc_percentile_1_99_range_10', 'mfcc_percentile_1_99_range_11', 'mfcc_percentile_1_99_range_12', 'mfcc_percentile_1_99_range_13', 'mfcc_linear_regression_offset_1', 'mfcc_linear_regression_offset_2', 'mfcc_linear_regression_offset_3', 'mfcc_linear_regression_offset_4', 'mfcc_linear_regression_offset_5', 'mfcc_linear_regression_offset_6', 'mfcc_linear_regression_offset_7', 'mfcc_linear_regression_offset_8', 'mfcc_linear_regression_offset_9', 'mfcc_linear_regression_offset_10', 'mfcc_linear_regression_offset_11', 'mfcc_linear_regression_offset_12', 'mfcc_linear_regression_offset_13', 'mfcc_linear_regression_slope_1', 'mfcc_linear_regression_slope_2', 'mfcc_linear_regression_slope_3', 'mfcc_linear_regression_slope_4', 'mfcc_linear_regression_slope_5', 'mfcc_linear_regression_slope_6', 'mfcc_linear_regression_slope_7', 'mfcc_linear_regression_slope_8', 'mfcc_linear_regression_slope_9', 'mfcc_linear_regression_slope_10', 'mfcc_linear_regression_slope_11', 'mfcc_linear_regression_slope_12', 'mfcc_linear_regression_slope_13', 'mfcc_linear_regression_mse_1', 'mfcc_linear_regression_mse_2', 'mfcc_linear_regression_mse_3', 'mfcc_linear_regression_mse_4', 'mfcc_linear_regression_mse_5', 'mfcc_linear_regression_mse_6', 'mfcc_linear_regression_mse_7', 'mfcc_linear_regression_mse_8', 'mfcc_linear_regression_mse_9', 'mfcc_linear_regression_mse_10', 'mfcc_linear_regression_mse_11', 'mfcc_linear_regression_mse_12', 'mfcc_linear_regression_mse_13', 'localJitter', 'localabsoluteJitter', 'rapJitter', 'ppq5Jitter', 'ddpJitter', 'localShimmer', 'localdbShimmer', 'apq3Shimmer', 'apq5Shimmer', 'apq11Shimmer', 'hnr', 'ppe', 'dfa']
    os.chdir(curdir)
    shutil.rmtree(wav_folder)

    return features, labels
