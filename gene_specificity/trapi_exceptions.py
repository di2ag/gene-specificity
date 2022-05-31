class NoSupportedQueriesFound(Exception):

    def __str__(self):
        return 'No Gene Specificity supported queries where found in passed query.'
