class NoSupportedQueriesFound(Exception):

    def __str__(self):
        return 'No Gene Specificity supported queries where found in passed query.'

class CurieNotSupported(Exception):

    def __init__(self, *args):
        self.curie = args[0]

    def __str__(self):
        return '{} not supported in gene_specificity app'.format(self.curie)
