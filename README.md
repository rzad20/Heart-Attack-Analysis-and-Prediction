# Analisa Kinerja Algoritma *K-Nearest Neighbor*, *Logistic Regression*, dan *Random Forest* Dalam Memprediksi Pasien Berisiko Serangan Jantung  
Proyek ini dibuat sebagai bahan tugas pengerjaan proyek dalam kursus Machine Learning Terapan Dicoding
## Domain Proyek
### Latar Belakang
Kematian mendadak tanpa diketahui diagnosa penyakit sebelumnya kerap terjadi di kalangan masyarakat. Salah satu penyebab kematian mendadak adalah
Serangan Jantung. Serangan jantung disebut juga sebagai *infark miokart* adalah gangguan jantung serius ketika otot jantung tidak mendapat aliran darah. Kondisi ini akan mengganggu
Fungsi Jantung dalam mengalirkan darah ke seluruh tubuh. Penyebab utama kondisi ini adalah penyakit jantung koroner, yang terjadi ketika pembuluh darah koroner yang memasok darah
ke dalam jantung tersumbat. Penyumbatan ini terjadi ketika timbunan kolestrol yang membentuk plak di dinding pembuluh darah [1].

Serangan jantung ini dapat terjadi dimana saja dan kapan saja dan dapat berakibat fatal hingga menyebabkan kematian, Sehingga hal ini perlu diwaspadai sejak dini. Namun, situasi
yang terjadi di masyarakat saat ini, kebanyakan tidak memahami secara *detail* mengenai gejala dan hal-hal yang menyebabkan serangan jantung, sehingga masyarakat tidak mengetahui jika
mengalami serangan ini dan tidak mendapatkan penanganan yang cepat, akan berakibat fatal kepada kematian. [2] Secara teori, gejala serangan jantung yaitu rasa tidak nyaman atau nyeri didada , sesak nafas, pusing, mual, muntah, dan keringat dingin.  

Selain mengenali gejala serangan jantung, masyarakat juga perlu mengetahui faktor penyebab serangan jantung. Sehingga dengan mengetahui faktor penyebab, masyarakat dapat meminimalkan   faktor resiko terjadinya serangan jantung. Faktor penyebab yaitu semakin bertambahnya usia semakin beresiko untuk mengalami serangan jantung, dan faktor lain seperti Tingkat Kolestrol,
tekanan darah, denyut jantung, diabetes, merokok, obesitas, riwayat keluarga dan lain sebagainya [3]. Jika faktor penyebab dapat diminimalkan, maka akan mengurangi risiko kematian akibat serangan jantung di kalangan masyarakat.

Dalam mengatasi hal ini, tentunya pihak medis atau pihak dalam industri kesehatan memiliki peranan dalam mengedukasi masyarakat untuk rutin mengecek kondisi mereka dan rutin
dalam menjaga diri mereka agar tidak mengalami serangan jantung. Namun, dengan jumlah masyarakat yang cukup banyak sering kali menyulitkan pihak medis untuk memberikan perhatian dan
edukasi pada setiap individu. Oleh karena itu, dibutuhkan algoritma prediksi serangan jantung, yang diharapkan dapat memberikan dukungan tambahan bagi pihak medis dalam
mengidentifikasi potensi risiko serangan jantung pada setiap individu secara lebih efisien.

Dalam tahap awal proyek ini, fokus penelitian adalah mencari algoritma klasifikasi yang tepat dalam menentukan risiko individu berisiko terkena serangan jantung atau tidak, algoritma
ini nantinya akan mengintegrasikan berbagai data klinis dan faktor risiko yang relevan untuk memprediksi risiko serangan jantung pada individu. Diharapkan dengan algoritma ini akan
menjadi alat yang berguna bagi pihak medis dalam meningkatkan deteksi dini dalam pencegahan serangan jantung, serta meningkatkan kesadaran masyarakat tentang pentingnya menjaga
kesehatan jantung.

## Business Understanding

Proyek ini diharapkan dapat memberi dampak signifikan baik bagi dunia bisnis dan dunia kesehatan. Dalam sudut pandang bisnis, diharapkan proyek ini dapat memberikan
solusi teknologi yang inovatif bagi lembaga kesehatan. Dalam sudut pandang dunia kesehatan, proyek ini dapat memiliki potensi untuk meningkatkan deteksi dini serangan jantung,
dapat membantu pihak medis dalam menentukan risiko penyakit jantung lebih cepat, sehingga dapat berpotensi mengurangi angka kematian, meningkatkan kualitas hidup pasien dan
memungkinkan intervensi medis yang lebih tepat waktu terhadap pasien berisiko terkena serangan jantung.

### Problem Statement
1. Bagaimana mengembangkan algoritma prediksi yang efektif untuk klasifikasi risiko serangan jantung pada pasien berdasarkan data klinis mereka?
2. Bagaimana implementasi algoritma prediksi dalam meningkatkan deteksi dini serangan jantung berdasarkan teknologi yang akan dibangun?

### Goals
1. Mengembangkan algoritma dengan tingkat akurasi prediksi yang cukup akurat untuk mengklasifikasi risiko serangan jantung pada pasien.
2. Membantu Dunia Kesehatan dan Medis meningkatkan efisiensi dalam mendeteksi risiko serangat jantung pada pasien.
3. Membantu bidang medis agar dapat mengintervensi dini kemungkinan serangan jantung untuk mengurangi tingkat kematian akibat serangan jantung

### Solution
1. Mengumpulkan data klinis pasien yang relevan dan memproses data tersebut agar bisa diolah oleh algortima prediksi.
2. Mengembangkan model prediksi menggunakan beberapa algoritma pilian seperti *K-Nearest Neighbor*, *Logistic Regression*, dan *Random Forest*
3. Melakukan analisa terhadap kinerja masing masing model dengan metrik evaluasi seperti *Accuracy*, *Precision*, *Recall*, dan *F1 Score* dan memilih model dengan metrik evaluasi terbaik

## Data Understanding
Dalam membangun model prediksi, proyek ini akan menggunakan data *Heart Attack Risk Prediction Dataset* yang dibuat oleh Sourav Banerjee.  
dataset ini didapatkan dari platform *Kaggle* dan dapat diakses di [link berikut ini](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset)
### Daftar Variabel dalam Dataset
1. **Patient ID** - Identifikasi unik untuk setiap pasien.
2. **Age** - Usia Pasien (Numerikal).
3. **Sex** - Kategori Jenis Kelamin Pasien (Kategorikal : Laki-Laki/Perempuan).
4. **Cholesterol** - Tingkat Kolesterol Pasien (Numerikal).
5. **Blood Pressure** - Tingkat tekanan darah pasien (Numerikal).
6. **Heart Rate** - Denyut jantung pasien.
7. **Diabetes** - Apakah pasien memiliki diabetes (Kategorikal : Ya/Tidak).
8. **Family History** - Riwayat Keluarga terkait masalah jantung (Kategorikal : 1 - Ya, 0 - Tidak)
9. **Smoking** - Status Perokok Pasien (Kategorikal : 1 - Ya, 0 - Tidak)
10. **Obesity** - Status Obesitas Pasien (Kategorikal : 1 - Obesitas, 0 - Tidak Obesitas)
11. **Alcohol Consumption** - Tingkat konsumsi alkohol oleh pasien (Kategorikal : None/Light/Moderate/Heavy)
12. **Exercise Hours Per Week** - Jumlah Jam Olahraga Per Minggu (Numerikal)
13. **Diet** - Kebiasaan diet pasien (Kategorikal : Healthy/Average/Unhealthy)
14. **Previous Heart Problems** - Riwayat penyakit jantung pasien sebelumnya (Kategorikal : 1 - Ya, 0 - Tidak)
15. **Medication Use** - Penggunaan obat oleh pasien (Kategorikal : 1 - Ya, 0 - Tidak)
16. **Stress Level** - Tingkat Level Stress Pasien (1-10)
17. **Sedentary Hours Per Day** - Jam aktivitas duduk per hari (Kategorikal)
18. **Income** - Tingkat pendapatan pasien (Numerikal)
19. **BMI** - Index massa tubuh pasien (Numerikal)
20. **Triglycerides** - Tingkat trgliserida Pasien
21. **Physical Activity Days Per Week** - Hari-hari aktivitas fisik per minggu.
22. **Sleep Hours Per Day** - Jam tidur per hari
23. **Country** - Negara Tempat Tinggal Pasien
24. **Continent** - Benua tempat Tinggal Pasien
25. **Hemisphere** - Belahan bumi tempat tinggal pasien
26. **Heart Attack Risk** - Variabel Target Prediksi risiko serangan jantung (Kategori 1 : Memiliki Risiko, 0 - Tidak)
## Referensi
[1] Alodokter. (2022). Pengertian Serangan Jantung. Diakses tanggal 15 Februari 2024, dari https://www.alodokter.com/serangan-jantung  
[2] Rahayu, S., Subekhi, A., Astuti, D., Widaningsih, I., Sartika, I., Nurhayani, N., ... & Rafidah, R. (2020). Upaya mewaspadai serangan jantung melalui pendidikan kesehatan. JMM (Jurnal Masyarakat Mandiri), 4(2), 163-171.  
[3] American Heart Association (AHA). (2019). *Warning signs of a heart attack*. Diakses Dari from https://www.heart.org/en/health-topics/heart-attack/warningsigns-of-a-heart-attack
