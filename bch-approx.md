
---
title:  BCHの公式の一次近似
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css bch-approx.md > bch-approx.html
-->

[ホームに戻る](./index.html)

# このページについて

BCH (Baker-Campbell-Hausdorff)の公式の一次近似が、[こちらの論文](https://www.researchgate.net/publication/288975577)で証明されていたので、順に追ってみます。

## BCHの公式

ある行列$\mathbf{A}$、$\mathbf{B}$について、次のような関係が成り立つ。
この関係は、BCH (Baker-Campbell-Hausdorff)の公式とよばれている。

$$
  \begin{eqnarray}
    \ln(\exp(\mathbf{A}) \exp(\mathbf{B})) &=& \mathbf{A} + \mathbf{B}
      + \frac{1}{2} [\mathbf{A}, \mathbf{B}]
      + \frac{1}{12} [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} [\mathbf{B}, [\mathbf{A}, \mathbf{B}]]
      + \cdots
  \end{eqnarray}
$$

$\exp$は行列指数関数であり、次のように定義される。

$$
  \exp(\mathbf{A}) = \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
    + \frac{1}{3!} \mathbf{A}^3 + \cdots
    = \sum_{n = 0}^\infty \frac{\mathbf{A}^n}{n!}
$$

また、$[\mathbf{A}, \mathbf{B}]$はリー括弧積 (Lie bracket)であり、次のように定義される。

$$
  [\mathbf{A}, \mathbf{B}] = \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A}
$$

## BCHの公式の一次近似

上式において、$\mathbf{B}$に線形な項だけを考えると、以下の近似式が成り立つ。
[こちらの論文](https://iopscience.iop.org/article/10.1088/0305-4470/22/21/018)と、[こちらのテキスト](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)を参照。

$$
  \ln(\exp(\mathbf{A}) \exp(\mathbf{B}))
  \approx \mathbf{A} + \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
    \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_{n} \mathbf{B}] \cdots ]]]
$$

上式において、$B_n^-$はベルヌーイ数であり、次のように定義される。

$$
  B_0^- = 1, B_1^- = -\frac{1}{2}, B_2^- = \frac{1}{6},
  B_3^- = 0, B_4^- = -\frac{1}{30}, B_5^- = 0, \cdots
$$

これらは次のように、関数のテイラー展開の係数となっている。

$$
  \frac{z}{e^z - 1} = \sum_{n = 0}^\infty \frac{B_n^- z^n}{n!}
$$

[こちらの論文](https://www.researchgate.net/publication/288975577)では、上記の近似式が導出されており、それをいまから追ってみる。

## 下準備

最初に、スカラー$t$の関数$\mathbf{W}(t)$を考え、行列$\mathbf{A}$、$\mathbf{B}$について、次の関係が成り立っているとする。

$$
  \begin{eqnarray}
    \exp(\mathbf{W}(t)) &=& \exp(\mathbf{A}) \exp(t \mathbf{B}) \\
    \mathbf{W}(t) &=& \ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))
  \end{eqnarray}
$$

$\mathbf{W}(t)$は次のように、項$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$の総和として表されるとする。
$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$は、$\mathbf{A}$と$\mathbf{B}$を合計で$n$個含むような項を、まとめたものである。

$$
  \mathbf{W}(t) = \sum_{n = 0}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B})
$$

この定義から、次が得られる。

$$
  \begin{eqnarray}
    \exp(\mathbf{A}) \exp(t \mathbf{B})
    &=& \exp \left( \sum_{n = 0}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B}) \right) \\
    \ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))
    &=& \sum_{n = 0}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B})
  \end{eqnarray}
$$

ただし、行列の対数$\ln(\mathbf{X})$は以下のように定義される。

$$
  \ln(\mathbf{X}) = \left( \mathbf{X} - \mathbf{I} \right)
    - \frac{1}{2} \left( \mathbf{X} - \mathbf{I} \right)^2
    + \frac{1}{3} \left( \mathbf{X} - \mathbf{I} \right)^3 + \cdots
  = \sum_{n = 1}^{\infty} \frac{(-1)^{n - 1}}{n} \left( \mathbf{X} - \mathbf{I} \right)^n
$$

$\mathbf{X}$に$\exp(\mathbf{A}) \exp(\mathbf{B})$を代入して、$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$を計算してみると、次のようになる。

$$
  \begin{eqnarray}
    \mathbf{F}_0(\mathbf{A}, t \mathbf{B}) &=& \mathbf{0} \\
    \mathbf{F}_1(\mathbf{A}, t \mathbf{B}) &=& \mathbf{A} + t \mathbf{B} \\
    \mathbf{F}_2(\mathbf{A}, t \mathbf{B})
    &=& \frac{1}{2} t \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right)
    = \frac{1}{2} t [\mathbf{A}, \mathbf{B}] \\
    \mathbf{F}_3(\mathbf{A}, t \mathbf{B})
    &=& \frac{1}{12} t \left( \mathbf{A}^2 \mathbf{B} - 2 \mathbf{A} \mathbf{B} \mathbf{A}
      + t \mathbf{A} \mathbf{B}^2 + \mathbf{B} \mathbf{A}^2
      - 2 t \mathbf{B} \mathbf{A} \mathbf{B} + t \mathbf{B}^2 \mathbf{A} \right) \\
    &=& \frac{1}{12} t [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} t^2 [\mathbf{B}, [\mathbf{A}, \mathbf{B}]] \\
    \mathbf{F}_4(\mathbf{A}, t \mathbf{B})
    &=& \frac{1}{24} t^2 \left( \mathbf{A}^2 \mathbf{B}^2
      - 2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + 2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      - \mathbf{B}^2 \mathbf{A}^2 \right) \\
    &=& -\frac{1}{24} t^2 [\mathbf{B}, [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]]
  \end{eqnarray}
$$

この計算は非常に煩雑であるため、[こちらのページ](./bch-approx-supp.html)にまとめた。

$\mathbf{F}_0(\mathbf{A}, t \mathbf{B}) = \mathbf{0}$であったので、$\mathbf{W}_t$は結局、$\mathbf{F}_1(\mathbf{A}, t \mathbf{B})$以降の総和として書ける。

$$
  \mathbf{W}(t) = \sum_{n = 1}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B})
$$

## 導出 (その1)

最初に、$\mathbf{W}(0) = \mathbf{A}$であることを確認する($\exp(\mathbf{0}) = \mathbf{I}$)。

$$
  \mathbf{W}(0) = \ln(\exp(\mathbf{A}) \exp(\mathbf{0})) = \ln(\exp(\mathbf{A})) = \mathbf{A}
$$

続いて、$\mathbf{W}(t)$の$t = 0$における微分を考える。まず、

$$
  \left. \frac{d}{dt} \exp(\mathbf{W}(t)) \right|_{t = 0}
  = \left. \frac{d}{dt} \exp(\mathbf{A}) \exp(t \mathbf{B}) \right|_{t = 0}
  = \left. \exp(\mathbf{A}) \mathbf{B} \exp(t \mathbf{B}) \right|_{t = 0}
  = \exp(\mathbf{A}) \mathbf{B}
$$

ここで、$\cfrac{d}{dt} \exp(t \mathbf{X}) = \mathbf{X} \exp(t \mathbf{X})$の関係を用いた。また同時に、

$$
  \left. \frac{d}{dt} \exp(\mathbf{W}(t)) \right|_{t = 0}
  = \left. \sum_{n = 1}^\infty \frac{d}{dt} \mathbf{F}_n(\mathbf{A}, t \mathbf{B}) \right|_{t = 0}
$$

簡単のため、$t = 0$における微分を$D_0$として表す。

$$
  \left. \frac{d}{dt} \mathbf{F}_n(\mathbf{A}, t \mathbf{B}) \right|_{t = 0}
  = D_0(\mathbf{F}_n)
$$

試しに、上記の$\mathbf{F}_1(\mathbf{A}, t \mathbf{B})$、$\mathbf{F}_2(\mathbf{A}, t \mathbf{B})$、$\mathbf{F}_3(\mathbf{A}, t \mathbf{B})$、$\mathbf{F}_4(\mathbf{A}, t \mathbf{B})$を$t = 0$で微分してみると、次のようになる。

$$
  \begin{eqnarray}
    D_0(\mathbf{F}_1) &=& \left. \frac{d}{dt}
      \left( \mathbf{A} + t \mathbf{B} \right) \right|_{t = 0} = \mathbf{B} \\
    D_0(\mathbf{F}_2) &=& \left. \frac{d}{dt}
      \left( \frac{1}{2} t [\mathbf{A}, \mathbf{B}] \right) \right|_{t = 0}
    = \frac{1}{2} [\mathbf{A}, \mathbf{B}] \\
    D_0(\mathbf{F}_3) &=& \left. \frac{d}{dt}
      \left( \frac{1}{12} t [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} t^2 [\mathbf{B}, [\mathbf{A}, \mathbf{B}]] \right) \right|_{t = 0} \\
    &=& \left. \frac{1}{12} [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{6} t [\mathbf{B}, [\mathbf{A}, \mathbf{B}]] \right|_{t = 0}
      = \frac{1}{12} [\mathbf{A}, [\mathbf{A}, \mathbf{B}]] \\
    D_0(\mathbf{F}_4) &=& \left. \frac{d}{dt}
      \left( -\frac{1}{24} t^2 [\mathbf{B}, [\mathbf{A},
      [\mathbf{A}, \mathbf{B}]]] \right) \right|_{t = 0} \\
    &=& \left. -\frac{1}{12} t [\mathbf{B}, [\mathbf{A},
      [\mathbf{A}, \mathbf{B}]]] \right|_{t = 0} = 0
  \end{eqnarray}
$$

これらの結果から、$D_0(\mathbf{F}_n)$は、以下のような形をとることが推測される。

$$
  D_0(\mathbf{F}_n) \stackrel{?}{=} (-1)^{n - 1} \frac{B_{n - 1}^-}{(n - 1)!}
    \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_{n - 1} \mathbf{B}] \cdots ]]]
$$

$\mathbf{W}(t)$の一次近似に上記の推測を代入すると、$\mathbf{W}(t)$は以下のような形になる。

$$
  \begin{eqnarray}
    \mathbf{W}(t) &\approx& \mathbf{W}(0) + t \left. \frac{d}{dt} \mathbf{W}(t) \right|_{t = 0} \\
    &=& \mathbf{A} + t \left. \sum_{n = 1}^\infty \frac{d}{dt}
      \mathbf{F}_n(\mathbf{A}, t \mathbf{B}) \right|_{t = 0} \\
    &=& \mathbf{A} + t \sum_{n = 1}^\infty D_0(\mathbf{F}_n) \\
    &\stackrel{?}{=}& \mathbf{A} + t \sum_{n = 1}^\infty (-1)^{n - 1} \frac{B_{n - 1}^-}{(n - 1)!}
      \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_{n - 1} \mathbf{B}] \cdots ]]] \\
    &=& \mathbf{A} + t \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
      \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_n \mathbf{B}] \cdots ]]]
  \end{eqnarray}
$$

ここで$t = 1$とすれば、いま示そうとしている一次近似の式となる。

$$
  \ln(\exp(\mathbf{A}) \exp(\mathbf{B})) = \mathbf{W}(1)
  \stackrel{?}{\approx} \mathbf{A} + \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
    \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_{n} \mathbf{B}] \cdots ]]]
$$

従って、$D_0(\mathbf{F}_n)$に関する上記の予想が、正しいことを確かめればよい。
簡単のため、演算子$\mathrm{ad}_\mathbf{A}$を次のように定める。

$$
  \mathrm{ad}_\mathbf{A}(\mathbf{B}) = \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A}
  = [\mathbf{A}, \mathbf{B}]
$$

$(\mathrm{ad}_\mathbf{A})^2$、$(\mathrm{ad}_\mathbf{A})^3$は、次のことを意味する。

$$
  (\mathrm{ad}_\mathbf{A})^2(\mathbf{B}) = [\mathbf{A}, [\mathbf{A}, \mathbf{B}]], \quad
  (\mathrm{ad}_\mathbf{A})^3(\mathbf{B}) = [\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]]
$$

この$\mathrm{ad}_\mathbf{A}$を使うと、いま示そうとしているのは、次の式である。

$$
  D_0(\mathbf{F}_n) \stackrel{?}{=} (-1)^{n - 1} \frac{B_{n - 1}^-}{(n - 1)!}
    (\mathrm{ad}_\mathbf{A})^{n - 1}(\mathbf{B})
$$

## 導出 (その2)

以下の式を考える。

$$
  \exp(\mathbf{W}(t)) = \mathbf{I} + \mathbf{W}(t) + \frac{1}{2!} (\mathbf{W}(t))^2
  + \frac{1}{3!} (\mathbf{W}(t))^3 + \cdots
  = \sum_{n = 0}^\infty \frac{(\mathbf{W}(t))^n}{n!}
$$

上式の$t = 0$における微分は、

$$
  \begin{eqnarray}
    \left. \frac{d}{dt} \exp(\mathbf{W}(t)) \right|_{t = 0}
    &=& D_0(\mathbf{W}) + \frac{1}{2} \left( D_0(\mathbf{W}) \mathbf{A}
      + \mathbf{A} D_0(\mathbf{W}) \right) \\
    && + \frac{1}{3!} \left( D_0(\mathbf{W}) \mathbf{A}^2
      + \mathbf{A} D_0(\mathbf{W}) \mathbf{A}
      + \mathbf{A}^2 D_0(\mathbf{W}) \right) + \cdots \\
    &=& \exp(\mathbf{A}) \mathbf{B} \\
    &=& \left( \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
      + \frac{1}{3!} \mathbf{A}^3 + \cdots \right) \mathbf{B}
  \end{eqnarray}
$$

ただし、$D_0(\mathbf{W})$は次のように定義される。
また、$\mathbf{W}(0) = \mathbf{A}$である。

$$
  D_0(\mathbf{W}) = \left. \frac{d}{dt} \mathbf{W}(t) \right|_{t = 0}
$$

上記から、以下が成り立つことが予想される。

$$
  \begin{eqnarray}
    D_0(\mathbf{W}) &=& \left. \frac{d}{dt} \sum_{n = 1}^\infty
      \mathbf{F}_n(\mathbf{A}, t \mathbf{B}) \right|_{t = 0} \\
    &=& \sum_{n = 1}^\infty D_0(\mathbf{F}_n) \\
    &\stackrel{?}{=}& \sum_{n = 1}^\infty (-1)^{n - 1} \frac{B_{n - 1}^-}{(n - 1)!}
      (\mathrm{ad}_\mathbf{A})^{n - 1}(\mathbf{B}) \\
    &=& \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B})
  \end{eqnarray}
$$

この予想を代入してみると、

$$
  \begin{eqnarray}
    \left. \frac{d}{dt} \exp(\mathbf{W}(t)) \right|_{t = 0}
    &=& \left( \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
      + \frac{1}{3!} \mathbf{A}^3 + \cdots \right) \mathbf{B} \\
    &\stackrel{?}{=}& \sum_{n = 0}^\infty \frac{(-1)^n B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \\
    && + \frac{1}{2!} \left( \sum_{n = 0}^\infty \frac{(-1)^n B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \mathbf{A}
      + \mathbf{A} \sum_{n = 0}^\infty \frac{(-1)^n B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \right) \\
    && + \frac{1}{3!} \Bigg( \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \mathbf{A}^2
      + \mathbf{A} \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \mathbf{A} \\
    && \quad + \mathbf{A}^2 \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
      (\mathrm{ad}_\mathbf{A})^n(\mathbf{B}) \Bigg) + \cdots
  \end{eqnarray}
$$

上式から、$n$次の項、言い換えると、$\mathbf{A}$と$\mathbf{B}$を合計で$n$個含んでいる項を取り出す。
$(\mathrm{ad}_\mathbf{A})^n(\mathbf{B})$は、$n + 1$次の項となることに注意する。

$$
  \begin{eqnarray}
    && \frac{1}{(n - 1)!} \mathbf{A}^{n - 1} \mathbf{B} \\
    &\stackrel{?}{=}& \frac{(-1)^{n - 1} B_{n - 1}^-}{(n - 1)!}
      (\mathrm{ad}_\mathbf{A})^{n - 1}(\mathbf{B})
      + \frac{(-1)^{n - 2} B_{n - 2}^-}{2! (n - 2)!}
      \left( (\mathrm{ad}_\mathbf{A})^{n - 2}(\mathbf{B}) \mathbf{A}
      + \mathbf{A} (\mathrm{ad}_\mathbf{A})^{n - 2}(\mathbf{B}) \right) \\
    && + \frac{(-1)^{n - 3} B_{n - 3}^-}{3! (n - 3)!}
      \left( (\mathrm{ad}_\mathbf{A})^{n - 3}(\mathbf{B}) \mathbf{A}^2
      + \mathbf{A} (\mathrm{ad}_\mathbf{A})^{n - 3}(\mathbf{B}) \mathbf{A}
      + \mathbf{A}^2 (\mathrm{ad}_\mathbf{A})^{n - 3}(\mathbf{B}) \right) \\
    && + \cdots + \frac{B_0^-}{n!} \left(
      \underbrace{\mathbf{B} \mathbf{A}^{n - 1} + \mathbf{A} \mathbf{B} \mathbf{A}^{n - 2}
      + \cdots + \mathbf{A}^{n - 1} \mathbf{B}}_{n} \right)
  \end{eqnarray}
$$

この予想が、全ての$n$について成り立つことを示す。

以下の関係を使って、上式を書き直す。

$$
  (\mathrm{ad}_\mathbf{A})^n(\mathbf{B})
  = \sum_{k = 0}^n \frac{n!}{k! (n - k)!} (-1)^k \mathbf{A}^{n - k} \mathbf{B} \mathbf{A}^k
$$

上式は、$n = 0$のときは明らかに成立する。
$n = k$のときに成立すると仮定して、$n = k + 1$の場合を考えると

$$
  \begin{eqnarray}
    && (\mathrm{ad}_\mathbf{A})^{k + 1}(\mathbf{B}) \\
    &=& (\mathrm{ad}_\mathbf{A})((\mathrm{ad}_\mathbf{A})^k(\mathbf{B})) \\
    &=& (\mathrm{ad}_\mathbf{A})
      \left( \sum_{m = 0}^k \frac{k!}{m! (k - m)!} (-1)^m \mathbf{A}^{k - m}
      \mathbf{B} \mathbf{A}^m \right) \\
    &=& \sum_{m = 0}^k \frac{k!}{m! (k - m)!} (-1)^m \mathbf{A}^{k + 1 - m}
      \mathbf{B} \mathbf{A}^m
      + \sum_{m = 0}^k \frac{k!}{m! (k - m)!} (-1)^{m + 1} \mathbf{A}^{k - m}
      \mathbf{B} \mathbf{A}^{m + 1} \\
    &=& \sum_{m = 0}^k \frac{k!}{m! (k - m)!} (-1)^m \mathbf{A}^{k + 1 - m}
      \mathbf{B} \mathbf{A}^m
      + \sum_{m = 1}^{k + 1} \frac{k!}{(m - 1)! (k + 1 - m)!} (-1)^m \mathbf{A}^{k + 1 - m}
      \mathbf{B} \mathbf{A}^m \\
    &=& \sum_{m = 1}^k \left( \frac{k!}{m! (k - m)!} + \frac{k!}{(m - 1)! (k + 1 - m)!} \right)
      (-1)^m \mathbf{A}^{k + 1 - m} \mathbf{B} \mathbf{A}^m \\
    && \quad + \mathbf{A}^{k + 1} \mathbf{B}
      + (-1)^{k + 1} \mathbf{B} \mathbf{A}^{k + 1} \\
    &=& \sum_{m = 1}^k \frac{(k + 1)!}{m! (k + 1 - m)!}
      (-1)^m \mathbf{A}^{k + 1 - m} \mathbf{B} \mathbf{A}^m
      + \underbrace{\mathbf{A}^{k + 1} \mathbf{B}}_{m = 0}
      + \underbrace{(-1)^{k + 1} \mathbf{B} \mathbf{A}^{k + 1}}_{m = k + 1} \\
    &=& \sum_{m = 0}^{k + 1} \frac{(k + 1)!}{m! (k + 1 - m)!} (-1)^m \mathbf{A}^{k + 1 - m}
      \mathbf{B} \mathbf{A}^m
  \end{eqnarray}
$$

となるから、上の関係が正しいことがわかる(途中では二項定理の公式を用いている)。
これを使うと

$$
  \begin{eqnarray}
    && \frac{1}{(n - 1)!} \mathbf{A}^{n - 1} \mathbf{B} \\
    &\stackrel{?}{=}& \frac{(-1)^{n - 1} B_{n - 1}^-}{(n - 1)!}
      \sum_{k = 0}^{n - 1} \frac{(n - 1)!}{k! (n - 1 - k)!}
      (-1)^k \mathbf{A}^{n - 1 - k} \mathbf{B} \mathbf{A}^k \\
    && + \frac{(-1)^{n - 2} B_{n - 2}^-}{(n - 2)!}
      \sum_{k = 0}^{n - 2} \frac{(n - 2)!}{k! (n - 2 - k)!} (-1)^k
      \left( \mathbf{A}^{n - 2 - k} \mathbf{B} \mathbf{A}^{k + 1}
      + \mathbf{A}^{n - 1 - k} \mathbf{B} \mathbf{A}^k \right) \\
    && + \frac{(-1)^{n - 3} B_{n - 3}^-}{(n - 3)!}
      \sum_{k = 0}^{n - 3} \frac{(n - 3)!}{k! (n - 3 - k)!} (-1)^k
      \left( \mathbf{A}^{n - 3 - k} \mathbf{B} \mathbf{A}^{k + 2}
      + \mathbf{A}^{n - 2 - k} \mathbf{B} \mathbf{A}^{k + 1}
      + \mathbf{A}^{n - 1 - k} \mathbf{B} \mathbf{A}^k \right) \\
    && + \cdots + \frac{1}{n!} \left(
      \underbrace{\mathbf{B} \mathbf{A}^{n - 1} + \mathbf{A} \mathbf{B} \mathbf{A}^{n - 2}
      + \cdots + \mathbf{A}^{n - 1} \mathbf{B}}_{n} \right)
  \end{eqnarray}
$$

上記が全ての$n$について成り立つことを示せばよい。
そのため、[こちらの論文](https://www.researchgate.net/publication/288975577)では、シンボルというものを導入している。
上式をみると、どの項も、$s(\mathbf{A}^p \mathbf{B} \mathbf{A}^q)$の形をとることが分かる($p + q = n - 1$、$s$は適当な係数)。
そこで、項$\mathbf{A}^p \mathbf{B} \mathbf{A}^q$を、シンボル$t^q$で置き換える($t$は適当な係数)。

例えば、$1 = \mathbf{A}^{n - 1} \mathbf{B}$、$t = \mathbf{A}^{n - 2} \mathbf{B} \mathbf{A}$、$t^2 = \mathbf{A}^{n - 3} \mathbf{B} \mathbf{A}^2$のようになる。
シンボルと、元の項は、1対1で対応している。

シンボルについて、次の関係が成り立つ。

$$
  \begin{eqnarray}
    (\mathrm{ad}_\mathbf{A})^{n - 1}(\mathbf{B})
    &=& \sum_{k = 0}^{n - 1} \frac{(n - 1)!}{k! (n - 1 - k)!}
      (-1)^k \mathbf{A}^{n - 1 - k} \mathbf{B} \mathbf{A}^k \\
    &=& \sum_{k = 0}^{n - 1} \frac{(n - 1)!}{k! (n - 1 - k)!} (-t)^k \\
    &=& (1 - t)^{n - 1} \\
    (\mathrm{ad}_\mathbf{A})^{n - m - 1}(\mathbf{B}) \mathbf{A}^m
    &=& \sum_{k = 0}^{n - m - 1} \frac{(n - m - 1)!}{k! (n - m - 1 - k)!}
      (-1)^k \mathbf{A}^{n - m - 1 - k} \mathbf{B} \mathbf{A}^k \mathbf{A}^m \\
    &=& (1 - t)^{n - m - 1} t^m \\
    \mathbf{A}^m (\mathrm{ad}_\mathbf{A})^{n - m - 1}(\mathbf{B})
    &=& \mathbf{A}^m \sum_{k = 0}^{n - m - 1} \frac{(n - m - 1)!}{k! (n - m - 1 - k)!}
      (-1)^k \mathbf{A}^{n - m - 1 - k} \mathbf{B} \mathbf{A}^k \\
    &=& (1 - t)^{n - m - 1}
  \end{eqnarray}
$$

これらを使うと、先ほどの式は

$$
  \begin{eqnarray}
    && \frac{1}{(n - 1)!} \\
    &\stackrel{?}{=}& \frac{(-1)^{n - 1} B_{n - 1}^-}{(n - 1)!} (1 - t)^{n - 1}
      + \frac{(-1)^{n - 2} B_{n - 2}^-}{2! (n - 2)!}
      \left( (1 - t)^{n - 2} t + (1 - t)^{n - 2} \right) \\
    && + \frac{(-1)^{n - 3} B_{n - 3}^-}{3! (n - 3)!}
      \left( (1 - t)^{n - 3} t^2 + (1 - t)^{n - 3} t + (1 - t)^{n - 3} \right) \\
    && + \cdots + \frac{1}{n!} \left( t^{n - 1} + t^{n - 2} + \cdots + t + 1 \right) \\
    &=& \frac{(-1)^{n - 1} B_{n - 1}^-}{(n - 1)!} (1 - t)^{n - 1}
      + \frac{(-1)^{n - 2} B_{n - 2}^-}{2! (n - 2)!} (1 - t)^{n - 2} (1 + t) \\
    && + \frac{(-1)^{n - 3} B_{n - 3}^-}{3! (n - 3)!}
      (1 - t)^{n - 3} (1 + t + t^2) \\
    && + \cdots + \frac{1}{n!} (1 + t + t^2 + \cdots + t^{n - 1}) \\
    &=& \frac{(-1)^{n - 1} B_{n - 1}^-}{(n - 1)!} (1 - t)^{n - 1}
      + \frac{(-1)^{n - 2} B_{n - 2}^-}{2! (n - 2)!} (1 - t)^{n - 2} \frac{1 - t^2}{1 - t} \\
    && + \frac{(-1)^{n - 3} B_{n - 3}^-}{3! (n - 3)!}
      (1 - t)^{n - 3} \frac{1 - t^3}{1 - t}
      + \cdots + \frac{1}{n!} \frac{1 - t^n}{1 - t} \\
    &=& \sum_{k = 0}^{n - 1} \frac{(1 - t^{n - k})}{(1 - t) (n - k)!}
      \frac{B_k^- (-1)^k (1 - t)^k}{k!} \\
  \end{eqnarray}
$$

従って

$$
  \frac{1}{(n - 1)!} \stackrel{?}{=} \sum_{k = 0}^{n - 1}
    \frac{(1 - t^{n - k})}{(1 - t) (n - k)!} \frac{B_k^- (-1)^k (1 - t)^k}{k!}
$$

ここで、次の関数を考える。

$$
  \begin{eqnarray}
    P(z, t) &=& \sum_{k = 0}^\infty \frac{(1 - t^{k + 1}) z^k}{(1 - t) (k + 1)!} \\
    Q(z, t) &=& \sum_{n = 0}^\infty \frac{B_n^-}{n!} (-z(1 - t))^n \\
    R(z) &=& \sum_{n = 0}^\infty \frac{z^n}{n!} = e^z
  \end{eqnarray}
$$

$$
  \begin{eqnarray}
    P(z, t) Q(z, t) &=& \left( \sum_{k = 0}^\infty
      \underbrace{\frac{(1 - t^{k + 1})}{(1 - t) (k + 1)!}}_{\alpha_k} z^k \right)
      \left( \sum_{n = 0}^\infty \underbrace{\frac{B_n^-}{n!} (-1)^n (1 - t)^n}_{\beta_k} z^n \right) \\
    &=& \sum_{n = 0}^\infty \left( \sum_{k = 0}^n \alpha_k \beta_{n - k} \right) z^n \\
    &=& \sum_{n = 0}^\infty \left( \sum_{k = 0}^n \alpha_{n - k} \beta_k \right) z^n \\
    &=& \sum_{n = 0}^\infty \left( \sum_{k = 0}^n
      \frac{(1 - t^{n - k + 1})}{(1 - t) (n - k + 1)!}
      \frac{B_k^-}{k!} (-1)^k (1 - t)^k \right) z^n \\
    &=& \sum_{n = 1}^\infty \left( \sum_{k = 0}^{n - 1}
      \frac{(1 - t^{n - k})}{(1 - t) (n - k)!}
      \frac{B_k^-}{k!} (-1)^k (1 - t)^k \right) z^{n - 1}
  \end{eqnarray}
$$

また

$$
  \begin{eqnarray}
    R(z) = e^z = \sum_{n = 0}^\infty \frac{z^n}{n!}
    = \sum_{n = 1}^\infty \frac{z^{n - 1}}{(n - 1)!}
  \end{eqnarray}
$$

さて、$P(z, t)$は、次のようにも書ける。

$$
  \begin{eqnarray}
    P(z, t) &=& \sum_{k = 0}^\infty \frac{(1 - t^{k + 1}) z^k}{(1 - t) (k + 1)!} \\
    &=& \frac{1}{1 - t} \sum_{k = 1}^\infty \frac{(1 - t^k) z^{k - 1}}{k!} \\
    &=& \frac{1}{1 - t} \sum_{k = 1}^\infty \frac{(1 - t^k)}{k!} \frac{z^k}{z} \\
    &=& \frac{1}{1 - t} \sum_{k = 1}^\infty \frac{1}{k!} \frac{z^k - (tz)^k}{z} \\
    &=& \frac{1}{1 - t} \left( \frac{1}{z} \sum_{k = 0}^\infty \frac{z^k}{k!} - \frac{1}{z} \right)
      - \frac{1}{1 - t} \left( \frac{1}{z} \sum_{k = 0}^\infty \frac{(tz)^k}{k!} - \frac{1}{z} \right) \\
    &=& \frac{1}{1 - t} \left( \frac{e^z - 1}{z} - \frac{e^{tz} - 1}{z} \right) \\
    &=& \frac{e^z - e^{tz}}{(1 - t)z}
  \end{eqnarray}
$$

$Q(z, t)$は、ベルヌーイ数について$\sum_{n = 0}^\infty \cfrac{B_n^-}{n!} z^n = \cfrac{z}{e^z - 1}$であることを使えば、$z$を$-z(1 - t)$とみなすことにより

$$
  Q(z, t) = \sum_{n = 0}^\infty \frac{B_n^-}{n!} (-z (1 - t))^n \\
  = \frac{-z (1 - t)}{e^{-z(1 - t)} - 1}
$$

以上より、$P(z, t) Q(z, t)$は$R(z)$に等しいことが分かる。

$$
  \begin{eqnarray}
    P(z, t) Q(z, t) &=& \frac{e^z - e^{tz}}{(1 - t)z} \frac{-z(1 - t)}{e^{-z(1 - t)} - 1} \\
    &=& \frac{e^z - e^{tz}}{1 - e^{-z(1 - t)}} \\
    &=& \frac{e^z - e^{tz}}{e^z - e^{tz}} e^z \\
    &=& e^z = R(z)
  \end{eqnarray}
$$

$R(z) = P(z, t) Q(z, t)$であるから、両辺をテイラー展開したとき、全ての$n \ge 0$について、$z^n$の係数も等しい。
これは、全ての$n \ge 1$について、次が成り立つことを意味する($z^{n - 1}$の項に着目する)。

$$
  \frac{1}{(n - 1)!} = \sum_{k = 0}^{n - 1}
    \frac{(1 - t^{n - k})}{(1 - t) (n - k)!} \frac{B_k^- (-1)^k (1 - t)^k}{k!}
$$

従って、当初の仮定は正しかったことになる。

$$
  D_0(\mathbf{F}_n) = (-1)^{n - 1} \frac{B_{n - 1}^-}{(n - 1)!}
    (\mathrm{ad}_\mathbf{A})^{n - 1}(\mathbf{B})
$$

これより、BCHの公式の一次近似について、以下が成り立つことが示せた。

$$
  \ln(\exp(\mathbf{A}) \exp(\mathbf{B})) = \mathbf{W}(1)
  \approx \mathbf{A} + \sum_{n = 0}^\infty (-1)^n \frac{B_n^-}{n!}
    \underbrace{[\mathbf{A}, [\mathbf{A}, [\mathbf{A}, \cdots, [\mathbf{A},}_{n} \mathbf{B}] \cdots ]]]
$$

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM: From Theory to Practice](https://github.com/gaoxiang12/slambook-en)
- [The Campbell-Baker-Hausdorff formula](https://www.researchgate.net/publication/288975577)
- [The Baker-Campbell-Hausdorff formula and the convergence of the Magnus expansion](https://iopscience.iop.org/article/10.1088/0305-4470/22/21/018)

