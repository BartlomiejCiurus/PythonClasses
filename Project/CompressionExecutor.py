import sys

from LempelZivWelchEncoder import LempelZivWelchEncoder
from RunLengthEncoder import RunLengthEncoder

lvwExecutor = LempelZivWelchEncoder()
rleExecutor = RunLengthEncoder()

if len(sys.argv) != 3:
    raise ValueError("There should be arguments!")
if sys.argv[1] != 'lvw' and sys.argv[1] != 'rle':
    raise ValueError("First argument is lvw (Lempel Ziv Welch Algorithm) or rle (Run Length Algorithm)!")

if sys.argv[1] == 'lvw':
    lvwExecutor.input = str(sys.argv[2])
    print(lvwExecutor.encode())
else:
    rleExecutor.input = str(sys.argv[2])
    print(rleExecutor.encode())
