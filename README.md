# **WIP**

Se provate a installare 99% non funzionerà, ci sto lavorando.

## **Installazione**
- Assicurarsi di aver installato:
    - python
    - pytube
    - moviepy
- Copiare la Repo github
    - consiglio di copiarla a livello di C:\\Users\\Nome_User per chi\
    non ha familiarità con il terminale e il filesystem
- Creare una copia di private_var_template.py
    - Rinominarlo private_var.py
    - Modificarlo:
        - outputFolder-> inserire nella stringa il percorso (assoluto)\
        in cui verranno salvati i file, assicurandosi che abbia uno dei\
        seguenti formati:
            - r'C:\\Users\\Nome_User\\'
            - 'C:\\\Users\\\\Nome_User\\\\'
            - 'C:/Users/Nome_User/'


## **Utilizzo**
SYTDL deve essere utilizzato da terminale:
- aprite cmd
- utilizzate il comando:\
\
py SYTDL2 [link] [argomento]\

- se cambiate il nome della cartella di installazione sostituite SYTDL2
con il nuovo nome che gli avete dato
- se utilizzate link di playlist o radio assicuratevi che il link termini con \
v=[id del video]
    - ad esempio il link:\
https://www.youtube.com/watch?v=kagdsGKHZvU&list=RD8rTbVtrm4G0&index=7
deve diventare:
https://www.youtube.com/watch?v=kagdsGKHZvU
    - **Attenzione**: le **&** non fanno parte dell'id video


### **Argomenti**
qualsiasi argomento non listato sotto-printa info sul video 

i-printa il nome

d-download con qualità massima ma richiede tempo

ad-dowload solo stream audio (formato .mp4)

pd-progressive download
