# 认知连续学习

面向数学、统计、算法、教材和论文的中文学习 Skill。比如学条件期望时，先用同一组小数据算出总体平均，再加入一个已知条件，看看哪些数据和权重需要调整，最后把计算写成公式。

## 在 Codex 中安装

在 Codex 对话中发送下面这句话。

```text
用 $skill-installer 从 GitHub 仓库 shizian0809-cpu/-skill 安装 cognitive-continuity-learning 目录里的技能。
```

也可以在 GitHub 仓库首页通过 **Code → Download ZIP** 下载并解压，再将整个 `cognitive-continuity-learning` 文件夹复制到个人技能目录。

- Windows 使用 `%USERPROFILE%\.agents\skills\`。
- macOS 和 Linux 使用 `~/.agents/skills/`。

安装后，`SKILL.md` 应位于 `.agents/skills/cognitive-continuity-learning/SKILL.md`。如果技能没有出现在选择器里，重启 Codex。参见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。

## 开始使用

在 Codex 输入框键入 `$`，选择 `cognitive-continuity-learning`，再写下学习任务。可以直接试下面的提示词。

```text
$cognitive-continuity-learning 用一组小数字解释条件期望。先算总体平均，再演示加入条件后计算怎么变。
```

- **精读论文**。附上论文或相关页，说「先讲研究问题，再结合图 2 解释作者用什么证据回答它」。
- **理解公式**。附上公式或截图，说「用小数字代入，解释每个符号对应什么，以及每一步怎么算」。
- **修补卡点**。指出具体一句或一步，说「沿用刚才的数据，只补这一步」。之后可以说「继续」，接回原来的讲解。

如果所用平台没有技能加载功能，可以把 [SKILL.md](cognitive-continuity-learning/SKILL.md) 的正文和学习材料一起发到对话中，请助手按这份说明讲解。

## 仓库文件

- [技能定义](cognitive-continuity-learning/SKILL.md)
- [详细使用说明](cognitive-continuity-learning/README.md)
- [验收场景](cognitive-continuity-learning/references/acceptance-tests.md)
