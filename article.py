
import hashlib

class article:
    '''
     class article represents one class 

    '''

    def __init__(self, url):
        self.url = url
        self.id =

if __name__ == '__main__':
    url = "https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage"
    result = hashlib.md5(url.encode())

    # printing the equivalent hexadecimal value.
    print("The hexadecimal equivalent of hash is : ", end="")
    print(result.hexdigest())