# Cleant Python input handling
# https://youtube.com/shorts/-Xswnq39Q3M?si=j76r0yoNdcMLH6UG
# www.youtube.com/@b001

def do_this():
    print('Doing this')

def do_that():
    print('Doing that')

match input('Do this or that? '):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print('I don\'t know what to do')
