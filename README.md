# Proyek Analisis Data Penggunaan Sepeda

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis penggunaan sepeda berdasarkan data yang dikumpulkan dari sistem berbagi sepeda. Analisis mencakup faktor-faktor seperti musim, waktu, dan hari kerja versus hari libur.

## Struktur Folder
- **dashboard/**: Berisi berkas data dan berkas Python untuk dashboard Streamlit.
- **data/**: Berisi dataset yang digunakan dalam analisis.
- **notebook.ipynb**: Berkas Jupyter Notebook yang berisi analisis dan visualisasi.
- **requirements.txt**: Library yang diperlukan untuk menjalankan proyek.
- **url.txt**: Tautan untuk mengakses dashboard.

## Cara Menjalankan Dashboard (Setup Environment - VS Code)
1. Clone Repositori

git clone https://github.com/nspweb/Analisis-Data-Bike-Sharing-Dataset.git

2. Di terminal, buat folder proyek Anda dengan perintah berikut:

cd proyek_analisis_data

3. Siapkan Lingkungan Kerja:

Jika proyek ini memerlukan lingkungan virtual, buat dan aktifkan lingkungan virtual dengan perintah berikut (pastikan kamu sudah menginstal venv):

python -m venv env
.\env\Scripts\activate  # Untuk PowerShell
# atau
.\env\Scripts\activate.bat  # Untuk Command Prompt

4. Install Dependensi
Install semua library yang diperlukan dengan menggunakan file requirements.txt:

pip install -r requirements.txt

5. Jalankan Dashboard
Jalankan aplikasi Streamlit dengan perintah berikut:

streamlit run dashboard/dashboard.py

6. Akses Dashboard
Buka browser dan akses alamat yang ditampilkan di terminal (biasanya http://localhost:8501).

## Insight
1. Pengaruh Musim: Musim Gugur memiliki jumlah pengguna sepeda tertinggi, sementara Musim Semi mencatat penggunaan terendah, menunjukkan pentingnya faktor cuaca dan kenyamanan.
2. Dampak Kondisi Cuaca: Cuaca cerah meningkatkan penggunaan sepeda hingga 4.876 pengguna, sedangkan cuaca buruk menurunkan angka tersebut drastis menjadi 1.803 pengguna.
3. Pola Penggunaan Berdasarkan Waktu: Puncak penggunaan sepeda pada hari kerja terjadi pada pukul 17:00, sementara pada hari libur puncaknya lebih awal di pukul 13:00.

## Lisensi
Proyek ini dilisensikan di bawah MIT License.