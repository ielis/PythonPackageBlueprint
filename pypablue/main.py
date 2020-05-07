import argparse
import logging
import sys

import pypablue


def main():
    """Python package blueprint"""
    logger = logging.getLogger(main.__name__)

    parser = argparse.ArgumentParser(description=main.__doc__,
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     prog=pypablue.__name__)
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=pypablue.__version__))

    # ################################### DEFINE CLI PARSER ############################################################
    #
    #

    # generate subparsers/subcommands
    subparsers = parser.add_subparsers(dest='command')

    # #################### -------------- `fasta` -------------- ####################
    parser_fasta = subparsers.add_parser('fasta', help='tasks that use Fasta files')
    subparsers_fasta = parser_fasta.add_subparsers(dest='fasta_cmd')

    # 1 - `fetch`
    parser_fasta_fetch = subparsers_fasta.add_parser('fetch', help='get sequence for specified interval')
    parser_fasta_fetch.add_argument('interval', help='interval to get the sequence for (e.g. chrM:1-10)')
    parser_fasta_fetch.add_argument('fasta', help='path to indexed Fasta file')

    #
    #
    # ############################### END DEFINE CLI PARSER ############################################################

    # If no arguments provided, print full help menu
    argv = sys.argv[1:]  # strip away the script name which is the first item in the `argv` list
    if len(argv) == 0:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args(argv)

    if hasattr(args, 'fasta_cmd'):
        if args.fasta_cmd == 'fetch':
            logger.info('Running `fasta fetch` command')
            logger.info('Using Fasta located at `{}`'.format(args.fasta))

            region = pypablue.fasta.fetch_sequence_region(interval=args.interval, fasta_path=args.fasta)
            if region:
                print(region)

        else:
            parser_fasta.print_help()
    else:
        logger.warning("No command was specified")
