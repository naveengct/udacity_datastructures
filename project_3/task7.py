class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = {}

class Router:
    def __init__(self,root_handler,error_handler):
        self.root=RouteTrieNode()        
        self.root_handler=root_handler        
        self.error_handler=error_handler

    def add_handler(self,path,handler):
        path_nodes=path.split('/')
        current_node = self.root
        for x in path_nodes[1:]:
             if x not in current_node.children:
                current_node.children[x] = RouteTrieNode()
             current_node = current_node.children[x]
        current_node.handler = handler
        
    def lookup(self,path):
        if path=='/':
            return self.root_handler
        path_nodes=path.split('/')
        if path_nodes[-1] == '':
            path_nodes=path_nodes[:-1]      
        current_node=self.root
        
        for x in path_nodes[1:]:
            if x not in current_node.children:
                return self.error_handler
            current_node = current_node.children[x]
        return current_node.handler if current_node.handler else self.error_handler
     
        
# create the router and add a route
router = Router("root handler", "not found handler") 
router.add_handler("/home/team", "web handler")  # add a route
router.add_handler("/home/login", "web handler") # add a route
router.add_handler("/program/python/program1", "program handler")  # add a route
router.add_handler("/program/cpp/program1", "program handler")  # add a route
router.add_handler("/program/python/program2", "program handler")  # add a route
router.add_handler("/program/cpp/program2", "program handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' 
print(router.lookup("/home/team")) # should print 'web handler'
print(router.lookup("/home/login/")) # should print 'web handler' 
print(router.lookup("/home/team/me")) # should print 'not found handler' 

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/program/python")) # should print 'not handler'
print(router.lookup("/program/python/program1/")) # should print 'program handler' 
print(router.lookup("/program/python/program2/")) # should print 'program handler' 
print(router.lookup("/program/cpp")) # should print 'not handler'
print(router.lookup("/program/cpp/program1/")) # should print 'program handler' 
print(router.lookup("/program/cpp/program2/")) # should print 'program handler