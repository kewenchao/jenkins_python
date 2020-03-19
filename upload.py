import os
def test():
    print("yes , you are")
    a=os.environ
    print(a)
    TEST_ENV="22222222222222222"
    os.putenv('NEW_ENV',"11111111111111111111")
    b=os.environ
    print(b)
    print("upload yes")
   
test()
