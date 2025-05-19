user_input = input('Enter a text to write to the file: ')
file = open('output.txt', 'w')
file.write(user_input + '\n')
file.close()
print('Data successfully written to output.txt')

add_input = input('Enter additional text to append: ')
file = open('output.txt', 'a')
file.write(add_input + '\n')
file.close()
print('Data successfully appended.')

file = open('output.txt', 'r')
content_file = file.read()
file.close()
print("\nFinal file content:")
print(content_file)

