# Responsi Workshop Python

perintah kali ini yaitu melakukan penampilan data `.csv` atau `.json`. dan kali ini saya akan menampilkan file data `.csv` yaitu file `diabetes.csv`. untuk menampilkan data saya menggunakan `pandas`, pada `pandas` menyediakan setidaknya tiga cara menampilkan (menyeleksi data), yaitu `.loc`, `.iloc`, dan `[]`.
* `.loc` digunakan untuk memilih baris dan kolomberdasarkan labelnya.
* `.iloc` digunakan untuk memilih baris dan kolom berdasarkan posisi yang ditunjukkan dengan angka integer.
* `[]` digunakan untuk memilih baris dan kolom berdasarkan nama kolom, mirip dengan `.loc` namun fitur ini yang paling sering digunakan karena umumnya kebutuhan kita adalah mengambil semua barisdan kolom tertentu.

program di bawah merupakan program yang akan menampilkan sebagian data atau hanya beberapa data yang ingin kita tampilkan saja yang akan ditampilkan. 

```python
import pandas as pd # import library 
df = pd.read_csv("diabetes.csv") #load data diabetes.csv

df.loc[0:5, ['Glucose', 'BloodPressure', 'Age', 'Outcome']]
df.iloc[0:5, [0, 1, 5]]
df[['Glucose', 'BloodPressure', 'Age', 'Outcome']][:5]
df[:5][['Glucose','BloodPressure', 'Age', 'Outcome']]
```

outputnya :
```python
Glucose	BloodPressure	Age	Outcome
0	148	72	50	1
1	85	66	31	0
2	183	64	32	1
3	89	66	21	0
4	137	40	33	1
```