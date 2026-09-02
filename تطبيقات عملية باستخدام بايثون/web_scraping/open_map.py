import webbrowser, sys


if len(sys.argv)>1:

    adress=' '.join(sys.argv[1:])
    

else:
    print('enter the adress')    
    
webbrowser.open(f'https://www.google.com/maps/place/{adress}')

