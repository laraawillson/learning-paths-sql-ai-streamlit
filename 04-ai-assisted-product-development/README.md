# AI-Assisted Product Development

Learn to direct AI well — as both a coding partner and a planning partner. This path is the **meta-skill** that supports the other three (SQL, AI Development, Streamlit), not a separate technical domain to master in isolation. Practice it on real work from those paths, not toy examples.

## Why this path exists

Being good at using AI to build and plan things is a skill in its own right, distinct from writing SQL or Python yourself. Two parts to it:

1. **AI-assisted development** — prompting well, reviewing AI output critically, using AI as a pair-programmer/code-reviewer instead of a code-generator you don't examine.
2. **Product/requirements planning** — turning a vague idea into a clear, scoped spec (a PRD, user stories, acceptance criteria) before building it.

These two connect directly to the ADHD-aware design goal behind the [Work Tracker](../03-streamlit-development/README.md): breaking an overwhelming, vague thing into small, clear, externalized pieces is *both* a professional product-management skill *and* a personal coping mechanism. This path is where you practice that deliberately.

## Learning Progression

### 📍 Level 1: Prompting Fundamentals
- Structured prompting for *learning* something vs. prompting to just get something *done*
- Asking for review-not-rewrite ("point out the issue, don't fix it for me")
- Asking for a quiz or practice set on a topic before seeing solutions
- Recognizing when a prompt is too vague to get a useful answer, and tightening it

### 📍 Level 2: AI-Assisted Development Workflow
- The draft-then-review loop: write your own attempt first, then get targeted AI feedback, then iterate
- Practicing this on real work in progress — a SQL query from Path 1, a lint rule from the Tableau assistant in Path 2, a Streamlit component from Path 3
- Knowing when to ask AI to explain vs. when to ask it to critique vs. when to ask it to generate
- Reading and evaluating AI-suggested code before accepting it — not just running it

### 📍 Level 3: Product & Requirements Planning
- Writing a PRD: problem statement, goals, non-goals, scope
- User stories and acceptance criteria — making "done" checkable, not vibes-based
- A lightweight "definition of ready" checklist for a task before it's worth starting
- Turning a vague idea ("the tracker should be smarter about stale tasks") into a scoped, buildable spec

### 📍 Capstone: Work Tracker v2 PRD → Tickets
- Write a real PRD for an actual next version of the Work Tracker, informed by what you've learned from using it
- Break it into user stories with acceptance criteria
- Feed those into [Path 3's AI Jira ticket-drafting feature](../03-streamlit-development/README.md) to generate the first real tickets that tool has ever drafted — closing the loop between planning and the tool that operationalizes it

## 📚 Topics Covered

### Prompting
1. **Prompt Structure**
   - Context, constraint, and desired-output-shape as distinct parts of a prompt
   - Tutor-mode phrasing vs. builder-mode phrasing (see [`CLAUDE.md`](../CLAUDE.md))
   - Iterating on a prompt that didn't get you what you needed

### Development Workflow
2. **Draft-Then-Review**
   - Writing your own first attempt before asking for help
   - Asking for critique of a specific attempt vs. asking for a solution from scratch
   - Spotting when AI-suggested code is subtly wrong, not just when it errors

3. **Code Review Skills**
   - What to look for: correctness, edge cases, readability, whether it does more than asked
   - Giving specific, actionable feedback (to AI or to your own past attempt)

### Requirements & Planning
4. **PRDs**
   - Problem statement vs. solution — don't jump straight to "build X"
   - Scope: what's in, what's explicitly out
   - Success criteria

5. **User Stories & Acceptance Criteria**
   - "As a [user], I want [goal], so that [benefit]"
   - Acceptance criteria as a checklist, not prose
   - Sizing/story points as a rough conversation tool, not a precise estimate

6. **Breaking Work Down**
   - Turning one big vague feature into several small, independently shippable pieces
   - A "definition of ready" checklist before a task is worth starting

## 🎓 Projects

### Project 1: Prompt Practice Log
**Level:** Beginner
**Skills:** Structured prompting
Keep a short log (a few tasks in the Work Tracker's "Ideas" column work fine) of prompts you tried, what worked, and what you'd phrase differently next time.

### Project 2: Code Review Practice
**Level:** Intermediate
**Skills:** Critical review, draft-then-review workflow
Take a real piece of code from Path 1, 2, or 3. Review it yourself first and write down what you'd change. Then ask AI to review it. Compare the two reviews — what did you catch that it didn't, and vice versa?

### Project 3: Work Tracker v2 PRD *(capstone)*
**Level:** Intermediate-Advanced
**Skills:** PRD writing, user stories, acceptance criteria
Write a full PRD for a real enhancement to the Work Tracker, based on actual usage friction. Break it into user stories with acceptance criteria, then generate the first tickets from it using Path 3's ticket-drafting tool.

## 💻 Tech Stack

- No new libraries — this path is about how you use Claude Code and the Claude API you're already using in Paths 2 and 3, plus plain markdown for PRDs/user stories.

## 💡 Learning Tips

1. **Practice on real work, not toy examples** - the whole point is directing AI on things you actually care about getting right
2. **Write your own attempt first** - even a rough one, before asking for review — otherwise you're not practicing the skill, just delegating
3. **Be specific in feedback requests** - "review this" is weaker than "check whether this handles the empty-list case"
4. **Treat vagueness as a signal** - if you can't write acceptance criteria for a feature, it's not scoped yet

## 🤖 Working through this with AI

Default to tutor mode (see [`CLAUDE.md`](../CLAUDE.md)). Example prompts:
- "Here's my first draft of a PRD for the tracker's stale-task feature [paste]. Ask me questions about what's underspecified instead of rewriting it."
- "I want to practice code review. Here's a query I wrote — don't tell me what's wrong yet, ask me what I'd check for first."
- "Quiz me on the difference between a user story and an acceptance criterion before I write either for this feature."

## 📖 Resources

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic Prompt Engineering Guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Atlassian: How to write an agile user story](https://www.atlassian.com/agile/project-management/user-stories)
- [Google's PRD template (as a reference shape, not a rule)](https://www.atlassian.com/agile/product-management/requirements)

## 🚀 Next Steps

1. Practice Level 1-2 continuously, alongside whatever you're building in Paths 1-3
2. When the Work Tracker has been used for a few weeks, write the capstone PRD
3. Feed it into Path 3's ticket-drafting feature as its first real test

---

**Ready to start?** Pick one piece of code you wrote this week in any other path, and practice the draft-then-review loop on it.
