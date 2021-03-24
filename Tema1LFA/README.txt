Algoritmul deschide fisierele de input si output. Citeste din input string1 si
string2. Se creeaza 2 liste: una cu literele de la A-Z si una cu toate
substring-urile lui string1, inclusiv e (elementul vid). Se initializeaza
matricea delta in functie de numarul de elementele din listele anterior create,
si toate valorile din aceasta devin 0.
Se iau in 2 for-uri fiecare element din cele 2 liste (fiecare substring si
litera), si se apeleaza functia delta_function care umple matricea cu starile
in care se ajunge la fiecare pas. Aceasta functie concateneaza substring-ul cu
litera respectiva in variabila word si se ia un for de la 0 pana la 
min(len(word), len(string1)), si de fiecare data se compara sufixul word-ului 
(ultimele i litere) si prefixul lui string1 (primele i litere), iar atunci cand
acestea coincid, este returnata valoarea i+1 care reprezinta starea in care se
ajunge cand sunt citite substring-ul si litera respectiva, si aceasta ajunge in
matricea delta. La final, este parcursa matricea delta cu fiecare litera din
string2, iar atunci cand se ajunge in starea finala, este returnat indicele
unde de a fost gasit string1 in string2.