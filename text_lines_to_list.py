# Transform text lines into list items

# text_file_name = 'today\'s_articles/text.txt'

def r_lines(text_file_name):
    o_file = open(text_file_name, 'r')
    re_lines = o_file.readlines()
    lines = [x[:-1] for x in re_lines if len(x) >= 3]
    return lines



