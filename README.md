# Proyek Analisis Data Penggunaan Sepeda

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis penggunaan sepeda berdasarkan data yang dikumpulkan dari sistem berbagi sepeda. Analisis mencakup faktor-faktor seperti musim, waktu, dan hari kerja versus hari libur.

## Struktur Folder

- **dashboard/**: Berisi berkas Python untuk dashboard Streamlit.
- **data/**: Berisi dataset yang digunakan dalam analisis dan dataset bersih.
- **notebook.ipynb**: Berkas Jupyter Notebook yang berisi analisis dan visualisasi.
- **requirements.txt**: Library yang diperlukan untuk menjalankan proyek.
- **url.txt**: Tautan untuk mengakses dashboard.

## Cara Menjalankan Dashboard (Setup Environment - Shell/Terminal)

1. Tentukan/sesuaikan Directory tempat Anda akan menyimpan dan menjalankan Proyek. Misal:

_C:\Users\Vivobook 15\Desktop_

2. Akses Directory tersebut ke Terminal. Kemudian buat folder proyek Anda dengan perintah berikut:

_mkdir proyek_analisis_data_

3. Setelah folder berhasil terbuat, masuk ke dalam folder tersebut dengan perintah berikut:

_cd proyek_analisis_data_

4. Clone Repositori:

_git clone https://github.com/nspweb/Analisis-Data-Bike-Sharing.git_

5. Setelah Repositori berhasil ter-Clone, masuk ke dalam folder lanjutan dari Repositori tersebut dengan perintah berikut:

_cd Analisis-Data-Bike-Sharing_

6. Siapkan Lingkungan Kerja:

Proyek ini memerlukan lingkungan virtual, buat lingkungan virtual dengan perintah berikut:

_python -m venv env_

Kemudian aktifkan lingkungan virtual tersebut dengan perintah berikut:

Untuk PowerShell

_.\env\Scripts\activate_

atau

Untuk Command Prompt

_env\Scripts\activate.bat_

7. Install Dependensi:

_pip install streamlit_

Kemudian lanjut install semua library yang diperlukan dengan menggunakan file requirements.txt:

_pip install -r requirements.txt_

8. Jalankan Dashboard:

Jalankan aplikasi Streamlit dengan perintah berikut:

_streamlit run dashboard/dashboard.py_

9. Akses Dashboard
   Buka browser dan akses alamat yang ditampilkan di terminal (biasanya http://localhost:8501).

## Insight

1. Pengaruh Musim: Musim Gugur memiliki jumlah pengguna sepeda tertinggi, sementara Musim Semi mencatat penggunaan terendah, menunjukkan pentingnya faktor cuaca dan kenyamanan.
2. Dampak Kondisi Cuaca: Cuaca cerah meningkatkan penggunaan sepeda hingga 4.876 pengguna, sedangkan cuaca buruk menurunkan angka tersebut drastis menjadi 1.803 pengguna.
3. Pola Penggunaan Berdasarkan Waktu: Puncak penggunaan sepeda pada hari kerja terjadi pada pukul 17:00, sementara pada hari libur puncaknya lebih awal di pukul 13:00.

## Lisensi

Proyek ini dilisensikan di bawah MIT License.