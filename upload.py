import os
def test():
    envs=os.getenv("TEST_ENV")
    print("yes,youget first" + envs)
    name="test"+envs
    print(111111111111)
    return name
test()
