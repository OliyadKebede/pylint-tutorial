from doc_string_checker import TripleDoubleStringChecker

def register(linter):
    """ This required method auto-registers the checker during initialization.
    : param linter: The linter to register the checker to.
    """
    linter.register_checker(TripleDoubleStringChecker(linter))