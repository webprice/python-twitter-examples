#all we need to do is to create a function
import string,random
def api_generator(size=11, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
  #fucntion will generate 11 characters long random code
  #with chars(lowercase+uppercase)+integers
  #you can change "size" to whatever you need.
