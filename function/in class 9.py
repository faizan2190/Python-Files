# Modify the recursive function countdown, previously done in class so it exhibits this behavior:
# >>> countdown3(5)
# 5
# 4
# 3
# BOOOM!!!
# Scared you...
# 2
# 1
# Blast off!!!
def countdown(n):
    print(n)
    countdown(n-1)
countdown(5)