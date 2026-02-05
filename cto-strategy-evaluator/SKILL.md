---
name: CTO & R&D Strategy Evaluator (Dual Curve & IPO)
description: A strategic framework for evaluating a CTOs plan to balance Legacy Stability (Curve 1) with Innovation Speed (Curve 2) and IPO Compliance.
---

# CTO Strategy Evaluator: The Architect & The Builder

此 Skill 旨在帮助 CEO 或董事会评估 **CTO / 产研负责人** 的战略规划。
核心挑战：如何在未来3年 IPO 冲刺期，既要**维护第一曲线（遗留系统）的稳定**，又要**支持第二曲线（创新业务）的极速迭代**，同时满足**上市合规（审计与安全）**的严苛要求。

## **核心理念 (Core Philosophy)**

一个胜任上市冲刺期的 CTO，不能只是“技术大拿”或“需求翻译机”，而必须是**“资产分层专家” (Asset Portfolio Manager)** 和 **“熵增抵抗者” (Entropy Fighter)**。

## **评估核心顺序 (Evaluation Order)**

判断逻辑必须遵循：**先分层（架构），再分队（组织），后负债（取舍），最后安检（合规）。**

### **Step 1: 架构分层策略 (The "Pace Layering" Test)**
**目标**：解决“快与慢”的矛盾。

*   **核心理论**：
    *   **Gartner's Pace Layering Strategy (配速分层策略)**：
        *   *评估点*：CTO 是否强行把所有业务都塞进一个单体巨石应用里？
        *   *Pass标准*：
            *   **第一曲线（记录系统 Systems of Record）**：核心交易、财务、ERP。追求：**稳定、准确、合规**。变革速率：慢。
            *   **第二曲线（创新系统 Systems of Innovation）**：AI 应用、新增长点、试错项目。追求：**速度、灵活性**。变革速率：极快。
            *   *红线*：绝不允许为了第二曲线的一个小功能，去修改且重启第一曲线的核心财务系统。必须通过 **API / 中台** 进行隔离。

### **Step 2: 组织与架构映射 (The "Conway" Test)**
**目标**：解决“人多反而乱”的问题。

*   **核心理论**：
    *   **Inverse Conway Maneuver (逆康威定律)**：
        *   *评估点*：组织结构是否阻碍了架构的解耦？
        *   *Pass标准*：
            *   **平台型团队 (Platform Team)**：负责第一曲线 + 基础设施（K8s, DB, Security）。考核指标：SLA、可用性。
            *   **流式团队 (Stream-aligned Team)**：负责第二曲线业务闭环。考核指标：TTM (Time to Market)、DORA 指标。
        *   *警惕*：如果第二曲线的开发需要频繁等待第一曲线团队排期改接口，说明组织结构不匹配。

### **Step 3: 技术债务管理 (The "Debt" Test)**
**目标**：解决“屎山代码”拖垮上市审计的问题。

*   **核心理论**：
    *   **Technical Debt Quadrant (技术债务象限 - Martin Fowler)**：
        *   *评估点*：CTO 如何处理老代码？是一刀切重构，还是放任不管？
        *   *Pass标准*：
            *   **第一曲线**：必须偿还 **“鲁莽的债务”**。为了上市审计，核心链路的代码必须规范、文档齐全、无高危漏洞。
            *   **第二曲线**：允许借入 **“谨慎的债务”**。为了抢占市场，可以接受暂时的代码潦草，但必须有后续的偿还计划（Refactoring Roadmap）。
            *   *策略*：**Strangler Fig Pattern (绞杀植物模式)**——对于太烂的老系统，不要重写，而在其周围建立新系统逐步替代。

### **Step 4: IPO 合规与安全 (The "Compliance" Test)**
**目标**：确保不因技术漏洞导致 IPO 暂停。

*   **核心理论**：
    *   **Defense in Depth (纵深防御)** & **DevSecOps**：
        *   *评估点*：安全是否是开发的“外挂”？
        *   *Pass标准*：
            *   **数据合规**：GDPR/PIPL 个人隐私保护。所有敏感数据（手机号、身份证）必须脱敏、加密。
            *   **审计留痕**：所有的代码变更、数据库操作必须有日志（Audit Trail）。这是 IPO 审计的必查项。
            *   **灾备演练**：必须有 RTO/RPO 承诺和演练记录。

## **使用指南 (How to use this skill)**

让 AI 扮演 CEO，向 CTO 提出以下灵魂拷问（Prompt 示例）：

1.  **架构拷问 (Pace Layering)**：“如果第二曲线明天要上线一个实验性功能，是否需要第一曲线的核心系统通过发版来配合？如果是，你的架构分层是不是失败了？”
2.  **组织拷问 (Conway)**：“我们现在的开发团队，哪几个人是专门负责修路（基建/平台），哪几个人是专门负责开车（业务）？如果混在一起，怎么保证修路的不影响开车的速度？”
3.  **债务拷问 (Tech Debt)**：“为了上市，我们要对核心系统进行代码审计。你现在的技术债务里，哪一部分是‘如果不还就会导致审计不通过’的？请列出 Top 3 的‘偿债计划’。”
4.  **安全拷问 (IPO)**：“如果明天审计入驻，查某一个用户 3 年前的敏感数据访问记录，你能立刻拿出来吗？如果不能，我们离上市还有多远？”
