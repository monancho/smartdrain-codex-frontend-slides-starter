# Codex prompts

## Prompt 1 — 시작 분석 / 설계안 요청

아래 프롬프트를 Codex에 먼저 넣으세요. 이 단계에서는 아직 HTML을 만들지 않게 합니다.

```txt
You are helping me create a new frontend-slides HTML presentation for the SmartDrain project.

Do not create the final presentation yet.

First, read:
- .agents/skills/frontend-slides/SKILL.md
- input/brief.md
- input/00_project-context.md
- input/01_content-spec.md
- input/02_asset-map.md
- input/03_design-direction.md
- input/04_claim-safety.md
- input/05_slide-outline-expanded.md
- input/07_implementation-notes.md

Task:
1. Summarize the intended presentation direction.
2. Check whether the content spec is sufficient.
3. Identify missing assets, messy assets, and risky claims.
4. Propose a section-by-section slide plan.
5. Explain how you will handle architecture, ERD, async callback, WebSocket, YOLO/OpenCV, XGBoost, and collaboration sections.
6. Do not write output/presentation.html yet.

Important:
- Do not preserve the old PPT layout.
- Treat old PPTs only as content and asset references.
- This is a technical portfolio-style project presentation, not a minimal pitch deck.
- Do not aggressively reduce content.
- Use a clear agenda and section dividers.
- Split dense technical content into multiple slides instead of deleting it.
```

---

## Prompt 2 — HTML 발표자료 생성

Prompt 1 결과가 괜찮으면 아래 프롬프트를 넣습니다.

```txt
Now create the frontend-slides presentation.

Read:
- .agents/skills/frontend-slides/SKILL.md
- input/brief.md
- input/00_project-context.md
- input/01_content-spec.md
- input/02_asset-map.md
- input/03_design-direction.md
- input/04_claim-safety.md
- input/05_slide-outline-expanded.md
- input/06_speaker-key-lines.md
- input/07_implementation-notes.md
- input/08_review-criteria.md

Output:
- output/presentation.html

Requirements:
- Create a 16:9 single-file HTML presentation.
- Use inline CSS and inline JavaScript only.
- No npm build step, no CDN, no external library.
- Make it directly openable in a browser.
- Add keyboard navigation and a slide counter.
- Do not preserve the old PPT layout.
- Use old materials only as content and asset references.
- Do not aggressively reduce content.
- Include a clear agenda and section divider slides.
- Keep architecture, ERD, AI pipeline, async callback, WebSocket, system architecture, collaboration, and demo sections.
- Split dense technical content into multiple slides instead of deleting it.
- Use assets from input/assets when useful.
- If an asset is too dense or messy, recreate it as clean HTML/CSS/SVG instead of placing the image directly.
- Do not include draft comments, sticky notes, console logs, warning screenshots, or unreadable diagrams.
- Check for overflow, broken images, cropped text, and unreadable diagrams.
```

---

## Prompt 3 — 검수 및 수정

생성 후 아래 프롬프트로 품질 검수를 시킵니다.

```txt
Review output/presentation.html and revise it directly.

Check:
1. Are all required sections from input/01_content-spec.md included?
2. Are important technical decisions preserved?
3. Are architecture, ERD, AI pipeline, callback, WebSocket, and collaboration sections clear?
4. Are there any unsupported claims according to input/04_claim-safety.md?
5. Is any slide too dense or too empty?
6. Are screenshots and diagrams readable at 16:9?
7. Are there old draft notes, sticky notes, Streamlit warnings, console logs, or messy screenshots?
8. Are image paths relative and working?
9. Are slide transitions and keyboard navigation working?

Then revise output/presentation.html directly.
```

---

## Prompt 4 — 디자인 2차 개선

내용이 다 들어간 뒤, 디자인만 다듬을 때 사용합니다.

```txt
Improve only the visual design of output/presentation.html without removing technical content.

Goals:
- More polished technical portfolio deck.
- Stronger section hierarchy.
- Better contrast and typography.
- More readable diagrams.
- Less static slide repetition.
- Do not reduce architecture, ERD, async flow, AI pipeline, or collaboration content.
- Do not copy old PPT layout.
```
