
---
title:  練習用ページ
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css ./style.css ./sandbox.md > ./sandbox.html
-->

# このページについて

こちらは練習用ページです。

## リンク

- [ようこそ](./index.html)
- [Pandoc ユーザーズガイド 日本語版](http://sky-y.github.io/site-pandoc-jp/users-guide/)
- [まだ Word で消耗してるの? 大学のレポートを Markdown で書こう](https://qiita.com/Kumassy/items/5b6ae6b99df08fb434d9)
- [Pandoc用拡張Markdown記法の覚え書き](http://www.grkt.com/2013/01/14/1422)

## 数式

$$f(x) = ax^2 + bx + c$$ {#eq:sample1}
$$G(s) = \cfrac{\omega_n^2}{s^2 + 2 \zeta \omega_n s + \omega_n^2}$$ {#eq:sample2}
$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j \omega t} dt$$ {#eq:fourier}
$$Q(s_t, a_t) \leftarrow (1 - \eta) Q(s_t, a_t) + \eta (R_{t + 1} + \gamma Q(s_{t + 1}, a_{t + 1}))$$ {#eq:q-learning}

[@eq:sample2]は2次遅れ要素の伝達関数です。$\zeta$を減衰係数、$\omega_n$を固有角周波数といいます。
[@eq:fourier]はフーリエ変換の定義式です。[@eq:q-learning]はQ学習の式です。

## ソースコード

```{#lst:cpp-source .cpp .numberLines startFrom="1" caption="C++のソースコード"}
#include <iostream>
#include <cstdlib>

int main(int argc, char** argv)
{
    std::cout << "Hello, World" << std::endl;
    return EXIT_SUCCESS;
}
```

```{#lst:py-source .py .numberLines startFrom="1" caption="Pythonのソースコード"}
def main():
    print("Hello, World")

if __name__ == "__main__":
    main()
```

[@lst:cpp-source]はC++のソースコードです。
