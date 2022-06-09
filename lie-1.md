
---
title:  SO(3)とSE(3)についてのメモ書き (その1)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css lie-1.md > lie-1.html
-->

[ホームに戻る](./index.html)

# このページについて

3次元の回転を表すリー群$\mathrm{SO}(3)$と、リー代数$\mathfrak{so}(3)$に関する、自分用のメモ書きです。

## $\mathfrak{so}(3)$から$\mathrm{SO}(3)$への変換

リー代数$\boldsymbol{\phi} \in \mathfrak{so}(3)$と、それに対応するリー群(回転行列)$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge) \in \mathrm{SO}(3)$を考える。
$\boldsymbol{\phi}$のノルムを$\phi = | \boldsymbol{\phi} |$, ノルム1に正規化されたベクトルを$\mathbf{a} \in \mathbb{R}^3 = \boldsymbol{\phi} / \phi$と定めると、$\boldsymbol{\phi} = \phi \mathbf{a}$と記述できる。
このとき、$\mathbf{a}$は回転軸、$\phi$は回転軸まわりの回転角を表すので、$\boldsymbol{\phi}$は回転ベクトルとして捉えられる。
$\boldsymbol{\phi}$と$\mathbf{C}$との間には、次の関係が成り立つ。この関係はロドリゲスの公式とよばれる。

$$
  \begin{eqnarray}
    \mathbf{C} &=& \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right) \mathbf{a} \mathbf{a}^\top
      + \sin \phi \mathbf{a}^\wedge
  \end{eqnarray}
$$

$\mathbf{a} \mathbf{a}^\top = \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge$の関係が成り立つので、上式に代入して変形すれば、次の関係も得られる。

$$
  \begin{eqnarray}
    \mathbf{C} &=& \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right)
      \left( \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge \right)
      + \sin \phi \mathbf{a}^\wedge \\
    &=& \mathbf{I} + \left( 1 - \cos \phi \right)
      \mathbf{a}^\wedge \mathbf{a}^\wedge
      + \sin \phi \mathbf{a}^\wedge \\
  \end{eqnarray}
$$

$\boldsymbol{\phi} = \phi \mathbf{a}$を再度代入すると、次のようになる。

$$
  \mathbf{C} = \cos \phi \mathbf{I} + \frac{1 - \cos \phi}{\phi^2}
    \boldsymbol{\phi} \boldsymbol{\phi}^\top
    + \frac{\sin \phi}{\phi} \boldsymbol{\phi}^\wedge
$$
$$
  \mathbf{C} = \mathbf{I} + \frac{1 - \cos \phi}{\phi^2}
    \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
    + \frac{\sin \phi}{\phi} \boldsymbol{\phi}^\wedge
$$

以後、$\mathrm{sinc1}(\phi) = \cfrac{\sin \phi}{\phi}$、$\mathrm{sinc2}(\phi) = \cfrac{1 - \cos \phi}{\phi^2}$とおく。

## Sinc関数$\mathrm{sinc1}(\phi)$と$\mathrm{sinc2}(\phi)$の計算

$\phi$が小さい値のとき、$\mathrm{sinc1}(\phi)$と$\mathrm{sinc2}(\phi)$の計算は不安定になるので、テイラー展開による近似で対処する。
$\mathrm{sinc1}(\phi)$と$\mathrm{sinc2}(\phi)$をテイラー展開すると、次のようになる。

$$
  \begin{eqnarray}
    \mathrm{sinc1}(\phi) &=& \frac{\sin \phi}{\phi} \\
    &=& \frac{1}{\phi} \left( \phi - \frac{1}{3!} \phi^3
      + \frac{1}{5!} \phi^5 - \frac{1}{7!} \phi^7 + \cdots \right) \\
    &=& 1 - \frac{1}{3!} \phi^2 + \frac{1}{5!} \phi^4 - \frac{1}{7!} \phi^6 + \cdots \\
    &=& 1 - \frac{1}{6} \phi^2 \left( 1 - \frac{1}{20} \phi^2
      \left( 1 - \frac{1}{42} \phi^2 \right) \right) + \cdots
  \end{eqnarray}
$$

$$
  \begin{eqnarray}
    \mathrm{sinc2}(\phi) &=& \frac{1 - \cos \phi}{\phi^2} \\
    &=& \frac{1}{\phi^2} \left( 1 - 1 + \frac{1}{2!} \phi^2 - \frac{1}{4!} \phi^4
      + \frac{1}{6!} \phi^6 - \frac{1}{8!} \phi^8 + \cdots \right) \\
    &=& \frac{1}{2!} - \frac{1}{4!} \phi^2
      + \frac{1}{6!} \phi^4 - \frac{1}{8!} \phi^6 + \cdots \\
    &=& \frac{1}{2} \left( 1 - \frac{1}{12} \phi^2 \left( 1 - \frac{1}{30} \phi^2
      \left( 1 - \frac{1}{56} \phi^2 \right) \right) \right) + \cdots
  \end{eqnarray}
$$

## $\mathrm{SO}(3)$から$\mathfrak{so}(3)$への変換

$\mathbf{C}$から$\boldsymbol{\phi} = \phi \mathbf{a}$への変換を考える。
$\mathbf{C}$のトレース$\mathrm{tr}(\mathbf{C})$は、次のようになる。

$$
  \begin{eqnarray}
    \mathrm{tr}(\mathbf{C}) &=& \mathrm{tr} \left(
      \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right) \mathbf{a} \mathbf{a}^\top
      + \sin \phi \mathbf{a}^\wedge \right) \\
    &=& \cos \phi \mathrm{tr}(\mathbf{I})
      + \left( 1 - \cos \phi \right) \mathrm{tr}(\mathbf{a} \mathbf{a}^\top)
      + \sin \phi \mathrm{tr}(\mathbf{a}^\wedge) \\
    &=& 3 \cos \phi + \left( 1 - \cos \phi \right) = 2 \cos \phi - 1
  \end{eqnarray}
$$

$\mathrm{tr}(\mathbf{a} \mathbf{a}^\top) = \mathrm{tr}(\mathbf{a}^\top \mathbf{a}) = \mathrm{tr}(1) = 1$であることに注意。
上式を変形すれば、回転角$\phi$は次のように得られる。

$$
  \phi = \arccos \frac{\mathrm{tr}(\mathbf{C}) + 1}{2}
$$

続いて、$\mathbf{C} - \mathbf{C}^\top$は、次のようになる。

$$
  \begin{eqnarray}
    \mathbf{C} - \mathbf{C}^\top &=& \left(
      \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right) \mathbf{a} \mathbf{a}^\top
      + \sin \phi \mathbf{a}^\wedge \right)
      - \left( \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right) \mathbf{a} \mathbf{a}^\top
      - \sin \phi \mathbf{a}^\wedge \right) \\
    &=& 2 \sin \phi \mathbf{a}^\wedge = 2 \frac{\sin \phi}{\phi} \boldsymbol{\phi}^\wedge
  \end{eqnarray}
$$

$\mathbf{a}^\wedge$は歪対称行列であり、$\left( \mathbf{a}^\wedge \right)^\top = -\mathbf{a}^\wedge$が成り立つことに注意。
上式を変形すると、$\boldsymbol{\phi}^\wedge \in \mathbb{R}^{3 \times 3}$は次のようになる。

$$
  \boldsymbol{\phi}^\wedge = \frac{1}{2 \mathrm{sinc1}(\phi)}
    \left( \mathbf{C} - \mathbf{C}^\top \right)
$$

3次ベクトル$\mathbf{x} = \left[ x_0, x_1, x_2 \right]^\top \in \mathbb{R}^3$について、演算子$\wedge$は以下のように定義される(Wedge演算子)。

$$
  \mathbf{x}^\wedge = \left[ \begin{array}{ccc}
    0 & -x_2 & x_1 \\ x_2 & 0 & -x_0 \\ -x_1 & x_0 & 0 \end{array} \right]
$$

従って、$\boldsymbol{\phi}^\wedge$の$(2, 1)$要素、$(0, 2)$要素、$(1, 0)$要素を順に取り出せば、リー代数$\boldsymbol{\phi}$が得られる。

## $\mathrm{sinc1}(\phi)$が小さい値をとるときの対処

$\mathrm{sinc1}(\phi)$が$0$に近いときは、上記の方法では$\boldsymbol{\phi}^\wedge$の値が不安定になるので、別の方法を考える。
$\mathbf{C}$の各要素を順に書き下すと、次のようになる。

$$
  \begin{eqnarray}
    \mathbf{C} &=& \cos \phi \mathbf{I} + \left( 1 - \cos \phi \right) \mathbf{a} \mathbf{a}^\top
      + \sin \phi \mathbf{a}^\wedge \\
    &=& \left[ \begin{array}{ccc}
      \cos \phi & 0 & 0 \\ 0 & \cos \phi & 0 \\ 0 & 0 & \cos \phi \end{array} \right]
      + \left( 1 - \cos \phi \right) \left[ \begin{array}{ccc}
      a_0^2 & a_0 a_1 & a_0 a_2 \\ a_1 a_0 & a_1^2 & a_1 a_2 \\
      a_2 a_0 & a_2 a_1 & a_2^2 \end{array} \right]
      + \sin \phi \left[ \begin{array}{ccc}
      0 & -a_2 & a_1 \\ a_2 & 0 & -a_0 \\ -a_1 & a_0 & 0 \end{array} \right] \\
    &=& \left[ \begin{array}{ccc}
      \cos \phi + \left( 1 - \cos \phi \right) a_0^2
      & \left( 1 - \cos \phi \right) a_0 a_1 - a_2 \sin \phi
      & \left( 1 - \cos \phi \right) a_0 a_2 + a_1 \sin \phi \\
      \left( 1 - \cos \phi \right) a_1 a_0 + a_2 \sin \phi
      & \cos \phi + \left( 1 - \cos \phi \right) a_1^2
      & \left( 1 - \cos \phi \right) a_1 a_2 - a_0 \sin \phi \\
      \left( 1 - \cos \phi \right) a_2 a_0 - a_1 \sin \phi
      & \left( 1 - \cos \phi \right) a_2 a_1 + a_0 \sin \phi
      & \cos \phi + \left( 1 - \cos \phi \right) a_2^2 \end{array} \right]
  \end{eqnarray}
$$

$\mathbf{A} = \cfrac{\phi^2}{2} \left( \mathbf{C} + \mathbf{I} \right)$の幾つかの要素を考える。

$$
  \begin{eqnarray}
    A_{00} &=& \frac{\phi^2}{2} \left( 1 + \cos \phi + \left( 1 - \cos \phi \right) a_0^2 \right) \\
    &=& \frac{\phi^2}{2} \left( 2 \cos^2 \frac{\phi}{2} + 2 \sin^2 \frac{\phi}{2} a_0^2 \right) \\
    &=& \phi^2 \left( \cos^2 \frac{\phi}{2} + \sin^2 \frac{\phi}{2} a_0^2 \right) \\
    A_{11} &=& \phi^2 \left( \cos^2 \frac{\phi}{2} + \sin^2 \frac{\phi}{2} a_1^2 \right) \\
    A_{22} &=& \phi^2 \left( \cos^2 \frac{\phi}{2} + \sin^2 \frac{\phi}{2} a_2^2 \right) \\
    A_{02} &=& \frac{\phi^2}{2} \left( \left( 1 - \cos \phi \right) a_0 a_2 + a_1 \sin \phi \right) \\
    &=& \frac{\phi^2}{2} \left( 2 \sin^2 \frac{\phi}{2} a_0 a_2 + a_1 \sin \phi \right) \\
    A_{12} &=& \frac{\phi^2}{2} \left( \left( 1 - \cos \phi \right) a_1 a_2 - a_0 \sin \phi \right) \\
    &=& \frac{\phi^2}{2} \left( 2 \sin^2 \frac{\phi}{2} a_1 a_2 - a_0 \sin \phi \right)
  \end{eqnarray}
$$

ここでは、$-\pi \le \phi \le \pi$であるとする。
$\mathrm{sinc1}(\phi) \approx 0$のとき、$\phi \approx \pm \pi$である。
また、$\cos^2 \cfrac{\phi}{2} \approx 0$、$\sin^2 \cfrac{\phi}{2} \approx 1$であるから、$A_{00} \approx \phi^2 a_0^2 = \phi_0^2$、$A_{11} \approx \phi^2 a_1^2 = \phi_1^2$、$A_{22} \approx \phi^2 a_2^2 = \phi_2^2$、$A_{02} \approx \phi^2 a_0 a_2 = \phi_0 \phi_2$、$A_{12} \approx \phi^2 a_1 a_2 = \phi_1 \phi_2$である。

従って、$A_{00}$、$A_{11}$、$A_{22}$の平方根をとると、$\boldsymbol{\phi}$の各要素の絶対値$| \phi_0 |$、$| \phi_1 |$、$| \phi_2 |$が得られる。
続いて、$\phi_0$の符号が正であると仮定すると、$A_{02} = \phi_0 \phi_2$から$\phi_2$の符号、$A_{02} A_{12} \approx \phi_0 \phi_1 \phi_2^2$から$\phi_1$の符号が得られる($\phi_0 = 0$のときは正として扱う)。
各要素の絶対値と符号を基に、$\boldsymbol{\phi}$が得られる。

$\phi_0$の符号が負であると仮定すれば、$\phi_1$と$\phi_2$の符号も逆になるので、$-\boldsymbol{\phi} = -\phi \mathbf{a}$が得られる。
$-\boldsymbol{\phi}$は、$\boldsymbol{\phi}$と同じ回転軸$\mathbf{a}$について、反対方向に同じ角度だけ($-\phi$だけ)回転させることを意味する。
ここでは、$\phi \approx \pm \pi$の状況を想定している。
同じ回転軸に対して$\pi$だけ回転させても、あるいは反対方向に$\pi$だけ回転させても、結果は全く同じになる。
従って、$\phi_0$の符号は正と負のどちらに仮定してもよいと考えられる。

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM From Theory to Practice](https://github.com/gaoxiang12/slambook-en)

