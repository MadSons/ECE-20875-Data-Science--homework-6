import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: True or False
    """
    # 1-7 letters, 0-4 digits, end with '@jediacademy.edu'
    p = re.compile(r'\b^(\D{1,7}\d{0,4})\b(@jediacademy\.edu)$')

    if p.search(searchstring):
        return True
    else:
        return False


def problem2(searchstring):
    """
    Extract student and ship.

    :param searchstring: string
    :return: tuple
    """
    p = re.compile(r'([A-Z][a-z]*) flies the ([A-Z]+\-\w+)|'
                   r'([A-Z][a-z]* [A-Z][a-z]*) flies the ([A-Z]+\-\w+)')
    match = p.search(searchstring)
    if match:
        if match.group(1) and match.group(2):
            return match.group(1), match.group(2)
        elif match.group(3) and match.group(4):
            return match.group(3), match.group(4)
    else:
        return "noname", "noship"


def problem3(searchstring):
    """
    Replace apprentice with title.

    :param searchstring: string
    :return: string
    """

    p_jedi = re.compile(r'([Jj]edi) ([Aa]pprentice)')
    p_sith = re.compile(r'([Ss]ith) ([Aa]pprentice)')

    if p_jedi.search(searchstring) is None and p_sith.search(searchstring) is None:
        return 'nomatch'
    if p_jedi:
        searchstring = p_jedi.sub(r'\1 Master', searchstring)
    if p_sith:
        searchstring = p_sith.sub(r'\1 Darth', searchstring)
    return searchstring


if __name__ == "__main__":
    print("To test your code, run the `test_problems.py` file provided.")
