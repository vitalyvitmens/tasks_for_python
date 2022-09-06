def to_rna(dna: str):
    """
    функция to_rna принимает на вход строку (цепь ДНК) и возвращает строку (цепь РНК),
    совершает транскрипцию РНК.
        ДНК и РНК это последовательности нуклеотидов.
        Четыре нуклеотида в ДНК это аденин (A), цитозин (C), гуанин (G) и тимин (T).
        Четыре нуклеотида в РНК это аденин (A), цитозин (C), гуанин (G) и урацил (U).
        Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого нуклеотида:
            G -> C
            C -> G
            T -> A
            A -> U
    """
    dna_new = []
    for i in dna:
        if i == 'G':
            i = 'C'
        elif i == 'C':
            i = 'G'
        elif i == 'T':
            i = 'A'
        elif i == 'A':
            i = 'U'
        dna_new.append(i)
    print(dna)
    return print(*dna_new, sep='')


to_rna('ACGTGGTCTTAA')