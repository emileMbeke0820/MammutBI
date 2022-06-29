from argparse import ArgumentParser

parser = ArgumentParser()

# parser.add_argument('--output')
parser.add_argument('--output', '-o', required=True, help='Checking out argparse')
parser.add_argument('--text', '-t', required=True, help='The Text to write in the file')

args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text+'\n')
print(f'Wrote "{args.text}" to the file "{args.output}"')

print(args.output)
