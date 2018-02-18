import  sqlite3

vt=sqlite3.connect("d:/py3/bioinformatics/mkt/greengenes/db/greengenes.db")
im=vt.cursor()

def taxGetir(kelime):
    return {
        'k__':'kingdom',
        's__':'species',
        'g__':'genus',
        'f__':'family',
        'o__':'orderr',
        'c__':'class',
        'p__':'phylum',
    }.get(kelime)

def parsEtSqlYaz(fileName):
    sqlTam=""
    file = open(fileName, "r")
    satirNo = 0
    insertKeys = "(fragment,"
    valueKeys = "("
    for line in file:
        satirNo += 1
        if line.startswith('>'):
            tanimSatir = line.split()
            insertKeys = "("
            valueKeys = "("
            for kelime in tanimSatir:
                if kelime.find("__") > 0 and kelime.find(";") > 0 and len(kelime[3:-1])>0:
                    insertKeys += taxGetir(kelime[:3]) + ","
                    valueKeys += "'" + kelime[3:-1] + "'" + ","
        else:
            insertKeys = insertKeys + "fragment,satir_no,frag_len,acc_number,otu)"
            valueKeys = valueKeys + "'" + line[:-1] + "'," + str(satirNo) + "," + str(len(line[:-1])) + ",'" + tanimSatir[1] + "','" + tanimSatir[-1] + "')"
            sql = "insert into fragment_bilgi" + insertKeys + "values" + valueKeys
           # sqlTam+=sql+";"
            #print(str(satirNo)+" "+sql)
            im.execute(sql)
            #vt.commit()
            if (satirNo%1000)==0:
                print(satirNo)
    return sqlTam


fileNameTest="C:\\Users\\Hakan\\Downloads\\test.fasta"
fileNameOriginal="C:\\Users\\Hakan\\Downloads\\current_GREENGENES_gg16S_unaligned.fasta"
sqlDis=parsEtSqlYaz(fileNameOriginal)
#print(sqlDis)
vt.commit()

