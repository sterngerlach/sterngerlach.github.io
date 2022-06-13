
---
title:  BCHの公式の一次近似 (補足)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css bch-approx-supp.md > bch-approx-supp.html
-->

[ホームに戻る](./index.html)

# このページについて

[こちらのメモ](./bch-approx.html)の補足です。
おまけとして、BCH (Baker-Campbell-Hausdorff) の公式の最初の部分を示します。

## 準備

行列$\mathbf{A}$、$\mathbf{B}$があるとする。
$\exp(\mathbf{A})$は行列指数関数であり、次のように定義される。

$$
  \exp(\mathbf{A}) = \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
    + \frac{1}{3!} \mathbf{A}^3 + \cdots
    = \sum_{n = 0}^\infty \frac{\mathbf{A}^n}{n!}
$$

また、$[\mathbf{A}, \mathbf{B}]$はリー括弧積 (Lie bracket)であり、次のように定義される。

$$
  [\mathbf{A}, \mathbf{B}] = \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A}
$$

スカラー$t$の関数$\mathbf{W}(t)$があり、以下の関係が成り立つとする。

$$
  \exp(\mathbf{W}(t)) = \exp(\mathbf{A}) \exp(t \mathbf{B})
  \quad \Longrightarrow \quad
  \mathbf{W}(t) = \ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))
$$

$\mathbf{W}(t)$は次のように、項$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$の総和として表されるとする。
$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$は、$\mathbf{A}$と$\mathbf{B}$を合計で$n$個含むような項を、まとめたものである。

$$
  \mathbf{W}(t) = \sum_{n = 0}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B})
$$

ただし、行列の対数$\ln(\mathbf{X})$は以下のように定義される。

$$
  \ln(\mathbf{X}) = \left( \mathbf{X} - \mathbf{I} \right)
    - \frac{1}{2} \left( \mathbf{X} - \mathbf{I} \right)^2
    + \frac{1}{3} \left( \mathbf{X} - \mathbf{I} \right)^3 + \cdots
  = \sum_{n = 1}^{\infty} \frac{(-1)^{n - 1}}{n} \left( \mathbf{X} - \mathbf{I} \right)^n
$$

よって

$$
  \begin{eqnarray}
    \mathbf{W}(t) &=& \ln(\exp(\mathbf{A}) \exp(t \mathbf{B})) \\
    &=& \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right) \\
    && - \frac{1}{2} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^2 \\
    && + \frac{1}{3} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3 \\
    && - \frac{1}{4} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4 + \cdots
  \end{eqnarray}
$$

以下では、最初に$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)$から$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4$までを計算する。
続いて、$\ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))$から4次までの項($\mathbf{A}$と$\mathbf{B}$を最大4つまで含む項)を取り出して、$\mathbf{F}_0(\mathbf{A}, t \mathbf{B})$から$\mathbf{F}_4(\mathbf{A}, t \mathbf{B})$までを実際に計算する。

## $\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)$の計算

$\exp(\mathbf{A}) \exp(t \mathbf{B})$は、4次の項まで展開すれば次のようになる。

$$
  \begin{eqnarray}
    \exp(\mathbf{A}) \exp(t \mathbf{B})
    &=& \left( \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
      + \frac{1}{3!} \mathbf{A}^3 + \frac{1}{4!} \mathbf{A}^4 + \cdots \right) \\
    && \left( \mathbf{I} + t \mathbf{B} + \frac{1}{2!} t^2 \mathbf{B}^2
      + \frac{1}{3!} t^3 \mathbf{B}^3 + \frac{1}{4!} t^4 \mathbf{B}^4 + \cdots \right) \\
    &=& \mathbf{I} + \mathbf{A} + \frac{1}{2} \mathbf{A}^2
      + \frac{1}{6} \mathbf{A}^3 + \frac{1}{24} \mathbf{A}^4 \\
    && + t \mathbf{B} + t \mathbf{A} \mathbf{B} + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{6} t \mathbf{A}^3 \mathbf{B} \\
    && + \frac{1}{2} t^2 \mathbf{B}^2 + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{4} t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && + \frac{1}{6} t^3 \mathbf{B}^3 + \frac{1}{6} t^3 \mathbf{A} \mathbf{B}^3 \\
    && + \frac{1}{24} t^4 \mathbf{B}^4 + \cdots
  \end{eqnarray}
$$

従って、$\exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I}$は、次のようになる。

$$
  \begin{eqnarray}
    \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I}
    &=& \mathbf{A} + \frac{1}{2} \mathbf{A}^2
      + \frac{1}{6} \mathbf{A}^3 + \frac{1}{24} \mathbf{A}^4 \\
    && + t \mathbf{B} + t \mathbf{A} \mathbf{B} + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{6} t \mathbf{A}^3 \mathbf{B} \\
    && + \frac{1}{2} t^2 \mathbf{B}^2 + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{4} t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && + \frac{1}{6} t^3 \mathbf{B}^3 + \frac{1}{6} t^3 \mathbf{A} \mathbf{B}^3 \\
    && + \frac{1}{24} t^4 \mathbf{B}^4 + \cdots \\
    &=& \mathbf{A} + t \mathbf{B} \\
    && + \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \\
    && + \frac{1}{6} \mathbf{A}^3 + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{B}^3 \\
    && + \frac{1}{24} \mathbf{A}^4 + \frac{1}{6} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{4} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{A} \mathbf{B}^3
      + \frac{1}{24} t^4 \mathbf{B}^4 + \cdots \\
    &=& \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots
  \end{eqnarray}
$$

$\mathbf{U}_{11}$、$\mathbf{U}_{12}$、$\mathbf{U}_{13}$、$\mathbf{U}_{14}$はそれぞれ、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)$の1次、2次、3次、4次の項である。

## $\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^2$の計算

$(\exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I})^2$は、以下のように求められる(4次の項まで)。

$$
  \begin{eqnarray}
    && (\exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I})^2 \\
    &=& \left( \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots \right)
      \left( \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots \right) \\
    &=& \mathbf{U}_{11}^2
      + \left( \mathbf{U}_{11} \mathbf{U}_{12} + \mathbf{U}_{12} \mathbf{U}_{11} \right)
      + \left( \mathbf{U}_{11} \mathbf{U}_{13}
        + \mathbf{U}_{12}^2 + \mathbf{U}_{13} \mathbf{U}_{11} \right) + \cdots \\
    &=& \left( \mathbf{A} + t \mathbf{B} \right) \left( \mathbf{A} + t \mathbf{B} \right) \\
    && + \Bigg\{ \left( \mathbf{A} + t \mathbf{B} \right)
      \left( \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \right) \\
    && + \left( \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \right)
      \left( \mathbf{A} + t \mathbf{B} \right) \Bigg\} \\
    && + \Bigg\{ \left( \mathbf{A} + t \mathbf{B} \right)
      \left( \frac{1}{6} \mathbf{A}^3
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{B}^3 \right) \\
    && + \left( \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \right)
      \left( \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \right) \\
    && + \left( \frac{1}{6} \mathbf{A}^3
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{B}^3 \right)
      \left( \mathbf{A} + t \mathbf{B} \right) \Bigg\} + \cdots
  \end{eqnarray}
$$

これを順に計算すれば
$$
  \begin{eqnarray}
    && (\exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I})^2 \\
    &=& \left( \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + t \mathbf{B} \mathbf{A} + t^2 \mathbf{B}^2 \right) \\
    && + \Bigg\{ \left( \frac{1}{2} \mathbf{A}^3 + t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{2} t \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^3 \mathbf{B}^3 \right) \\
    && \quad + \left( \frac{1}{2} \mathbf{A}^3
      + t \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A}
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{2} t^3 \mathbf{B}^3 \right) \Bigg\} \\
    && + \Bigg\{ \Bigg( \frac{1}{6} \mathbf{A}^4
      + \frac{1}{2} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{A} \mathbf{B}^3 \\
    && \qquad + \frac{1}{6} t \mathbf{B} \mathbf{A}^3
      + \frac{1}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2
      + \frac{1}{6} t^4 \mathbf{B}^4 \Bigg) \\
    && \quad + \Bigg( \frac{1}{4} \mathbf{A}^4
      + \frac{1}{2} t \mathbf{A}^3 \mathbf{B} + \frac{1}{4} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^3 \mathbf{A} \mathbf{B}^3 \\
    && \qquad + \frac{1}{4} t^2 \mathbf{B}^2 \mathbf{A}^2
      + \frac{1}{2} t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + \frac{1}{4} t^4 \mathbf{B}^4 \Bigg) \\
    && \quad + \Bigg( \frac{1}{6} \mathbf{A}^4
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + \frac{1}{6} t^3 \mathbf{B}^3 \mathbf{A} \\
    && \qquad + \frac{1}{6} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{2} t^3 \mathbf{A} \mathbf{B}^3
      + \frac{1}{6} t^4 \mathbf{B}^4 \Bigg) \Bigg\} + \cdots
  \end{eqnarray}
$$

項をまとめて

$$
  \begin{eqnarray}
    && (\exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I})^2 \\
    &=& \left( \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + t \mathbf{B} \mathbf{A} + t^2 \mathbf{B}^2 \right) \\
    && + \Bigg\{ \mathbf{A}^3 + \frac{3}{2} t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \\
    && \quad + \frac{1}{2} t \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A} 
      + t^3 \mathbf{B}^3 \Bigg\} \\
    && + \Bigg\{
      \frac{7}{12} \mathbf{A}^4
      + \frac{7}{6} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + \frac{5}{4} t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && \quad + \frac{1}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + \frac{7}{6} t^3 \mathbf{A} \mathbf{B}^3 \\
    && \quad + \frac{1}{6} t \mathbf{B} \mathbf{A}^3
      + \frac{1}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && \quad + \frac{1}{4} t^2 \mathbf{B}^2 \mathbf{A}^2
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + \frac{1}{6} t^3 \mathbf{B}^3 \mathbf{A}
      + \frac{7}{12} t^4 \mathbf{B}^4 \Bigg\} + \cdots \\
    &=& \mathbf{U}_{22} + \mathbf{U}_{23} + \mathbf{U}_{24} + \cdots
  \end{eqnarray}
$$

$\mathbf{U}_{22}$、$\mathbf{U}_{23}$、$\mathbf{U}_{24}$はそれぞれ、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^2$の2次、3次、4次の項である。

## $\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3$の計算

続いて、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3$は、以下のようになる(4次の項まで)。

$$
  \begin{eqnarray}
    && \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3 \\
    &=& \left( \mathbf{U}_{22} + \mathbf{U}_{23} + \mathbf{U}_{24} + \cdots \right)
      \left( \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots \right) \\
    &=& \mathbf{U}_{22} \mathbf{U}_{11}
      + \left( \mathbf{U}_{22} \mathbf{U}_{12} + \mathbf{U}_{23} \mathbf{U}_{11} \right) + \cdots \\
    &=& \left( \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + t \mathbf{B} \mathbf{A} + t^2 \mathbf{B}^2 \right)
      \left( \mathbf{A} + t \mathbf{B} \right) \\
    && + \Bigg\{ \left( \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + t \mathbf{B} \mathbf{A} + t^2 \mathbf{B}^2 \right)
      \left( \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B} + \frac{1}{2} t^2 \mathbf{B}^2 \right) \\
    && \quad + \Bigg( \mathbf{A}^3 + \frac{3}{2} t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \\
    && \qquad + \frac{1}{2} t \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A}
      + t^3 \mathbf{B}^3 \Bigg)
      \left( \mathbf{A} + t \mathbf{B} \right) \Bigg\} + \cdots
  \end{eqnarray}
$$

これを順に計算すれば

$$
  \begin{eqnarray}
    && \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3 \\
    &=& \left( \mathbf{A}^3 + t \mathbf{A} \mathbf{B} \mathbf{A}
      + t \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{B}^2 \mathbf{A}
      + t \mathbf{A}^2 \mathbf{B} + t^2 \mathbf{A} \mathbf{B}^2
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} + t^3 \mathbf{B}^3 \right) \\
    && + \Bigg\{ \frac{1}{2} \mathbf{A}^4
      + \frac{1}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + \frac{1}{2} t \mathbf{B} \mathbf{A}^3
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A}^2 \\
    && \quad + t \mathbf{A}^3 \mathbf{B}
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B} \\
    && \quad + \frac{1}{2} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{2} t^3 \mathbf{A} \mathbf{B}^3
      + \frac{1}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2
      + \frac{1}{2} t^4 \mathbf{B}^4 \\
    && \quad + \mathbf{A}^4 + \frac{3}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A} \\
    && \quad + \frac{1}{2} t \mathbf{B} \mathbf{A}^3
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A}^2
      + t^3 \mathbf{B}^3 \mathbf{A} \\
    && \quad + t \mathbf{A}^3 \mathbf{B}
      + \frac{3}{2} t^2 \mathbf{A}^2 \mathbf{B}^2
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{3}{2} t^3 \mathbf{A} \mathbf{B}^3 \\
    && \quad + \frac{1}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2
      + \frac{1}{2} t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + t^4 \mathbf{B}^4 \Bigg\} + \cdots
  \end{eqnarray}
$$

項をまとめて

$$
  \begin{eqnarray}
    && \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3 \\
    &=& \left( \mathbf{A}^3 + t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A} + t^2 \mathbf{A} \mathbf{B}^2
      + t \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{B}^2 \mathbf{A} + t^3 \mathbf{B}^3 \right) \\
    && + \Bigg\{ \frac{3}{2} \mathbf{A}^4 + 2 t \mathbf{A}^3 \mathbf{B}
      + \frac{3}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + 2 t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && \quad + \frac{3}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + 2 t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + 2 t^3 \mathbf{A} \mathbf{B}^3 \\
    && \quad + t \mathbf{B} \mathbf{A}^3
      + \frac{3}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{3}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && \quad + t^2 \mathbf{B}^2 \mathbf{A}^2
      + \frac{3}{2} t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + t^3 \mathbf{B}^3 \mathbf{A}
      + \frac{3}{2} t^4 \mathbf{B}^4 \Bigg\} + \cdots \\
    &=& \mathbf{U}_{33} + \mathbf{U}_{34} + \cdots
  \end{eqnarray}
$$

$\mathbf{U}_{33}$、$\mathbf{U}_{34}$はそれぞれ、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3$の3次、4次の項である。

## $\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4$の計算

最後に、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4$は、以下のようになる(4次の項まで)。

$$
  \begin{eqnarray}
    && \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4 \\
    &=& \left( \mathbf{U}_{33} + \mathbf{U}_{34} + \cdots \right)
      \left( \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots \right) \\
    &=& \mathbf{U}_{33} \mathbf{U}_{11} + \cdots \\
    &=& \big( \mathbf{A}^3 + t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A} + t^2 \mathbf{A} \mathbf{B}^2 \\
    && \quad + t \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{B}^2 \mathbf{A} + t^3 \mathbf{B}^3 \big)
      \left( \mathbf{A} + t \mathbf{B} \right) + \cdots \\
    &=& \big( \mathbf{A}^4 + t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + t \mathbf{A} \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A} \\
    && \quad + t \mathbf{B} \mathbf{A}^3 + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + t^2 \mathbf{B}^2 \mathbf{A}^2 + t^3 \mathbf{B}^3 \mathbf{A} \big) \\
    && + \big( t \mathbf{A}^3 \mathbf{B} + t^2 \mathbf{A}^2 \mathbf{B}^2
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B} + t^3 \mathbf{A} \mathbf{B}^3 \\
    && \quad + t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B} + t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2
      + t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B} + t^4 \mathbf{B}^4 \big) + \cdots \\
    &=& \mathbf{A}^4 + t \mathbf{A}^3 \mathbf{B}
      + t \mathbf{A}^2 \mathbf{B} \mathbf{A} + t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && + t \mathbf{A} \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A} + t^3 \mathbf{A} \mathbf{B}^3 \\
    && + t \mathbf{B} \mathbf{A}^3 + t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && + t^2 \mathbf{B}^2 \mathbf{A}^2 + t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + t^3 \mathbf{B}^3 \mathbf{A} + t^4 \mathbf{B}^4 + \cdots \\
    &=& \mathbf{U}_{44} + \cdots
  \end{eqnarray}
$$

$\mathbf{U}_{44}$はそれぞれ、$\left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4$の4次の項である。

## $\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$の計算 ($0 \le n \le 2$)

これらを$\ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))$に代入する。

$$
  \begin{eqnarray}
    \ln(\exp(\mathbf{A}) \exp(t \mathbf{B}))
    &=& \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right) \\
    && \quad - \frac{1}{2} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^2 \\
    && \quad + \frac{1}{3} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^3 \\
    && \quad - \frac{1}{4} \left( \exp(\mathbf{A}) \exp(t \mathbf{B}) - \mathbf{I} \right)^4 + \cdots \\
    &=& \left( \mathbf{U}_{11} + \mathbf{U}_{12} + \mathbf{U}_{13} + \mathbf{U}_{14} + \cdots \right) \\
    && \quad - \frac{1}{2} \left( \mathbf{U}_{22} + \mathbf{U}_{23} + \mathbf{U}_{24} + \cdots \right) \\
    && \quad - \frac{1}{3} \left( \mathbf{U}_{33} + \mathbf{U}_{34} + \cdots \right) \\
    && \quad - \frac{1}{4} \left( \mathbf{U}_{44} + \cdots \right) + \cdots \\
    &=& \sum_{n = 0}^\infty \mathbf{F}_n(\mathbf{A}, t \mathbf{B})
  \end{eqnarray}
$$

0次から4次までの項を順に取り出して、$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$を計算すると、次のようになる。

$$
  \mathbf{F}_0(\mathbf{A}, t \mathbf{B}) = 0
$$

$$
  \mathbf{F}_1(\mathbf{A}, t \mathbf{B})
  = \mathbf{U}_{11} = \mathbf{A} + t \mathbf{B}
$$

$$
  \begin{eqnarray}
    \mathbf{F}_2(\mathbf{A}, t \mathbf{B})
    &=& \mathbf{U}_{12} - \frac{1}{2} \mathbf{U}_{22} \\
    &=& \frac{1}{2} \mathbf{A}^2 + t \mathbf{A} \mathbf{B} + \frac{1}{2} t^2 \mathbf{B}^2
      - \frac{1}{2} \left( \mathbf{A}^2 + t \mathbf{A} \mathbf{B}
      + t \mathbf{B} \mathbf{A} + t^2 \mathbf{B}^2 \right) \\
    &=& \frac{1}{2} t \mathbf{A} \mathbf{B} - \frac{1}{2} t \mathbf{B} \mathbf{A} \\
    &=& \frac{1}{2} t \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right) \\
    &=& \frac{1}{2} t [\mathbf{A}, \mathbf{B}]
  \end{eqnarray}
$$

## $\mathbf{F}_3(\mathbf{A}, t \mathbf{B})$の計算

$$
  \begin{eqnarray}
    && \mathbf{F}_3(\mathbf{A}, t \mathbf{B}) \\
    &=& \mathbf{U}_{13} - \frac{1}{2} \mathbf{U}_{23} + \frac{1}{3} \mathbf{U}_{33} \\
    &=& \left( \frac{1}{6} \mathbf{A}^3 + \frac{1}{2} t \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{B}^3 \right) \\
    && - \frac{1}{2} \Bigg( \mathbf{A}^3 + \frac{3}{2} t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \\
    && \quad + \frac{1}{2} t \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A} 
      + t^3 \mathbf{B}^3 \Bigg) \\
    && + \frac{1}{3} \big( \mathbf{A}^3 + t \mathbf{A}^2 \mathbf{B}
      + t \mathbf{A} \mathbf{B} \mathbf{A} + t^2 \mathbf{A} \mathbf{B}^2 \\
    && \quad + t \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{B}^2 \mathbf{A} + t^3 \mathbf{B}^3 \big)
  \end{eqnarray}
$$

項をまとめて

$$
  \begin{eqnarray}
    && \mathbf{F}_3(\mathbf{A}, t \mathbf{B}) \\
    &=& \left( \frac{1}{6} - \frac{1}{2} + \frac{1}{3} \right) \mathbf{A}^3
      + t \left( \frac{1}{2} - \frac{3}{4} + \frac{1}{3} \right) \mathbf{A}^2 \mathbf{B} \\
    && + t \left( -\frac{1}{2} + \frac{1}{3} \right) \mathbf{A} \mathbf{B} \mathbf{A}
      + t^2 \left( \frac{1}{2} - \frac{3}{4} + \frac{1}{3} \right) \mathbf{A} \mathbf{B}^2 \\
    && + t \left( -\frac{1}{4} + \frac{1}{3} \right) \mathbf{B} \mathbf{A}^2
      + t^2 \left( -\frac{1}{2} + \frac{1}{3} \right) \mathbf{B} \mathbf{A} \mathbf{B} \\
    && + t^2 \left( -\frac{1}{4} + \frac{1}{3} \right) \mathbf{B}^2 \mathbf{A}
      + t^3 \left( \frac{1}{6} - \frac{1}{2} + \frac{1}{3} \right) \mathbf{B}^3 \\
    &=& \frac{1}{12} t \left( \mathbf{A}^2 \mathbf{B} - 2 \mathbf{A} \mathbf{B} \mathbf{A}
      + t \mathbf{A} \mathbf{B}^2 + \mathbf{B} \mathbf{A}^2
      - 2 t \mathbf{B} \mathbf{A} \mathbf{B} + t \mathbf{B}^2 \mathbf{A} \right) \\
    &=& \frac{1}{12} t \big( \left( \mathbf{A}
      \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right)
      - \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right) \mathbf{A} \right) \\
    && \quad - \left( t \mathbf{B} \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right)
      - \left( \mathbf{A} \mathbf{B} - \mathbf{B} \mathbf{A} \right) t \mathbf{B} \right) \big) \\
    &=& \frac{1}{12} [\mathbf{A}, [\mathbf{A}, t \mathbf{B}]]
      - \frac{1}{12} [t \mathbf{B}, [\mathbf{A}, t \mathbf{B}]] \\
    &=& \frac{1}{12} t [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} t^2 [\mathbf{B}, [\mathbf{A}, \mathbf{B}]]
  \end{eqnarray}
$$

## $\mathbf{F}_4(\mathbf{A}, t \mathbf{B})$の計算

$$
  \begin{eqnarray}
    && \mathbf{F}_4(\mathbf{A}, t \mathbf{B}) \\
    &=& \mathbf{U}_{14} - \frac{1}{2} \mathbf{U}_{24}
      + \frac{1}{3} \mathbf{U}_{34} - \frac{1}{4} \mathbf{U}_{44} \\
    &=& \left( \frac{1}{24} \mathbf{A}^4 + \frac{1}{6} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{4} t^2 \mathbf{A}^2 \mathbf{B}^2
      + \frac{1}{6} t^3 \mathbf{A} \mathbf{B}^3
      + \frac{1}{24} t^4 \mathbf{B}^4 \right) \\
    && \quad - \frac{1}{2} \Bigg\{
      \frac{7}{12} \mathbf{A}^4
      + \frac{7}{6} t \mathbf{A}^3 \mathbf{B}
      + \frac{1}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + \frac{5}{4} t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && \qquad + \frac{1}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{1}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + \frac{7}{6} t^3 \mathbf{A} \mathbf{B}^3 \\
    && \qquad + \frac{1}{6} t \mathbf{B} \mathbf{A}^3
      + \frac{1}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + \frac{1}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && \qquad + \frac{1}{4} t^2 \mathbf{B}^2 \mathbf{A}^2
      + \frac{1}{2} t^2 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + \frac{1}{6} t^3 \mathbf{B}^3 \mathbf{A}
      + \frac{7}{12} t^4 \mathbf{B}^4 \Bigg\} \\
    && \quad + \frac{1}{3} \Bigg\{ \frac{3}{2} \mathbf{A}^4
      + 2 t \mathbf{A}^3 \mathbf{B}
      + \frac{3}{2} t \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + 2 t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && \qquad + \frac{3}{2} t \mathbf{A} \mathbf{B} \mathbf{A}^2
      + 2 t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + \frac{3}{2} t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + 2 t^3 \mathbf{A} \mathbf{B}^3 \\
    && \qquad + t \mathbf{B} \mathbf{A}^3
      + \frac{3}{2} t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + \frac{3}{2} t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && \qquad + t^2 \mathbf{B}^2 \mathbf{A}^2
      + \frac{3}{2} t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + t^3 \mathbf{B}^3 \mathbf{A}
      + \frac{3}{2} t^4 \mathbf{B}^4 \Bigg\} \\
    && \quad - \frac{1}{4} \Bigg\{ \mathbf{A}^4 + t \mathbf{A}^3 \mathbf{B}
      + t \mathbf{A}^2 \mathbf{B} \mathbf{A} + t^2 \mathbf{A}^2 \mathbf{B}^2 \\
    && \qquad + t \mathbf{A} \mathbf{B} \mathbf{A}^2 + t^2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + t^2 \mathbf{A} \mathbf{B}^2 \mathbf{A} + t^3 \mathbf{A} \mathbf{B}^3 \\
    && \qquad + t \mathbf{B} \mathbf{A}^3 + t^2 \mathbf{B} \mathbf{A}^2 \mathbf{B}
      + t^2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A} \\
    && \qquad + t^3 \mathbf{B} \mathbf{A} \mathbf{B}^2
      + t^2 \mathbf{B}^2 \mathbf{A}^2 + t^3 \mathbf{B}^2 \mathbf{A} \mathbf{B}
      + t^3 \mathbf{B}^3 \mathbf{A} + t^4 \mathbf{B}^4 \Bigg\}
  \end{eqnarray}
$$

これほど長大な足し算は人生で初めてかもしれない。
項をまとめて

$$
  \begin{eqnarray}
    && \mathbf{F}_4(\mathbf{A}, t \mathbf{B}) \\
    &=& \left( \frac{1}{24} - \frac{7}{24} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{A}^4
      + t \left( \frac{1}{6} - \frac{7}{12} + \frac{2}{3} - \frac{1}{4} \right) \mathbf{A}^3 \mathbf{B} \\
    && \quad + t \left( -\frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{A}^2 \mathbf{B} \mathbf{A}
      + t^2 \left( \frac{1}{4} - \frac{5}{8} + \frac{2}{3} - \frac{1}{4} \right) \mathbf{A}^2 \mathbf{B}^2 \\
    && \quad + t \left( -\frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{A} \mathbf{B} \mathbf{A}^2
      + t^2 \left( -\frac{1}{2} + \frac{2}{3} - \frac{1}{4} \right) \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B} \\
    && \quad + t^2 \left( -\frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{A} \mathbf{B}^2 \mathbf{A}
      + t^3 \left( \frac{1}{6} - \frac{7}{12} + \frac{2}{3} - \frac{1}{4} \right) \mathbf{A} \mathbf{B}^3 \\
    && \quad + t \left( -\frac{1}{12} + \frac{1}{3} - \frac{1}{4} \right) \mathbf{B} \mathbf{A}^3
      + t^2 \left( -\frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{B} \mathbf{A}^2 \mathbf{B} \\
    && \quad + t^2 \left( \frac{1}{3} - \frac{1}{4} \right) \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + t^3 \left( -\frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{B} \mathbf{A} \mathbf{B}^2 \\
    && \quad + t^2 \left( -\frac{1}{8} + \frac{1}{3} - \frac{1}{4} \right) \mathbf{B}^2 \mathbf{A}^2
      + t^3 \left( \frac{1}{4} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{B}^2 \mathbf{A} \mathbf{B} \\
    && \quad + t^3 \left( -\frac{1}{12} + \frac{1}{3} - \frac{1}{4} \right) \mathbf{B}^3 \mathbf{A}
      + t^4 \left( \frac{1}{24} - \frac{7}{24} + \frac{1}{2} - \frac{1}{4} \right) \mathbf{B}^4 \\
    &=& \frac{1}{24} t^2 \left( \mathbf{A}^2 \mathbf{B}^2
      - 2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      + 2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      - \mathbf{B}^2 \mathbf{A}^2 \right)
  \end{eqnarray}
$$

これを次のように整理すれば

$$
  \begin{eqnarray}
    && \mathbf{F}_4(\mathbf{A}, t \mathbf{B}) \\
    &=& -\frac{1}{24} t^2 \left( \mathbf{B} \mathbf{A}^2 \mathbf{B}
      - 2 \mathbf{B} \mathbf{A} \mathbf{B} \mathbf{A}
      + \mathbf{B}^2 \mathbf{A}^2 - \mathbf{A}^2 \mathbf{B}^2
      + 2 \mathbf{A} \mathbf{B} \mathbf{A} \mathbf{B}
      - \mathbf{B} \mathbf{A}^2 \mathbf{B} \right) \\
    &=& -\frac{1}{24} t^2 \left( \mathbf{B} \left( \mathbf{A}^2 \mathbf{B}
      - 2 \mathbf{A} \mathbf{B} \mathbf{A} + \mathbf{B} \mathbf{A}^2 \right)
      - \left( \mathbf{A}^2 \mathbf{B} - 2 \mathbf{A} \mathbf{B} \mathbf{A}
      + \mathbf{B} \mathbf{A}^2 \right) \mathbf{B} \right) \\
    &=& -\frac{1}{24} t^2 [\mathbf{B}, \mathbf{A}^2 \mathbf{B}
      - 2 \mathbf{A} \mathbf{B} \mathbf{A} + \mathbf{B} \mathbf{A}^2] \\
    &=& -\frac{1}{24} t^2 [\mathbf{B}, \mathbf{A} \left( \mathbf{A} \mathbf{B}
      - \mathbf{B} \mathbf{A} \right) - \left( \mathbf{A} \mathbf{B}
      - \mathbf{B} \mathbf{A} \right) \mathbf{A}] \\
    &=& -\frac{1}{24} t^2 [\mathbf{B}, [\mathbf{A}, \left( \mathbf{A} \mathbf{B}
      - \mathbf{B} \mathbf{A} \right)]] \\
    &=& -\frac{1}{24} t^2 [\mathbf{B}, [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]]
  \end{eqnarray}
$$

## BCHの公式 (一部)

上記の$\mathbf{F}_n(\mathbf{A}, t \mathbf{B})$を使うと、$\mathbf{W}(t)$の最初の項は次のようになる。

$$
  \begin{eqnarray}
    \ln(\exp(\mathbf{A}) \exp(t \mathbf{B})) &=& \mathbf{W}(t) \\
    &=& \mathbf{F}_1(\mathbf{A}, t \mathbf{B})
      + \mathbf{F}_2(\mathbf{A}, t \mathbf{B})
      + \mathbf{F}_3(\mathbf{A}, t \mathbf{B})
      + \mathbf{F}_4(\mathbf{A}, t \mathbf{B}) + \cdots \\
    &=& \mathbf{A} + t \mathbf{B} + \frac{1}{2} t [\mathbf{A}, \mathbf{B}]
      + \frac{1}{12} t [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} t^2 [\mathbf{B}, [\mathbf{A}, \mathbf{B}]] \\
    && \quad - \frac{1}{24} t^2 [\mathbf{B}, [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]]
      + \cdots
  \end{eqnarray}
$$

$t = 1$とすれば次のように、BCH (Baker-Campbell-Hausdorff) の公式の最初の部分が得られる。

$$
  \begin{eqnarray}
    \ln(\exp(\mathbf{A}) \exp(\mathbf{B}))
    &=& \mathbf{A} + \mathbf{B} + \frac{1}{2} [\mathbf{A}, \mathbf{B}]
      + \frac{1}{12} [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]
      - \frac{1}{12} [\mathbf{B}, [\mathbf{A}, \mathbf{B}]] \\
    && \quad - \frac{1}{24} [\mathbf{B}, [\mathbf{A}, [\mathbf{A}, \mathbf{B}]]]
      + \cdots
  \end{eqnarray}
$$

