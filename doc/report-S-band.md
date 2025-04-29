
# Table of Contents

1.  [Измерения параметров патч-антенн S-диапазона](#orgbb58c42)
    1.  [Патч-антенна на 2.32 ГГц](#orgc8a63c7)
        1.  [Измерения без резистора (R = $\infty$)](#org1042615)
        2.  [Измерения с резистором (R = 100 Ом)](#org23bbe58)
    2.  [Патч-антенна на 2.42 ГГц](#org847857a)
        1.  [Измерения без резистора (R = $\infty$)](#org948b4b5)
        2.  [Измерения с резистором (R = 100 Ом)](#org3801a29)
    3.  [Измерение коэффициента направленного действия антенн](#org61842bf)
    4.  [Оценка коэффициента усиления антенн](#orge020571)
    5.  [Заключение](#org7beee8e)


<a id="orgbb58c42"></a>

# Измерения параметров патч-антенн S-диапазона


<a id="orgc8a63c7"></a>

## Патч-антенна на 2.32 ГГц

Измерения патч-антенны проводились в двух режимах:

1.  Без резистора в цепи делителя Вилкинсона (R = $\infty$)
2.  С резистором

Без резитора измерения S-параметров указывают на ширину полосы самой
антенны. С припаянным резистором измеряется ширина полосы не антенны,
а самого делителя (она больше ширины полосы антенны).

Измерения показали, что резонансная частота антенны отличается от
расчетной примерно на 2 процента. Поэтому для справки на графиках
зависимости коэффициента отражения от частоты приведены как исходные
расчетные данные, так и смещенные на эти самые 2 процента по частоте.


<a id="org1042615"></a>

### Измерения без резистора (R = $\infty$)

<div class="ORG" id="org87545ce">

<div id="org589a34a" class="figure">
<p><img src="images/report_ant_2_32GHz_infR.svg" alt="report_ant_2_32GHz_infR.svg" class="org-svg" />
</p>
<p><span class="figure-number">Figure 1: </span>Патч 2.32 ГГц, R = \(\infty\)</p>
</div>

</div>

<div class="ORG" id="org282b03f">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 1:</span> Полосы частот антенны 2.32 ГГц (R = \(\infty\))</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">Центральная частота, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, %</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">HFSS, original</td>
<td class="org-right">2.3220</td>
<td class="org-right">0.1060</td>
<td class="org-right">4.5650</td>
</tr>

<tr>
<td class="org-left">HFSS, shifted</td>
<td class="org-right">2.2756</td>
<td class="org-right">0.1039</td>
<td class="org-right">4.5650</td>
</tr>

<tr>
<td class="org-left">Measured</td>
<td class="org-right">2.2748</td>
<td class="org-right">0.1125</td>
<td class="org-right">4.9456</td>
</tr>
</tbody>
</table>

</div>


<a id="org23bbe58"></a>

### Измерения с резистором (R = 100 Ом)

<div class="ORG" id="orgdebd8bf">

<div id="org85d5be3" class="figure">
<p><img src="images/report_ant_2_32GHz_100R.svg" alt="report_ant_2_32GHz_100R.svg" class="org-svg" />
</p>
<p><span class="figure-number">Figure 2: </span>Патч 2.32 ГГц, R = 100 Ohm</p>
</div>

</div>

<div class="ORG" id="orge2f3d59">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 2:</span> Полосы частот антенны 2.32 ГГц (R = 100 Ohm)</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">Центральная частота, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, %</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">HFSS, original</td>
<td class="org-right">2.3100</td>
<td class="org-right">0.5280</td>
<td class="org-right">22.8571</td>
</tr>

<tr>
<td class="org-left">HFSS, shifted</td>
<td class="org-right">2.2638</td>
<td class="org-right">0.5174</td>
<td class="org-right">22.8571</td>
</tr>

<tr>
<td class="org-left">Measured</td>
<td class="org-right">2.2763</td>
<td class="org-right">0.5385</td>
<td class="org-right">23.6573</td>
</tr>
</tbody>
</table>

</div>


<a id="org847857a"></a>

## Патч-антенна на 2.42 ГГц


<a id="org948b4b5"></a>

### Измерения без резистора (R = $\infty$)

<div class="ORG" id="orgcef7d09">

<div id="orgc140d53" class="figure">
<p><img src="images/report_ant_2_42GHz_infR.svg" alt="report_ant_2_42GHz_infR.svg" class="org-svg" />
</p>
<p><span class="figure-number">Figure 3: </span>Патч 2.42 ГГц, R = inf</p>
</div>

</div>

<div class="ORG" id="org706b8c3">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 3:</span> Полосы частот антенны 2.42 ГГц (R = infty)</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">Центральная частота, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, %</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">HFSS, original</td>
<td class="org-right">2.4250</td>
<td class="org-right">0.1160</td>
<td class="org-right">4.7835</td>
</tr>

<tr>
<td class="org-left">HFSS, shifted</td>
<td class="org-right">2.3765</td>
<td class="org-right">0.1137</td>
<td class="org-right">4.7835</td>
</tr>

<tr>
<td class="org-left">Measured</td>
<td class="org-right">2.3768</td>
<td class="org-right">0.1155</td>
<td class="org-right">4.8596</td>
</tr>
</tbody>
</table>

</div>


<a id="org3801a29"></a>

### Измерения с резистором (R = 100 Ом)

<div class="ORG" id="orgfb22fde">

<div id="org5ee49f4" class="figure">
<p><img src="images/report_ant_2_42GHz_100R.svg" alt="report_ant_2_42GHz_100R.svg" class="org-svg" />
</p>
<p><span class="figure-number">Figure 4: </span>Патч 2.42 ГГц, R = 100 Ohm</p>
</div>

</div>

<div class="ORG" id="orgda1457e">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 4:</span> Полосы частот антенны 2.42 ГГц (R = 100 Ohm)</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">Центральная частота, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, ГГц</th>
<th scope="col" class="org-right">Ширина полосы, %</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">HFSS, original</td>
<td class="org-right">2.4215</td>
<td class="org-right">0.4290</td>
<td class="org-right">17.7163</td>
</tr>

<tr>
<td class="org-left">HFSS, shifted</td>
<td class="org-right">2.3731</td>
<td class="org-right">0.4204</td>
<td class="org-right">17.7163</td>
</tr>

<tr>
<td class="org-left">Measured</td>
<td class="org-right">2.3843</td>
<td class="org-right">0.4815</td>
<td class="org-right">20.1950</td>
</tr>
</tbody>
</table>

</div>


<a id="org61842bf"></a>

## Измерение коэффициента направленного действия антенн

Для измерения КНД патч-антенн одинаковые антенны располагались на
подставках на расстоянии L = 150 см друг от друга. Исходно антенны
ориентированы друг на друга, а в процессе измерения варьируется угол
установки одной из антенн $\theta$. Измерению подлежит коэффициент
передачи между антеннами S21. Измерения были проведены для двух
взаимных осевых ориентаций антенн ($\phi = 0$ и $\phi = 90$ градусов).

Результаты расчета и эксперимента для обеих антенн приведены ниже.

![img](images/directivity_reference_2_32ghz.png "Нормированный на 0 коэффициент направленного действия антенны на 2.32 ГГц, расчет")

![img](images/directivity_measured_2_32ghz.png "Нормированный на 0 коэффициент направленного действия антенны на 2.32 ГГц, измерение")

![img](images/directivity_reference_2_32ghz.png "Нормированный на 0 коэффициент направленного действия антенны на 2.42 ГГц, расчет")

![img](images/directivity_measured_2_32ghz.png "Нормированный на 0 коэффициент направленного действия антенны на 2.42 ГГц, измерение")

<table id="org6913053" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 5:</span> Ширины ДН антенн по уровню -3 дБ относительно максимума</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Тип</th>
<th scope="col" class="org-left">Значение</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">ДН 2.32 ГГц, расчет</td>
<td class="org-left">94..99 град</td>
</tr>

<tr>
<td class="org-left">ДН 2.32 ГГц, измерение</td>
<td class="org-left">100±5 град</td>
</tr>

<tr>
<td class="org-left">ДН 2.42 ГГц, расчет</td>
<td class="org-left">94..97 град</td>
</tr>

<tr>
<td class="org-left">ДН 2.42 ГГц, измерение</td>
<td class="org-left">98±3 град</td>
</tr>
</tbody>
</table>

Видно, что измеренные ширины ДН согласуются с расчетными


<a id="orge020571"></a>

## Оценка коэффициента усиления антенн

Две антенны размещались на расстоянии около 1.5 метров друг от друга и
подключались к портам векторного анализатора цепей. Далее вариацией
взаимного поворота антенн и высоты установки подбиралось положение,
максимизирующее коэффициент передачи S<sub>21</sub>.

Для одинаковых антенн по формулу Фрииса можно оценить значение
коэффициента усиления:

\begin{equation*}
G = \cfrac{1}{2} \left(S_{21} - 20 \lg{\cfrac{\lambda}{4 \pi D}} + CableLoss\right)
\end{equation*}

Здесь $CableLoss$ &#x2013; потери в подводящих кабелях, измеряются путем
соединения портов векторного анализатора использованными кабелями и
измерением их коэффициента передачи S21.

<table id="org8b06f2e" border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 6:</span> Результаты измерения коэффициента усиления антенн</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Тип антенны</th>
<th scope="col" class="org-left">Частота Fc</th>
<th scope="col" class="org-left">Расстояние L</th>
<th scope="col" class="org-left">Коэффициент Фрииса</th>
<th scope="col" class="org-left">Cable Loss</th>
<th scope="col" class="org-left">Gain (измеренный)</th>
<th scope="col" class="org-left">Gain (расчет)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">патч 2.32 ГГц</td>
<td class="org-left">2.284 ГГц</td>
<td class="org-left">150 см</td>
<td class="org-left">-43.1 дБ</td>
<td class="org-left">5.1 дБ</td>
<td class="org-left">7.1 дБи</td>
<td class="org-left">5.7 дБи</td>
</tr>

<tr>
<td class="org-left">патч 2.42 ГГц</td>
<td class="org-left">2.362 ГГц</td>
<td class="org-left">150 см</td>
<td class="org-left">-43.4 дБ</td>
<td class="org-left">5.6 дБ</td>
<td class="org-left">6.6 дБи</td>
<td class="org-left">5.6 дБи</td>
</tr>
</tbody>
</table>

Видно, что измеренные значение отличаются от расчетных в большую
сторону. Это обуславливается тем, что измерения проводились не в
безэховой камер &#x2013; влияние паразитных отражений приводило к
эффективному увеличению КНД антенн и, как следствие, максимального
значения коэффициента усиления.


<a id="org7beee8e"></a>

## Заключение

Обе антенны имеют похожие характеристики:

1.  Ширина полосы антенны без делителя Вилкинсона: 5 процентов
2.  Ширина полосы делителя: 20 процентов
3.  Резонансные частоты отличаются от расчетных на 2 процента в меньшую сторону
4.  Измерения ДН показывают согласие ее формы (в частности, ширины по уровню -3 дБ) с расчетными.
5.  Значения КУ изготовленных антенн находятся в удовлетворительном
    согласии с расчетом, если принимать во внимание неточность
    измерения, связанную с отражением от стен комнаты.

По итогу &#x2013; требуется коррекция размера патч-антенн с учетом
фактической резонансной частоты.

