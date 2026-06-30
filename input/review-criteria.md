# 발표자료 검수 기준

이 체크리스트는 style preview, slide map, final HTML, PDF export를 승인하기 전에 사용한다.

## 시나리오

- 발표 흐름은 `input/09_final-slide-map.md`를 기준으로 한다.
- 팀 구성과 역할은 초반부에 짧게 제시한다.
- 비용 추정 슬라이드는 포함하지 않는다.
- 운영 관련 슬라이드는 정성적 점검 항목으로만 구성하고, 완성된 production monitoring system처럼 말하지 않는다.
- DB/ERD는 callback 저장과 WebSocket 설명보다 먼저 나온다.
- Fingtron은 디자인 참고가 아니라 서비스 시나리오 벤치마킹으로만 사용한다.

## 현재 구현 범위

- sample images는 현재 시연/검증용 입력으로 설명한다.
- mock sensor data는 현재 시연/검증용 입력으로 설명한다.
- async analysis 흐름이 포함되어 있다.
- result persistence 흐름이 포함되어 있다.
- WebSocket UI reflection 흐름이 포함되어 있다.
- RTSP/CCTV, MQTT/IoT, 알림, 리포트는 향후 확장으로 분리한다.

## 기술 정확성

- YOLO 단독 분석 한계가 설명되어 있다.
- OpenCV 결합 이유가 설명되어 있다.
- XGBoost 입력 feature가 설명되어 있다.
- 위험도 분류 로직이 설명되어 있다.
- callback 저장 흐름이 설명되어 있다.
- WebSocket은 화면 갱신 trigger로 설명되어 있다.
- PostgreSQL 저장 구조가 설명되어 있다.
- Docker, Nginx, Jenkins 구성은 포함하되 실제 운영 완료처럼 과장하지 않는다.
- `sensor_data`는 단일 `id` primary key를 사용한다고 설명한다.
- `sensor_data`가 composite primary key를 사용한다고 설명하지 않는다.
- `risk_score`는 실제 물리적 침수 확률이 아니라 내부 분류용 계산 점수로 설명한다.

## 주장 안전성

- 근거 없는 정확한 운영 비용 추정은 넣지 않는다.
- complete production monitoring, real-time CCTV current integration, real IoT/MQTT current integration을 주장하지 않는다.
- 현장 검증 완료 또는 실제 침수 예측 검증 완료처럼 말하지 않는다.
- scheduler, callback, WebSocket, DB 저장은 코드 기준 구현 범위와 실행 검증 범위를 구분해서 말한다.
- 이전 프로젝트명이나 `SmartDrain`이 visible slide text로 남지 않도록 확인한다.

## 리소스

- 모든 이미지 경로가 실제로 로드된다.
- 다이어그램은 발표 화면에서 읽을 수 있다.
- 스크린샷에는 발표자가 설명할 수 있는 명확한 callout 또는 caption이 있다.
- 생성 이미지나 임시 이미지는 실제 운영 캡처처럼 보이게 설명하지 않는다.
- 불필요한 원본 제목, 이전 프로젝트명, draft note, sticky comment가 보이지 않는다.

## 디자인 / 레이아웃

- 1920x1080 fixed-stage behavior가 유지된다.
- 모든 슬라이드는 16:9 stage 안에서 잘리지 않는다.
- 텍스트 overflow, panel overlap, clipping이 없다.
- 한국어가 읽기 쉬운 크기와 줄 길이를 유지한다.
- 기술명은 필요한 경우에만 English로 유지한다.
- Style A의 색상, 타이포그래피, 카드/도식 문법을 유지한다.

## 최종 산출물

- 최종 HTML 경로는 `output/presentation.html`이다.
- 최종 HTML은 브라우저에서 단독 실행 가능해야 한다.
- keyboard navigation과 slide counter가 동작해야 한다.
- PDF export는 HTML QA 통과 후 진행한다.
- 주요 변경 전후에는 커밋을 남겨 형상관리를 유지한다.
