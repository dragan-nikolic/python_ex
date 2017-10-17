"""
Created on 2012-05-02

@author: dnikolic
"""

# ImportError
try:
    import unknown_module
except ImportError:
    print ("module 'unknown_module' doesn not exist!")
    print ('===')

class ValidationError(Exception):
    def __init__(
            self, 
            message,
            capture_screen_on_error=False,
            expected_image=None,
            searched_screen_region='Screen',
            screenshot_name=None):

        # Call the base class constructor with the parameters it needs
        self.message = message
        
        self.searched_screen_region = searched_screen_region

        # Now for your custom code...
        print ('capture_screen_on_error=%s' % capture_screen_on_error)
        print ('expected_image=%s' % expected_image)
        print ('searched_screen_region=%s' % searched_screen_region)
        print ('screenshot_name=%s' % screenshot_name)
        
def test_validation_error_01():
    try:
        raise ValidationError('this is validation error message', True)
    except ValidationError as err:
        print ('message=%s' % err.message)
        print ('searched_screen_region=%s' % err.searched_screen_region)

def test_validation_error_02():
    try:
        raise ValidationError('this is validation error message', True)
    except Exception as err:
        print ('message=%s' % err.message)
        print ('searched_screen_region=%s' % err.searched_screen_region)
        print (str(err))

class MyException(Exception):
    pass
        
def test_exception_attributes():
    try:
        raise MyException('my exception')
    except Exception as e:
        print ('Exception attributes are: %s' % dir(e))
        print ('message=%s' % e.message)
        print ('str=%s' % str(e))
        print ('type=%s' % type(e))
        print ('value=%s' % e.value)

        
        
if __name__ == '__main__':
    test_validation_error_01()
    test_validation_error_02()
    test_exception_attributes()
