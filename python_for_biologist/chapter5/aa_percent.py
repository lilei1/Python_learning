def aa_percent(protein, aa):
    protein = protein.upper()
    aa = aa.upper()
    protein_len = len(protein)
    aa_nb = protein.count(aa)
    aa_percent = (aa_nb/protein_len) * 100
    return aa_percent

def aa_percent(protein, aaList=['A','I','L','M','F','W','Y','V']):
    protein = protein.upper()
    protein_len = len(protein)
    total_nb = 0
    for aa in aaList:
        aa = aa.upper()
        aa_nb = protein.count(aa)   
        total_nb = total_nb + aa_nb

    aa_percent = round (100 * total_nb / protein_len, 0)
    return aa_percent