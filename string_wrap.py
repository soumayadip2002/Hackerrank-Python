import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    word = wrapper.wrap(string)
    
    return('\n'.join([i for i in word[0:]]))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)