![PyPI](https://img.shields.io/pypi/v/zstdcat)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zstdcat)

[![Downloads](https://pepy.tech/badge/zstdcat)](https://pepy.tech/project/zstdcat)
[![Downloads](https://pepy.tech/badge/zstdcat/month)](https://pepy.tech/project/zstdcat)
[![Downloads](https://pepy.tech/badge/zstdcat/week)](https://pepy.tech/project/zstdcat)

[![Donate](https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png)](https://www.buymeacoffee.com/adw0rd)

# zstdcat

Zstandard console reader

### Install

`pip install zstdcat`

### Usage

```
$ cat /tmp/response.bin
eDʔ�I��mWv��̤C'wV�z'$(�|�s�ߜ�is6@.*vC{v  |�w3�����WI�)v�����ui��#��tH
ACFNN68�O��*�Ln ��͢Q�,

$ od /tmp/response.bin
0000000 132450 176457 154040 001705 001000 013107 110030 006665
0000020 062415 145104 154224 156511 066740 073127 146257 122314
0000040 023503 053167 144402 075025 022047 175450 115574 110563
0000060 116337 174406 135252 071551 040066 025056 041566 075417
0000100 004566 007574 073744 105063 145643 006014 012242 053622
0000120 141511 073051 127201 164645 160620 072670 143151 002343
0000140 113043 072337 005110 040400 043103 047116 033007 120070
0000160 047432 126275 110052 067114 142440 146765 050642 026331
0000200 000003
0000201
```

Now let's read with zstdcat:

```
$ cat /tmp/response.bin | zstdcat
{"friendship_status":{"following":false,"followed_by":false,"blocking":false,...,"status":"ok"}

$ zstdcat -i /tmp/response.bin
{"friendship_status":{"following":false,"followed_by":false,"blocking":false,...,"status":"ok"}
```
