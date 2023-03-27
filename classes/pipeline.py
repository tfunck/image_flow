import hashlib

class Workflow():
    pass

class Node():
    def __init__(self, inputs, outputs, function, output_root_dir, name, prev_node=None, next_node=None, qc_function=None, clobber=False):
    self.name=name
    self.output_root_dir=output_root_dir

    self.current_output_dir = output_root_dir + os.sep + name

    os.makedirs(self.current_output_dir, exist_ok=True)

    self.to_run = self.check_if_run()

    def run_all_preceding(self):
        self.to_run = True
        self.clobber = True
        if prev_node != None :
            self.prev_node.run_all_preceding()
           
    def save_node_info(self):
        pass

    def create_hash(self):
        
        h = hashlib.new('sha256') #sha256 can be replaced with diffrent algorithms
        h.update('Hello World'.encode()) #give a encoded string. Makes the String to the Hash 
        return h.hexdigest()

    def check_hash(self):
        pass

    def check_to_run(self):
        self.to_run=False
        #for fn in inputs :
        #    assert os.path.exists(fn) :  f'Error: Node {self.name}, missing input file\n{fn}' 
       
        for in_fn in inputs :
            for out_fn in inputs :
                if newer_than(in_fn, out_fn) :

                    self.to_run=True
                    self.clobber=True

                    if self.prev_node != None :
                        self.prev_node.run_all_preceding()


