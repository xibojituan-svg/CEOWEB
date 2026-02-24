---
name: weekly-meeting-analyzer
description: 分析每周会议纪要，判断战略拆解执行情况及战略反推需求，评估核心成员胜任情况。综合了 artyomx33（第一性原理、MSPOT、逆向思考等）和 marketing-mode 的战略与复盘思维。
---

# 周会战略分析器 (Weekly Meeting Strategic Analyzer)

## 核心目的 (Core Purpose)

快速从复杂的周会纪要中提取高价值的“战略信号”。

1. **判断战略对齐度**：本周讨论和决议是否在既定的战略拆解路径上（MSPOT框架）。
2. **发现战略盲区（反向推动）**：本周暴露的问题中，有哪些是原战略指标未考虑到的（First Principles / Inversion）。
3. **核心成员胜任力评估**：从各成员的动作反馈，判断是“策略不清楚”还是“执行不到位”。

## 分析维度与对应的方法论 (Analytical Dimensions)

### 1. 战略对齐与拆解进度 (Strategic Alignment & Progress)

* **应用工具**：MSPOT (Mission, Strategy, Projects, Omissions, Tracking)
* **分析视角**：
  * 本周各部门的“核心事项”是否在推进既定的 Projects 和 Tracking 指标？
  * 是否有部门在做应该被 Omissions (明确不做) 的事情？
  * **判断标准**：高度对齐 / 局部偏离 / 严重跑题

### 2. 战略盲区与反向修正 (Strategic Blindspots & Reverse Push)

* **应用工具**：First Principles (第一性原理), Inversion (逆向思考)
* **分析视角**：
  * 本周暴露的“客户之声”或“负面反馈”深层原因是什么？（剥离表象，直击本质）
  * 若放任此问题，会如何引发战略级失败？（Inversion）
  * 当前的 BSC (平衡计分卡) 指标是防住了这个风险，还是甚至在“鼓励”这个风险？
  * **结论导向**：需要新增/修改什么战略指标或流程闭环。

### 3. 核心成员胜任力透视 (Core Member Competency)

* **分析视角**：区分“策略问题”与“执行问题”。
  * **策略不清楚**：成员提出的动作散乱，没有抓手，或者与公司当前核心矛盾不符。（需要上级介入辅导策略）
  * **执行不到位**：方向没问题，但关键指标进度（🔴/🟡）落后，或承诺的 ToDo 逾期、跨部门协同卡壳。（需要介入督办执行）
  * **胜任力评价**：A (引领战略) / B (稳健执行) / C (策略或执行存疑，需辅导)

## 分析输出格式 (Output Format)

```html
<!-- 生成 HTML 格式的分析报告 -->
<div class="weekly-analysis-report">
    <h2>周会战略分析报告: [会议日期]</h2>
    
    <div class="section alignment">
        <h3>1. 战略拆解与对齐评估 (Strategic Alignment)</h3>
        <p><strong>整体状态：</strong>[高度对齐 / 局部偏离 / 重点预警]</p>
        <ul>
            <li><strong>正向表现：</strong>[哪些动作紧扣核心战略]</li>
            <li><strong>偏离预警：</strong>[是否存在偏离 MSPOT 核心项目、或是陷入无效细节的动作]</li>
        </ul>
    </div>

    <div class="section blindspots">
        <h3>2. 战略盲区与反向修正建议 (Strategic Blindspots)</h3>
        <ul>
            <li><strong>关键发现：</strong>[基于本周问题（如客诉/数据下降），发现的战略级遗漏]</li>
            <li><strong>深层归因 (第一性原理)：</strong>[问题背后的本质是什么]</li>
            <li><strong>反向推动建议：</strong>[建议修改哪个 BSC 指标，或补充什么流程机制以避免失败(Inversion)]</li>
        </ul>
    </div>

    <div class="section competency">
        <h3>3. 核心成员动作与胜任力透视 (Member Competency)</h3>
        <table>
            <tr><th>核心成员</th><th>本周关键动作</th><th>状态诊断 (策略/执行)</th><th>管理建议</th></tr>
            <tr>
                <td>[@Name]</td>
                <td>[核心动作简述]</td>
                <td>[策略清晰/执行坚决 或 策略模糊/执行卡壳]</td>
                <td>[继续保持 / 需对齐策略 / 需强化督办]</td>
            </tr>
            <!-- 遍历关键成员 -->
        </table>
    </div>
</div>
```

## 执行方式 (Execution Trigger)

当被要求“使用周会评审skill分析[某某纪要]”时，严格按照以上三个维度的视角，提取文档中的信息进行归纳和翻译，最终输出指定格式的 HTML 代码。
