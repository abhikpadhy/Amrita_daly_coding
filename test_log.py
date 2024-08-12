
def read_file_1(log_file):
    with open(log_file,'r') as file:
        content = file.read()
        #for line in file:
        #    content = line.strip()
            #print(type(content))
    #print(content)
    new_content = content.replace('INFO' ,'PASS')
    print(new_content)

def main():
    logfile = 'logs.log'  # Replace with your log file name
    read_file_1(logfile)    

if __name__ == "__main__":
    main()            