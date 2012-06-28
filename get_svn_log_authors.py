import os


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


if __name__ == '__main__':
    # Add the input file here. Command line options to follow
    input_file = ''
    authors = get_authors(input_file)
    default_line = "%(author)s = %(author_name)s <%(author_email)s>\n"
    with open("authors.txt", 'w') as authors_fd:
        for author in authors:
            author_name = author
            author_email = "%s@example.net" % author
            authors_fd.write(default_line % {'author': author,
                                             'author_name': author_name,
                                             'author_email': author_email})

