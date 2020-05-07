import logging
import re

import pysam

logger = logging.getLogger(__name__)

# matches e.g `chr1:10-20`
interval_pattern = re.compile(r'^(?P<contig>\w+):(?P<begin>\d+)-(?P<end>\d+)$')


def fetch_sequence_region(interval: str, fasta_path: str, fasta_fai_path: str = None):
    """
    Get nucleotide sequence for the specified interval from Fasta file.

    :param interval: interval string, e.g. `chr1:101-110`
    :param fasta_path: path to indexed Fasta file
    :param fasta_fai_path: path to Fasta index file
    :return: nucleotide sequence string or None if `interval` is malformed
    """
    match = interval_pattern.match(interval)
    if not match:
        logger.warning('Invalid interval: `{}`'.format(interval))
        return None

    contig = match.group('contig')
    begin = int(match.group('begin'))
    end = int(match.group('end'))

    with pysam.FastaFile(filename=fasta_path, filepath_index=fasta_fai_path) as fasta:
        # this method requires half-open interval coordinates
        return fasta.fetch(reference=contig, start=begin - 1, end=end)
