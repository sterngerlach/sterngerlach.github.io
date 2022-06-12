
---
title:  SO(3)とSE(3)についてのメモ書き (その5)
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css lie-5.md > lie-5.html
-->

[ホームに戻る](./index.html)

# このページについて

3次元の剛体変換を表すリー群$\mathrm{SE}(3)$と、リー代数$\mathfrak{se}(3)$に関する、自分用のメモ書きです。

## $\mathrm{SE}(3)$の微分

リー代数$\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right] \in \mathfrak{se}(3)$と、それに対応するリー群(剛体変換)$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge) \in \mathrm{SE}(3)$を考える。
$\boldsymbol{\phi} \in \mathfrak{so}(3)$、$\boldsymbol{\rho} \in \mathbb{R}^3$である。
$\mathrm{SO}(3)$のとき([こちらのメモ](./lie-2.html))と同じように、$\mathbf{T}$の$\boldsymbol{\xi}$に関する偏微分も、2通りの方法で計算できる。

$\boldsymbol{\phi}$、$\boldsymbol{\rho}$の各要素を$\phi_i$、$\rho_i$($0 \le i \le 2$)とする。
また、$\boldsymbol{\xi}$の各要素を$\xi_i$($0 \le i \le 5$)とする。
$\mathbf{T}$は$4 \times 4$行列であるため、$\phi_i$、$\rho_i$、あるいは$\xi_i$に関する$\mathbf{T}$の偏微分$\cfrac{\partial \mathbf{T}}{\partial \phi_i}$、$\cfrac{\partial \mathbf{T}}{\partial \rho_i}$、$\cfrac{\partial \mathbf{T}}{\partial \xi_i}$も$4 \times 4$行列になる。

ある3次実ベクトル$\mathbf{p} \in \mathbb{R}^3$について、$\mathbf{T} \mathbf{p}$の$\boldsymbol{\xi}$に関する偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$を考えることもできる。
$\mathbf{T} \mathbf{p}$を計算する際は、$\mathbf{p}$を同次座標$\left[ \begin{array}{c} \mathbf{p} \\ 1 \end{array} \right]$に直すものとする。
従って、$\mathbf{T} \mathbf{p}$は4次ベクトルとなり、その最後の要素は$1$である(最初の3要素は、$\mathbf{p}$を$\mathbf{T}$で剛体変換した結果)。
ここでは、$\mathbf{p}$とその同次座標を特に区別せず、必要に応じて適宜変換されるとする。
$\boldsymbol{\xi}$は6次、$\mathbf{T} \mathbf{p}$は4次ベクトルであるから、偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$は$4 \times 6$行列となる。

## 下準備: $\mathrm{SE}(3)$に摂動を加える

2つのリー代数$\boldsymbol{\xi}_1, \boldsymbol{\xi}_2 \in \mathfrak{se}(3)$について、以下の近似式が得られる。
これは、$\mathrm{SO}(3)$のときと同様である。

$$
  \ln(\exp(\boldsymbol{\xi}_1^\wedge) \exp(\boldsymbol{\xi}_2^\wedge))^\vee
  \approx \left\{ \begin{array}{cc}
    \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}_2)^{-1} \boldsymbol{\xi}_1 + \boldsymbol{\xi}_2
    & \text{$\boldsymbol{\xi}_1$が小さいとき} \\
    \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}_1)^{-1} \boldsymbol{\xi}_2 + \boldsymbol{\xi}_1
    & \text{$\boldsymbol{\xi}_2$が小さいとき}
    \end{array} \right.
$$

$6 \times 6$のヤコビ行列$\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})$、$\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})$は次のように定義される($\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right]$)。

$$
  \begin{eqnarray}
    \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) &=& \left[ \begin{array}{cc}
      \mathbf{J}_l(\boldsymbol{\phi}) & \mathbf{Q}_l(\boldsymbol{\xi}) \\
      \mathbf{0} & \mathbf{J}_l(\boldsymbol{\phi}) \end{array} \right] \\
    \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) &=& \left[ \begin{array}{cc}
      \mathbf{J}_r(\boldsymbol{\phi}) & \mathbf{Q}_r(\boldsymbol{\xi}) \\
      \mathbf{0} & \mathbf{J}_r(\boldsymbol{\phi}) \end{array} \right]
  \end{eqnarray}
$$

$\mathbf{Q}_l(\boldsymbol{\xi})$、$\mathbf{Q}_r(\boldsymbol{\xi})$は以下のように定義される。

$$
  \begin{eqnarray}
    \mathbf{Q}_l(\boldsymbol{\xi}) &=& \frac{1}{2} \boldsymbol{\rho}^\wedge
      + \frac{\phi - \sin \phi}{\phi^3} \left(
      \boldsymbol{\phi}^\wedge \boldsymbol{\rho}^\wedge
      + \boldsymbol{\rho}^\wedge \boldsymbol{\phi}^\wedge
      + \boldsymbol{\phi}^\wedge \boldsymbol{\rho}^\wedge \boldsymbol{\phi}^\wedge \right) \\
      && + \frac{\phi^2 + 2 \cos \phi - 2}{2 \phi^4}
      \left( \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge \boldsymbol{\rho}^\wedge
      + \boldsymbol{\rho}^\wedge \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      - 3 \boldsymbol{\phi}^\wedge \boldsymbol{\rho}^\wedge \boldsymbol{\phi}^\wedge \right) \\
      && + \frac{2 \phi - 3 \sin \phi + \phi \cos \phi}{2 \phi^5}
      \left( \boldsymbol{\phi}^\wedge \boldsymbol{\rho}^\wedge
      \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      + \boldsymbol{\phi}^\wedge \boldsymbol{\phi}^\wedge
      \boldsymbol{\rho}^\wedge \boldsymbol{\phi}^\wedge \right) \\
    \mathbf{Q}_r(\boldsymbol{\xi}) &=& \mathbf{Q}_l(-\boldsymbol{\xi})
  \end{eqnarray}
$$

上式において、$\phi = | \boldsymbol{\phi} |$である。

ヤコビ行列の逆行列$\boldsymbol{\mathcal{J}}_l^{-1}(\boldsymbol{\xi})$、$\boldsymbol{\mathcal{J}}_r^{-1}(\boldsymbol{\xi})$は、次のように表される。

$$
  \begin{eqnarray}
    \boldsymbol{\mathcal{J}}_l^{-1}(\boldsymbol{\xi})
    &=& \left[ \begin{array}{cc} \mathbf{J}_l(\boldsymbol{\phi})^{-1}
      & -\mathbf{J}_l(\boldsymbol{\phi})^{-1} \mathbf{Q}_l(\boldsymbol{\xi})
      \mathbf{J}_l(\boldsymbol{\phi})^{-1} \\
      \mathbf{0} & \mathbf{J}_l(\boldsymbol{\phi})^{-1} \end{array} \right] \\
    \boldsymbol{\mathcal{J}}_r^{-1}(\boldsymbol{\xi})
    &=& \left[ \begin{array}{cc} \mathbf{J}_r(\boldsymbol{\phi})^{-1}
      & -\mathbf{J}_r(\boldsymbol{\phi})^{-1} \mathbf{Q}_r(\boldsymbol{\xi})
      \mathbf{J}_r(\boldsymbol{\phi})^{-1} \\
      \mathbf{0} & \mathbf{J}_r(\boldsymbol{\phi})^{-1} \end{array} \right]
  \end{eqnarray}
$$

これを使うと、$\boldsymbol{\xi}$に摂動$\Delta \boldsymbol{\xi}$を加えたときに、剛体変換$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$がどのように変化するのかが分かる。
$\mathbf{T}$に対して**左側から**摂動$\exp(\Delta \boldsymbol{\xi})$を加えると、新たな剛体変換は次のようになる。

$$
  \ln(\exp(\Delta \boldsymbol{\xi}^\wedge) \exp(\boldsymbol{\xi}^\wedge))^\vee
  \approx \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})^{-1}
    \Delta \boldsymbol{\xi} + \boldsymbol{\xi}
$$

また、$\mathbf{T}$に対して**右側から**摂動$\exp(\Delta \boldsymbol{\xi})$を加えると、新たな剛体変換は次のようになる。

$$
  \ln(\exp(\boldsymbol{\xi}^\wedge) \exp(\Delta \boldsymbol{\xi}^\wedge))^\vee
  \approx \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})^{-1}
    \Delta \boldsymbol{\xi} + \boldsymbol{\xi}
$$

次のようにも書ける。

$$
  \begin{eqnarray}
    \exp(\Delta \boldsymbol{\xi}^\wedge) \exp(\boldsymbol{\xi}^\wedge)
    &\approx& \exp((\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})^{-1}
      \Delta \boldsymbol{\xi} + \boldsymbol{\xi})^\wedge) \\
    \exp(\boldsymbol{\xi}^\wedge) \exp(\Delta \boldsymbol{\xi}^\wedge)
    &\approx& \exp((\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})^{-1}
      \Delta \boldsymbol{\xi} + \boldsymbol{\xi})^\wedge)
  \end{eqnarray}
$$

## 偏微分の計算 (その1)

$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$の$\xi_i$に関する偏微分は、次のように書ける。

$$
  \frac{\partial \mathbf{T}}{\partial \xi_i}
  = \frac{\partial \exp(\boldsymbol{\xi}^\wedge)}{\partial \xi_i}
  = \lim_{h \to 0} \frac{\exp((\boldsymbol{\xi} + h \mathbf{1}_i)^\wedge)
    - \exp(\boldsymbol{\xi}^\wedge)}{h}
$$

$\mathbf{1}_i$は6次元ベクトルである。
[こちらのメモ](./lie-2.html)で示されるように、$\mathbf{1}_i$は、$i$番目の要素が$1$で、それ以外は$0$のOne-Hotベクトルである。
$\boldsymbol{\xi} + h \mathbf{1}_i$は、$\boldsymbol{\xi}$の$i$番目の要素に、微小な変動$h$を加えたものである。
さて、$\mathrm{SO}(3)$のときと同じように、2種類のヤコビ行列を使って、この偏微分を求めてみる。

- ヤコビ行列の左側バージョン$\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})$を使うと、$\exp(\boldsymbol{\xi}^\wedge)$の項は次のように近似できる。

  $$
    \begin{eqnarray}
      \exp(\boldsymbol{\xi}^\wedge)
      &=& \exp((\boldsymbol{\xi} + \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})^{-1}
        \underbrace{h \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})
        \mathbf{1}_i}_{\boldsymbol{\Delta \xi}})^\wedge) \\
      &\approx& \exp((h \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge)
        \exp(\boldsymbol{\xi}^\wedge) \\
      &\approx& \left( \mathbf{I} + (h \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})
        \mathbf{1}_i)^\wedge \right) \exp(\boldsymbol{\xi}^\wedge)
    \end{eqnarray}
  $$

  最後の式変形は、行列指数関数の定義による([こちらのメモ](./lie-2.html)を参照)。
  この近似を偏微分の式に代入すれば、次が得られる。

  $$
    \lim_{h \to 0} \frac{\left( \mathbf{I} + (h \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})
      \mathbf{1}_i)^\wedge \right) \exp(\boldsymbol{\xi}^\wedge)
      - \exp(\boldsymbol{\xi}^\wedge)}{h}
    = (\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge \exp(\boldsymbol{\xi}^\wedge)
  $$

- ヤコビ行列の右側バージョン$\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}))$を使うと、$\exp(\boldsymbol{\xi}^\wedge)$の項は次のように近似できる。

  $$
    \begin{eqnarray}
      \exp(\boldsymbol{\xi}^\wedge)
      &=& \exp((\boldsymbol{\xi} + \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})^{-1}
        \underbrace{h \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})
        \mathbf{1}_i}_{\boldsymbol{\Delta \xi}})^\wedge) \\
      &\approx& \exp(\boldsymbol{\xi}^\wedge)
        \exp((h \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge) \\
      &\approx& \exp(\boldsymbol{\xi}^\wedge)
        \left( \mathbf{I} + (h \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})
        \mathbf{1}_i)^\wedge \right)
    \end{eqnarray}
  $$

  この近似を偏微分の式に代入すれば、次が得られる。

  $$
    \lim_{h \to 0} \frac{\exp(\boldsymbol{\xi}^\wedge)
      \left( \mathbf{I} + (h \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})
      \mathbf{1}_i)^\wedge \right) - \exp(\boldsymbol{\xi}^\wedge)}{h}
    = \exp(\boldsymbol{\xi}^\wedge) (\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge
  $$

以上より、$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$の$\xi_i$に関する偏微分は、次のようになる。

$$
  \frac{\partial \mathbf{T}}{\partial \xi_i}
  = \left\{ \begin{array}{cc}
    (\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge
    \mathbf{T} & \text{$\boldsymbol{\mathcal{J}}_l$を使うとき} \\
    \mathbf{T} (\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge
    & \text{$\boldsymbol{\mathcal{J}}_r$を使うとき} \end{array} \right.
$$

これを使えば、ある3次実ベクトル$\mathbf{p}$について、偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$が求められる。
$\mathbf{T} \mathbf{p}$の$\xi_i$に関する偏微分は、右端に$\mathbf{p}$を足せば、次のようになる。

$$
  \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}
  = \left\{ \begin{array}{cc}
    (\boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge
    \mathbf{T} \mathbf{p} & \text{$\boldsymbol{\mathcal{J}}_l$を使うとき} \\
    \mathbf{T} (\boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i)^\wedge \mathbf{p}
    & \text{$\boldsymbol{\mathcal{J}}_r$を使うとき} \end{array} \right.
$$

$\mathbf{a}^\wedge \mathbf{b} = \mathbf{b}^\odot \mathbf{a}$であるから、次のように書き直す(マイナスはつかない)。

$$
  \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}
  = \left\{ \begin{array}{cc}
    (\mathbf{T} \mathbf{p})^\odot
    \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i
    & \text{$\boldsymbol{\mathcal{J}}_l$を使うとき} \\
    \mathbf{T} \mathbf{p}^\odot
    \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i
    & \text{$\boldsymbol{\mathcal{J}}_r$を使うとき} \end{array} \right.
$$

同次座標を表す4次ベクトル$\mathbf{a} = \left[ \begin{array}{c} \boldsymbol{\varepsilon} \\ \eta \end{array} \right]$について、$\odot$演算子は次のように定義される。
$\boldsymbol{\varepsilon}$は3次ベクトルであり、$\boldsymbol{\varepsilon}^\wedge$における$\wedge$演算子は、[こちらのメモ](./lie-1.html)で定義されている。
$\mathbf{a}^\odot$は$4 \times 6$行列となる。

$$
  \mathbf{a}^\odot = \left[ \begin{array}{c} \boldsymbol{\varepsilon} \\ \eta \end{array} \right]^\odot
  = \left[ \begin{array}{cc} \eta \mathbf{I} & -\boldsymbol{\varepsilon}^\wedge \\
    \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right] \in \mathbb{R}^{4 \times 6}
$$

$(\mathbf{T} \mathbf{p})^\odot \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi}) \mathbf{1}_i$と$\mathbf{T} \mathbf{p}^\odot \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi}) \mathbf{1}_i$はそれぞれ、$4 \times 6$行列$(\mathbf{T} \mathbf{p})^\odot \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})$および$\mathbf{T} \mathbf{p}^\odot \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})$の、$i$列目のベクトルである。

以上より、全ての$i$について、上記の4次ベクトルを**列方向に**並べれば、$4 \times 6$行列の偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$が得られる。

$$
  \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
  = \left\{ \begin{array}{cc}
    (\mathbf{T} \mathbf{p})^\odot
    \boldsymbol{\mathcal{J}}_l(\boldsymbol{\xi})
    & \text{$\boldsymbol{\mathcal{J}}_l$を使うとき} \\
    \mathbf{T} \mathbf{p}^\odot
    \boldsymbol{\mathcal{J}}_r(\boldsymbol{\xi})
    & \text{$\boldsymbol{\mathcal{J}}_r$を使うとき} \end{array} \right.
$$

## 偏微分の計算 (その2)

上記の方法で偏微分$\cfrac{\partial \mathbf{T}}{\partial \xi_i}$あるいは$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$を求めるためには、ヤコビ行列$\boldsymbol{\mathcal{J}}_l$、$\boldsymbol{\mathcal{J}}_r$の計算が必要であり、非常に面倒である。
そこで、ヤコビ行列を計算せずに、これらの偏微分を求める方法を考える。

$\xi_i$について摂動を加えたときに得られる剛体変換を、先ほどは$\exp((\boldsymbol{\xi} + h \mathbf{1}_i)^\wedge)$のように表現したが、ここでは、$\exp((h \mathbf{1}_i)^\wedge) \mathbf{T}$、あるいは$\mathbf{T} \exp((h \mathbf{1}_i)^\wedge)$と表すことにする。
前者は**左側から**、後者は**右側から**、$h \mathbf{1}_i$に対応する微小な剛体変換$\exp((h \mathbf{1}_i)^\wedge)$を適用している。

- **左側から**適用する場合、偏微分$\cfrac{\partial \mathbf{T}}{\partial \xi_i}$、$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$は次のようになる。

  $$
    \begin{eqnarray}
      \frac{\partial \mathbf{T}}{\partial \xi_i}
      &=& \lim_{h \to 0} \frac{\exp((h \mathbf{1}_i)^\wedge) \mathbf{T} - \mathbf{T}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\left( \mathbf{I}
        + (h \mathbf{1}_i)^\wedge \right) \mathbf{T} - \mathbf{T}}{h} \\
      &=& (\mathbf{1}_i)^\wedge \mathbf{T}
    \end{eqnarray}
  $$

  これに右側から$\mathbf{p}$を付け足せば、偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}$は次のようになる。

  $$
    \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}
    = (\mathbf{1}_i)^\wedge \mathbf{T} \mathbf{p}
    = \left( \mathbf{T} \mathbf{p} \right)^\odot \mathbf{1}_i
  $$

  $(\mathbf{T} \mathbf{p})^\odot$は$4 \times 6$行列、$\mathbf{1}_i$は6次ベクトルであるから、上記の計算結果は確かに4次ベクトルとなる。
  $(\mathbf{T} \mathbf{p})^\odot \mathbf{1}_i$は、行列$(\mathbf{T} \mathbf{p})^\odot$の$i$列目のベクトルである。
  全ての$i$について、上記の4次ベクトルを列方向に並べれば、次のように$4 \times 6$の偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$が求まる。

  $$
    \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
    = (\mathbf{T} \mathbf{p})^\odot
  $$

  ここでは$\mathbf{p}$は、正確には同次座標$\left[ \begin{array}{c} \mathbf{p} \\ 1 \end{array} \right]$となっている。
  上記を計算してみると、次のようになる。

  $$
    \begin{eqnarray}
      \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
      = (\mathbf{T} \mathbf{p})^\odot
      = \left( \left[ \begin{array}{cc} \mathbf{C} & \mathbf{r} \\
        \mathbf{0}^\top & 1 \end{array} \right]
        \left[ \begin{array}{c} \mathbf{p} \\ 1 \end{array} \right] \right)^\odot
      = \left[ \begin{array}{c} \mathbf{C} \mathbf{p} + \mathbf{r} \\ 1 \end{array} \right]^\odot
      = \left[ \begin{array}{c} \mathbf{I} & -(\mathbf{C} \mathbf{p} + \mathbf{r})^\wedge \\
        \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    \end{eqnarray}
  $$

  上記の計算において、剛体変換は$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$、$\mathbf{T}$に対応するリー代数は$\boldsymbol{\xi} = \left[ \begin{array}{c} \boldsymbol{\phi} \\ \boldsymbol{\rho} \end{array} \right]$、$\mathbf{T}$の右上ブロックは$\mathbf{r} = \mathbf{J}_l(\boldsymbol{\phi}) \boldsymbol{\rho}$と表す。
  $\mathbf{C}$は剛体変換$\mathbf{T}$における回転行列、$\mathbf{r}$は$\mathbf{T}$における並進ベクトルとなる。
  $\mathbf{J}_l(\boldsymbol{\phi})$は、[こちらのメモ](./lie-2.html)で定義された、$\mathrm{SO}(3)$における左側バージョンのヤコビ行列である。

- **右側から**適用する場合、偏微分$\cfrac{\partial \mathbf{T}}{\partial \xi_i}$、$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$は次のようになる。

  $$
    \begin{eqnarray}
      \frac{\partial \mathbf{T}}{\partial \xi_i}
      &=& \lim_{h \to 0} \frac{\mathbf{T} \exp((h \mathbf{1}_i)^\wedge) - \mathbf{T}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\mathbf{T} \left(
        \mathbf{I} + (h \mathbf{1}_i)^\wedge \right) - \mathbf{T}}{h} \\
      &=& \mathbf{T} (\mathbf{1}_i)^\wedge
    \end{eqnarray}
  $$

  従って、偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}$は、右側から$\mathbf{p}$を付け足せば次のようになる。

  $$
    \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \xi_i}
    = \mathbf{T} (\mathbf{1}_i)^\wedge \mathbf{p}
    = \mathbf{T} \mathbf{p}^\odot \mathbf{1}_i
  $$

  $\mathbf{T} \mathbf{p}^\odot \mathbf{1}_i$は、$4 \times 6$行列$\mathbf{T} \mathbf{p}^\odot$の$i$列目のベクトルである。
  全ての$i$について、上記の4次ベクトルを列方向に並べれば、次のように$4 \times 6$の偏微分$\cfrac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}$が求まる。

  $$
    \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
    = \mathbf{T} \mathbf{p}^\odot
  $$

  上記を実際に計算してみると、次のようになる。

  $$
    \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
    = \mathbf{T} \mathbf{p}^\odot
    = \left[ \begin{array}{cc} \mathbf{C} & \mathbf{r} \\ \mathbf{0}^\top & 1 \end{array} \right]
    \left[ \begin{array}{c} \mathbf{I} & -\mathbf{p}^\wedge \\
      \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    = \left[ \begin{array}{c} \mathbf{C} & -\mathbf{C} \mathbf{p}^\wedge \\
      \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
  $$

  左側のときとは異なり、$\mathbf{r}$が含まれていない。

以上より、$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$の$\xi_i$に関する偏微分は、次のようになる。

$$
  \frac{\partial \mathbf{T}}{\partial \xi_i}
  = \left\{ \begin{array}{cc}
    (\mathbf{1}_i)^\wedge \mathbf{T} & \text{左側バージョン} \\
    \mathbf{T} (\mathbf{1}_i)^\wedge & \text{右側バージョン} \end{array} \right.
$$

また、$\mathbf{T} \mathbf{p}$の$\boldsymbol{\xi}$に関する偏微分は、次のようになる($\mathbf{T} = \left[ \begin{array}{cc} \mathbf{C} & \mathbf{r} \\ \mathbf{0}^\top & 1 \end{array} \right]$)。

$$
  \frac{\partial (\mathbf{T} \mathbf{p})}{\partial \boldsymbol{\xi}}
  = \left\{ \begin{array}{ll}
    (\mathbf{T} \mathbf{p})^\odot
    = \left[ \begin{array}{c} \mathbf{I} & -(\mathbf{C} \mathbf{p} + \mathbf{r})^\wedge \\
    \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    & \text{左側バージョン} \\
    \mathbf{T} \mathbf{p}^\odot
    = \left[ \begin{array}{c} \mathbf{C} & -\mathbf{C} \mathbf{p}^\wedge \\
    \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    & \text{右側バージョン} \end{array} \right.
$$

最初の方法と比較すると、ヤコビ行列$\boldsymbol{\mathcal{J}}_l$、$\boldsymbol{\mathcal{J}}_r$が消えているので、計算が楽になる。

## $\mathbf{T}^{-1} \mathbf{p}$の$\boldsymbol{\xi}$に関する偏微分

ここでは、2つ目の方法を使って、$\mathbf{T}^{-1} \mathbf{p}$の$\boldsymbol{\xi}$に関する偏微分を求める(自分が使うため)。
ただし、$\mathbf{T} = \exp(\boldsymbol{\xi}^\wedge)$、$\mathbf{T}^{-1} = \exp(-\boldsymbol{\xi}^\wedge)$である。
上記と同じように、左側バージョンと、右側バージョンの2種類を考える。

- **左側から**摂動を加えるときは、偏微分$\cfrac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}$は次のようになる。

  最初に、$\xi_i$についての偏微分を計算する。

  $$
    \begin{eqnarray}
      \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \xi_i}
      &=& \lim_{h \to 0} \frac{\exp(-(h \mathbf{1}_i)^\wedge)
        \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}
        - \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\left( \mathbf{I} - (h \mathbf{1}_i)^\wedge \right)
        \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}
        - \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}}{h} \\
      &=& - (\mathbf{1}_i)^\wedge \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p} \\
      &=& - (\mathbf{1}_i)^\wedge \mathbf{T}^{-1} \mathbf{p} \\
      &=& - \left( \mathbf{T}^{-1} \mathbf{p} \right)^\odot \mathbf{1}_i
    \end{eqnarray}
  $$

  最初の式変形は、$\exp(\mathbf{A}) \approx \mathbf{I} + \mathbf{A}$による。
  上記の4次ベクトルを、全ての$i$について列方向に並べれば、次のように、$4 \times 6$の偏微分を得る。

  $$
    \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}
    = - \left( \mathbf{T}^{-1} \mathbf{p} \right)^\odot
  $$

  $\mathbf{T} = \left[ \begin{array}{cc} \mathbf{C} & \mathbf{r} \\ \mathbf{0}^\top & 1 \end{array} \right]$のとき、$\mathbf{T}^{-1} = \left[ \begin{array}{cc} \mathbf{C}^\top & -\mathbf{C}^\top \mathbf{r} \\ \mathbf{0}^\top & 1 \end{array} \right]$である。
  これを上式に代入して計算すれば、次のようになる。

  $$
    \begin{eqnarray}
      \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}
      &=& - \left( \mathbf{T}^{-1} \mathbf{p} \right)^\odot \\
      &=& - \left( \left[ \begin{array}{cc} \mathbf{C}^\top & -\mathbf{C}^\top \mathbf{r} \\
        \mathbf{0}^\top & 1 \end{array} \right]
        \left[ \begin{array}{c} \mathbf{p} \\ 1 \end{array} \right] \right)^\odot \\
      &=& - \left[ \begin{array}{c} \mathbf{C}^\top \mathbf{p}
        - \mathbf{C}^\top \mathbf{r} \\ 1 \end{array} \right]^\odot \\
      &=& \left[ \begin{array}{cc} -\mathbf{I} &
        \left( \mathbf{C}^\top \mathbf{p} - \mathbf{C}^\top \mathbf{r} \right)^\wedge \\
        \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    \end{eqnarray}
  $$

- **右側から**摂動を加えるときは、偏微分$\cfrac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}$は次のようになる。

  最初に、$\xi_i$についての偏微分を計算する。

  $$
    \begin{eqnarray}
      \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \xi_i}
      &=& \lim_{h \to 0} \frac{\exp(-\boldsymbol{\xi}^\wedge)
        \exp(-(h \mathbf{1}_i)^\wedge) \mathbf{p}
        - \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}}{h} \\
      &\approx& \lim_{h \to 0} \frac{\exp(-\boldsymbol{\xi}^\wedge)
        \left( \mathbf{I} - (h \mathbf{1}_i)^\wedge \right) \mathbf{p}
        - \exp(-\boldsymbol{\xi}^\wedge) \mathbf{p}}{h} \\
      &=& -\exp(-\boldsymbol{\xi}^\wedge) (\mathbf{1}_i)^\wedge \mathbf{p} \\
      &=& -\mathbf{T}^{-1} (\mathbf{1}_i)^\wedge \mathbf{p} \\
      &=& -\mathbf{T}^{-1} \mathbf{p}^\odot \mathbf{1}_i
    \end{eqnarray}
  $$

  上記の4次ベクトルを、全ての$i$について列方向に並べれば、次のように、$4 \times 6$の偏微分が得られる。

  $$
    \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}
    = -\mathbf{T}^{-1} \mathbf{p}^\odot
  $$

  これを具体的に計算してみると、次のようになる。

  $$
    \begin{eqnarray}
      \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}
      &=& -\mathbf{T}^{-1} \mathbf{p}^\odot \\
      &=& -\left[ \begin{array}{cc} \mathbf{C}^\top & -\mathbf{C}^\top \mathbf{r} \\
        \mathbf{0}^\top & 1 \end{array} \right]
        \left[ \begin{array}{c} \mathbf{p} \\ 1 \end{array} \right]^\odot \\
      &=& -\left[ \begin{array}{cc} \mathbf{C}^\top & -\mathbf{C}^\top \mathbf{r} \\
        \mathbf{0}^\top & 1 \end{array} \right]
        \left[ \begin{array}{cc} \mathbf{I} & -\mathbf{p}^\wedge \\
        \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right] \\
      &=& \left[ \begin{array}{cc} -\mathbf{C}^\top & \mathbf{C}^\top \mathbf{p}^\wedge \\
        \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    \end{eqnarray}
  $$

以上より、$\mathbf{T}^{-1} \mathbf{p}$の$\boldsymbol{\xi}$に関する偏微分は、次のようになる。

$$
  \frac{\partial (\mathbf{T}^{-1} \mathbf{p})}{\partial \boldsymbol{\xi}}
  = \left\{ \begin{array}{ll}
    - \left( \mathbf{T}^{-1} \mathbf{p} \right)^\odot
    = \left[ \begin{array}{cc} -\mathbf{I} &
    \left( \mathbf{C}^\top \mathbf{p} - \mathbf{C}^\top \mathbf{r} \right)^\wedge \\
    \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    & \text{左側バージョン} \\
    - \mathbf{T}^{-1} \mathbf{p}^\odot
    = \left[ \begin{array}{cc} -\mathbf{C}^\top & \mathbf{C}^\top \mathbf{p}^\wedge \\
    \mathbf{0}^\top & \mathbf{0}^\top \end{array} \right]
    & \text{右側バージョン} \end{array} \right.
$$

## 参考文献

- [State Estimation for Robotics](http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf)
- [Introduction to Visual SLAM: From Theory to Practice](https://github.com/gaoxiang12/slambook-en)

