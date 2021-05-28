import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import sklearn
import sklearn.linear_model
import sklearn.ensemble
import sklearn.neighbors
import sklearn.svm

con = sqlite3.connect("prostate_cancer.db")

df = pd.read_sql("SELECT * FROM PATIENT", con)

# Distribution histograms
fig, axs = plt.subplots(4, 3, figsize=(20,15))
n_bins = len(df)
axs[0][0].hist(df['age'], bins=n_bins)
axs[0][0].set_title('age')
axs[0][1].hist(df['weight'], bins=n_bins)
axs[0][1].set_title('weight')
axs[0][2].hist(df['height'], bins=n_bins)
axs[0][2].set_title('height')
axs[1][0].hist(df['bmi'], bins=n_bins)
axs[1][0].set_title('bmi')
axs[1][1].hist(df['prostate_volume'], bins=n_bins)
axs[1][1].set_title('prostate_volume')
axs[1][2].hist(df['psa'], bins=n_bins)
axs[1][2].set_title('psa')
axs[2][0].hist(df['density_psa'], bins=n_bins)
axs[2][0].set_title('density_psa')
axs[2][1].hist(df['G'], bins=n_bins)
axs[2][1].set_title('glison_score')
axs[2][2].hist(df['T'], bins=n_bins)
axs[2][2].set_title('T')
axs[3][0].hist(df['N'], bins=n_bins)
axs[3][0].set_title('N')
axs[3][1].hist(df['M'], bins=n_bins)
axs[3][1].set_title('M')

# Math expectation and variance for numeric variables
# get values
age = np.array(list(df['age']))
bmi = np.array(list(df['bmi']))
prostate_volume = np.array(list(df['prostate_volume']))
psa = np.array(list(df['psa']))
density_psa = np.array(list(df['density_psa']))
glison_score = np.array(list(df['G']))

# auxiliary variables
mean_age = 0.0
mean_bmi = 0.0
mean_pr_v = 0.0
mean_psa = 0.0
mean_den_psa = 0.0
mean_glison = 0.0
dis_age = 0.0
dis_bmi = 0.0
dis_pr_v = 0.0
dis_psa = 0.0
dis_den_psa = 0.0
dis_glison = 0.0

# find mathematical expectation
for i in range(age.size):
  mean_age = mean_age + age[i]
  mean_bmi = mean_bmi + bmi[i]
  mean_pr_v = mean_pr_v + prostate_volume[i]
  mean_psa = mean_psa + psa[i]
  mean_den_psa = mean_den_psa + density_psa[i]
  mean_glison = mean_glison + glison_score[i]
mean_age = mean_age/age.size
mean_bmi = mean_bmi/bmi.size
mean_pr_v = mean_pr_v/prostate_volume.size
mean_psa = mean_psa/psa.size
mean_den_psa = mean_den_psa/density_psa.size
mean_glison = mean_glison/glison_score.size
print('math expectation')
print(mean_age)
print(mean_bmi)
print(mean_pr_v)
print(mean_psa)
print(mean_den_psa)
print(mean_glison)
print()

# calculate variance
for i in range(age.size):
  dis_age = dis_age + ((age[i] - mean_age) * (age[i] - mean_age))
  dis_bmi = dis_bmi + ((bmi[i]-mean_bmi)*(bmi[i]-mean_bmi))
  dis_pr_v = dis_pr_v + ((prostate_volume[i] - mean_pr_v)*(prostate_volume[i] - mean_pr_v))
  dis_psa = dis_psa + ((psa[i]-mean_psa)*(psa[i]-mean_psa))
  dis_den_psa = dis_den_psa + ((density_psa[i]-mean_den_psa)*(density_psa[i]-mean_den_psa))
  dis_glison = dis_glison + ((glison_score[i]-mean_glison)*(glison_score[i]-mean_glison))
dis_age = dis_age/age.size
dis_bmi = dis_bmi/age.size
dis_pr_v = dis_pr_v/age.size
dis_psa = dis_psa/age.size
dis_den_psa = dis_den_psa/age.size
dis_glison = dis_glison/age.size

# calculate and print standard deviation
print("standard deviation")
print(sqrt(dis_age))
print(sqrt(dis_bmi))
print(sqrt(dis_pr_v))
print(sqrt(dis_psa))
print(sqrt(dis_den_psa))
print(sqrt(dis_glison))
print()

# Correlation between features
# Graphical view
# dependence of the result on features
fig2, axs2 = plt.subplots(4, 3, figsize=(20, 15))
y = df['G']

x_1 = df['age']
axs2[0][0].scatter(x_1, y)
axs2[0][0].set_title('age')

x_2 = df['weight']
axs2[0][1].scatter(x_2, y)
axs2[0][1].set_title('weight')

x_3 = df['height']
axs2[0][2].scatter(x_3, y)
axs2[0][2].set_title('height')

x_4 = df['bmi']
axs2[1][0].scatter(x_4, y)
axs2[1][0].set_title('bmi')

x_5 = df['prostate_volume']
axs2[1][1].scatter(x_5, y)
axs2[1][1].set_title('prostate_volume')

x_6 = df['psa']
axs2[1][2].scatter(x_6, y)
axs2[1][2].set_title('psa')

x_7 = df['density_psa']
axs2[2][0].scatter(x_7, y)
axs2[2][0].set_title('density_psa')

axs2[2][1].scatter(x_4,x_1)
axs2[2][1].set_title('bmi/age')

axs2[2][2].scatter(x_6,x_4)
axs2[2][2].set_title('psa/bmi')

axs2[3][0].scatter(x_6,x_1)
axs2[3][0].set_title('psa/age')

axs2[3][1].scatter(x_7,x_1)
axs2[3][1].set_title('prostate_volume/age')

axs2[3][2].scatter(x_7,x_4)
axs2[3][2].set_title('prostate_volume/bmi')

# Text view and multiple correlation
t_to_int = []
n_to_int = []
m_to_int = []
for i in range(len(df)):
    n_to_int.append(int(df['N'][i]))
    m_to_int.append(int(df['M'][i]))
    if df['T'][i] == '1':
        t_to_int.append(1)
    if df['T'][i] == '2':
        t_to_int.append(2)
    if df['T'][i] == '2b':
        t_to_int.append(3)
    if df['T'][i] == '2c':
        t_to_int.append(4)
    if df['T'][i] == '3':
        t_to_int.append(5)
    if df['T'][i] == '3a':
        t_to_int.append(6)
    if df['T'][i] == '3b':
        t_to_int.append(7)
    if df['T'][i] == '4':
        t_to_int.append(8)
correlG = df[['age', 'bmi', 'prostate_volume', 'psa', 'G','T']]
correlT = pd.DataFrame(t_to_int,
                   columns=['T'])
correl = pd.concat([correlG, correlT], axis=1)
correlN = df[['age', 'bmi', 'prostate_volume', 'psa', 'N']]
pd.set_option('display.max_columns', None)

# consider two methods: Pearson and Spearman
print(correl.corr(method='pearson'))
print()
print(correl.corr(method='spearman'))
print()
A = np.matrix('1.000000 -0.106871 0.127555 0.007858 -0.110815; -0.106871 1.000000 0.116146 0.037647 0.053997; 0.127555 0.116146 1.000000 0.087774 -0.028541; 0.007858 0.037647 0.087774 1.000000 0.113570; -0.110815 0.053997 -0.028541 0.113570 1.000000')
A_small = np.matrix('1.000000 -0.106871 0.127555 0.007858; -0.106871 1.000000 0.116146 0.037647; 0.127555 0.116146 1.000000 0.087774; 0.007858 0.037647 0.087774 1.000000')
B = np.matrix('1.000000 -0.091538 0.125416 -0.062808 -0.078494; -0.091538 1.000000 0.030320 0.016410 0.038074; 0.125416 0.030320 1.000000 0.267838 -0.022243; -0.062808 0.016410 0.267838 1.000000 0.155974; -0.078494 0.038074 -0.022243 0.155974 1.000000')
B_small = np.matrix('1.000000 -0.091538 0.125416 -0.062808; -0.091538 1.000000 0.030320 0.016410; 0.125416 0.030320 1.000000 0.267838; -0.062808 0.016410 0.267838 1.000000')
A_t = np.matrix('1.000000 -0.106871 0.127555 0.007858 -0.146134; -0.106871 1.000000 0.116146 0.037647 0.043986; 0.127555 0.116146 1.000000 0.087774 -0.105494; 0.007858 0.037647 0.087774 1.000000 0.084078; -0.146134 0.043986 -0.105494 0.084078 1.000000')
B_t = np.matrix('1.000000 -0.091538 0.125416 -0.062808 -0.137139; -0.091538 1.000000 0.030320 0.016410 0.067020; 0.125416 0.030320 1.000000 0.267838 -0.078902; -0.062808 0.016410 0.267838 1.000000 0.051869; -0.137139 0.067020 -0.078902 0.051869 1.000000')
m_corr_p_g = 1 - (np.linalg.det(A)/np.linalg.det(A_small))
m_corr_s_g = 1 - (np.linalg.det(B)/np.linalg.det(B_small))
m_corr_p_t = 1 - (np.linalg.det(A_t)/np.linalg.det(A_small))
m_corr_s_t = 1 - (np.linalg.det(B_t)/np.linalg.det(B_small))
print(sqrt(m_corr_p_g))
print(sqrt(m_corr_s_g))
print(sqrt(m_corr_p_t))
print(sqrt(m_corr_s_t))

# Show results 
plt.show()
