import json
import cherrypy

# We assume a list formatted like the following
#booksList=[{"title":"Newest book","date":1993},{"title":"OldestBook","date":1457},{"title":"MediumBook","date":1885}]

class BookSorter(object):
    exposed=True
    def __init__(self):
        pass
    def POST(self,*uri):
        #Parameter to define the sorting order (ascending vs. descending)
        reverse=False
        #If an uri is present we check if it is equal to "D" (descending)
        #in that case we will sor tthe book in descending order
        if len(uri)!=0:
            if list(uri)[0]=="D":
                reverse=True
        #We get the body of the POST request
        body=cherrypy.request.body.read()
        #Conver thte body to a json
        books=json.loads(body)
        #We create a list containing the date of each book
        dates=[book['date'] for book in books]
        #We sort the date's list according to the order defined before
        dates.sort(reverse=reverse)
        #Create and empty output list
        sortedBooks=[]
        #For each element of the list of date that is now sorted
        #we pick the corresponding element of the books's list
        #and we append it to the output list. In this Way the books will be 
        #sorted by their date value
        for x in dates:
            for book in books:
                if book['date']==x:
                    sortedBooks.append(book)
        #We return the sorted list
        return json.dumps(sortedBooks)

if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}		
	cherrypy.tree.mount(BookSorter(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
