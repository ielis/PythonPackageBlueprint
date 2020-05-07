import unittest

from pkg_resources import resource_filename

from . import fasta

fasta_path = resource_filename(__name__, 'test_data/chrM.small.fa')
fasta_fai_path = resource_filename(__name__, 'test_data/chrM.small.fa.fai')


class FastaTest(unittest.TestCase):
    """
    Toy tests, more tests would be required in real life.
    """

    def test_fetch_sequence_region(self):
        # first 5 bases
        region = 'chrM:1-5'
        sequence = fasta.fetch_sequence_region(region, fasta_path=fasta_path, fasta_fai_path=fasta_fai_path)
        self.assertEqual('GATCA', sequence)

        # last 5 bases
        region = 'chrM:96-100'
        sequence = fasta.fetch_sequence_region(region, fasta_path=fasta_path, fasta_fai_path=fasta_fai_path)
        self.assertEqual('CGCTG', sequence)
