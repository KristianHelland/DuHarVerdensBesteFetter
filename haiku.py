#her er brukerens mulighet til å sette in sin haiku
linjeEn = input("Linje 1 i din Haiku: ")
linjeTo = input("Linje 2 i din Haiku: ")
linjeTre = input("Linje 3 i din Haiku: ")

#Dette definerer el liste som er alle linjene kombinert
Haiku = [linjeEn, linjeTo, linjeTre]
#Dette er en tom liste som brukes for å måle lengden på linjene i haikuen
Haiku_len = []

#dette er definering av mellomrom for at det skal se bra ut
space = " "

#her er en loop som gjentas for hver linje i haikuen og den finner ut alle individuelle lengder
for line in Haiku:
    i = int(len(line))
    Haiku_len.append(i)

#denne definerer den lengste linjen i haikuen 
Haiku_Max = max(Haiku_len)

#printer den øverste borden rundt Haikuen
print("@" * (Haiku_Max + 4))

#funksjonen går en gang per linje i haikuen 
for line in Haiku:
    #så lenge en av linjene er kortere enn den lengste linjen
    while len(line) < Haiku_Max:
        #legger til et mellomrom frem til alle linjer er like lange
        line = space + line
    #printer alle linjene med border på sidene 
    print("@", line, "@")

#printer den nederste borden rundt Haikuen
print("@" * (Haiku_Max + 4))