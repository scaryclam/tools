import os
import sys
#import argparse
import optparse


def get_authors(filename):
    authors = []
    with open(filename, 'r') as log_fd:
        parse_next = False
        while True:
            line = log_fd.readline()
            if not line:
                break
            if parse_next:
                author = line.split('|')[1].replace(' ', '')
                if not author in authors:
                    authors.append(author)
                parse_next = False
            elif line.startswith("------"):
                parse_next = True

    return authors


def write_output(filename, authors, email_host=None):
    if not email_host:
        email_host = "example.com"

    # Add the input file here. Command line options to follow
    default_line = "%(author)s = %(author_name)s <%(author_email)s>\n"

    with open(filename, 'w') as authors_fd:
        for author in authors:
            author_name = author
            author_email = "%s@%s" % (author, email_host)
            authors_fd.write(default_line % {'author': author,
                                             'author_name': author_name,
                                             'author_email': author_email})


if __name__ == '__main__':
    parser = optparse.OptionParser()
    #parser.add_option('input_file', metavar='FILENAME',
    #                  help="The path to the input file")
    parser.add_option('-o', metavar="FILENAME",
                      help="The path to the output file",
                      default="authors.txt", dest="output_file")
    parser.add_option('--email-host', dest="email_host", default="example.net")
    opts, args = parser.parse_args()

    if len(args) != 1:
        print "You must provide an input file"
        sys.exit(0)
    input_file = args[0]

    # Add the input file here. Command line options to follow
    authors = get_authors(input_file)
    write_output(opts.output_file, authors, email_host=opts.email_host)

