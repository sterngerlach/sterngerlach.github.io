
---
title:  SO(3)とSE(3)についてのメモ書き (その3)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css lie-3.md > lie-3.html
-->

[ホームに戻る](./index.html)

# このページについて

3次元の回転を表すリー群$\mathrm{SO}(3)$と、リー代数$\mathfrak{so}(3)$に関する、自分用のメモ書きです。

## $\mathrm{SO}(3)$のヤコビ行列の計算

リー代数$\boldsymbol{\phi} \in \mathfrak{so}(3)$と、それに対応する回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge) \in \mathrm{SO}(3)$を考える。
[前回のメモ](./lie-2.html)では、$\boldsymbol{\phi}$に対するヤコビ行列$\mathbf{J}_l(\boldsymbol{\phi})$、$\mathbf{J}_r(\boldsymbol{\phi})$をみた。
これらのヤコビ行列は、$\mathbf{C}$の$\boldsymbol{\phi}$に関する偏微分を求める際に必要であった(必要としない計算方法もあった)。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi}) &=& \frac{\sin \phi}{\phi} \mathbf{I}
      + \left( 1 - \frac{\sin \phi}{\phi} \right) \mathbf{a} \mathbf{a}^\top
      + \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi}) &=& \frac{\sin \phi}{\phi} \mathbf{I}
      + \left( 1 - \frac{\sin \phi}{\phi} \right) \mathbf{a} \mathbf{a}^\top
      - \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge
  \end{eqnarray}
$$

これらの式において、$\boldsymbol{\phi} = \phi \mathbf{a}$、$\phi = | \boldsymbol{\phi} |$、$\mathbf{a} = \boldsymbol{\phi} / \phi$である。
$\phi$は$\boldsymbol{\phi}$のノルム、$\mathbf{a}$はノルム1に正規化されたベクトルである([こちらのメモ](./lie-1.html)を参照)。

逆行列$\mathbf{J}_l^{-1}$、$\mathbf{J}_r^{-1}$は、次のように表された。
$\cot \theta = \cfrac{1}{\tan \theta} = \cfrac{\cos \theta}{\sin \theta}$である。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi})^{-1} &=& \frac{\phi}{2} \cot \frac{\phi}{2} \mathbf{I}
      + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right) \mathbf{a} \mathbf{a}^\top
      - \frac{\phi}{2} \mathbf{a}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi})^{-1} &=& \frac{\phi}{2} \cot \frac{\phi}{2} \mathbf{I}
      + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right) \mathbf{a} \mathbf{a}^\top
      + \frac{\phi}{2} \mathbf{a}^\wedge
  \end{eqnarray}
$$

ここでは、これらの具体的な計算方法を考える。

## ヤコビ行列$\mathbf{J}_l$、$\mathbf{J}_r$の計算

$\mathbf{J}_l$と$\mathbf{J}_r$を、$\mathbf{a} \mathbf{a}^\top = \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge$の関係を使って、次のように書き直す。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi}) &=& \frac{\sin \phi}{\phi} \mathbf{I}
      + \left( 1 - \frac{\sin \phi}{\phi} \right)
      \left( \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge \right)
      + \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge \\
    &=& \mathbf{I} + \left( 1 - \frac{\sin \phi}{\phi} \right)
      \mathbf{a}^\wedge \mathbf{a}^\wedge
      + \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi}) &=& \frac{\sin \phi}{\phi} \mathbf{I}
      + \left( 1 - \frac{\sin \phi}{\phi} \right)
      \left( \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge \right)
      - \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge \\
    &=& \mathbf{I} + \left( 1 - \frac{\sin \phi}{\phi} \right)
      \mathbf{a}^\wedge \mathbf{a}^\wedge
      - \frac{1 - \cos \phi}{\phi} \mathbf{a}^\wedge
  \end{eqnarray}
$$

さらに、$\mathbf{a} = \boldsymbol{\phi} / \phi$を代入して、次のように表す。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi}) &=&
      \mathbf{I} + \frac{1}{\phi^2} \left( 1 - \frac{\sin \phi}{\phi} \right)
      \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      + \frac{1 - \cos \phi}{\phi^2} \boldsymbol{\phi}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi}) &=&
      \mathbf{I} + \frac{1}{\phi^2} \left( 1 - \frac{\sin \phi}{\phi} \right)
      \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      - \frac{1 - \cos \phi}{\phi^2} \boldsymbol{\phi}^\wedge
  \end{eqnarray}
$$


$\mathbf{J}_l$と$\mathbf{J}_r$は、[こちらのメモ](./lie-1.html)で定義した$\mathrm{sinc2}(\phi)$と、$\mathrm{sinc3}(\phi) = \cfrac{\phi - \sin \phi}{\phi^3}$を使って、次のように書ける。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi}) &=& \mathbf{I}
      + \mathrm{sinc3}(\phi) \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      + \mathrm{sinc2}(\phi) \boldsymbol{\phi}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi}) &=& \mathbf{I}
      + \mathrm{sinc3}(\phi) \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      - \mathrm{sinc2}(\phi) \boldsymbol{\phi}^\wedge
  \end{eqnarray}
$$

[こちらのメモ](./lie-1.html)に書いたように、$\phi$が小さい値のとき、$\mathrm{sinc2}(\phi)$、$\mathrm{sinc3}(\phi)$の計算は不安定になるので、テイラー展開による近似で対処する。
これらの近似は、次のようになる。

$$
  \begin{eqnarray}
    \mathrm{sinc2}(\phi) &=& \frac{1 - \cos \phi}{\phi^2} \\
    &=& \frac{1}{2} \left( 1 - \frac{1}{12} \phi^2 \left( 1 - \frac{1}{30} \phi^2
      \left( 1 - \frac{1}{56} \phi^2 \right) \right) \right) + \cdots
  \end{eqnarray}
$$

$$
  \begin{eqnarray}
    \mathrm{sinc3}(\phi) &=& \frac{\phi - \sin \phi}{\phi^3} \\
    &=& \frac{1}{\phi^3} \left( \phi - \phi + \frac{1}{3!} \phi^3 - \frac{1}{5!} \phi^5
      + \frac{1}{7!} \phi^7 - \frac{1}{9!} \phi^9 + \cdots \right) \\
    &=& \frac{1}{3!} - \frac{1}{5!} \phi^2 + \frac{1}{7!} \phi^4 - \frac{1}{9!} \phi^6 + \cdots \\
    &=& \frac{1}{6} \left( 1 - \frac{1}{24} \phi^2 \left(
      1 - \frac{1}{42} \phi^2 \left( 1 - \frac{1}{72} \phi^2 \right) \right) \right) + \cdots
  \end{eqnarray}
$$

$\phi$がある程度大きな値であれば、上式を素直に計算できる。

## ヤコビ行列の逆行列$\mathbf{J}_l^{-1}$、$\mathbf{J}_r^{-1}$の計算

$\mathbf{J}_l^{-1}$と$\mathbf{J}_r^{-1}$を、$\mathbf{a} \mathbf{a}^\top = \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge$の関係を使って、次のように書き直す。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi})^{-1} &=& \frac{\phi}{2} \cot \frac{\phi}{2} \mathbf{I}
      + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \left( \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge \right)
      - \frac{\phi}{2} \mathbf{a}^\wedge \\
    &=& \mathbf{I} + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \mathbf{a}^\wedge \mathbf{a}^\wedge
      - \frac{\phi}{2} \mathbf{a}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi})^{-1} &=& \frac{\phi}{2} \cot \frac{\phi}{2} \mathbf{I}
      + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \left( \mathbf{I} + \mathbf{a}^\wedge \mathbf{a}^\wedge \right)
      - \frac{\phi}{2} \mathbf{a}^\wedge \\
    &=& \mathbf{I} + \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \mathbf{a}^\wedge \mathbf{a}^\wedge
      + \frac{\phi}{2} \mathbf{a}^\wedge
  \end{eqnarray}
$$

さらに、$\mathbf{a} = \boldsymbol{\phi} / \phi$を代入して、次のように表す。

$$
  \begin{eqnarray}
    \mathbf{J}_l(\boldsymbol{\phi})^{-1} &=&
      \mathbf{I} + \frac{1}{\phi^2} \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      - \frac{1}{2} \mathbf{a}^\wedge \\
    \mathbf{J}_r(\boldsymbol{\phi})^{-1} &=&
      \mathbf{I} + \frac{1}{\phi^2} \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right)
      \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      + \frac{1}{2} \mathbf{a}^\wedge
  \end{eqnarray}
$$

$\phi$が小さい値のとき、上式の$\cfrac{1}{\phi^2} \left( 1 - \cfrac{\phi}{2} \cot \cfrac{\phi}{2} \right)$の計算は不安定になるので、テイラー展開による近似で対処する。
この近似を求めるのは、少々面倒である。

$\cot$の定義から、$(\phi \cot \phi) \sin \phi = \phi \cos \phi$である。
これに$\sin \phi$と$\cos \phi$のテイラー展開を代入すれば、以下のようになる。

$$
  \phi \cot \phi \left( \phi - \frac{1}{3!} \phi^3 + \frac{1}{5!} \phi^5
    - \frac{1}{7!} \phi^7 + \frac{1}{9!} \phi^9 + \cdots \right)
  = \phi - \frac{1}{2!} \phi^3 + \frac{1}{4!} \phi^5
    - \frac{1}{6!} \phi^7 + \frac{1}{8!} \phi^9 + \cdots
$$

$\cot \phi = \cfrac{1}{\tan \phi}$は奇関数であるから、$\phi \cot \phi$は偶関数となる。
テイラー展開すれば、$\phi^0$、$\phi^2$、$\phi^4$、$\phi^6$のように、$\phi$の偶数乗の項だけが並ぶはずである。
従って、$\phi \cot \phi$を次のように定めて、係数$a_0$、$a_2$、$a_4$、$a_6$、$a_8$の値を順に求める。

$$
  \phi \cot \phi = a_0 + a_2 \phi^2 + a_4 \phi^4 + a_6 \phi^6 + a_8 \phi^8 + \cdots
$$

これを代入すれば、次のようになる。

$$
  \begin{eqnarray}
    && \left( a_0 + a_2 \phi^2 + a_4 \phi^4 + a_6 \phi^6 + a_8 \phi^8 + \cdots \right)
    \left( \phi - \frac{1}{3!} \phi^3 + \frac{1}{5!} \phi^5
      - \frac{1}{7!} \phi^7 + \frac{1}{9!} \phi^9 + \cdots \right) \\
    &=& \phi - \frac{1}{2!} \phi^3 + \frac{1}{4!} \phi^5
      - \frac{1}{6!} \phi^7 + \frac{1}{8!} \phi^9 + \cdots
  \end{eqnarray}
$$

左辺と右辺の係数の比較から、次の方程式が得られる。

$$
  \begin{eqnarray}
    a_0 &=& 1 \\
    -\frac{a_0}{3!} + a_2 &=& -\frac{1}{2!} \\
    \frac{a_0}{5!} - \frac{a_2}{3!} + a_4 &=& \frac{1}{4!} \\
    -\frac{a_0}{7!} + \frac{a_2}{5!} - \frac{a_4}{3!} + a_6 &=& -\frac{1}{6!} \\
    \frac{a_0}{9!} - \frac{a_2}{7!} + \frac{a_4}{5!} - \frac{a_6}{3!} + a_8 &=& \frac{1}{8!}
  \end{eqnarray}
$$

各係数は次のように求まる。

$$
  \begin{eqnarray}
    a_0 &=& 1 \\
    a_2 &=& -\frac{1}{2} + \frac{1}{6} = -\frac{1}{3} \\
    a_4 &=& \frac{1}{24} - \frac{1}{6} \cdot \frac{1}{3} - \frac{1}{120}
      = \frac{15 - 20 - 3}{360} = -\frac{1}{45} \\
    a_6 &=& -\frac{1}{720} - \frac{1}{6} \cdot \frac{1}{45}
      + \frac{1}{120} \cdot \frac{1}{3} + \frac{1}{5040} \\
    &=& \frac{-21 - 56 + 42 + 3}{15120} = -\frac{2}{945} \\
    a_8 &=& \frac{1}{40320} - \frac{1}{6} \cdot \frac{2}{945} + \frac{1}{120} \cdot \frac{1}{45}
      - \frac{1}{5040} \cdot \frac{1}{3} - \frac{1}{362880} \\
    &=& \frac{45 - 640 + 336 - 120 - 5}{1814400} = -\frac{1}{4725}
  \end{eqnarray}
$$

$\phi \cot \phi$は次のようになる。

$$
  \phi \cot \phi = 1 - \frac{1}{3} \phi^2 - \frac{1}{45} \phi^4
    - \frac{2}{945} \phi^6 - \frac{1}{4725} \phi^8 + \cdots
$$

上記より、$\cfrac{1}{\phi^2} \left( 1 - \cfrac{\phi}{2} \cot \cfrac{\phi}{2} \right)$は次のようになる。

$$
  \begin{eqnarray}
    && \frac{1}{\phi^2} \left( 1 - \frac{\phi}{2} \cot \frac{\phi}{2} \right) \\
    &=& \frac{1}{\phi^2} \left( 1 - 1
      + \frac{1}{3} \cdot \frac{1}{2^2} \phi^2
      + \frac{1}{45} \cdot \frac{1}{2^4} \phi^4
      + \frac{2}{945} \cdot \frac{1}{2^6} \phi^6
      + \frac{1}{4725} \cdot \frac{1}{2^8} \phi^8 + \cdots \right) \\
    &=& \frac{1}{\phi^2} \left( 1 - 1 + \frac{1}{12} \phi^2
      + \frac{1}{720} \phi^4 + \frac{1}{30240} \phi^6
      + \frac{1}{1209600} \phi^8 + \cdots \right) \\
    &=& \frac{1}{12} + \frac{1}{720} \phi^2 + \frac{1}{30240} \phi^4
      + \frac{1}{1209600} \phi^6 + \cdots \\
    &=& \frac{1}{12} + \frac{1}{720} \phi^2 \left( 1 + \frac{1}{42} \phi^2
      \left( 1 + \frac{1}{40} \phi^2 \right) \right) + \cdots
  \end{eqnarray}
$$

$\phi$がある程度大きな値であれば、$\mathbf{J}_l^{-1}$、$\mathbf{J}_r^{-1}$の定義に沿って、素直に計算できる。

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM From Theory to Practice](https://github.com/gaoxiang12/slambook-en)

