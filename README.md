# 把知识讲明白，让理解留下来

### 兰彻的中文学习 Skills 与 Obsidian 知识工作流

**让公式有数字，让算法有过程，让论文有主线，让一次精彩的讨论成为可以回查、连接和继续生长的知识。**

这里收录 5 个围绕真实学习困难打磨的 Skill，以及一份 DSH × Obsidian 知识探索与管理总提示词。覆盖从概念入门、数学推导、算法理解、论文精读，到教材卡片整理和个人知识库维护的连续工作流。

你可以按眼前的问题单独选用，也可以把它们组合成自己的学习工具箱。

[挑选 Skill](#按当前任务挑选) · [安装与调用](#安装与调用) · [Obsidian 知识系统](prompts/obsidian-knowledge-system/) · [目录与文件](#仓库目录)

## 按当前任务挑选

| 你现在遇到的困难 | 推荐入口 | 主要收获 |
|---|---|---|
| “解释太抽象，我想看它实际怎么工作” | [例子驱动讲解](lizi-qudong-jiangjie/) | 紧跟术语的具体例子、小数字演算、算法输入与输出 |
| “定义里的每个字都认识，连起来却不懂” | [推导讲解](tuidao-jiangjie/) | 从已有直觉出发的知识链、三种版本的目标定义 |
| “单步能懂，连续学下去就跟丢了” | [认知连续学习](cognitive-continuity-learning/) | 稳定情境、旧办法与新办法的比较、卡点修补和续学 |
| “摘要看过了，仍不知道作者为什么这样做” | [论文故事解读](lunwen-gushi-jiangjie/) | 对象—行动—证据的研究主线、原图解读、结论与边界 |
| “想把一本教材里的定义变成可查的笔记” | [名词解释 PDF 制作](mingci-jieshi-pdf/) | Obsidian 概念卡、分章索引、来源页码和检查脚本 |
| “聊天里学到了很多，过后却找不回、接不上” | [DSH × Obsidian 总提示词](prompts/obsidian-knowledge-system/) | 精选保存、理解核验、项目管理、关联发现和定期检查 |

## 五个 Skill，分别解决什么问题？

### 例子驱动讲解：让每个陌生概念都能被看见

学习常常卡在“说得很专业，却没有一个可以跟着观察的对象”。这个 Skill 把具体例子放在讲解中心：术语一出现，就接一个最小、可观察的例子；公式一出现，就代入小数字；算法一出现，就展示输入、关键处理和输出。

比如解释一个循环，会把代码与实际输出放在一起；解释感染率，会先数出病斑 15 格、叶片 100 格，再算出 15%。遇到新方法，还会展示直观旧办法究竟卡在哪里，让下一步有明确来由。

适合数学、统计、编程、生物学和论文中的局部机制解释。用户只要结论、严格定义或原文摘录时，遵从当前任务，不强行添加演示。

[完整介绍](lizi-qudong-jiangjie/README.md) · [技能原文](lizi-qudong-jiangjie/SKILL.md)

### 推导讲解：从熟悉的现象，走到真正能理解的定义

它按“理解需要的顺序”组织知识：从已有经验出发，发现尚未解决的问题，引入恰好需要的概念，再把前后的关系接起来。新术语当场解释，位置、组成和容易混淆的边界也会补足。

比如学习“等位基因”，可以从个体差异出发，逐步连接遗传信息、DNA、染色体、同源染色体和基因座，最后再拼装目标概念。完成后给出白话版、标准版、脑内图像版，以及完整知识链。

默认以初中刚毕业者能够理解的基础为起点，也可以明确指定自己的基础。适合补概念根基、理解定义中的前置关系，以及准备向别人讲清一个知识点。

[完整介绍](tuidao-jiangjie/README.md) · [技能原文](tuidao-jiangjie/SKILL.md)

### 认知连续学习：让新知识接在刚才真正完成的事情后面

围绕“真实问题 → 旧办法 → 新需求 → 具体操作 → 新结果”推进，始终交代手里有什么信息、已经能做什么、新知识具体改变了哪一步。

公式用同一组数据贯穿；算法先用小数据展示关键内部运算，再与真实研究的输入、评价和证据对应；论文沿实际问题展开；教材则保留原书结构并补足关键连接。

当你说“这里没懂”，它会定位对象、符号、条件、计算或论证关系中的缺口，在原情境中补这一步。局部答疑后停下，等你说“继续”再返回主线。正式理解检验由你主动启动，一次一个具体问题。

适合持续学习统计、算法、教材和论文，也适合解决“每句话都有道理，整体却没有真正理解”的困难。技能文件本身不提供跨会话永久记忆，换对话时需要带上相关材料或进度笔记。

[原版使用说明](cognitive-continuity-learning/README.md) · [技能原文](cognitive-continuity-learning/SKILL.md) · [验收场景](cognitive-continuity-learning/references/acceptance-tests.md)

### 论文故事解读：跟住研究者做了什么，以及凭什么相信

先核对论文材料，再用少量关键词之间的关系固定主线。围绕研究对象、现实困难、方法选择、关键实验、图表证据、实际验证和局限，把全文串成可以跟随的研究故事。

讲方法时展示输入、必要操作和输出；讲图时解释坐标、单位、颜色、具体对比及其支持的结论。故事中的情境重建、教学假设和论文事实会明确区分，不能把推测写成作者经历，也不能把相关性写成因果证明。

支持全文一次讲完、分段阅读、接续讲解和局部图表答疑。配图优先使用论文原图及可靠来源；实际能否读图、检索或显示附件，取决于所用平台的工具。

[完整介绍](lunwen-gushi-jiangjie/README.md) · [技能原文](lunwen-gushi-jiangjie/SKILL.md)

### 名词解释 PDF 制作：让教材定义有卡片，也有出处

**输入是教材或书籍 PDF，主要输出是 Markdown 概念卡与章节索引。** 它逐页渲染并视觉核对，只把书上确实给出定义的术语纳入正表；仅被提及却未定义的词单列附录。

每张卡片保留教材定义原句、英文信息、PDF 页码／书页／段落位置，并补充“为什么要有这个概念”的解释。索引用 Obsidian 双链连到卡片，方便按章节浏览和回原书核查。

随附两个 Python 工具：`check.py` 检查双链与文件对应、序号、PDF 页码和行数；`progress.py` 用 SHA-256 内容指纹统计卡片相对基线的变化，生成总览与分章进度报告。内容变化可以记录学习整理活动，不能直接证明已经掌握知识。

[完整介绍与脚本用法](mingci-jieshi-pdf/README.md) · [技能原文](mingci-jieshi-pdf/SKILL.md) · [教材案例档案](mingci-jieshi-pdf/references/试验统计方法.md)

## DSH × Obsidian：让讨论成为长期知识资产

**把一次讨论中的精彩例子、图片、推导和解释，整理成带来源、带理解记录、可以持续核验与连接的知识。**

这份总提示词设计了 ChatGPT 与 DSH 的协作：ChatGPT 承担深入探索；DSH 读取用户提供的讨论材料，筛选值得保存的片段，独立核验知识，记录用户最初的理解，再按确认后的结构写入现有 Obsidian 知识库。

它还规定了项目总览、动态总体笔记、整理工作台、附件补充、双重状态管理、增量更新、跨项目关联建议、每周探索报告和每月健康检查。原始内容、用户理解与后续纠错分别保留，方便追踪认识怎样变化。

例如，讨论条件期望时出现一张特别有帮助的表格，可以只保存该表格及必要上下文、你的最初理解、核验意见和来源链接；后续学到预测误差时，再提出两篇笔记之间具体有什么联系，由你决定是否建立双链。

**这是可交给助手执行的工作流总指令。** 分享页读取、本地读写、图片保存、联网查证和定时执行，需要运行环境提供对应能力；上传文档不会自动连接 Obsidian 或创建任何定时任务。原文中提到的历史可行接口也需要在当前环境重新验证。

[功能全解与上手方法](prompts/obsidian-knowledge-system/README.md) · [完整总提示词原文](prompts/obsidian-knowledge-system/DSH_Obsidian_知识探索与管理系统_总提示词.md)

## 安装与调用

### 在 Codex 中安装

向具备 `skill-installer` 的 Codex 发送：

~~~text
用 $skill-installer 从 GitHub 仓库 shizian0809-cpu/-skill 安装以下目录中的技能：
lizi-qudong-jiangjie
tuidao-jiangjie
cognitive-continuity-learning
lunwen-gushi-jiangjie
mingci-jieshi-pdf
~~~

也可以只选需要的目录。手动安装时，在仓库首页选择 **Code → Download ZIP**，解压后将目标 Skill 的**整个文件夹**放入当前 Codex 支持的技能目录，保留 `references/` 和 `scripts/`。

| 范围 | 目录 |
|---|---|
| 当前项目 | `<项目>/.agents/skills/<skill-name>/` |
| 当前用户，Windows | `%USERPROFILE%\.agents\skills\<skill-name>\` |
| 当前用户，macOS / Linux | `~/.agents/skills/<skill-name>/` |

安装说明依据 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。不同版本和安装器可能采用不同目录，优先使用当前环境的官方方式；未出现在选择器时重启 Codex 后检查。

### 直接复制这些调用示例

~~~text
$lizi-qudong-jiangjie 用 3 个小数字解释方差，展示每一步计算。

$tuidao-jiangjie 从我已知的遗传现象出发，推导等位基因的概念。

$cognitive-continuity-learning 用同一组数据讲条件期望，先算总体平均，再看加入条件后计算怎样改变。

$lunwen-gushi-jiangjie 解读我附上的论文，一次讲完整条研究主线，关键结果结合原图说明。

$mingci-jieshi-pdf 把这本 PDF 的第一章做成 Obsidian 概念卡和索引。先确认来源和输出位置，给我看一章成品。
~~~

Codex CLI／IDE 可以输入 `$` 提及技能，或通过 `/skills` 选择，具体入口以客户端为准。安装与显式调用方法见 [OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)。

### DSH 与其他助手

在支持 `SKILL.md` 的环境中，按照该平台的加载方式导入完整文件夹。原始文件包含部分 DeepSeek Harness 工具名、本机路径和历史案例参数；换环境时需要提供实际可用的 PDF、图片、文件和检索工具。

没有技能加载功能时，可把所选 `SKILL.md` 的正文作为对话约定，再附上材料、具体目标和已有基础。Obsidian 总提示词则单独按其[上手说明](prompts/obsidian-knowledge-system/README.md)使用。

## 如何组合使用

- **想把一个概念讲透**：推导讲解安排知识依赖，例子驱动讲解补足具体演示。
- **想精读一篇论文**：论文故事解读保持研究主线，遇到难公式时用例子演算，需要补前置概念时再从底层推导。
- **想持续学一个方法**：认知连续学习管理当前问题与停点，保持数据和符号连续，按需调用其他讲解方式。
- **想留下可复用的成果**：教材定义用卡片与索引保存；讨论中的精彩内容用 Obsidian 工作流进行筛选、核验和整理。

同一任务同时使用多个 Skill 时，应让它们各司其职，并优先遵从你当次明确的范围、篇幅和交互要求。

## 仓库目录

延续原有“根目录放独立 Skill”的结构，目录名与技能 `name` 对应；总提示词放在 `prompts/`，便于区分两类入口。

~~~text
.
├── README.md
├── cognitive-continuity-learning/
│   ├── README.md
│   ├── SKILL.md
│   └── references/acceptance-tests.md
├── lizi-qudong-jiangjie/
│   ├── README.md
│   └── SKILL.md
├── tuidao-jiangjie/
│   ├── README.md
│   └── SKILL.md
├── lunwen-gushi-jiangjie/
│   ├── README.md
│   └── SKILL.md
├── mingci-jieshi-pdf/
│   ├── README.md
│   ├── SKILL.md
│   ├── references/试验统计方法.md
│   └── scripts/
│       ├── check.py
│       └── progress.py
└── prompts/
    └── obsidian-knowledge-system/
        ├── README.md
        └── DSH_Obsidian_知识探索与管理系统_总提示词.md
~~~

## 使用前了解

这些 Skill 提供可复用的讲解规则与工作流程，实际效果取决于模型、材料和工具能力。论文解读需要原文，教材整理需要 PDF 与图像阅读能力，知识库管理需要明确的 Vault 位置及相应授权。

本次发布保留五个 Skill 的原始文件与总提示词原文，新增的介绍负责导航、说明用法和交代环境条件。案例档案中的本机路径、历史数量和定时配置是原案例记录，使用自己的资料时应重新确认，仓库未附带相应教材 PDF、概念卡或后台服务。
