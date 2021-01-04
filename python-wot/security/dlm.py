
import json


class DLM(dict):
    _instance_number = 0

    def __init__(self):
        type(self)._instance_number+=1
        print("New DLM model instance=",type(self)._instance_number)
        dict.__init__(self)
        # self['Instance']=type(self)._instance_number
        # print("My state:",self)

    def addPolicy(self, name, readers=[]):
        self[name]=readers

    # def default(self, obj):
    #     print("Calling default method!!!")
    #     return dict(_class_object={})
    #     return json.dumps({})
    
    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, 
    #         sort_keys=True, indent=4)
