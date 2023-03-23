import argparse
from random_username.generate import UsernameGenerator


def main():
    parser = argparse.ArgumentParser(description='Generate Compelling Usernames.')
    parser.add_argument('num_results', type=int, default=1, nargs='?',
                        help='Number of results to return')
    parser.add_argument('num_digits', type=int, default=1, nargs='?',
                        help='Number of digits in the end of a username')
    args = parser.parse_args()

    for username in UsernameGenerator().generate_usernames(num_results=args.num_results, num_digits=args.num_digits):
        print(username)


if __name__ == "__main__":
    main()
