def main():
 file_name = './books/frankenstein.txt'
 file_contents = get_file_contents(file_name)
 line_count = len(file_contents.split('\n')) - 1
 word_count = len(file_contents.split())
 char_count = len(file_contents)
 print(f'\t{line_count}\t{word_count}\t{char_count}\t{file_name}')

def get_file_contents(file_name):
 with open(file_name) as f:
  return f.read()

main()
