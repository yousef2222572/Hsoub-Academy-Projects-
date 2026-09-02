from argparse import ArgumentParser
from .task_controlar import Task_Controller
def main():
    controller=Task_Controller('tasks.txt')
    parser=ArgumentParser(description='hello what you are need')

    subparsers=parser.add_subparsers()
    add_task=subparsers.add_parser('add',help='Add the given task')
    add_task.add_argument('title',help='Title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description of the task',type=str,default=None)
    add_task.add_argument('-s','--start_date',help='Date to begin the task',type=str,default=None)
    add_task.add_argument('-e','--end_date',help='Date to end the task',type=str,default=None)
    add_task.add_argument('--done',help='Check wether the task is done or not',default=False)
    add_task.set_defaults(func=controller.add_task)

    
    list_tasks=subparsers.add_parser('list',help='list unfinshed task')
    list_tasks.add_argument('-a','--all',help='the list is have all the task',action='store_true')
    list_tasks.set_defaults(func=controller.display)




    check_task=subparsers.add_parser('check',help='list unfinished')
    check_task.add_argument('-t','--task',help='number of the task to be done . if not specified , last task will be removed .',type=int)
    check_task.set_defaults(func=controller.check_task)


    remove=subparsers.add_parser('remove',help='remve a task')
    remove.add_argument('-t','--task',help='the task to be removed (number)',type=int)

    remove.set_defaults(func=controller.remove)
    


    reset=subparsers.add_parser('reset',help='remove all tasks')
    reset.set_defaults(func=controller.reset)
    

    args=parser.parse_args()

    args.func(args)




if __name__ == '__main__':
    main()
