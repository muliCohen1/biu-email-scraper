# def read_file(title):
#     try:
#         read_value = open("records/"+ title +".txt", "r")
#         read_value = read_value.read()
#     except IOError:
#         print("Creating new record")
#         read_value = ''
#     return read_value

def write_file(element):
    try:
        write_value = open("records.txt", "a")
        write_value.write(element + ", ")
        write_value.close()
    except UnicodeEncodeError:
        print("Writing error occurred")