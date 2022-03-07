
error_message1 = 'VALUE MUST BE OF TYPE STRING';
error_message2 = 'STRING MUST BE LONGER THAN FIVE LETTERS'

def myDecorator(params):
    def wrapper(*args,**kwargs):
        for arg in args:
            if not isinstance(arg,str):
                raise TypeError(error_message1)
            if len(arg)<6:
                raise ValueError(error_message2)
        for kwarg in kwargs:
            if not isinstance(kwargs[kwarg],str):
                raise TypeError(error_message1)
            if len(kwargs[kwarg])<6:
                raise ValueError(error_message2)
        return params(*args,**kwargs)
    return wrapper

@myDecorator
def main_func(param1,param2):
    print('Param:',param1,param2)
    
main_func('python is fu',param2='n, ...')
