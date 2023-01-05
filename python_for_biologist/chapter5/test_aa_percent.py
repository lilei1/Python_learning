import pytest

def aa_percent(protein, aa):
    protein = protein.upper()
    aa = aa.upper()
    protein_len = len(protein)
    aa_nb = protein.count(aa)
    aa_percent = (aa_nb/protein_len) * 100
    return aa_percent

def test_aa_percent():
    assert aa_percent('MSRSLLLRFLLFLLLLPPLP', 'M') == 5
    assert aa_percent('MSRSLLLRFLLFLLLLPPLP', 'r') == 10
    assert aa_percent('MSRSLLLRFLLfLLLLPPLP', 'F') == 10