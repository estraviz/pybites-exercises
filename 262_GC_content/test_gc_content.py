"""
Tests for gc_content.py
Uses various DNA sequences retrieved from NCBI as input
Compares user function with calculated GC content
Inputs are modified to check how the function deals with unknown characters
"""

import pytest
from gc_content import calculate_gc_content

DNA_SEQUENCES = [
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3
            "tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
            "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
            "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
            "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
            "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
            "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
            "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
            "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
            "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
            "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
            "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
            "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
            "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
            "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
            "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
            "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
            "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
            "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
            "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
            "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
            "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"
        ),
        51.35,
    ),
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
            "gttaatatttatgattcctgaaaagaaatcaatcgcaatcatgaaagaactaagcattgg"
            "aaatacaaagcaaatgctgatgattaatggagttgacgtgaaaaatccattgctgctttt"
            "tttacatggcgggccgggaacgccgcaaatcggatatgttagacattatcaaaaagagct"
            "ggaacagtattttacagtagttcattgggatcagagaggatcggggctttcttattctaa"
            "gcgaatttcgcatcactctatgacaataaatcacttcattaaagatacaatccaagtcac"
            "tcaatggcttttagctcatttttcaaaatcaaaactttacctagccggtcattcttgggg"
            "atcaatactggcgcttcatgtgctgcagcagcgtcctgatttattttacacgtattatgg"
            "aatcagccaggttgttaacccgcaagatgaagaatcaactgcttatcaacatattcgtga"
            "aatttccgaatcaaaaaaagccagcatattatctttccttacacgtttcattggtgctcc"
            "gccttggaagcaggatatccagcaccttatctatcggttttgtgttgagctaaccagggg"
            "aggattcactcaccgtcatcgtcaatctctcgctgtattatttcaaatgcttactggcaa"
            "tgagtatggagtgcggaacatgcacagcttccttaatggattgcgcttcagtaaaaaaca"
            "tttaactgatgagttgtaccggtttaatgcttttacatcagttccttctattaaagtacc"
            "gtgtgttttcatttcagggaaacatgacttaattgttcctgcagaaatatcgaaacagta"
            "ttatcaagaacttgaggcacctgaaaagcgctggtttcaatttgagaattcagctcacac"
            "cccgcatattgaggagccatcattattcgcgaacacattaagtcggcatgcacgacacca"
            "tttatgatagatccttgataaataagaaaaacccctgtataataaaaaaagtgtgcaaat"
            "catgcatattttaaataagtcttgcaacatgcgcctattttctgtataatggtgtatgtt"
            "ggtctttgactgcgatgaagtgagaggttgctgacacacccggccgctttgccatggcaa"
            "ggtgttcaggtttttctcacggagaactgtctaacgtgatgtaggcgaaaaggagggaaa"
            "ataatggcaaaacaaaaaattcgtattcgtttgaaagcatatgatcatagaatccttgat"
        ),
        39.37,
    ),
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
            # but all As removed, upper and lower case
            "gtttttttgttcctggtctcgctctggctgcttgg"
            "tcgctgctgtgtttgggttgcgtgtccttgctgctttt"
            "tttctggcgggccgggcgccgctcggttgttgctttcggct"
            "ggcgtttttcgtgttcttgggtcggggtcggggctttcttttct"
            "gcgtttcgctcctcttgcttccttcttgtctccgtcc"
            "tctggcttttgctctttttctcctttcctgccggtcttcttgggg"
            "tctctggcgcttctgtgctgcgcgcgtcctgtttttttccgttttgg"
            "tcgccggttgttcccgcgtGGtcctgctttcctttcgtg"
            "tttccgtcgccgcttttctttccttccgtttcttggtgctcc"
            "gccttgggcggttccgccctttcttcggttttgtgttggctccgggg"
            "ggttcctcccgtctcgtctctctcgctgttttttctgcttctggc"
            "tggttgggtgcggctgccgcttcctttggttgcgcttcgtc"
            "tttctgtggttgtccggttttgcttttctcgttccttctttgtcc"
            "gtgtgttttctttcgggCtgcttttgttcctgcgttcgcgt"
        ),
        55.88,
    ),
]


@pytest.mark.parametrize("dna,gc_content", DNA_SEQUENCES)
def test_calculate_gc_content(dna, gc_content):

    assert calculate_gc_content(dna) == gc_content

    dna_with_spaces = "".join([base + " " for base in dna])
    assert calculate_gc_content(dna_with_spaces) == gc_content

    dna_with_special_chars = "".join([base + ".!?/," for base in dna])
    assert calculate_gc_content(dna_with_special_chars) == gc_content

    dna_line_breaks = "\n" + dna + "\n" + dna + "\n"
    assert calculate_gc_content(dna_line_breaks) == gc_content
