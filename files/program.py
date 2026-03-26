import sys

if len(sys.argv) != 4:
    print('usage: program.py option int int', file=sys.stderr)
    print('  --add    add numbers (default)', file=sys.stderr)
    print('  --mul    multiply numbers', file=sys.stderr)
    sys.exit(1)

a = int(sys.argv[2])
b = int(sys.argv[3])
if sys.argv[1] == '--add':
    print(a + b)
elif sys.argv[1] == '--mul':
    print(a * b)
else:
    print('error: unrecognized option', sys.argv[1], file=sys.stderr)
    sys.exit(1)
