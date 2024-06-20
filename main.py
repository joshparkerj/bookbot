def main():
 file_name = './books/frankenstein.txt'
 with open(file_name) as f:
  file_contents = f.read() 
  #  print(file_contents)
  line_count = len(file_contents.split('\n')) - 1
  word_count = len(file_contents.split())
  char_count = len(file_contents)
  print(f'\t{line_count}\t{word_count}\t{char_count}\t{file_name}')

main()
