# use recursion to implement a countdown counter

def countdown(x):
    if x == 0: # breaking condition
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        print("foo") # executes in order after countdown is complete
        # the call stack is being unwound after the final return statement

countdown(5)
