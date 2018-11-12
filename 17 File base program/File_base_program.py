class todolist:
    def __init__(self,file_name):
        self.file_name = file_name
        self.task = self.loaded_file_list()

    def loaded_file_list(self , file_name):
        task = []
        with open(self.file_name , 'r') as ff:
            for task in ff:
                task.append(task.srip())
        return task

    def list_of_task(self):
        for index , tsk in enumerate(self.task, start=1):
            print("{}) {}".format(index,tsk))

    def write_to_file(self):
        with open(self.file_name , 'w') as ff:
            for tsk in self.task:
                ff.write("{}\n".format(tsk))

    def add_new_task(self , tsk):
        self.task.append(tsk)
        self.write_to_file()

    def remove_done_task(self , index):
        try:
            del(self.task[index - 1])
            self.write_to_file()
        except IndexError:
            print('There are no open tasks with index {}'.format(index))

def help():
    print('To do list')
    print('# to add new task for list : 1 YOUR_TASK')
    print('# Remove you already done task : 2 YOUR_TASK')
    print('# to show your curent tasks : 3')
    print('# Exit from the programm : 4')
    print()

def run():
    variable = todolist('text.txt')
    help()

    while True:
        cmd = input('~#/  ')

        if cmd == '3' :
            variable.list_of_task()
        elif cmd == '1' :
            nwTask = input("enter your new task here :")
            variable.add_new_task(nwTask)
        elif cmd == '2' :
            val = input("type here value of position your already done task :")
            variable.remove_done_task(val)
        elif cmd == '5' :
            hlep()
        elif cmd == '4' :
            break
run()