import matplotlib.pyplot as plt

file = open("hans_im_glueck.txt")
inhalt = file.read()

inhalt_reduziert = inhalt.replace('.', '').replace(',', '')
inhalt_alles_klein = inhalt_reduziert.lower()
inhalt_zerhackt = inhalt_alles_klein.split()

wortzaehler = {len(wort): 0 for wort in inhalt_zerhackt}

for wort in inhalt_zerhackt:
    wortlaenge = len(wort)
    wortzaehler[wortlaenge] += 1

sortiert = sorted(wortzaehler)
for key in sortiert:
    zaehler = wortzaehler[key]
    print("Es gibt", zaehler, "Worte mit", key, "Zeichen.")

plt.bar(wortzaehler.keys(), wortzaehler.values())
plt.show()
