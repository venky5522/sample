def switch(choice):
    switcher = {'venky':'Monday',
                'loki':'Sunday'}
    print(switcher.get(choice,'Hi,User, Thank You'))
switch('venky')
switch('loki')
switch('ani')