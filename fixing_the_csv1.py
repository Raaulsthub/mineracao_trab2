import codecs
import csv


# script used to change ";" to "," in a new csv file
file = codecs.open('./data/saudeRS_2022.csv', encoding='utf-8')
contents = file.read()
new_file = open('./data/saudeRS_2022_commas.csv', 'r+')
new_file.truncate(0)
new_contets = contents.replace(';', ',')

new_file.write(new_contets)
new_file.close()
file.close()

# excluding extra nonsense fields in rows
with open('./data/saudeRS_2022_commas.csv') as source:
    reader = csv.reader(source)
    with open('./data/final.csv', 'w') as result:
        writer = csv.writer(result)
        for r in reader:
            writer.writerow((r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],
            r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16],
            r[17], r[18], r[19], r[20], r[21], r[22], r[23], r[24], r[25],
            r[26], r[27], r[28], r[29]))