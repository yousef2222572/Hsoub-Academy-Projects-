name={
    1:'yousef',
    2:'omar',
    3:'ahmad',
}
print(name)

print(type(name))


print(name[1])
print(name[2])

name[1]='salem'
print(name)

print('-----------------------------------------------')
task={}
task['sunday']=('maths test')
task['monday']={'mon':'sayans test'}
task['tuseday']=['english test','tus']

sn=task['sunday'][0:]
#print(task)
print(sn)
print(f'the test for tomoro is {sn}')
print('sunday' in  task)
print(len(task['sunday']))
#task.clear()
print('---------------------------------------------------------------------------')
taskkeys=task.keys()
taskvalues=task.values()
taskitems=task.items()
task['tharasday']='frensh test'

print(list(taskitems))
print(taskvalues)
print(taskkeys)
task.pop('tharasday')
print(task)
task.popitem()
print(task)