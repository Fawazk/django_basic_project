from django.db import models

# Create your models here.
class Employee:
    image=str
    name=str
    job=str
    des=str
emp1=Employee()
emp2=Employee()
emp3=Employee()
emp4=Employee()

emp1.image='trainer-1.jpg'
emp2.image='trainer-2.jpg'
emp3.image='trainer-3.jpg'


emp1.name='sanin'
emp2.name='fathima'
emp3.name='FAWAZ'
emp4.name='kans'

emp1.job='Web developer'
emp2.job='Front-end developer'
emp3.job='Back-end developer'
emp4.job ='software engineer'

emp1.des='Passionate in business'
emp2.des='Curious about mandhi'
emp3.des='Hard worker'
emp4.des='Day dreamer'
  
emp=[emp1,emp2,emp3]

class experience:
    name=str
    year=str
    company=str
e1=experience()
e2=experience()
e3=experience()
e4=experience()

e1.name='sanin'
e2.name='fawas'
e3.name='ameeer'
e4.name='kans'

e1.year=2
e2.year=10
e3.year=5
e4.year=3

e1.company='Cross Roads'
e2.company='Packapeer'
e3.company='Cross Roads'
e4.company='Packapeer'

ex=[e1,e2,e3,e4]

class card:
    img=str
    titile=str
    title2=str
    like=int
    name=str
    share=int
    price=int
b1=card()
b2=card()
b3=card()

b1.img='course-1.jpg'
b1.titile='Web Development'
b1.price=165
b1.title2='Website Design'
b1.name='antonio'
b1.share=65
b1.like=50


b2.img='course-2.jpg'
b2.titile='Marketing'
b2.price=155
b2.title2='Search Engine Optimization'
b2.name='lana'
b2.share=70
b2.like=60


b3.img='course-3.jpg'
b3.titile='Content'
b3.price=185
b3.title2='Copywriting'
b3.name='Brandon'
b3.share=95
b3.like=45

cards=[b1,b2,b3]