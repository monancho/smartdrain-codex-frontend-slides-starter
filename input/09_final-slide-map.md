# 우수주의보 Final Slide Map

이 문서는 최종 Korean HTML 발표자료 `output/presentation.html`의 구조 기준이다. 현재 발표자료는 프로토타입에서 고도화 단계로 전환한다. Style A의 기술 보고형 디자인을 유지하되, 각 슬라이드는 발표자가 설명하기 쉬운 하나의 장면으로 구성한다.

## 작성 원칙

- visible project/team name은 `우수주의보`로만 사용한다.
- visible slide text에 `SmartDrain`을 사용하지 않는다.
- Fingtron은 디자인 참고가 아니라 서비스 시나리오 벤치마킹으로만 사용한다.
- 비용 추정 슬라이드는 포함하지 않는다.
- 운영 모니터링은 정성적 고려사항으로만 설명한다.
- `sensor_data`는 composite primary key가 아니라 단일 `id` primary key로 설명한다.
- `risk_score`는 실제 물리적 침수 확률이 아니라 내부 분류용 계산 점수로 설명한다.
- real-time CCTV, real IoT sensor, MQTT 연동, field-validated flood prediction은 현재 구현으로 주장하지 않는다.
- 현재 구현 범위는 sample images, mock sensor data, async analysis, result persistence, WebSocket UI reflection로 명확히 둔다.
- RTSP CCTV, MQTT sensor, alert, report는 향후 확장으로 분리한다.
- DB/ERD는 callback 저장과 WebSocket 갱신보다 먼저 배치한다.
- 이미지가 없는 경우에는 깨진 이미지 대신 HTML/SVG diagram 또는 명시적 placeholder를 사용한다.

## 0. 인트로

### 1. 표지

- 제목: 우수주의보
- 부제: 이미지·센서 기반 빗물받이 상태 판단 및 관리 화면 반영
- 핵심 메시지: 빗물받이 상태를 이미지와 센서값으로 판단하고, 결과를 DB 저장과 화면 갱신 흐름으로 연결한 프로젝트
- 시각: 어두운 도로/빗물받이 분위기 + 시스템 흐름 라인

### 2. 프로젝트 한 줄 요약

- 한 줄 요약: sample image와 mock sensor data를 분석 작업으로 연결하고, callback 저장 후 WebSocket event로 화면 갱신을 유도한다.
- 현재 구현 범위: sample images, mock sensor data, async analysis, result persistence, WebSocket UI reflection
- 금지: MVP라는 표현을 과도하게 반복하지 않는다.
- 시각: 입력 -> 분석 작업 -> AI 서버 -> callback -> DB -> WebSocket -> 화면 갱신

### 3. 팀 구성과 역할

- 역할 중심으로 짧게 제시한다.
- AI pipeline: YOLO, OpenCV, 이미지 전처리, 모델 기준
- Backend/DB: FastAPI, PostgreSQL, callback 저장, WebSocket event
- Frontend/Infra: dashboard/detail UI, Docker, Nginx, Jenkins
- 발표/분류 기준: XGBoost feature, 판단 기준, 발표 구성

### 4. 목차

- 개발 필요성과 벤치마킹
- AI 분석 설계
- 웹 서버 및 서비스 구축
- 인프라 / 운영 설계
- 시연과 마무리

### 5. 전체 기술 스택/구성 한 장 요약

- Frontend: Next.js, React, TypeScript, TanStack Query, Zustand, Kakao Maps, Recharts
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic, WebSocket
- AI: YOLO, OpenCV, XGBoost, scikit-learn
- DB/Infra: PostgreSQL, Docker, Nginx, Jenkins
- 시각: 계층형 system architecture diagram

## 1. 개발 필요성과 벤치마킹

### 6. 도시 침수와 빗물받이

- 빗물받이는 도로 위 빗물이 배수관으로 들어가는 첫 지점이다.
- 낙엽, 쓰레기, 토사 등으로 막히면 강우 중 배수 흐름이 제한된다.
- 목표는 도시 침수 전체를 예측하는 것이 아니라, 개별 빗물받이 상태 판단과 우선 확인 흐름을 만드는 것이다.
- 리소스: `drain-danger.png` 또는 `drain-sample.jpg`

### 7. 강우 중 상태 변화

- 강우 중에는 이물질 유입, 막힌비율 증가, 수위 상승, 유속 저하가 짧은 시간 안에 함께 발생할 수 있다.
- 정기 점검 시점과 실제 강우 중 상태는 다를 수 있다.
- 그래서 상태 변화가 발생한 뒤 화면에 반영되는 흐름이 중요하다.
- 시각: time-based state transition diagram

### 8. 기존 점검 방식의 한계

- 정기 점검과 청소는 유지관리에서 필요하다.
- 다만 강우 중 동시다발적으로 변하는 개별 시설 상태를 빠르게 정렬하기 어렵다.
- 시민 신고는 현장 발견에 강점이 있지만, 신고 전 우선순위 계산에는 한계가 있다.
- 시각: 정기 점검 / 시민 신고 / 우선순위 공백 비교

### 9. 기존 방식/서비스 벤치마킹

- 정기 점검: 기준과 이력 관리에 강점
- 시민 신고: 현장 발견과 민원 접수에 강점
- QR/관리번호: 위치 특정과 이력 연결에 강점
- 센서/관제: 수치 상태와 다지점 모니터링에 강점
- Fingtron은 시나리오 벤치마킹으로만 사용하고 디자인은 복제하지 않는다.

### 10. 우수주의보 차별점

- 이미지 근거와 센서 근거를 함께 사용한다.
- 개별 빗물받이 단위로 판단 결과와 근거를 저장한다.
- WebSocket event 이후 화면이 최신 데이터를 다시 조회해 반영한다.
- 신고 대체가 아니라 점검 우선순위와 상태 확인을 보조한다.
- 시각: 기존 방식 보완 matrix

### 11. 참고 자료/정책/사례 기반 목표

- 기존 관리·신고 체계와 정책/사례를 참고해 기능 범위를 설정했다.
- 정확한 근거가 없는 비용, 운영 수치, 현장 검증 수치는 사용하지 않는다.
- 구현 목표는 상태 판단, 근거 저장, 화면 반영 흐름이다.
- 리소스: `reference-policy-page.png`

### 12. 일정표

- 기획·설계
- AI 분석 설계
- Backend/DB 구현
- Frontend 구현
- 통합·시연 준비
- 시각: horizontal timeline

## 2. AI 분석 설계

### 13. AI 분석 설계 개요

- AI 분석은 이미지 근거와 센서 근거를 결합해 내부 위험도 분류로 연결한다.
- YOLO는 객체/영역 탐지, OpenCV는 전처리와 영역 보정, XGBoost는 feature 기반 분류를 맡는다.
- 시각: image + sensor -> YOLO/OpenCV -> XGBoost -> status

### 14. YOLO 단독 분석 한계

- YOLO는 보이는 객체와 후보 영역 탐지에 강점이 있다.
- 하지만 어두운 이미지, 빗물 반사, 낙엽/토사 혼재 상황에서는 단독 결과만으로 막힌비율을 안정적으로 설명하기 어렵다.
- 따라서 후처리와 센서 feature가 필요하다.
- 리소스: `yolo-opencv-error-graph.png`

### 15. OpenCV 결합 이유

- OpenCV는 전처리, mask 처리, 어두운 영역 보정, obstruction area estimation을 보조한다.
- YOLO 탐지 결과를 실제 막힌 영역 해석으로 연결하는 중간 단계다.
- 시각: raw image -> preprocessing -> mask/area -> obstruction ratio
- 리소스: `yolo-opencv-process.jpg`

### 16. 차폐율·이미지 품질·객체 탐지

- 차폐율은 이미지 기반 막힘 정도를 설명하는 내부 feature다.
- 이미지 품질과 탐지 신뢰도는 결과 해석의 신뢰도를 보정한다.
- 판단 불가 상태는 실패가 아니라 근거 부족을 명시하는 안전장치다.
- 리소스: `drain-good.png`, `drain-caution.jpg`, `drain-danger.png`, `drain-unknown.png`

### 17. XGBoost 입력 feature

- 입력 feature: obstruction ratio, detection confidence, water level, flow velocity
- sensor data는 mock sensor data 기준의 시연 입력이다.
- XGBoost는 feature 조합을 바탕으로 내부 상태 분류를 수행한다.
- 시각: feature cards -> classifier -> status

### 18. 위험도 분류 로직

- 출력 상태: 양호, 주의, 위험, 판단불가
- `risk_score`는 우수주의보 내부 분류용 계산 점수다.
- 실제 침수 확률 또는 물리적 flood-risk score로 표현하지 않는다.
- YOLO 실패 시에도 센서 근거가 명확하면 위험으로 분류할 수 있다.

### 19. 결과/검증

- 검증은 현재 구현 흐름과 sample/mock data 기반 결과 확인 범위로 한정한다.
- 현장 검증 완료나 실제 침수 예측 검증 완료로 말하지 않는다.
- 보여줄 것은 입력, 중간 결과, 최종 분류, DB 저장 가능성이다.
- 리소스: 상태별 drain sample 이미지

## 3. 웹 서버 및 서비스 구축

### 20. 서비스 구축 개요

- 시스템은 dashboard, Backend, AI server, PostgreSQL, WebSocket으로 구성된다.
- Frontend가 분석을 직접 요청하는 구조가 아니라, Backend 중심의 비동기 분석 흐름으로 설명한다.
- 시각: service responsibility diagram

### 21. 관리자 대시보드 흐름

- 전체 상태, 지도, 위험 시설 목록, 선택 시설 정보를 확인한다.
- WebSocket event 이후 최신 데이터를 다시 조회해 화면을 갱신한다.
- 리소스: `dashboard-main.png`

### 22. 상세 화면 흐름

- 시설별 이미지 분석 결과, 센서 추이, AI 결과, 이력을 확인한다.
- 왜 특정 상태로 판단됐는지 근거를 확인하는 화면이다.
- 리소스: `dashboard-detail.png`

### 23. DB 설계 / ERD

- drains, sensor_data, yolo_results, xgboost_results, analysis_jobs 관계를 먼저 설명한다.
- callback 저장과 WebSocket 갱신은 DB 저장 구조 이후에 설명한다.
- 리소스: `erd.png` 또는 HTML/SVG ERD

### 24. 센서 데이터 시계열 조회 기준

- dev 브랜치 실제 코드 기준으로 `sensor_data`는 단일 `id` primary key를 사용한다.
- 하나의 drain은 여러 sensor_data row를 가진다.
- 분석 작업은 `drain_id`와 `measured_at` 기준으로 특정 시설의 최신 센서값을 연결한다.
- 금지: composite primary key claim

### 25. 비동기 분석 요청

- scheduler 또는 운영 트리거가 분석 작업을 생성한다.
- Backend는 AnalysisJob을 기준으로 AI server에 분석 요청을 보낸다.
- 화면 응답과 분석 처리를 분리하는 것이 목적이다.
- 시각: scheduler -> AnalysisJob -> AI request

### 26. callback 저장

- AI server가 YOLO/OpenCV 결과와 XGBoost 결과를 callback으로 전달한다.
- Backend는 결과를 DB에 저장하고 작업 상태를 갱신한다.
- callback 실패 또는 중복 요청은 운영 점검 대상이다.
- 시각: AI server -> callback endpoint -> PostgreSQL

### 27. WebSocket 갱신

- WebSocket은 전체 데이터를 직접 전달하는 통로가 아니라 화면 갱신 trigger다.
- result persistence 이후 event가 발생하면 Frontend가 최신 데이터를 다시 조회한다.
- 관련 event: drain status, YOLO result, XGBoost result 갱신 계열
- 리소스: `sequence-callback-websocket.png` 또는 HTML/SVG sequence

### 28. 전체 서비스 흐름 요약

- sample image / mock sensor data
- async analysis
- AI server processing
- callback persistence
- WebSocket UI reflection
- 시각: one-line end-to-end flow

## 4. 인프라 / 운영 설계

### 29. 시스템 아키텍처

- Browser, Nginx, Frontend, Backend, AI server, PostgreSQL 구성으로 설명한다.
- 현재 구현과 향후 확장 경계를 분리한다.
- 리소스: `architecture-cropped.png` 또는 HTML/SVG architecture

### 30. Docker / Nginx / Jenkins

- Docker: 실행 환경과 배포 단위 구성
- Nginx: frontend, backend, WebSocket routing entry
- Jenkins: GitHub 변경 이후 build/deploy 흐름 구성
- 실제 production 운영 완료로 과장하지 않는다.

### 31. PostgreSQL 저장 구조

- drains: 시설 단위
- sensor_data: 시계열 센서값
- analysis_jobs: 비동기 분석 작업 상태
- yolo_results: 이미지 분석 결과
- xgboost_results: 최종 분류 결과
- 시각: storage responsibility cards

### 32. 운영 모니터링 고려

- Backend health check
- PostgreSQL 상태 확인
- AI 분석 실패 로그 추적
- WebSocket 연결 상태 확인
- callback 실패 또는 중복 요청 추적
- 향후 알림·리포트 확장 가능성
- 금지: complete production monitoring system claim

### 33. 향후 RTSP, MQTT, 알림 확장

- RTSP CCTV, MQTT sensor, alert, report는 향후 확장이다.
- 현재 발표에서는 sample images와 mock sensor data 기반 구현 범위를 명확히 유지한다.
- 시각: current scope vs future extension

## 5. 시연과 마무리

### 34. 시연 시나리오

- sample drain image와 mock sensor data를 준비한다.
- 분석 작업이 생성되고 AI server 요청으로 이어진다.
- callback 결과가 저장되고 화면이 갱신된다.
- 시각: demo checklist

### 35. 시연 흐름

- 대시보드에서 위험 시설 확인
- 상세 화면에서 이미지/센서/AI 근거 확인
- callback 저장 결과와 WebSocket 갱신 흐름 설명
- 리소스: `dashboard-main.png`, `dashboard-detail.png`

### 36. 기대효과 / Q&A

- 시설별 상태 확인
- 위험 시설 우선 확인
- 이미지·센서·AI 판단 근거 확인
- 분석 결과 저장과 화면 반영 흐름 확인
- 마지막 문장: 질문 받겠습니다.
