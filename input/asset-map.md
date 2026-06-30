# 우수주의보 Asset Map

이 문서는 최종 HTML 발표자료 `output/presentation.html`에서 사용하는 리소스와 대체 도식 기준을 정리한다.

## 현재 리소스 상태

최종 발표자료는 `output/assets`의 실제 리소스와 HTML/CSS 도식을 함께 사용한다. 이미지가 없거나 읽기 어려운 경우에는 깨진 이미지 대신 HTML diagram을 사용한다.

## 사용 리소스

| 파일 | 사용처 | 역할 |
| --- | --- | --- |
| `architecture-cropped.png` | 5 | 전체 시스템 구성 보조 리소스 |
| `dashboard-main.png` | 21, 35 | 관리자 대시보드 구현 캡처 |
| `dashboard-detail.png` | 22, 35 | 상세 화면 구현 캡처 |
| `drain-danger.png` | 6 | 막힘 상태 sample image |
| `drain-caution.jpg` | 34 | 시연용 sample image |
| `drain-good.png` | 19 | 양호 상태 sample image |
| `erd.png` | 보조 리소스 | 원본 ERD 참고용. 최종 Slide 23은 HTML/CSS ERD 사용 |
| `qr-code.png` | 36 | GitHub 또는 Demo QR 코드 |
| `reference-policy-page.png` | 11 | 정책/사례 참고 자료 |
| `sequence-callback-websocket.png` | 보조 리소스 | 원본 sequence 참고용. 최종 Slide 27은 HTML/CSS sequence 사용 |
| `yolo-opencv-error-graph.png` | 14 | YOLO 단독 해석 한계 설명 |
| `yolo-opencv-process.jpg` | 15 | YOLO/OpenCV 처리 과정 설명 |

## 보조 리소스

- `drain-sample.jpg`: 추가 sample image가 필요할 때 사용 가능
- `drain-unknown.png`: 판단불가 상태를 별도 장면으로 분리할 때 사용 가능

## HTML/CSS로 재작성한 도식

- 프로젝트 한 줄 요약 end-to-end flow
- 전체 기술 스택 계층 도식
- 강우 중 상태 변화 flow
- 기존 방식/서비스 벤치마킹 table
- AI 분석 설계 flow
- XGBoost feature cards
- DB/ERD entity cards
- 비동기 분석 요청 flow
- callback/WebSocket sequence flow
- system architecture board
- PostgreSQL 저장 구조 cards
- 운영 모니터링 고려 cards
- 현재 구현 범위 vs 향후 확장 table

## 리소스 사용 원칙

- 이전 프로젝트명이나 불필요한 제목이 보이는 이미지는 crop된 리소스를 사용한다.
- 사진형 sample image는 실제 운영 입력처럼 설명하지 않는다.
- dashboard/detail screenshot은 구현 화면 근거로 사용한다.
- ERD, callback/WebSocket sequence, system architecture는 최종 발표 화면에서 HTML/CSS 도식을 우선 사용한다.
- 원본 ERD, sequence, architecture 이미지는 참고용 또는 보조 리소스로만 둔다.
- real-time CCTV, real IoT sensor, MQTT 운영 연동을 현재 구현처럼 보이게 하는 이미지는 사용하지 않는다.

## 향후 개선 후보

- ERD를 고해상도 HTML/SVG로 완전 재작성
- callback/WebSocket sequence를 HTML/SVG로 완전 재작성
- AI 결과 예시를 상태별로 한 장씩 더 분리
- 발표용 PDF export 이후 페이지별 가독성 재검수
