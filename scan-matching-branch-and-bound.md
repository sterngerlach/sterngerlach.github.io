
---
title:  分枝限定法によるスキャンマッチング
author: SternGerlach
---

<!--
 pandoc -s --filter pandoc-crossref -M "crossrefYaml=./crossref_config.yaml" -f markdown -t html5 --mathjax --css style.css scan-matching-branch-and-bound.md > scan-matching-branch-and-bound.html
-->

[ホームに戻る](./index.html)

# このページについて

このページは、慶應理工アドベントカレンダー2021の15日目の記事です。

## スキャンマッチングとSLAM

皆さんは、2Dの占有格子地図(Occupancy Grid Map)と、2D LiDARから取得したスキャンデータを重ね合わせて、ロボットの現在の自己位置を推定したいと思ったことがあると思います。
このような重ね合わせ処理のことを、**スキャンマッチング**(Scan Matching)といいます。

- 占有格子地図とは、環境(2次元の平面)を格子状に区切って、それぞれの格子に障害物が存在する確率(占有確率)を割り当てるものです。
またLiDAR(Light Detection And Ranging)は、センサから周囲の環境に向けてレーザ光を照射し、その反射光を受光素子で検出することで、センサからみた障害物までの距離(Range, Distance)と方向(Angle, Bearing)を取得します。
レーザ光が障害物に当たって跳ね返り、センサの中心まで戻ってくるまでの時間(Time of Flight)を計測することで、障害物までの距離を計算できます。
LiDARセンサが回転しながら、あらゆる方向に対してレーザ光を照射するので、周囲の様々な障害物までの、距離と方向のペアが幾つも得られます。
LiDARセンサ1周分のデータをスキャンといい、周囲360度にある障害物(家具や壁など)の形状を反映した**点群**(Point Cloud)となります。

スキャン同士、スキャンと地図、地図同士など、重ね合わせの対象には幾つかの種類がありますが、Scan-to-scan Matching、Scan-to-map Matching、Map-to-map Matchingなどと呼んで区別します。
ここでは、**スキャンと占有格子地図の重ね合わせ**(Scan-to-map)を扱いますが、スキャン同士(Scan-to-scan)の場合と比べると誤差が小さいとされています。
ICP(Iterative Closest Point)とその派生は、スキャン同士のマッチング手法、NDT(Normal Distributions Transform)は、スキャンと地図のマッチング手法に分類できます(NDTは占有格子地図ではなく、各格子が正規分布を表す格子地図を使います)。

スキャンマッチングは、自己位置推定と地図構築、言い換えるとSLAM(Simultaneous Localization And Mapping)の核となる極めて重要な処理です。
SLAMでは、ロボットの自己位置(ロボットが辿った軌跡)と、環境地図(占有格子地図)の2つを推定しますが、これらの精度は、どのようなスキャンマッチングの手法を採用するかによって大きく左右されます。
各手法には長所と短所があるので、計算量、メモリ消費、精度などの様々な観点から、最適なものを1つ選んで用いたり、あるいは複数の手法を組み合わせて用いたりすることが重要です。

## 分枝限定法によるスキャンマッチング - 概要

2次元LiDAR SLAMの最先端であるGoogle Cartographerでは、**ループ検出**とよばれる処理に、分枝限定法(Branch-and-bound)ベースのスキャンマッチング手法を用いています。
ループ検出(Loop Detection)とは、ロボットが以前訪れた場所に、再び戻ってきたことを検出するための処理で、スキャンマッチングにより実現されます。

- SLAMでは通常、直近の幾つかのLiDARスキャンをもとに占有格子地図を作成し、最新のLiDARスキャンをこの地図とマッチングすることで、ロボットの現在位置を更新していきます。
しかし、上記のような、**直近の観測データ**と最新の観測データとのマッチングだけを繰り返していくと、ロボットの現在位置には誤差が累積していき、本来の正しい位置から大きく外れてしまいます。
ループ検出では、**古い観測データ**と最新の観測データとのマッチングを行います。
これによって、ある場所を訪れてから、再びそこを訪れるまでの間に溜まった誤差を一気に解消し、ロボットの現在位置を本来の正しい位置に戻すことができます。

ループ検出では、(以前その場所を訪れたときに取得した)古いスキャンを含む地図と、最新のスキャンとのマッチングを行います。
直近のスキャンと、最新のスキャンとのマッチングによって、ロボットの現在位置は一応得られています。
しかし、本来の位置からは大きくずれているので、ループ検出によって大幅に修正されるでしょう。
大幅に修正されるということは、初期値と最適解とが離れているということです。

ガウス・ニュートン法(Gauss-Newton)やレーベンバーグ・マーカート法(Levenberg-Marquardt)、山登り法(Hill-Climbing)のような逐次的なマッチング手法では、初期値が最適解にある程度近いことが要求されます。
言い換えると、ロボットの現在位置が真値とかなり近く、誤差が少ない状態である(地図とスキャンとが既にある程度重なり合っている)ことが求められますが、ループ検出での前提とは異なります。
従って、逐次的なマッチング手法は利用できず、初期値に依存しない頑健な手法が求められます。
分枝限定法によるスキャンマッチングは、効率が良く、しかも頑健な手法であるため、ループ検出に利用できます。

## 分枝限定法によるスキャンマッチング - 下準備

今まではロボットの位置と書きましたが、平面上の位置($x$座標と$y$座標)に加えて、実際にはロボットの向き(回転角$\theta$)も考慮しなければなりません。
並進成分($x$、$y$)と回転成分($\theta$)とがセットになったものを、位置とは区別して**姿勢**(Pose)とよびます。
2次元の姿勢は、$x$、$y$、$\theta$(ヨー角)の3成分で表されますが、3次元の場合は、$x$、$y$、$z$、$\phi$(ロール角)、$\theta$(ピッチ角)、$\psi$(ヨー角)の6成分で表されます。
2次元の姿勢を、ここでは$\mathbf{\xi} = \left[ \xi_x, \xi_y, \xi_\theta \right]^\top$と表記します。

スキャンデータは、LiDARセンサの中心から、障害物までの距離$r$と方向$\theta$のセットです。
これを$\mathcal{S} = \left\{ \mathbf{z}_1, \ldots, \mathbf{z}_N \right\} = \left\{ \left( r_1, \theta_1 \right), \ldots, \left( r_N, \theta_N \right) \right\}$と表しましょう。
$r \ge 0$、$-\pi \le \theta < \pi$が成立するほか、$N$は、スキャンデータに含まれる点の個数です。
$\mathbf{z}_i = \left( r_i, \theta_i \right)$は、単一のスキャン点(距離と方向のペア)です。
距離と方向は、いずれもLiDARの中心を原点とした座標系(LiDAR座標系)で表されます。

占有格子地図を$\mathcal{M}$とします。
$\mathcal{M}$の$(i, j)$番目の格子に対応する占有確率(Occupancy Probability)は$\mathcal{M}(i, j)$で表します($0 \le \mathcal{M}(i, j) \le 1$)。
格子のサイズ(Resolution)を$r$とします。

ロボットの姿勢$\mathbf{\xi}$は、地図座標系からみたLiDAR座標系の姿勢(座標変換、剛体変換)として捉えられます。
各スキャン点$\mathbf{z}_i = (r_i, \theta_i)$はLiDAR座標系ですが、姿勢$\mathbf{\xi} = \left[ \xi_x, \xi_y, \xi_\theta \right]^\top$を使えば、地図座標系に変換できます(スキャン点が、地図上でどの位置に対応するのかが分かります)。
以下の式によって、スキャン点$\mathbf{z}_i$を地図上の座標$\mathbf{p}_i = \left[ p_{i, x}, p_{i, y} \right]^\top = \varphi(\mathbf{\xi}, \mathbf{z}_i) \in \mathbb{R}^2$に変換できます($\mathbf{z}_i$は極座標ですが、$\mathbf{p}_i = \varphi(\mathbf{\xi}, \mathbf{z}_i)$は直交座標とします)。
$$
  \mathbf{p}_i = \varphi(\mathbf{\xi}, \mathbf{z}_i)
  = \left[ \begin{array}{c} p_x \\ p_y \end{array} \right]
  = \left[ \begin{array}{c} \xi_x + r_i \cos(\xi_\theta + \theta_i) \\
  \xi_y + r_i \sin(\xi_\theta + \theta_i) \end{array} \right] \in \mathbb{R}^2
$$

地図上の点$\mathbf{p}_i = \varphi(\mathbf{\xi}, \mathbf{z}_i)$における占有確率を考えましょう。
点$\mathbf{p}_i$と対応する格子のインデックス$(i, j)$は、各座標$p_x$、$p_y$を、格子のサイズ$r$で割れば求められます。
$\lfloor x \rfloor$は床関数であり、$x$以下の最大の整数を返します。
$$
  (i, j) = \left( \left\lfloor \frac{p_x}{r} \right\rfloor, \
  \left\lfloor \frac{p_y}{r} \right\rfloor \right) \in \mathbb{Z}^2
$$
この$(i, j)$を用いれば、地図上の点$\mathbf{p}_i$における占有確率は$\mathcal{M}(i, j)$と書けます。
ここでは簡潔さのために、$\mathbf{p}_i$における占有確率を単に$\mathcal{M}(\mathbf{p}_i)$で表しましょう。

## 分枝限定法によるスキャンマッチング - 定式化

スキャンマッチングでは、スコア関数$s(\mathbf{\xi}; \mathcal{M}, \mathcal{S})$を、ロボットの姿勢$\mathbf{\xi}$について最大化することで、最適な姿勢$\mathbf{\xi}^*$を求めます。
$$
  \mathbf{\xi}^* = \arg \max_{\mathbf{\xi}} s(\mathbf{\xi}; \mathcal{M}, \mathcal{S})
$$
スコア関数$s(\mathbf{\xi})$は次のように定義できます(最小値は$0$、最大値は$N$)。
$$
  s(\mathbf{\xi}; \mathcal{M}, \mathcal{S})
  = \sum_{i = 1}^N \mathcal{M}(\mathbf{p}_i)
  = \sum_{i = 1}^N \mathcal{M}(\varphi(\mathbf{\xi}, \mathbf{z}_i))
$$

- ガウス・ニュートン法などの逐次的な(勾配を基にした)手法では、上記の最大化の代わりに、以下の二乗誤差の最小化を考えます(ここでは忘れましょう)。
$$
  \sum_{i = 1}^N \left( 1 - \mathcal{M}(\mathbf{p}_i) \right)^2
  = \sum_{i = 1}^N \left( 1 - \mathcal{M}(\varphi(\mathbf{\xi}, \mathbf{z}_i)) \right)^2
$$

- 姿勢$\mathbf{\xi}$が正しいとします。
その姿勢を使って、スキャン点$\mathbf{z}_i$と対応する地図上の座標$\mathbf{p}_i$を求めると、その点における占有確率$\mathcal{M}(\mathbf{p}_i)$は$1$に近いはずです。
なぜかといえば、スキャン点は障害物の存在を表しているためです(スキャン点が指し示している地図上の格子は、障害物に占有されているべき)。
従って、姿勢$\mathbf{\xi}$が正しければ、スキャン点に対応する占有確率は大きく、その結果としてスコアも高くなるはずです。

- 一方、姿勢$\mathbf{\xi}$が正しくないとすると、$\mathcal{M}(\mathbf{p}_i)$は本来であれば$1$に近いはずなのに、実際には$0$に近い($\mathbf{p}_i$は障害物を指し示しているはずなのに、地図上で確認すると何もないことになっていて矛盾する)といったことが頻繁に発生するので、スコアは低くなるでしょう。
従ってスコア$s(\mathbf{\xi}; \mathcal{M}, \mathcal{S})$は、姿勢$\mathbf{\xi}$のもとで、占有格子地図$\mathcal{M}$とLiDARスキャン$\mathcal{S}$とが、どの程度綺麗に重なり合うのかを表します。


