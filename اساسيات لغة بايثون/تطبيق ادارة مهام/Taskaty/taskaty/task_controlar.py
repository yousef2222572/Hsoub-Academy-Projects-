
from .task import task
from tabulate import tabulate

from datetime import date
from argparse import Namespace

class Task_Controller:
    def __init__(self,file_name):
        self.file_name=file_name

    def add_task(self,args):

        if not args.start_date:
            now = date.today().isoformat()
            args.startـdate=now

        Tasks=task(args.title,args.description,args.start_date,args.end_date,args.done)
        with open(self.file_name,'a')as file:
            file.write(str(Tasks)+'\n')
    def list_tasks(self):
        unfinished_tasks=[]
        with open(self.file_name,'r') as file:
            for line in file :
                title,description,start_date,end_date,done=line.split(',')
                end_date=None if end_date=='None' else end_date
                done=False if done.strip('\n') == 'False' else True
                if done:
                    continue
                unfinished_tasks.append({'title':title,'description':description,'start_date':start_date,'end_date':end_date})
    
        return unfinished_tasks


    def list_all_tasks(self):
        all_tasks=[]
        with open(self.file_name,'r') as file:
            for line in file :
                title,description,start_date,end_date,done=line.split(',')
                end_date=None if end_date=='None' else end_date
                done=False if done.strip('\n') == 'False' else True

                
                all_tasks.append({'title':title,'description':description,'start_date':start_date,'end_date':end_date,'done':done})
    
        return all_tasks
    
    def deu_date(self,start,end):
        start_date=date.fromisoformat(start)
        end_date=date.fromisoformat(end)
        date_delte=start_date-end_date
        return f'{date_delte}'
    def print_table(self,tasks):
        formatted_tasks=[]
        for number ,task in enumerate(tasks,1):
            if task['start_date'] and task['end_date']:
                due_date=self.deu_date(task['start_date'],task['end_date'])
            else:
                due_date='open'
            formatted_tasks.append({'no.':number,**task,'due_date':due_date})
        print(tabulate(formatted_tasks,headers='keys'))                


    def display(self,args):
        all_tasks=self.list_all_tasks()
        unchecked_tasks=self.list_tasks()
        if not all_tasks :
            print('there are no tasks , to add task use add <task>')
            return 
        
        if args.all :
            self.print_table(all_tasks)
        else:
            if unchecked_tasks:
                self.print_table(unchecked_tasks)
            else:
                print('all tasks are checked')

    def check_task(self,args):
        index=args.task
        tasks=self.list_all_tasks()
        if index <0 or index >len(tasks):
            print(f'task num is {index} does not exist')
            return
        
        tasks[index-1]['done']=True
        with open(self.file_name,'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))


    def remove(self,args):
        tasks=self.list_all_tasks()
        if args.task:
            index=args.task
        else:
            index=len(tasks)-1
        if index <= 0 or index > len(tasks):
            print(f'task num {index} does not exist !')
            return
        tasks.pop(index-1)
        with open (self.file_name,'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def reset(self,*args):
        with open (self.file_name,'w')as file:
            file.write('')
            print('you have delete all tasks')

        



























if __name__ == '__mainــ' :
    pass