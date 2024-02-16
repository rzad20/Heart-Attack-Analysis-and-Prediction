#!/usr/bin/env python
# coding: utf-8

# # Analisa Kinerja *Random Forest Classifier* dan *AdaBoost Classifier* Dalam Memprediksi Pasien Berisiko Serangan Jantung

# Pihak medis atau pihak dalam industri kesehatan memiliki peranan dalam mengedukasi masyarakat untuk rutin mengecek kondisi mereka dan rutin dalam menjaga diri mereka agar tidak mengalami serangan jantung. Namun, dengan jumlah masyarakat yang cukup banyak sering kali menyulitkan pihak medis untuk memberikan perhatian dan edukasi pada setiap individu. Oleh karena itu, dibutuhkan algoritma prediksi serangan jantung, yang diharapkan dapat memberikan dukungan tambahan bagi pihak medis dalam mengidentifikasi potensi risiko serangan jantung pada setiap individu secara lebih efisien.
# 
# Dalam tahap awal proyek ini, fokus penelitian adalah mencari algoritma klasifikasi yang tepat dalam menentukan risiko individu berisiko terkena serangan jantung atau tidak, algoritma ini nantinya akan mengintegrasikan berbagai data klinis dan faktor risiko yang relevan untuk memprediksi risiko serangan jantung pada individu. Diharapkan dengan algoritma ini akan menjadi alat yang berguna bagi pihak medis dalam meningkatkan deteksi dini dalam pencegahan serangan jantung, serta meningkatkan kesadaran masyarakat tentang pentingnya menjaga kesehatan jantung.

# ## *Import Library* Yang Dibutuhkan

# Tahap ini merupakan tahap memasukkan *Library* yang digunakan dalam pengerjaan proyek, adapun library yang digunakan adalah :
# 1. **Numpy** - Library untuk operasi matematika pada array dan matriks multidimensi
# 2. **Pandas** - Menyediakan struktur data dan alat analisis data yang mudah digunakan, terutama untuk bekerja dengan dataframe
# 3. **Matplotlib** - Library untuk visualisasi data dalam bentuk grafik, plot, histogram, dll
# 4. **Seaborn** - Memperindah plot matplotlib dengan antarmuka 
# 5. **Label Encoder** - Untuk mengubah label kategorikal menjadi bentuk yang dapat diolah oleh algoritma
# 6. **StandardScaler** - Metode untuk menskalakan fitur sehingga memiliki rata-rata nol dan varians satu, membantu algoritma Machine Learning menangani data dengan efisien.
# 7. **TrainTestSplit** - Memisahkan data menjadi data latih dan data uji
# 8. **RandomForestClassifier** - Algoritma ensemble untuk klasifikasi yang menggunakan kombinasi dari pohon keputusan.
# 9. **AdaBoostClassifier** - Algoritma klasifikasi ensemble yang menggabungkan beberapa model klasifikasi lemah menjadi satu model klasifikasi yang kuat, dengan fokus pada perbaikan kesalahan klasifikasi iteratif.
# 10. **accuracy_score** - Metrik untuk mengukur akurasi klasifikasi.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score


# ## *Load* Data Kedalam Proyek Klasifikasi

# Tahap berikutnya adalah memasukkan dataset yang digunakan dalam proyek ini
# Dalam membangun model prediksi, proyek ini akan menggunakan data Heart Attack Risk Prediction Dataset yang dibuat oleh Sourav Banerjee.
# dataset ini didapatkan dari platform Kaggle dan dapat diakses di [Link Berikut Ini](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset)

# Kode dibawah ini digunakan untuk memasukkan dan *load* data terkait dalam *dataframe* menggunakan *library* **Pandas**. dan melihat preview data yang telah dimasukkan

# In[2]:


dataset = pd.read_csv('heart_attack_prediction_dataset.csv')
dataset


# Melihat *Preview* data diatas, tentunya tidak keseluruhan variabel akan digunakan untuk memprediksi risiko serangan jantung pada individu, hal ini akan ditentukan dalam tahapan selanjutnya yaitu Analisis Data.

# ## Tahapan Analisis Data

# Tahapan pertama yang dilakukan adalah Identifikasi Dataset yang dipakai, beserta tipe data masing masing kolom, hal ini dapat dilakukan menggunakan kode dibawah ini

# In[3]:


dataset.info()


# Sesuai dengan informasi dataset yang didapatkan dalam sumber data, Dataset terkait memiliki 26 fitur, yang mana 25 fitur akan diseleksi dalam proses analisis data selanjutnya untuk digunakan dalam algoritma prediksi, dan 1 fitur target yaitu **Heart Attack Risk**
# 
# Berikut adalah daftar variabel yang terdapat dalam dataset
# 1. **Patient ID** - Identifikasi unik untuk setiap pasien.
# 2. **Age** - Usia Pasien (Numerikal).
# 3. **Sex** - Kategori Jenis Kelamin Pasien (Kategorikal : Laki-Laki/Perempuan).
# 4. **Cholesterol** - Tingkat Kolesterol Pasien (Numerikal).
# 5. **Blood Pressure** - Tingkat tekanan darah pasien (Numerikal).
# 6. **Heart Rate** - Denyut jantung pasien.
# 7. **Diabetes** - Apakah pasien memiliki diabetes (Kategorikal : Ya/Tidak).
# 8. **Family History** - Riwayat Keluarga terkait masalah jantung (Kategorikal : 1 - Ya, 0 - Tidak)
# 9. **Smoking** - Status Perokok Pasien (Kategorikal : 1 - Ya, 0 - Tidak)
# 10. **Obesity** - Status Obesitas Pasien (Kategorikal : 1 - Obesitas, 0 - Tidak Obesitas)
# 11. **Alcohol Consumption** - Tingkat konsumsi alkohol oleh pasien (Kategorikal : None/Light/Moderate/Heavy)
# 12. **Exercise Hours Per Week** - Jumlah Jam Olahraga Per Minggu (Numerikal)
# 13. **Diet** - Kebiasaan diet pasien (Kategorikal : Healthy/Average/Unhealthy)
# 14. **Previous Heart Problems** - Riwayat penyakit jantung pasien sebelumnya (Kategorikal : 1 - Ya, 0 - Tidak)
# 15. **Medication Use** - Penggunaan obat oleh pasien (Kategorikal : 1 - Ya, 0 - Tidak)
# 16. **Stress Level** - Tingkat Level Stress Pasien (1-10)
# 17. **Sedentary Hours Per Day** - Jam aktivitas duduk per hari (Kategorikal)
# 18. **Income** - Tingkat pendapatan pasien (Numerikal)
# 19. **BMI** - Index massa tubuh pasien (Numerikal)
# 20. **Triglycerides** - Tingkat trgliserida Pasien
# 21. **Physical Activity Days Per Week** - Hari-hari aktivitas fisik per minggu.
# 22. **Sleep Hours Per Day** - Jam tidur per hari
# 23. **Country** - Negara Tempat Tinggal Pasien
# 24. **Continent** - Benua tempat Tinggal Pasien
# 25. **Hemisphere** - Belahan bumi tempat tinggal pasien
# 26. **Heart Attack Risk** - Variabel Target Prediksi risiko serangan jantung (Kategori 1 : Memiliki Risiko, 0 - Tidak)

# Langkah Selanjutnya adalah, Data harus dianalisa apakah dia memiliki **Missing Values** atau tidak, hal ini dapat dilakukan menggunakan fungsi isna() yang tersedia dalam **Pandas**

# In[4]:


dataset.isna().sum()


# Hasil analisa diatas dapat diketahui bahwa dataset yang digunakan tidak memiliki **Missing Values**.

# Selanjutnya adalah, kita harus mengecek apakah terdapat duplikasi terhadap data, jumlah duplikasi dapat dicari menggunakan fungsi **duplicated()** yang terdapat dalam pandas, dan kita menggunakan bantuan fungsi **Sum()** untuk menghitung jumlah data duplikat tersebut.

# In[5]:


print("Jumlah Duplikasi : ", dataset.duplicated().sum())


# Hasil kode diatas menunjukkan bahwa tidak ada duplikasi data dalam data terkait.

# Langkah selanjutnya adalah mengidentifikasi adanya **Outlier** atau **Pencilan** Dalam Data.
# **Outliers** adalah sampel yang nilainya sangat jauh dari cakupan umum data utama, ia adalah hasil pengamatan yang
# kemunculannya sangat jarang dan berbeda dari hasil pengamatan lainnya.

# Dalam proyek ini, kita akan menggunakan Metode **IQR Method** dalam mengatasi outlier.
# Metode *Inter Quartile Range* atau IQR berhubungan dengan konsep kuartil. Kuartil dari suatu populasi adalah
# tiga nilai yang membagi distribusi data menjadi empat sebaran. Seperempat dari data berada pada kuartil pertama (Q1),
# setengah dari data berada dibawah kuartil kedua (Q2), dan tiga perempat dari data berada di kuartil ketiga (Q3).
# 
# Nilai Interquartile Range didapatkan dengan rumus
# 
# IQR = Q3 - Q1
# 
# Kita akan menggunakan Bantuan Visualisasi Data Menggunakan **Boxplot** untuk mendeteksi outlier. dalam **Boxplot**, 
# menunjukkan ukuran lokasi dan penyebaran, serta memberikan informasi tentang simetri dan outliers.
# 
# Sekarang...mari visualisasikan dataset dengan *Boxplot* untuk mendeteksi *outliers* pada kolom numerikal.

# **Fitur *age***

# In[6]:


sns.boxplot(x=dataset['Age'])


# Dalam *Boxplot* diatas, tidak ditemukan *Outliers* pada kolom numerik *Age*

# **Fitur *Cholesterol***

# In[7]:


sns.boxplot(x=dataset['Cholesterol'])


# Dalam *Boxplot* diatas, tidak ditemukan Outliers pada kolom numerik *Cholesterol*

# Identifikasi *Outliers* dapat lebih cepat dilakukan apabila kita memanfaatkan *For Loop* untuk membuat visualisasi boxplot sekaligus kepada seluruh kolom numerikal dalam dataset

# In[8]:


# Pilih kolom numerikal kecuali 'Age' dan 'Cholesterol'
num_cols = dataset.select_dtypes(include=['number']).columns
num_cols = [col for col in num_cols if col not in ['Age', 'Cholesterol', 'Smoking', 'Heart Attack Disease']]

# Buat visualisasi boxplot
fig, axes = plt.subplots(len(num_cols), 1, figsize=(8, 6 * len(num_cols)))
axes = axes.flatten()

for i, column in enumerate(num_cols):
    sns.boxplot(x=dataset[column], ax=axes[i])
    axes[i].set_title(f'Boxplot for {column}')
    axes[i].set_xlabel(column)

plt.tight_layout(h_pad=2, w_pad=2)
plt.show()


# Hasil analisa juga menunjukkan jika dataset yang ada tidak memiliki *Outliers* untuk kolom numerikalnya

# Tahap berikutnya adalah mengetahui *Shape* dari dataset yang kita gunakan.

# In[9]:


dataset.shape


# Dataset yang kita gunakan memiliki 8763 baris data dengan 26 fitur.

# Tahapan selanjutnya yang dilakukan adalah tahapan **Univariate Analysis** dan **Multivariate Analysis**.

# ### Univariate Analysis
# Tahapan ini merupakan tahapan menganalisa satu persatu fitur kategorikal dan numerikal dalam dataset.

# ### Analisis Fitur Kategorikal

# **Fitur Jenis Kelamin (*Sex*)**

# Berikut adalah pengecekan distribusi data berdasarkan jenis kelamin.

# In[10]:


feature = 'Sex'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Distribusi data diatas menunjukkan bahwa lebih banyak data pasien pria ketimbang wanita didalam dataset

# **Fitur Diabetes**

# Berikut adalah pengecekan distribusi data berdasarkan kategori diabetes

# In[11]:


feature = 'Diabetes'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Visualisasi diatas menunjukkan bahwa kebanyakan pasien dalam data mengalami diabetes (65,2%), sedangkan sisanya tidak mengalami diabetes

# **Fitur *Family History***

# Berikut adalah hasil pengecekan untuk *Family History*

# In[12]:


feature = 'Family History'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dalam distribusi diatas terlihat terhadap jumlah yang hampir seimbang antara pasien yang memiliki riwayat keluarga terkena penyakit jantung, dan yang tidak

# **Fitur *Smoking***

# Berikut adalah kode untuk mengecek sebaran data berdasarkan pasien perokok atau tidak

# In[13]:


feature = 'Smoking'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dari visualisasi data diatas dapat dilihat, sebagian besar data pasien merupakan perokok (Sekitar 89 Persen) sedangkan sisanya adalah bukan perokok

# **Fitur *Obesity***

# Berikut adalah pengecekkan sebaran data berdasarkan pasien mengalami Obesitas atau Tidak

# In[14]:


feature = 'Obesity'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dalam distribusi diatas terlihat terhadap jumlah yang hampir seimbang antara pasien mengalami obesitas atau tidak

# **Fitur *Alcohol Consumption***

# Selanjutnya akan dicek penyebaran data berdasarkan tingkat konsumsi alkohol pasien

# In[15]:


feature = 'Alcohol Consumption'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dalam visualisasi diatas, dapat disimpulkan bahwa terdapat hampir lebih dari setengah data pasien pernah mengkonsumsi alkohol, sedangkan sisanya tidak

# **Fitur *Diet***

# Berikut adalah analisa untuk melihat sebaran data pasien berdasarkan kebiasaan diet mereka

# In[16]:


feature = 'Diet'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Terlihat dalam visualisasi data diatas, terdapat distribusi yang cukup seimbang antara pasien dengan kebiasaan diet *Healthy*, Kebiasan Diet *Average*, dan *Unhealthy*

# **Fitur *Previous Heart Problems***

# Berikut adalah pengecekkan sebaran data berdasarkan riwayat mereka mengalami penyakit jantung sebelumnya

# In[17]:


feature = 'Previous Heart Problems'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dalam data diatas, sekitar 49,6 Persen pasien memiliki riwayat penyakit jantung sebelumnya, sedangkan sisanya belum pernah mengalami

# **Fitur *Medication Use***

# Berikut adalah pengecekan distribusi data berdasarkan pasien sedang dalam penggunaan obat atau tidak

# In[18]:


feature = 'Medication Use'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Dalam data diatas, sekitar 49,8 Persen pasien memiliki riwayat penyakit jantung sebelumnya, sedangkan sisanya belum pernah mengalami

# **Fitur *Stress Level***

# Berikut adalah sebaran data berdasarkan level stress pasien

# In[19]:


feature = 'Stress Level'
count = dataset[feature].value_counts()
percent = 100*dataset[feature].value_counts(normalize=True)
count.plot(kind='bar', title=feature)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)


# Diketahui terdapat distribusi data yang cukup seimbang antara masing masing level stress pasien (Skala 1-100)

# ## Persiapan Data

# ### Menghapus Kolom Yang Tidak Digunakan

# Beberapa kolom dalam dataset tidak akan digunakan dalam proses membangun Algoritma Prediksi, hal tersebut dikarenakan kolom terkait tidak relevan terhadap proses analisis, Kolom Tersebut adalah Kolom **Patient ID**, **Country**, **Continent**, dan **Hemisphere**

# In[20]:


deleted_columns = ["Patient ID", "Country", "Continent", "Hemisphere"]
dataset = dataset.drop(columns=deleted_columns)
dataset.head()


# Dataset sudah menghapus beberapa kolom yang tidak dibutuhkan, dan siap untuk dilanjutkan ke proses berikutnya

# ### Memisahkan Data *Blood Pressure*

# Jika diperhatikan dalam dataset, fitur *Blood Pressure* Masih dalam bentuk Object yang tentunya belum dapat digunakan dalam predksi machine learning, proses berikutnya adalah memisahkan kolom *Blood Pressure*.  
# Nilai dalam *Blood Pressure* sendiri ditulis dalam format *Systolic/Diastolic*
# yang mana *Systolic* adalah tekanan darah pada saat jantung memompa darah atau saat berkontraksi, sedangkan *diastolic* adalah tekanan darah pada saat jantung relaksasi

# In[21]:


dataset[['BP_Systolic', 'BP_Diastolic']] = dataset['Blood Pressure'].str.split('/', expand=True)


# Selanjutnya, mari kita cek data kembali, akan ada penambahan kolom baru yaitu BP_Systolic dan BP_Diastolic

# In[22]:


dataset.info()


# Dengan sudah adanya dua kolom baru tersebut, maka kita perlu menghapus kolom *Blood Pressure* sebelumnya karena tidak kita gunakan lagi

# In[23]:


dataset = dataset.drop(columns="Blood Pressure")
dataset.head()


# Jika diperhatikan, dua kolom terbaru BP_Systolic dan BP_Diatolic masih memiliki tipe data object, tipe data ini harus dikonversikan ke int64 agar bisa diproses dalam algoritma prediksi

# In[24]:


dataset['BP_Systolic'] = dataset['BP_Systolic'].astype('int64')
dataset['BP_Diastolic'] = dataset['BP_Diastolic'].astype('int64')


# ### Proses Label Encoder

# Label Encoder adalah teknik pemrosesan data untuk data kategorikal, Tujuannya adalah untuk mengubah nilai-nilai dalam satu atau lebih pada kolom kategorikal menjadi numerik.

# Sebelum memulai, mari identifikasi kembali kolom dari dataset yang masih memiliki tipe data object

# In[25]:


dataset.info()


# Terdapat 2 Kolom yang memiliki tipe data object yang akan di *label encoder* sehingga menjadi bentuk numerik, proses tersebut akan dilakukan menggunakan kode dibawah ini

# In[26]:


encoder = LabelEncoder()
fitur_kategorikal = ['Sex', 'Diet']
kolom_kategorikal = dataset[fitur_kategorikal]
encoded_kategorikal = kolom_kategorikal.apply(encoder.fit_transform)
dataset[fitur_kategorikal] = encoded_kategorikal


# In[27]:


dataset


# In[28]:


dataset.info()


# Dataset siap diproses ke Langkah Selanjutnya, namun, saatnya mengecek korelasi antar data sehingga kita mengetahui faktor apa saja dalam dataset yang paling berpengaruh pada kondisi seseorang terkena serangan jantung

# In[29]:


corr = dataset.corr()

#Correlation Heatmap

plt.figure(figsize=(20, 20))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".3f", linewidths=0.5)
plt.title("Correlation Matrix Seluruh Fitur")
plt.show()


# Diketahui bahwa fitur yang berkorelasi tinggi dengan target variabel serangat jantung adalah ***Cholesterol***, ***Diabetes***, ***Exercise Hour Per Week***

# ### *Train Test Split* ###

# Proses ini membagi data menjadi data latih dan data uji. Data latih akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji hasil performa prediksi model.

# Langkah pertama dimulai dengan membagi Dataset menjadi fitur X (Fitur Independen) dan fitur Y (Fitur Y atau fitur target).
# Lalu proses dilanjutkan dengan membagi data menjadi data latih dan data uji

# In[30]:


X = dataset.drop(["Heart Attack Risk"], axis=1)
y = dataset['Heart Attack Risk']
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size = 0.20, random_state=123)


# Berikutnya adalah melihat jumlah Data Latih dan Data Uji

# In[31]:


print(f'Total of sample in whole dataset: {len(X)}')
print(f'Total of sample in train dataset: {len(X_train)}')
print(f'Total of sample in test dataset: {len(X_test)}')


# Terdapat 7010 baris data yang akan digunakan di data latih, dan 1753 data digunakan dalam data uji

# ### Proses Standardisasi

# Standardisasi adalah teknik transformasi yang paling umum digunakan dalam tahap persiapan pemodelan.  
# Algoritma machine learning memiliki performa lebih baik dan konvergen lebih cepat ketika dimodelkan pada data dengan skala relatif sama atau mendekati distribusi normal. Proses scaling dan standarisasi membantu untuk membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma.
# Untuk mengatasi kebocoran data, Standardisasi akan dilakukan di Data latih terlebih dahulu

# StandardScaler melakukan proses standarisasi fitur dengan mengurangkan mean (nilai rata-rata) kemudian membaginya dengan standar deviasi untuk menggeser distribusi.  StandardScaler menghasilkan distribusi dengan standar deviasi sama dengan 1 dan mean sama dengan 0.  
# Sebelum melakukan standardisasi, gunakan describe(), untuk melihat kolom data yang perlu dilakukan standardisasi

# In[32]:


dataset.describe().T


# Kolom *Age*, *Cholesterol*, *Heart Rate*, *Exercise Hours Per Week*, *Stress Level*, *Sedentary Hours Per Day*, *BMI*, *Income*, *Triglycerides*, *Physical Activity Days Per Week*, *Sleep Hours Per Day*, *BP_Systolic*, *BP_Diastolic* memiliki standar deviasi yang cukup tinggi, kolom tersebut akan di standardisasi menggunakan StandardScaler()

# In[33]:


kolom_standard = ['Age', 'Cholesterol', 'Heart Rate', 'Exercise Hours Per Week', 'Stress Level', 
                  'Sedentary Hours Per Day', 'BMI', 'Income', 'Triglycerides', 'Physical Activity Days Per Week', 
                  'Sleep Hours Per Day', 'BP_Systolic', 'BP_Diastolic']
scaler = StandardScaler()
scaler.fit(X_train[kolom_standard])
X_train[kolom_standard] = scaler.transform(X_train.loc[:,kolom_standard])
X_train[kolom_standard].head()


# In[34]:


X_train.describe().T


# Kolom Numerikal Dalam Data Latih sudah normal dan siap diproses menggunakan algoritma prediksi

# ## Klasifikasi Menggunakan *Random Forest Classifier*

# Algoritma *Random Forest* adalah salah satu algoritma pohon keputusan yang dapat digunakan untuk menyelesaikan masalah klasifikasi, algoritma ini cukup digunakan karena sederhana namun stabil.  
# Sebagai salah satu model *Ensemble Learning* (Model yang bekerja bersama-sama), model ini memiliki beberapa kelebihan diantaranya :  
# 1. Memiliki Kinerja yang baik dalam berbagai jenis masalah klasifikasi
# 2. Memiliki kemampuan bawaan untuk mengurangi overfitting
# 3. Mampu menangani dataset yang besar dan fitur yang banyak

# Beberapa kelebihan diatas membuat algoritma ini dapat digunakan sebagai salah satu model untuk memprediksi berdasarkan dataset *Heart Attack* yang kita gunakan, mengingat dimensi dataset kita yang juga cukup besar
# ada banyak sekali parameter yang kita masukkan dalam Random Forest Classfier, namun dalam proyek ini, kita hanya menggunakan 4 parameter dibawah ini :  
# - **n_estimator** : jumlah trees (pohon) di forest. (Nilai Default = 100)
# - **max_depth** : kedalaman atau panjang pohon. Ia merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan.
# - **random_state** : digunakan untuk mengontrol random number generator yang digunakan. 
# - **n_jobs**: jumlah job (pekerjaan) yang digunakan secara paralel. Ia merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel. n_jobs=-1 artinya semua proses berjalan secara paralel

# Berikut merupakan implementasi latih data menggunakan *Random Forest Classifier*
# Pertama kita akan instansiasi kelas RandomForestClassifier dengan mencoba hyperparameter dibawah ini
# - **n_estimators** = 50
# - **max_depth** = 12
# - **random_state** = 42
# - **n_jobs** = -1

# In[35]:


Random_Forest = RandomForestClassifier(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)


# Setelah itu, latih Model yang sudah di instansiasi dengan data latih

# In[36]:


Random_Forest.fit(X_train,y_train)


# Selanjutnya lakukan prediksi model terhadap data uji, namun sebelumnya, kita akan terapkan standard scaler juga ke Data Uji

# In[37]:


X_test[kolom_standard] = scaler.transform(X_test[kolom_standard])


# Sebelumnya, mari lihat performa model dalam memprediksi data latih terlebih dahulu

# In[38]:


y_train_prediksi = Random_Forest.predict(X_train)
RF_Acc_Train = accuracy_score(y_train,y_train_prediksi)
print(f"Akurasi Model terhadap data latih : {round(RF_Acc_Train * 100,2)}%")


# Selanjutnya, prediksi dan evaluasi performa model menggunakan data uji

# In[39]:


y_test_prediksi = Random_Forest.predict(X_test)
RF_Acc_Test = accuracy_score(y_test,y_test_prediksi)
print(f"Akurasi Model terhadap data latih : {round(RF_Acc_Test * 100,2)}%")


# Akurasi model terhadap data latih cukup baik karena mendapat skor akurasi 82,3% namun, model buruk dalam data uji, langkah berikutnya adalah mencoba penyesuaian Hyperparameter, mari mencoba dengan Hyperparameter dibawah ini
# - n_estimators = 50
# - max_depth = 18
# - random_state = 42
# - n_jobs = -1
# 
# kita akan mencoba menaikkan jumlah max_depth atau  kedalaman pohon, dan melakukan seluruh proses prediksi lagi

# In[40]:


Random_Forest2 = RandomForestClassifier(n_estimators=50, max_depth=18, random_state=42, n_jobs=-1)
Random_Forest2.fit(X_train,y_train)

y_train_prediksi2 = Random_Forest2.predict(X_train)

RF_Acc_Train2 = accuracy_score(y_train,y_train_prediksi2)
print(f"Akurasi Model terhadap data latih : {round(RF_Acc_Train2 * 100,2)}%")

y_test_prediksi2 = Random_Forest2.predict(X_test)
RF_Acc_Test2 = accuracy_score(y_test,y_test_prediksi2)
print(f"Akurasi Model terhadap data uji : {round(RF_Acc_Test2 * 100,2)}%")


# Dengan menaikkan jumlah parameter max_depth, akurasi model terhadap data latih meningkat menjadi 99 persen, namun untuk data uji, turun diangka 64 persen, kita akan mencoba langkah terakhir dengan menaikkan n_estimators menggunakan nilai default 100

# In[41]:


Random_Forest3 = RandomForestClassifier(n_estimators=100, max_depth=18, random_state=42, n_jobs=-1)
Random_Forest3.fit(X_train,y_train)

y_train_prediksi3 = Random_Forest3.predict(X_train)

RF_Acc_Train3 = accuracy_score(y_train,y_train_prediksi3)
print(f"Akurasi Model terhadap data latih : {round(RF_Acc_Train3 * 100,2)}%")

y_test_prediksi3 = Random_Forest3.predict(X_test)
RF_Acc_Test3 = accuracy_score(y_test,y_test_prediksi3)
print(f"Akurasi Model terhadap data uji : {round(RF_Acc_Test3 * 100,2)}%")


# Akurasi masih kurang baik di data uji. perlu dilakukan pengujian berulang kali hingga menemukan hyperparameter yang tepat dalam pengujian menggunakan *Random Forest Classifier*. mungkin menambah beberapa hyperparameter lain yang tersedia dalam dokumentasi resmi random forest classifier

# ### Analisa Menggunakan *AdaBoost Classifier*

# *Ada Boost* merupakan salah satu dari algoritma *Boosting*, yang mana algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi dengan menggabungkan beberapa model sederhana dan dianggap lemah sehingga membentuk model yang kuat.
# 
# *Ada Boost Classifier* adalah alat yang memperhatikan contoh yang sulit dikenali oleh klasifier sebelumnya. Itu membuat klasifier baru untuk mencoba memperbaiki kesalahan dan lebih fokus pada contoh yang sulit tersebut.
# 
# terdapat beberapa *hyperparameter* yang dapat digunakan dalam *Classifier* ini, namun dalam cakupan proyek terkait, kita hanya menggunakan :
# - learning_rate : Menentukan seberapa cepat model belajar dari kesalahan pada setiap iterasi. Jika nilai learning rate kecil, model akan belajar perlahan, sedangkan nilai yang lebih besar akan membuat model belajar lebih cepat.
# - n_estimators : Menentukan seberapa cepat model belajar dari kesalahan pada setiap iterasi. Jika nilai learning rate kecil, model akan belajar perlahan, sedangkan nilai yang lebih besar akan membuat model belajar lebih cepat.

# Berikut merupakan implementasi menggunakan *Ada Boost Classifier*, kali ini, kita akan menggunakan learning_rate = 0.1 dan random_state = 42 dan n_estimators = 20, dengan melatih model menggunakan data latih

# In[42]:


learning_rate = 0.1
Ada_clf1 = AdaBoostClassifier(learning_rate=learning_rate,n_estimators=50, random_state=42)
Ada_clf1.fit(X_train, y_train)


# Berikut merupakan hasil pengujian model dan akurasi model terhadap data latih dan data uji

# In[43]:


ada_pred_train = Ada_clf1.predict(X_train)
Ada_acc_train = accuracy_score(y_train,ada_pred_train)
print(f"Akurasi Model terhadap data latih : {round(Ada_acc_train * 100,2)}%")

ada_pred_test = Ada_clf1.predict(X_test)
Ada_acc_test = accuracy_score(y_test,ada_pred_test)
print(f"Akurasi Model terhadap data latih : {round(Ada_acc_test * 100,2)}%")


# Diketahui bahwa hasil menggunakan Ada boost classifier juga memiliki tingkat akurasi di angka 65%

# ### Kesimpulan

# berikut merupakan hasil performa pengujian model prediksi, yang mana pengujian dilakukan menggunakan *Random Forest Classifier* dengan 3 kali pengujian dan *Hyperparameter Tuning*, dan dengan 1x pengujian menggunakan *Ada Boost Classifier*

# In[44]:


models = pd.DataFrame({
    'Model':
    ['Random_Forest 1', 'Random_Forest 2', 'Random_Forest 3', 'Ada Boost Classifier'],
    'Accuracy Test' :
    [RF_Acc_Test, RF_Acc_Test2, RF_Acc_Test3, Ada_acc_test],
    'Accuracy Train' :
    [RF_Acc_Train, RF_Acc_Train2, RF_Acc_Train3, Ada_acc_train]
})
models


# Hasil Penelitian diatas mendapatkan kesimpulan :
# 1. Meskipun *Random Forest* diketahui dapat mengurangi *overfitting*, dalam 3 kali pengujian dengan mengubah beberapa *Hyperparameter*, model memrediksi sangat baik dalam data latih, namun tidak dengan data uji, dengan rata-rata hasil prediksi sebesar 64%
# 2. Pengujian menggunakan *Ada Boost Classifier* membuktikan tidak ada *overfitting* dalam data, namun, prediksi hasil data uji masih cukup rendah yaitu diangka 65%
# 
# berdasarkan pengujian menggunakan 2 algoritma diatas, dapat disimpulkan bahwa algoritma belum bisa bekerja lebih baik dengan data yang anda, walaupun data sudah dianalisis dengan memastikan tidak ada *missing values*, *duplicate*, ataupun *outlier*, dan data juga sudah di *normalisasi*.  

# Metode lain mungkin dapat dilakukan, seperti penerapan menggunakan *Artificial Neural Network* atau metode lainnya yang mungkin dapat menangani dataset lebih baik.
# Agar mencapai akurasi yang lebih baik daripada sebelumnya, mengingat masalah kesehatan tentunya  membutuhkan tingkat akurasi yang lebih baik dari yang sudah dihasilkan algorima ini

# In[ ]:




