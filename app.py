from flask import Flask, render_template, request, url_for, redirect, jsonify
from Levenshtein import distance
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
data = pd.read_csv('data/pertanyaan.csv')

def rubah_list_int_str(ini):
  versi_string_saya_sakit = [str(sindrom_kecil) for sindrom_kecil in ini]
  return "".join(versi_string_saya_sakit)

def calculate1(jawab):

  data2 = data.values
  sindrom = data2[:,1:] 
  tinggi = sindrom.shape[0]

  rubah_list_int_str(jawab)
  
  a = [] 
  b = []
  for i in range(tinggi):
    a.append(i)
    b.append(distance(rubah_list_int_str(jawab), rubah_list_int_str(sindrom[i:i+1, :][0])))
  
  result = dict(zip(a,b))
  daftar_penyakit = list(data.Nama.values[:])

  temp = min(result.values())
  res = [key for key in result if result[key] == temp]

  return daftar_penyakit[res[0]]

def calculate2(kalimat):

  lol = pd.read_csv('data/gejala.csv', delimiter=',')
  X = lol.iloc[:,0].values
  y = lol.iloc[:,1].values
    
  tfidfvectorizer = TfidfVectorizer(max_features=100, use_idf=True)
  tfidfvectorizer.fit(X[:])
  X_train = tfidfvectorizer.transform(X[:])
  y_train = y[:]

  tfidfvectorizer.transform([kalimat]).todense()
  response = tfidfvectorizer.transform([kalimat]).todense()

  text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)  
  text_classifier.fit(X_train, y_train)
  predictions = text_classifier.predict(response)

  hasilnya = (np.array(predictions).tolist())[0]

  return hasilnya

def calculate3(jawab, kalimat): 
                                                         
  data_fungsi1 = pd.read_csv('data/pertanyaan.csv') 
  data2 = data_fungsi1.values 
  sindrom = data2[:,1:] 
  tinggi = sindrom.shape[0]

  rubah_list_int_str(jawab) 
  
  a = [] 
  b = [] 

  for i in range(tinggi): 
    a.append(i)  
    b.append(distance(rubah_list_int_str(jawab), rubah_list_int_str(sindrom[i:i+1, :][0])))
     
  result = dict(zip(a,b))
  daftar_penyakit = list(data_fungsi1.Nama.values[:])
  output = dict(zip(daftar_penyakit, b))

  # Fungsi 2
  data_fungsi2 = pd.read_csv('data/gejala.csv', delimiter=',')  
                                                           
  X = data_fungsi2.iloc[:,0].values    
                                      
  y = data_fungsi2.iloc[:,1].values   
                                       
  tfidfvectorizer = TfidfVectorizer(max_features=100, use_idf=True) 
  tfidfvectorizer.fit(X[:])                                         
  X_train = tfidfvectorizer.transform(X[:])                         
  y_train = y[:]                                                    
 
  tfidfvectorizer.transform([kalimat]).todense()  
  response = tfidfvectorizer.transform([kalimat]).todense()  
 
  text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)   
  text_classifier.fit(X_train, y_train)                                        
                                                                              
  predictions = text_classifier.predict(response)    
                                                     
  for data_fungsi2 in predictions: 
    data_fungsi2 

  result1 = output 
  result2 = data_fungsi2 
  
  #hasil1[hasil2] = hasil1[hasil2] - 1 

  temp = min(result1.values()) 
  hasil1 = [key for key in result1 if result1[key] == temp] 
  hasil2 = result2

  obat = { 
        'Depresi' : {
            'Fluoxetine' : {
                'Dosis' : ['Dewasa : 20 mg, 1 kali / hari','Anak usia ≥ 8 tahun : 10 mg, 1 kali / hari'],
                'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
                'Harga' : 'Rp. 360.000 (20 mg)'
            },
            # 'Escitalopram' : {
            #     'Dosis' : ['Dewasa : 10 mg, 1 kali / hari	','Lansia : 5 mg, 1 kali / hari	'],
            #     'Cara_Konsumsi' : 'Lansia : 5 mg, 1 kali / hari	',
            #     'Harga' : 'Rp. 1.161.000 (20 mg)'
            # },
            # 'Sertraline' : {
            #     'Dosis' : ['Dewasa : 50 mg, sekali sehari	'],
            #     'Cara_Konsumsi' : 'Pagi atau malam hari, sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 185.000'
            # },
            # 'Fluvoxamine' : {
            #     'Dosis' : ['Dewasa: 50–100mg per hari sebagai dosis awal'],
            #     'Cara_Konsumsi' : 'Pagi atau malam hari, sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 594.000'
            # },
            # 'Venlafaxine' : {
            #     'Dosis' : ['Dewasa: 37,5–75 mg sekali sehari'],
            #     'Cara_Konsumsi' : 'Setelah makan',
            #     'Harga' : 'Rp. 1.095.000 (75 mg)'
            # }
        },
        'Gangguan Kecemasan' : {
            'Chlordiazepoxide' : {
                'Dosis' : ['Dewasa : 30 mg / hari'],
                'Cara_Konsumsi' : 'Setelah makan',
                'Harga' : 'Rp. 110.000'
            },
            # 'Alprazolam' : {
            #     'Dosis' : ['Dewasa (18-64 tahun) : 0,25-0,5 mg sebanyak 3 kali sehari	','Lansia : 0,25 mg 2-3 kali per hari'],
            #     'Cara_Konsumsi' : 'Setelah makan',
            #     'Harga' : 'Rp. 140.000 / strip'
            # },
            # 'Clobazam' : {
            #     'Dosis' : ['Dewasa : 20-30 mg per hari', 'Lansia : 10-20 mg per hari'],
            #     'Cara_Konsumsi' : 'Bersamaan dengan makan',
            #     'Harga' : 'Rp. 120.000 / strip'
            # },
            # 'Diazepam' : {
            #     'Dosis' : ['Dewasa : 2-10 mg, dikonsumsi 2-4 kali	'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 250.000 (10 mg)'
            # },
            # 'Lorazepam' : {
            #     'Dosis' : ['Dewasa : 1–4 mg per hari dibagi menjadi beberapa dosis dikonsumsi selama 2–4 minggu','Lansia : Dosis akan ditentukan dokter sesuai dengan kondisi pasien'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 294.000 (50 gram)'
            # }
        },
        'Bipolar' : {
            'Carbamazepine' : {
                'Dosis' : ['Dewasa : Dosis awal 400 mg per hari yang dibagi dalam beberapa jadwal konsumsi, Dosis perawatan 400–600 mg perhari yang dibagi dalam beberapa jadwal konsumsi, Dosis maksimal 1.600 mg per hari'],
                'Cara_Konsumsi' : 'Setelah makan',
                'Harga' : 'Rp. 35.000 (200 mg)'
            },
            # 'Asam Valproat' : {
            #     'Dosis' : ['Dewasa: 600–1.800 mg per hari, yang dibagi menjadi 2 kali konsumsi'],
            #     'Cara_Konsumsi' : 'Bersamaan dengan makan',
            #     'Harga' : 'Rp. 45.000 (250 mg)'
            # },
            # 'Aripiprazole' : {
            #     'Dosis' : ['Dewasa: Sebagai terapi tunggal, dosis awal 15 mg, 1 kali sehari', 'Anak usia > 10 tahun : dosis awal 2 mg per hari, selama 2 hari pertama'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 125.000 (5 mg)'
            # },
            # 'Olanzapine' : {
            #     'Dosis' : ['Dosis awal 10–15 mg per hari sebagai terapi tunggal atau 10 mg per hari'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 100.000 (10 mg)'
            # }
        },
        'Skizofrenia' : {
            'Sulpiride' : {
                'Dosis' : ['Dewasa: 200–400 mg 2 kali sehari', 'Anak-anak ≥14 tahun : sama seperti dosis dewasa', 'Lansia: lebih rendah dari dosis dewasa'],
                'Cara_Konsumsi' : 'Dengan atau tanpa makan',
                'Harga' : 'Rp. 100.000 (50 mg)'
            },
            # 'Haloperidol' : {
            #     'Dosis' : ['Dewasa: 0,5–5 mg, 2–3 kali sehari', 'Anak usia 3–12 tahun: dosis awal 0,5 mg per hari', 'Anak usia 13–17 tahun: dosis awal 0,5 mg per hari', 'Lansia: 0,5–2 mg, 2–3 kali sehari'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 70.000 (2 mg)'
            # },
            # 'Aripiprazole' : {
            #     'Dosis' : ['Dewasa: Dosis awal 10–15 mg, 1 kali sehari', 'Remaja usia ≥ 13 tahun: Dosis awal 2 mg untuk 2 hari pertama'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 125.000 (5 mg)'
            # },
            # 'Clozapine' : {
            #     'Dosis' : ['Dewasa: Dosis awal 12,5 mg, 1–2 kali sehari', 'Lansia: Dosis awal adalah 12,5–25 mg per hari'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 50.000 (25 mg)'
            # },
            # 'Risperidone' : {
            #     'Dosis' : ['Dewasa: Dosis awal 2 mg per hari'],
            #     'Cara_Konsumsi' : 'Sebelum atau sesudah makan',
            #     'Harga' : 'Rp. 180.000 (2 mg)'
            # }
        },
        'Sehat' : {
            'Sehat' : {
                'Dosis' : [],
                'Cara_Konsumsi' : '',
            }
        }
    }

  ot = { 
      'Nama_Penyakit_1' : hasil1[0],
      'Obat_1' : obat[hasil1[0]],
      'Nama_Penyakit_2' : hasil2,
      'Obat_2' : obat[hasil2]
  }
  
  return ot

@app.route("/", methods=["GET"])
def home():
  return render_template('index.html')

@app.route("/fungsi1", methods=["GET", "POST"])
def fungsi1():
    daftar_penyakit = list(data.columns.values[1:])
    panjang_data = len(daftar_penyakit)
    if request.method == 'POST':
        inp = dict(request.form)
        key = list(inp.values())
        jawab = list(map(int, key))
        hasil = calculate1(jawab)
        alert = True
        return render_template('fungsi1.html', data = daftar_penyakit, panjang = panjang_data, hasil = hasil, alert = alert)
    else:
        hasil = ""
        alert = False
        return render_template('fungsi1.html', data = daftar_penyakit, panjang = panjang_data, hasil = hasil, alert =  alert)

@app.route("/fungsi2", methods=["GET", "POST"])
def fungsi2():
    if request.method == 'POST':
      inp = request.form['kalimat']
      hasil = calculate2(inp)
      alert = True
      return render_template('fungsi2.html', hasil = hasil, alert = alert)
    else:
      return render_template('fungsi2.html', hasil = "", alert = False)

@app.route("/fungsi3", methods=["GET", "POST"])
def fungsi3():
  daftar_penyakit = list(data.columns.values[1:])
  panjang_data = len(daftar_penyakit)
  if request.method == 'POST':
    inp = dict(request.form)
    a = []
    b = []
    for i in inp:
      if i != 'kalimat':
        a.append(i)
        b.append(inp[i])

    jawab = dict(zip(a,b))
    kalimat = request.form['kalimat']
    key = list(jawab.values())
    jawab = list(map(int, key))
    hitung = calculate3(jawab, kalimat)
    hasil1 = hitung['Nama_Penyakit_1']
    obat1 = hitung['Obat_1']
    hasil2 = hitung['Nama_Penyakit_2']
    obat2 = hitung['Obat_2']
    alert = True
    return render_template('fungsi3.html', data = daftar_penyakit, panjang = panjang_data, hasil1 = hasil1, hasil2 = hasil2, alert = alert, obat1 = obat1, obat2 = obat2)
  else:
    alert = False
    return render_template('fungsi3.html', data = daftar_penyakit, panjang = panjang_data, hasil1 = "", hasil2 = "", alert =  alert, obat1 = {}, obat2 = {})


if __name__ == "__main__":
    app.run(debug=True)