Get started with Python programming
===================================

Exercise 1
---
Implement a "Point" class that is able to represent 2-D points.  
The class must contains the methods to obtain the results shown below
~~~
a=Point(7,1)
b=Point(1,1)
print(a.distance(b))
​
6.0

a.move(2,2)

print(a.x)
9

print(a.y)
3
~~~

**Tips and tricks**:
* The formula for the distance betwees two points is  
$$d(P_1,P_2)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$$
* To use the square root function you need to import math and use math.sqrt like below
~~~
import math
a=math.sqrt(b)
~~~

Exercise 2
---
Implement a "Line" class that is able to represent 2-D lines.
Using the class "Points" of the previous exercise and this one try to obtain the following results

~~~
​
l=Line(3,2)

l
print(l)
Line: y=3x+2

a=Point(0,1)
b=Point(2,2)

​
l.line_from_points(a,b)
Line: y=0.3333333333333333x+1.0


l=Line(1)

m=Line(-1)

a=Point(1,5)

print(l.distance(a))
2.82842712474619

i=l.intersection(m)
print(i)
(0.0,0.0)
~~~
**Tips and trics**
* The formula to obtain the equation from 2 points is
$$ y=(y_2-y_1)/(x_2-x_1)x-(y_2-y_1)/(x_2-x_1)x_1+y_1$$ 
* The formula for the distance between a line and a point is 
$$d(P,r)=\frac{|ax_P+by_P+c|}{\sqrt{a^2+b^2}}$$
* the formula to find the intersection is
$$P\left({\frac {q_2-q_1}{m_1-m_2}},m_1{\frac {q_2-q_1}{m_1-m_2}}+q_1\right)$$


Exercise 3
---
Create the classes "Contact" and "AddressBook"
All the contacts are stored in a json file named "contacts.json" and are similar to
~~~
{
                   "name": "Cassio",
                   "surname":"Zen",
                   "email": "cassiozen@gmail.com"
}
~~~
The "AddressBook" class must be able to read the content of the file and perform CRUD (**C**reate,**R**ead,**U**pdate,**D**elete). The Update is the most difficult so i suggest it to begin ith the other. Below you can find an example

~~~

>>>book=AddressBook()
>>>book.show()

Name:Cassio, Surname:Zen, mail:cassiozen@gmail.com

Name:Dan, Surname:Abramov, mail:gaearon@somewhere.com

Name:Pete, Surname:Hunt, mail:floydophone@somewhere.com

Name:Paul, Surname:Shannessy, mail:zpao@somewhere.com

Name:Ryan, Surname:Florence, mail:rpflorence@somewhere.com

Name:Sebastian, Surname:Markbage, mail:sebmarkbage@here.com


>>>book.find_by_name('Dan')

I found the following results:

Name:Dan, Surname:Abramov, mail:gaearon@somewhere.com


>>>book.remove_contact('Dan')
>>>book.show()
Name:Cassio, Surname:Zen, mail:cassiozen@gmail.com

Name:Pete, Surname:Hunt, mail:floydophone@somewhere.com

Name:Paul, Surname:Shannessy, mail:zpao@somewhere.com

Name:Ryan, Surname:Florence, mail:rpflorence@somewhere.com

Name:Sebastian, Surname:Markbage, mail:sebmarkbage@here.com


>>>book.add_contact('Peter','Parker','notspiderman@marvel.com')
>>>book.show()
Name:Cassio, Surname:Zen, mail:cassiozen@gmail.com

Name:Pete, Surname:Hunt, mail:floydophone@somewhere.com

Name:Paul, Surname:Shannessy, mail:zpao@somewhere.com

Name:Ryan, Surname:Florence, mail:rpflorence@somewhere.com

Name:Sebastian, Surname:Markbage, mail:sebmarkbage@here.com

Name:Peter, Surname:Parker, mail:notspiderman@marvel.com
~~~

Once you've done this you can now create a client to use the functions you implemented in a "user-frienldy way"
The result should be something like the following
~~~
Welcome to the application to manage your contacts
Press 's' tho show the list of contacts
Press 'n' to add a contact
Press 'f' to find a contact
Press 'd' to delete a contact
 s
Name:Cassio, Surname:Zen, mail:cassiozen@gmail.com

Name:Dan, Surname:Abramov, mail:gaearon@somewhere.com

Name:Pete, Surname:Hunt, mail:floydophone@somewhere.com

Name:Paul, Surname:Shannessy, mail:zpao@somewhere.com

Name:Ryan, Surname:Florence, mail:rpflorence@somewhere.com

Name:Sebastian, Surname:Markbage, mail:sebmarkbage@here.com

Press 's' tho show the list of contacts
Press 'n' to add a contact
Press 'f' to find a contact
Press 'd' to delete a contact
 g
Command not available
Press 's' tho show the list of contacts
Press 'n' to add a contact
Press 'f' to find a contact
Press 'd' to delete a contact
 q
 ~~~
<font color='red'>test blue color font</font>


