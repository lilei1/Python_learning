import pytest

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
#
def test_aa_percent():
    assert aa_percent("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert aa_percent("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert aa_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert aa_percent("MSRSLLLRFLLFLLLLPPLP", "Y") == 0