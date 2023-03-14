import grabAPI
import random

        
franchises = ['Marvel','Nickelodeon', 'Cartoon Network','Disney']
random_franch = franchises[random.randint(0,3)]
# using an older version of Python, no case match statements
start = "Here is a character from "
if random_franch == 'Marvel':
    print(start + "Marvel: ")
    grabAPI.grabMar()
elif random_franch == 'Nickelodeon':
    print(start + "Nickelodeon: ")
    grabAPI.grabNic()
elif random_franch == 'Cartoon Network':
    print(start + "Cartoon Network: ")
    grabAPI.grabNet()
elif random_franch == 'Disney':
    print(start + "Disney: ")
    grabAPI.grabDis()



