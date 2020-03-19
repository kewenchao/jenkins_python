import os
def test():
    print("yes , you are")
    myfile=open("/home/keke/jenkins/workspace/test--inject/env.properties","w")
    TEST_ENV="22222222222222222"
    print("upload yes")
    myfile.close()
test()
