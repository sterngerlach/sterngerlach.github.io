
---
title:  SO(3)とSE(3)についてのメモ書き (その4)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css lie-4.md > lie-4.html
-->

[ホームに戻る](./index.html)

# このページについて

3次元の剛体変換を表すリー群$\mathrm{SE}(3)$と、リー代数$\mathfrak{se}(3)$に関する、自分用のメモ書きです。

## $\mathfrak{se}(3)$から$\mathrm{SE}(3)$への変換

リー代数$\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right] \in \mathfrak{se}(3)$と、それに対応するリー群(剛体変換)$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge) \in \mathrm{SE}(3)$を考える。
$\boldsymbol{\phi} \in \mathfrak{so}(3)$、$\boldsymbol{\rho} \in \mathbb{R}^3$である。
$\boldsymbol{\xi}$と$\mathbf{T}$との間には、次の関係が成立する。

$$
  \mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)
  = \left[ \begin{array}{cc} \mathbf{C} & \mathbf{J}(\boldsymbol{\phi}) \boldsymbol{\rho} \\
    \mathbf{0}^\top & 1 \end{array} \right]
$$

ここで、$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge) \in \mathrm{SO}(3)$は、$\boldsymbol{\phi}$から得た回転行列である。
またヤコビ行列$\mathbf{J}$は、[こちらのメモ](./lie-2.html)で定義された$\mathbf{J}_l$と同じものである(左側バージョン)。
$\boldsymbol{\phi} = \phi \mathbf{a}$、$\phi = | \boldsymbol{\phi} |$、$\mathbf{a} = \boldsymbol{\phi} / \phi$である。

$$
  \mathbf{J}(\boldsymbol{\phi}) = \frac{\sin \phi}{\phi} \mathbf{I}
    + \left( 1 - \frac{\sin \phi}{\phi} \right) \mathbf{a} \mathbf{a}^\top
    + \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge
$$

$\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right] \in \mathfrak{se}(3)$に対して、$\wedge$演算子は次のように定義される(Wedge演算子)。
$\boldsymbol{\phi} \in \mathfrak{so}(3)$に対する$\wedge$演算子は、[こちらのメモ](./lie-1.html)を参照する。
$\vee$演算子は、$\wedge$とは真逆の操作を行う(Vee演算子)。

$$
  \boldsymbol{\xi}^\wedge = \left[ \begin{array}{cc}
    \boldsymbol{\phi}^\wedge & \boldsymbol{\rho} \\
    \mathbf{0}^\top & 0 \end{array} \right] \in \mathbb{R}^{4 \times 4}
$$

$\boldsymbol{\xi}$から$\mathbf{T}$を計算するためには、次のようにする。

- $\boldsymbol{\xi}$から回転を表す成分$\boldsymbol{\phi} \in \mathfrak{so}(3)$を取り出して、回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge) \in \mathrm{SO}(3)$を計算する。
計算方法は、[こちらのメモ](./lie-1.html)を参照する。
- $\boldsymbol{\phi} \in \mathfrak{so}(3)$から、(左側バージョンの)ヤコビ行列$\mathbf{J}(\boldsymbol{\phi})$を計算する。
計算方法は、[こちらのメモ](./lie-3.html)を参照する。
- $\boldsymbol{\xi}$から$\boldsymbol{\rho}$を取り出して、$\mathbf{J}(\boldsymbol{\phi}) \boldsymbol{\rho}$を計算する。
- $\mathbf{C}$、$\mathbf{J}(\boldsymbol{\phi}) \boldsymbol{\rho}$が揃ったので、それらをまとめて$\mathbf{T}$とする。

$\mathbf{T}$の逆行列$\mathbf{T}^{-1}$は、次のように表される($\mathbf{r} = \mathbf{J}(\boldsymbol{\phi}) \boldsymbol{\rho}$)。

$$
  \mathbf{T}^{-1} = \left[ \begin{array}{cc}
    \mathbf{C}^\top & -\mathbf{C}^\top \mathbf{r} \\
    \mathbf{0}^\top & 1 \end{array} \right]
$$

$\mathbf{T}$から$\mathbf{T}^{-1}$、あるいは$\boldsymbol{\xi}$から$\mathbf{T}^{-1}$は、容易に求められる。

## $\mathrm{SE}(3)$から$\mathfrak{se}(3)$への変換

$\mathbf{T}$から$\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right]$への変換は、次のように行う。

- $\mathbf{T}$の左上のブロック(回転行列)$\mathbf{C}$を取り出して、$\mathbf{C}$に対応するリー代数$\boldsymbol{\phi}$を計算する。
$\mathbf{C}$から$\boldsymbol{\phi}$への変換は、[こちらのメモ](./lie-1.html)を参照する。
- $\mathbf{T}$の右上のブロック$\mathbf{J}(\boldsymbol{\phi}) \boldsymbol{\rho}$を取り出して、ヤコビ行列の逆行列$\mathbf{J}(\boldsymbol{\phi})^{-1}$を掛けることで、$\boldsymbol{\rho}$を計算する。
$\mathbf{J}(\boldsymbol{\phi})^{-1}$は、次のように定義される。
計算方法は、[こちらのメモ](./lie-3.html)を参照する。
$$
  \mathbf{J}(\boldsymbol{\phi})^{-1} = \frac{\phi}{2} \cot \frac{\phi}{2} \mathbf{I}
    + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right) \mathbf{a} \mathbf{a}^\top
    - \frac{\phi}{2} \mathbf{a}^\wedge
$$
- $\boldsymbol{\phi}$と$\boldsymbol{\rho}$を結合して、$\boldsymbol{\xi}$を得る。

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM: From Theory to Practice](https://github.com/gaoxiang12/slambook-en)

