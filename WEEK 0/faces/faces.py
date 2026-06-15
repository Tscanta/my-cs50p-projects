def convert(n):
        #replace faces
        n = n.replace(':)', '🙂')
        n = n.replace(':(', '🙁')

        #return results
        return n;

#main function
def main():
        #enters users input
        user_input = input()
        result = convert(user_input)

        print(result)

main()
