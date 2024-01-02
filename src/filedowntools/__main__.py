from .download import *
import argparse
import os

parser = argparse.ArgumentParser(description='It is used to download files '
                                 'individually or in batches and store them in a specific location.')

parser.add_argument('file', nargs='+', metavar='file', 
                    help='URL of the file to be downloaded (multiple can be)')
parser.add_argument('-s', '--save', nargs='?', default=os.getcwd(), dest='save', 
                    metavar='save_location', help='The path where the file is saved.(Default current directory)')
parser.add_argument('-l', '--large', action='store_true', dest='large', 
                    help='Is it a large file? If so, then only one file can be downloaded.')

args = parser.parse_args()

def main(args):
    if not args.large:
        if len(args.file) == 1:
            file = download(args.file[0])
            file.save(args.save)
        else:
            fileurls = []
            for file in args.file:
                fileurls.append(file)
            files = downloads(*fileurls)
            files.save(args.save)
    else:
        file = large_download(args.file[0])
        file.save(args.save)

if __name__ == '__main__':
    main(args)