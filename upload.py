import os
def test():
    print("yes , you are")
    a=os.environ
    print(a)
    TEST_ENV="22222222222222222"
    os.environ['NEW_ENV'] = "111111111111111111111111111111"
    print("upload yes")
   
test()
