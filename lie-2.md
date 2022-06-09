
---
title:  SO(3)とSE(3)についてのメモ書き (その2)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css lie-2.md > lie-2.html
-->

[ホームに戻る](./index.html)

# このページについて

3次元の回転を表すリー群$\mathrm{SO}(3)$と、リー代数$\mathfrak{so}(3)$に関する、自分用のメモ書きです。

## $\mathrm{SO}(3)$の微分

リー代数$\boldsymbol{\phi} \in \mathfrak{so}(3)$と、それに対応する回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge) \in \mathrm{SO}(3)$を考える。
$\mathbf{C}$の$\boldsymbol{\phi}$に関する偏微分は、幾つかの方法で計算できる。

$\boldsymbol{\phi}$の各要素を$\phi_i$ ($0 \le i \le 2$)とする。
$\mathbf{C}$は$3 \times 3$行列であるため、$\phi_i$に関する偏微分$\cfrac{\partial \mathbf{C}}{\partial \phi_i}$も$3 \times 3$行列となる。
この偏微分は、$\phi_i$に微小な摂動$\Delta \phi_i$を加えたときに、$\mathbf{C}$がどのくらい変化するのかを表している。

あるいは、3次実ベクトル$\mathbf{p}$について、$\mathbf{C} \mathbf{p}$の$\boldsymbol{\phi}$に関する偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$を考えることもできる。
$\mathbf{C} \mathbf{p}$は3次ベクトル、$\boldsymbol{\phi}$も3次ベクトルであるから、この偏微分は$3 \times 3$行列になる。

## 下準備: $\mathbf{SO}(3)$に摂動を加える

BCH (Baker-Campbell-Hausdorff) の公式を使うと、2つのリー代数$\boldsymbol{\phi}_1, \boldsymbol{\phi}_2 \in \mathfrak{so}(3)$について、以下の近似式が得られる。

$$
  \ln(\exp(\boldsymbol{\phi}_1^\wedge) \exp(\boldsymbol{\phi}_2^\wedge))^\vee
  \approx \left\{ \begin{array}{cc}
    \mathbf{J}_l(\boldsymbol{\phi}_2)^{-1} \boldsymbol{\phi}_1 + \boldsymbol{\phi}_2
    & \text{$\boldsymbol{\phi}_1$が小さいとき} \\
    \mathbf{J}_r(\boldsymbol{\phi}_1)^{-1} \boldsymbol{\phi}_2 + \boldsymbol{\phi}_1
    & \text{$\boldsymbol{\phi}_2$が小さいとき}
    \end{array} \right.
$$

2つの回転行列$\exp(\boldsymbol{\phi}_1^\wedge)$、$\exp(\boldsymbol{\phi}_2^\wedge)$を合成して、新たな回転行列$\exp(\boldsymbol{\phi}_1^\wedge) \exp(\boldsymbol{\phi}_2^\wedge)$を作成する。
この新たな回転に対応するリー代数$\ln(\exp(\boldsymbol{\phi}_1^\wedge) \exp(\boldsymbol{\phi}_2^\wedge))^\vee$は、もし$\boldsymbol{\phi}_1$が小さい回転を表していれば上側、$\boldsymbol{\phi}_2$が小さい回転を表していれば下側のように近似される。

ヤコビ行列$\mathbf{J}_l(\boldsymbol{\phi})$と$\mathbf{J}_r(\boldsymbol{\phi})$は次のように定義される。
ただし、$\boldsymbol{\phi} = \phi \mathbf{a}$、$\phi = | \boldsymbol{\phi} |$、$\mathbf{a} = \boldsymbol{\phi} / \phi$である。
$\phi$は$\boldsymbol{\phi}$のノルム、$\mathbf{a}$はノルム1に正規化されたベクトルである([前回のメモ](./lie-1.html)を参照)。

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

2つのヤコビ行列$\mathbf{J}_l$、$\mathbf{J}_r$の間には、次の関係が成り立つ。

$$
  \mathbf{J}_r(\boldsymbol{\phi}) = \mathbf{J}_l(-\boldsymbol{\phi})
$$

逆行列$\mathbf{J}_l^{-1}$、$\mathbf{J}_r^{-1}$は、次のように表される。
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

上式を基に、$\boldsymbol{\phi}$に摂動$\Delta \boldsymbol{\phi}$を加えたとき、回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$がどのように変化するのかを考える。
回転$\mathbf{C}$に対して、**左側から**摂動$\exp(\Delta \boldsymbol{\phi}^\wedge)$を加えると、新たな回転は次のようになる。

$$
  \ln(\exp(\Delta \boldsymbol{\phi}^\wedge) \exp(\boldsymbol{\phi}^\wedge))^\vee
  \approx \mathbf{J}_l(\boldsymbol{\phi})^{-1} \Delta \boldsymbol{\phi} + \boldsymbol{\phi}
$$

続いて、回転$\mathbf{C}$に対して、**右側から**摂動$\exp(\Delta \boldsymbol{\phi}^\wedge)$を加えると、新たな回転は次のようになる。

$$
  \ln(\exp(\boldsymbol{\phi}^\wedge) \exp(\Delta \boldsymbol{\phi}^\wedge))^\vee
  \approx \mathbf{J}_r(\boldsymbol{\phi})^{-1} \Delta \boldsymbol{\phi} + \boldsymbol{\phi}
$$

次のようにも書ける。

$$
  \exp(\Delta \boldsymbol{\phi}^\wedge) \exp(\boldsymbol{\phi}^\wedge)
  \approx \exp((\mathbf{J}_l(\boldsymbol{\phi})^{-1} \Delta \boldsymbol{\phi}
    + \boldsymbol{\phi})^\wedge)
$$

$$
  \exp(\boldsymbol{\phi}^\wedge) \exp(\Delta \boldsymbol{\phi}^\wedge)
  \approx \exp((\mathbf{J}_r(\boldsymbol{\phi})^{-1} \Delta \boldsymbol{\phi}
    + \boldsymbol{\phi})^\wedge)
$$

## 偏微分の計算 (その1)

$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$の$\phi_i$に関する偏微分は、次のように表せる。

$$
  \frac{\partial \mathbf{C}}{\partial \phi_i}
  = \frac{\partial \exp(\boldsymbol{\phi}^\wedge)}{\partial \phi_i}
  = \lim_{h \to 0} \frac{\exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)
    - \exp(\boldsymbol{\phi}^\wedge)}{h}
$$

$\mathbf{1}_i$は$\boldsymbol{\phi}$と同様に3次ベクトルであり、$i$番目の要素が$1$で、他は全て$0$である。
従って$\boldsymbol{\phi} + h \mathbf{1}_i$は、$\boldsymbol{\phi}$の$i$番目の要素に、微小な変動$h$を加えたものである。

- $\mathbf{J}_l(\boldsymbol{\phi})$を使うと、$\exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)$の部分は、次のように近似できる。

  $$
    \begin{eqnarray}
      \exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)
      &=& \exp((\boldsymbol{\phi} + \mathbf{J}_l(\boldsymbol{\phi})^{-1}
        \underbrace{h \mathbf{J}_l(\boldsymbol{\phi})
        \mathbf{1}_i}_{\Delta \boldsymbol{\phi}})^\wedge) \\
      &\approx& \exp((h \mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge)
        \exp(\boldsymbol{\phi}^\wedge) \\
      &\approx& \left( \mathbf{I} + h (\mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \right)
        \exp(\boldsymbol{\phi}^\wedge)
    \end{eqnarray}
  $$

  最後の式変形は、行列指数関数$\exp(\mathbf{A})$の定義に基づいている。

  $$
    \exp(\mathbf{A}) = \mathbf{I} + \mathbf{A} + \frac{1}{2!} \mathbf{A}^2
      + \frac{1}{3!} \mathbf{A}^3 + \cdots
      = \sum_{n = 0}^\infty \frac{1}{n!} \mathbf{A}^n
  $$

  ここでは$h$が微小、言い換えると、$\mathbf{A} = (h \mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge$が微小である。
  従って、$\mathbf{A}$に関する項だけを残して、$\mathbf{A}^2$以降の項は無視できる。

  この近似を偏微分の定義に代入すれば、次が得られる。

  $$
    \frac{\left( \mathbf{I} + h (\mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \right)
      \exp(\boldsymbol{\phi}^\wedge) - \exp(\boldsymbol{\phi}^\wedge)}{h}
    = (\mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \exp(\boldsymbol{\phi}^\wedge)
  $$

- 一方、$\mathbf{J}_l(\boldsymbol{\phi})$を使うと、$\exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)$の部分は、次のように近似できる。

  $$
    \begin{eqnarray}
      \exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)
      &=& \exp((\boldsymbol{\phi} + \mathbf{J}_r(\boldsymbol{\phi})^{-1}
        \underbrace{h \mathbf{J}_r(\boldsymbol{\phi})
        \mathbf{1}_i}_{\Delta \boldsymbol{\phi}})^\wedge) \\
      &\approx& \exp(\boldsymbol{\phi}^\wedge)
        \exp((h \mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge) \\
      &\approx& \exp(\boldsymbol{\phi}^\wedge)
        \left( \mathbf{I} + (h \mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \right)
    \end{eqnarray}
  $$

  この近似を偏微分の定義に代入すれば、次が得られる。

  $$
    \frac{\exp(\boldsymbol{\phi}^\wedge)
      \left( \mathbf{I} + (h \mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \right)
      - \exp(\boldsymbol{\phi}^\wedge)}{h}
    = \exp(\boldsymbol{\phi}^\wedge) (\mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge
  $$

以上より、$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$の$\phi_i$に関する偏微分は、次のようになる。
3次ベクトル$\mathbf{1}_i$は、$i$番目の要素が$1$で、他は全て$0$である。

$$
  \frac{\partial \mathbf{C}}{\partial \phi_i}
  = \left\{ \begin{array}{cc}
    (\mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \mathbf{C}
    & \text{$\mathbf{J}_l$を使うとき} \\
    \mathbf{C} (\mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge
    & \text{$\mathbf{J}_r$を使うとき} \end{array} \right.
$$

上式を使うと、ある3次実ベクトル$\mathbf{p} \in \mathbb{R}^3$について、$\mathbf{C} \mathbf{p}$の$\boldsymbol{\phi}$による偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$が求められる。
偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$は、回転行列$\mathbf{C}$を微小に変動させたとき、回転の結果$\mathbf{C} \mathbf{p}$がどのぐらい動くのかを表している。

$\mathbf{C} \mathbf{p}$の$\phi_i$に関する偏微分は、右端に$\mathbf{p}$を足せば、次のようになる。

$$
  \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}
  = \left\{ \begin{array}{cc}
    (\mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \mathbf{C} \mathbf{p}
    & \text{$\mathbf{J}_l$を使うとき} \\
    \mathbf{C} (\mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i)^\wedge \mathbf{p}
    & \text{$\mathbf{J}_r$を使うとき} \end{array} \right.
$$

$\mathbf{a}^\wedge \mathbf{b}$は、2つのベクトルの外積$\mathbf{a} \times \mathbf{b}$を表すから、外積と同様に$\mathbf{a}^\wedge \mathbf{b} = -\mathbf{b}^\wedge \mathbf{a}$が成り立つ。
この関係を使うと、上式は次のように書ける。

$$
  \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}
  = \left\{ \begin{array}{cc}
    - (\mathbf{C} \mathbf{p})^\wedge \mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i
    & \text{$\mathbf{J}_l$を使うとき} \\
    -\mathbf{C} \mathbf{p}^\wedge \mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i
    & \text{$\mathbf{J}_r$を使うとき} \end{array} \right.
$$

$(\mathbf{C} \mathbf{p})^\wedge = \mathbf{C} \mathbf{p}^\wedge \mathbf{C}^\top$の関係が成り立つから、$(\mathbf{C} \mathbf{p})^\wedge$と$\mathbf{C} \mathbf{p}^\wedge$は別物である。

$(\mathbf{C} \mathbf{p})^\wedge \mathbf{J}_l(\boldsymbol{\phi}) \mathbf{1}_i$は、$3 \times 3$行列$(\mathbf{C} \mathbf{p})^\wedge \mathbf{J}_l(\boldsymbol{\phi})$の$i$列目のベクトルである。
同様に、$\mathbf{C} \mathbf{p}^\wedge \mathbf{J}_r(\boldsymbol{\phi}) \mathbf{1}_i$は、$3 \times 3$行列$\mathbf{C} \mathbf{p}^\wedge \mathbf{J}_r(\boldsymbol{\phi})$の$i$列目のベクトルである。

以上より、全ての$i$について、上記の3次ベクトルを**列方向に**並べれば、$3 \times 3$行列の偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$が得られる。

$$
  \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}
  = \left\{ \begin{array}{cc}
    - (\mathbf{C} \mathbf{p})^\wedge \mathbf{J}_l(\boldsymbol{\phi})
    & \text{$\mathbf{J}_l$を使うとき} \\
    -\mathbf{C} \mathbf{p}^\wedge \mathbf{J}_r(\boldsymbol{\phi})
    & \text{$\mathbf{J}_r$を使うとき} \end{array} \right.
$$

## 偏微分の計算 (その2)

上記の偏微分$\cfrac{\partial \mathbf{C}}{\partial \phi_i}$、あるいは$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$を求めるためには、ヤコビ行列$\mathbf{J}_l$あるいは$\mathbf{J}_r$の計算が必要である。
しかも、このヤコビ行列を計算するためには、$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$を$\boldsymbol{\phi} = \ln(\mathbf{C})^\vee$に一旦変換しなければならない([前回のメモ](./lie-1.html)を参照)。

そこで、上記とは別のアプローチで、偏微分$\cfrac{\partial \mathbf{C}}{\partial \phi_i}$、あるいは$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$を求めてみる。

先ほどは、$\phi_i$の方向に$\boldsymbol{\phi}$を摂動したときの回転行列を、$\exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)$で表現したが、ここでは$\exp((h \mathbf{1}_i)^\wedge) \exp(\mathbf{C})$、あるいは$\exp(\mathbf{C}) \exp((h \mathbf{1}_i)^\wedge)$と表すことにする。
前者は**左側から**、後者は**右側から**、$h \mathbf{1}_i$に対応する微小な回転行列$\exp((h \mathbf{1}_i)^\wedge)$を適用する。
先ほどと異なるのは、次のような点である。

- 先ほどの方法: $\boldsymbol{\phi}$に摂動$h \mathbf{1}_i$を加えた後、回転行列$\exp((\boldsymbol{\phi} + h \mathbf{1}_i)^\wedge)$に変換する
- ここでの方法: 摂動を回転行列$\exp((h \mathbf{1}_i)^\wedge)$に変換した後、元の回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$に適用する

- **左側から**適用する場合、偏微分$\cfrac{\partial \mathbf{C}}{\partial \phi_i}$と$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$は次のように書ける。

  $$
    \begin{eqnarray}
      \frac{\partial \mathbf{C}}{\partial \phi_i}
      &=& \lim_{h \to 0} \frac{\exp((h \mathbf{1}_i)^\wedge) \mathbf{C} - \mathbf{C}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\left(
        \mathbf{I} + (h \mathbf{1}_i)^\wedge \right) \mathbf{C} - \mathbf{C}}{h} \\
      &=& (\mathbf{1}_i)^\wedge \mathbf{C}
    \end{eqnarray}
  $$

  ここでも$\exp(\mathbf{A}) \approx \mathbf{I} + \mathbf{A}$のように、$\exp(\mathbf{A})$を一次の項までで近似している。

  偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}$は、上式に$\mathbf{p}$を付け足せば、以下のようになる。
  $\mathbf{a}^\wedge \mathbf{b} = -\mathbf{b}^\wedge \mathbf{a}$である。

  $$
    \cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}
    = (\mathbf{1}_i)^\wedge \mathbf{C} \mathbf{p}
    = - \left( \mathbf{C} \mathbf{p} \right)^\wedge \mathbf{1}_i
  $$

  $\left( \mathbf{C} \mathbf{p} \right)^\wedge \mathbf{1}_i$は、$3 \times 3$行列$(\mathbf{C} \mathbf{p})^\wedge$の$i$列目のベクトルである。
  全ての$i$について、上記の3次ベクトルを列方向に並べれば、次のように$3 \times 3$の偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$が得られる。

  $$
    \cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}
    = - \left( \mathbf{C} \mathbf{p} \right)^\wedge
  $$

- **右側から**適用する場合、偏微分$\cfrac{\partial \mathbf{C}}{\partial \phi_i}$は次のように書ける。

  $$
    \begin{eqnarray}
      \frac{\partial \mathbf{C}}{\partial \phi_i}
      &=& \lim_{h \to 0} \frac{\mathbf{C} \exp((h \mathbf{1}_i)^\wedge) - \mathbf{C}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\mathbf{C} \left(
        \mathbf{I} + (h \mathbf{1}_i)^\wedge \right) - \mathbf{C}}{h} \\
      &=& \mathbf{C} (\mathbf{1}_i)^\wedge
    \end{eqnarray}
  $$

  偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}$は、上式に$\mathbf{p}$を付け足せば、以下のようになる。

  $$
    \cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \phi_i}
    = \mathbf{C} (\mathbf{1}_i)^\wedge \mathbf{p}
    = - \mathbf{C} \mathbf{p}^\wedge \mathbf{1}_i
  $$

  $\mathbf{C} \mathbf{p}^\wedge \mathbf{1}_i$は、$3 \times 3$行列$\mathbf{C} \mathbf{p}^\wedge$の$i$列目のベクトルである。
  全ての$i$について、上記の3次ベクトルを列方向に並べれば、次のように$3 \times 3$の偏微分$\cfrac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}$が得られる。

  $$
    \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}
    = - \mathbf{C} \mathbf{p}^\wedge
  $$

以上より、$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$の$\phi_i$に関する偏微分は、次のようになる。

$$
  \frac{\partial \mathbf{C}}{\partial \phi_i}
  = \left\{ \begin{array}{cc}
    (\mathbf{1}_i)^\wedge \mathbf{C} & \text{左側から適用するとき} \\
    \mathbf{C} (\mathbf{1}_i)^\wedge & \text{右側から適用するとき} \end{array} \right.
$$

また、$\mathbf{C} \mathbf{p}$の$\boldsymbol{\phi}$に関する偏微分は、次のようになる。

$$
  \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}}
  = \left\{ \begin{array}{cc}
    - \left( \mathbf{C} \mathbf{p} \right)^\wedge & \text{左側から適用するとき} \\
    - \mathbf{C} \mathbf{p}^\wedge & \text{右側から適用するとき} \end{array} \right.
$$

先程のアプローチと比較すると、ヤコビ行列$\mathbf{J}_l$、$\mathbf{J}_r$が消えているので、計算が楽になる。

## 合成関数の微分

回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$の関数$L(\mathbf{C})$を考える。
スカラー関数$L(\mathbf{C})$の$\phi_i$による微分は、次のようになる。
$C_{ij}$は、$\mathbf{C}$の$(i, j)$要素である。
ここでは、2つ目のアプローチによる微分を使う。

$$
  \begin{eqnarray}
    \frac{\partial L(\mathbf{C})}{\partial \phi_i}
    &=& \sum_{j = 0}^2 \sum_{k = 0}^2 \frac{\partial C_{jk}}{\partial \phi_i}
      \frac{\partial L(\mathbf{C})}{\partial C_{jk}} \\
    &=& \sum_{j = 0}^2 \sum_{k = 0}^2 \left( \frac{\partial \mathbf{C}}{\partial \phi_i} \right)_{jk}
      \left( \frac{\partial L(\mathbf{C})}{\partial \mathbf{C}} \right)_{jk} \\
    &=& \left\{ \begin{array}{cc}
      \sum_{j = 0}^2 \sum_{k = 0}^2 \left( (\mathbf{1}_i)^\wedge \mathbf{C} \right)_{jk}
      \left( \frac{\partial L(\mathbf{C})}{\partial \mathbf{C}} \right)_{jk}
      & \text{左側から適用するとき} \\
      \sum_{j = 0}^2 \sum_{k = 0}^2 \left( \mathbf{C} (\mathbf{1}_i)^\wedge \right)_{jk}
      \left( \frac{\partial L(\mathbf{C})}{\partial \mathbf{C}} \right)_{jk}
      & \text{右側から適用するとき} \end{array} \right.
  \end{eqnarray}
$$

$L(\mathbf{C})$は、例えば、ニューラルネットにおける誤差関数となる。
このとき、リー代数$\boldsymbol{\phi}$を入力にとって、回転行列$\mathbf{C} = \exp(\boldsymbol{\phi}^\wedge)$を出力するレイヤー(ここでは$\mathrm{SO}(3)$レイヤーとする)が、ニューラルネットのなかに組み込まれているとする。
誤差逆伝播法を実施するとき、$\mathrm{SO}(3)$レイヤーは後ろの層から、出力に関する残差関数の勾配$\cfrac{\partial L(\mathbf{C})}{\partial \mathbf{C}}$を受け取って、入力に関する勾配$\cfrac{\partial L(\mathbf{C})}{\partial \boldsymbol{\phi}}$の各要素を上記のように計算し、前の層に引き渡すことができる。
$\mathrm{SO}(3)$レイヤーは、計算結果$\mathbf{C}$をどこかに保持しておく必要がある。

あるいは、$\mathbf{u} = \mathbf{C} \mathbf{p}$の関数$L(\mathbf{u})$を考える。
スカラー関数$L(\mathbf{u})$の$\boldsymbol{\phi}$に関する微分は、連鎖律から次のようになる。
ここでも、2つ目のアプローチによる微分を使っている。

$$
  \frac{\partial L(\mathbf{u})}{\partial \boldsymbol{\phi}}
  = \frac{\partial L(\mathbf{u})}{\partial \mathbf{u}}
    \frac{\partial (\mathbf{C} \mathbf{p})}{\partial \boldsymbol{\phi}} \\
  = \left\{ \begin{array}{cc}
    - \frac{\partial L(\mathbf{u})}{\partial \mathbf{u}}
    \left( \mathbf{C} \mathbf{p} \right)^\wedge & \text{左側から適用するとき} \\
    - \frac{\partial L(\mathbf{u})}{\partial \mathbf{u}}
    \mathbf{C} \mathbf{p}^\wedge & \text{右側から適用するとき}
    \end{array} \right.
$$

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM From Theory to Practice](https://github.com/gaoxiang12/slambook-en)

