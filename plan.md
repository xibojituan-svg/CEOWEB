Implementation Plan, Task List and Thought in Chinese

## 分析 (Thought)

用户的需求是：在 `index.html` 的“每周工作追踪”模块和“核心团队建设”模块中增加直接连接到高管（特别是王俊）的最新策略评价页面的链接，并在 `CoreTeam.html` 的高管介绍模块中增加同样的链接。

**目标拆解：**

1.  **修改 `index.html`：**
    *   **“每周工作追踪”模块：** 找到类似“2026-02-28 | Week 8 核心复盘”的地方，增加王俊（或其他高管）的策略评价页面链接。目前“每周战略追踪”里有三块（Week 4、Week 5、Week 8 核心复盘 以及 CEO核心工作动态清单）。我可以添加一个新的卡片，或者在现有卡片（如下周重点中）增加链接。考虑到是“02-28 内部会议”产生的策略评审，可以增加一个针对“组织与后台（王俊）”的策略追踪卡片。
    *   **“核心团队建设”模块：** 在王俊的头像/介绍下方，增加一个指向 `WangJun_Strategy_Review_0228.html` 的链接（类似“查看最新策略评审”），也可以给马长久、苏秦、姚涣等预留或者指向他们现有的 OKR Analysis 页面（如存在）。我先重点处理“王俊”。当然，用户的要求是“在每周工作追踪模块中建立对于每个高管的最新策略评价页面的链接”（这里说“每个”可能有点大，但特别强调了“除了王俊外其他高管也可以加”，不过我们刚生成了王俊的），我目前只确认有 `WangJun_Strategy_Review_0228.html` 和各业务线的 OKR (如 `HRD_OKR_Analysis_2026.html`)。等等，我可以把“每个高管的最新的OKR/策略评价”建立链接。
        *   马长久 -> First Curve 负责人 -> 好像没有专门他的名字命名的，但有 `Curve1_Ops_Analysis_2026.html` / `ExecutivePerformance.html`
        *   苏秦 -> `Content_OKR_Analysis_2026.html` / `ExecutivePerformance.html`
        *   姚涣 -> `CTO_OKR_Analysis_2026.html` / 第二曲线
        *   王俊 -> `WangJun_Strategy_Review_0228.html`
        *   杜康杰 -> 体验，315，`CX_OKR_Analysis_2026.html`
        为了不破坏原版式，在 `index.html` 的人物卡片下面加一个小按钮或链接，如“▶ 最新战略指标”。

2.  **修改 `CoreTeam.html`：**
    *   在高管介绍模块（包含马长久、苏秦、姚涣、杜康杰、王俊等），目前已经有 `🎯 核心指标 (BSC/GSA)`，我可以紧挨着或在职责下方增加一行 `📖 最新策略看板：[链接]`。
    *   马长久：`Curve1_Ops_Analysis_2026.html` 或者直接引向 `ExecutivePerformance.html`
    *   姚涣：`CTO_OKR_Analysis_2026.html`
    *   苏秦：`Content_OKR_Analysis_2026.html`
    *   杜康杰：`CX_OKR_Analysis_2026.html`
    *   王俊：`WangJun_Strategy_Review_0228.html`

**计划：**

**第一步：更新 `index.html`**
1. 在 "每周战略追踪 (Weekly Strategy Tracking)" (约 760 行) 添加一个新的卡片，专题展示“高管战略对齐与演进”，里面可以放各个高管最新战略的大盘链接，或者专门加一个高管个人专属链接。或者直接修改卡片。还是加一个大卡片比较醒目，或者放在“核心团队”下面。
    * 用户原话：“在首页的每周工作追踪模块中建立对于每个高管的最新策略评价页面的链接”
    * 当前有 4 个 Card (grid)。我可以直接在每个Card下面加，或者新增一个Card专门放高管的链接。
    * 新增一个卡片：“Week 8 高管战略演进”。
2. 在 "核心团队建设 (Team Building)" 的 grid 里面 (马长久, 王俊, 杜康杰等 Card, 约890行起)。为每个高管增加一个小的“查看最新策略”的标签或链接。

**第二步：更新 `CoreTeam.html`**
1. 找到 `CoreTeam.html` 里的高管介绍。
2. 为蒋德铭、马长久、苏秦、姚涣、杜康杰、王俊等人增加“最新策略评价”链接。

**第三步：使用工具编辑并验证**
使用 `multi_replace_file_content`，避免多步骤出错。

**第四步：部署**
最后执行 `deploy.sh`。

## 任务清单 (Task List)
- [ ] 审视并确定在 `index.html` 中的具体替换目标代码。
- [ ] 执行替换操作，增加高管策略链接。
- [ ] 审视并确定在 `CoreTeam.html` 中的具体替换目标代码。
- [ ] 执行替换操作，增加高管策略链接。
- [ ] 运行部署脚本推送更新。
