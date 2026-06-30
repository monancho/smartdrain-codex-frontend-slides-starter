# SmartDrain frontend-slides starter workspace

이 폴더는 Codex로 `frontend-slides` 기반 HTML 발표자료를 새로 만들기 위한 작업환경입니다.

## 목표

기존 PPT 형태를 그대로 유지하지 않고, SmartDrain 프로젝트를 **기술 포트폴리오형 발표자료**로 새로 구성합니다.

핵심 메시지:

> 빗물받이 아이디어 소개가 아니라, 이미지 분석 → 센서 데이터 → AI 판단 → DB 저장 → callback → WebSocket 화면 갱신까지 하나의 서비스 흐름으로 연결한 프로젝트입니다.

## 시작 순서

1. 이 ZIP을 압축 해제합니다.
2. Codex에서 이 폴더를 프로젝트 루트로 엽니다.
3. `PROMPTS.md`의 **Prompt 1**을 먼저 붙여 넣습니다.
4. Codex가 설계안을 낸 뒤, 방향이 맞으면 **Prompt 2**로 `output/presentation.html` 생성을 시킵니다.
5. 브라우저에서 `output/presentation.html`을 열어 확인합니다.
6. `PROMPTS.md`의 **Prompt 3**으로 검수·수정을 시킵니다.

## 폴더 구조

```txt
.agents/skills/frontend-slides/SKILL.md   # Codex가 읽을 제작 규칙
input/                                   # 발표 내용 명세와 자산
input/assets/                            # 정리된 이미지·다이어그램·시연 리소스
references/                              # 원본 PPT PDF와 코드 근거 발췌
output/                                  # Codex가 최종 presentation.html을 저장할 위치
templates/                               # HTML 슬라이드 기본 골격
scripts/                                 # 자산 확인용 스크립트
PROMPTS.md                               # Codex 시작/제작/검수 프롬프트
```

## 중요한 방향

- 기존 PPT 레이아웃은 유지하지 않아도 됩니다.
- 첫 번째 PPT는 정돈감만 참고합니다.
- 두 번째 PPT는 내용 소스로만 참고합니다.
- 시스템 아키텍처, ERD, 비동기 처리, WebSocket, AI 분석 구조, 협업 방식은 줄이지 않습니다.
- 필요하면 슬라이드 수를 늘립니다.
- 목차와 섹션 구분은 반드시 넣습니다.
