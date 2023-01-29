def add():
    name =input('enter your name\n')
    maths =input('enter maths marks\n')
    chemistry=input('enter chemistry marks\n')
    physics =input('enter physics marks\n')
    content ='\n'+','.join([name,maths,chemistry,physics])
    with open('student data\student_record.csv','a') as file:
        file.write(content)

def search():
    key =input('enter your name\n').strip().lower()
    with open('student data\student_record.csv','r') as file:
        file.readline()
        for line in file:
            if line=='\n':
                continue
            line =line.strip().split(',')
            name =line[0].strip().lower()
            if name==key:
                per =sum(map(int,line[-3:]))/3
                per =f'{per:.2f}'
                print(f'Name       ={name:>10}')
                print(f'Maths      ={line[1]:>10}')
                print(f'Chemistry  ={line[2]:>10}')
                print(f'Physics    ={line[3]:>10}')
                print(f'Percentage ={per:>10}')
                
                
                
def all_search():
    with open('student data\student_record.csv','r') as file:
        header =file.readline().strip().split(',')
        header.append('percentage')
        width = 61
        output = "|{:^15}|{:^10}|{:^10}|{:^10}|{:^10}|"
        print("-"*width)
        print(output.format(*header))
        print("-"*width)
        for line in file:
            if line=='\n':
                continue
            line =line.strip().split(',')
            line[0]=line[0].strip().title()
            per =sum(map(int,line[-3:]))/3
            per =f'{per:.2f}'
            line.append(per)
            print(output.format(*line))
            print("_"*width)

def main():
    menu ="""
    1.Add student
    2.Search student
    3.Search all student
    4.Exit
    """
    print(menu)
    choice =input('choose 1 to 3')
    if choice =='1':
        add()
    elif choice=='2':
        search()
    elif choice =='3':
        all_search()
    elif choice=='4':
        exit(0)
main()
