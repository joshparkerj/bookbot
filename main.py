def main():
 file_name = './books/frankenstein.txt'
 print(get_report_heading(file_name))
 file_contents = get_file_contents(file_name)
 print(get_word_count_report(file_contents)) 
 print(get_char_counts_report(file_contents))

def get_report_heading(file_name):
 return f'--- Begin report of {file_name} ---'

def get_word_count_report(file_contents):
 char_count = len(file_contents)
 word_count = len(file_contents.split())
 line_count = len(file_contents.split('\n')) - 1
 return f'{line_count} lines, {word_count}, words, and {char_count} characters found in the document'

def get_file_contents(file_name):
 with open(file_name) as f:
  return f.read()

def get_char_counts(text):
 char_count_dict = {char: 0 for char in set(text.lower())}
 for char in text.lower():
  char_count_dict[char] += 1
 return char_count_dict

def get_char_counts_report(text):
 char_counts = get_char_counts(text)
 list_of_dicts = [{ 'char': char, 'count': count } for char, count in char_counts.items()]
 list_of_dicts.sort(reverse=True, key=lambda d: d['count'])
 return '\n'.join([f'The \'{'\\n' if count_dict['char'] == '\n' else count_dict['char']}\' character was found {count_dict['count']} time{'' if count_dict['count'] == 1 else 's'}' for count_dict in list_of_dicts])
main()
