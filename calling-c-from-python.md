
---
title:  C言語の関数をPythonから呼び出す方法
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css calling-c-from-python.md > calling-c-from-python.html
-->

# このページについて

C言語の関数をPythonから呼び出す方法について書かれています。

## C言語のライブラリの作成

以下のようなC言語のソースファイルを用意します。ここではファイル名を`clib.c`とします。ソースファイルには3つの単純な関数`getValue()`、`multiplyAndAdd()`、`sayHello()`が含まれています。

```{#lst:clib-c .c .numberLines startFrom="1" caption="C言語で記述されたライブラリ"}

/* clib.c */

#include <stdio.h>

int getValue()
{
    return 42;
}

int multiplyAndAdd(int a, int b, int c)
{
    return a * b + c;
}

void sayHello(const char* name)
{
    printf("Hello, %s!\n", name);
}


```

## Makefileの作成

以下のような`Makefile`を作成します。

```{#lst:makefile .makefile .numberLines startFrom="1" caption="Makefile"}

# Makefile

default: clib.c
	gcc -c -fPIC clib.c -o clib.o
	gcc -shared -Wl,-soname,libclib.so -o libclib.so clib.o


```

## ライブラリを利用するPythonプログラムの作成

以下のようなPythonのソースファイルを作成します。ここではファイル名を`clib.py`とします。Pythonの標準ライブラリ`ctypes`を利用して、C言語で作成した共有ライブラリを読み込み、ライブラリに含まれる関数の引数と戻り値の型を適切に指定します。これにより、Pythonから共有ライブラリの関数を呼び出すための準備が整います。

```{#lst:clib-py .py .numberLines startFrom="1" caption="ライブラリを呼ぶPythonのプログラム"}

# clib.py

import ctypes

def main():
    # C言語で作成した共有ライブラリを読み込み
    lib = ctypes.cdll.LoadLibrary("./libclib.so")

    # 共有ライブラリに用意された関数を呼び出し
    # 関数の引数の型と戻り値の型は必ず設定
    lib.getValue.argtypes = None
    lib.getValue.restype = ctypes.c_int
    print(lib.getValue())

    # 関数の引数の型と戻り値の型は必ず設定
    lib.multiplyAndAdd.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
    lib.multiplyAndAdd.restype = ctypes.c_int
    print("5 * 10 + 15 = {0}".format(lib.multiplyAndAdd(5, 10, 15)))

    # 関数の引数の型と戻り値の型は必ず設定
    lib.sayHello.argtypes = [ctypes.c_char_p]
    lib.sayHello.restype = None
    lib.sayHello(ctypes.c_char_p("World".encode("utf-8")))

if __name__ == "__main__":
    main()


```

## 共有ライブラリの作成とサンプルプログラムの実行

共有ライブラリを生成して、Pythonのサンプルプログラムを実行すると次のようになります。Python側から、C言語で作成された共有ライブラリの関数に、文字列や数値を問題なく渡せていることが分かります。

```

    # ファイルの確認
    $ ls
    Makefile  clib.c  clib.py

    # 共有ライブラリの生成
    $ make
    gcc -c -fPIC clib.c -o clib.o
    gcc -shared -Wl,-soname,libclib.so -o libclib.so clib.o

    # 生成されたファイルの確認
    $ ls
    Makefile  clib.c  clib.o  clib.py  libclib.so

    # サンプルプログラムの実行
    $ python3 clib.py
    42
    5 * 10 + 15 = 65
    Hello, World!


```
