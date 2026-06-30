# SmartDrain Speaker Key Lines

Use these lines as speaker-oriented anchors. They are not full scripts. Keep the final presentation Korean-first and concise.

## 0. 인트로

### 1. 표지

오늘 발표는 빗물받이 아이디어 소개가 아니라, 이미지 분석부터 센서 데이터, AI 판단, DB 저장, callback, WebSocket 화면 반영까지 이어지는 SmartDrain MVP 구현 흐름입니다.

### 2. 프로젝트 한 줄 요약

SmartDrain은 개별 빗물받이의 sample image와 mock sensor data를 함께 분석해서 위험도 상태를 판단하고, 그 결과를 관리자 화면에 반영하는 서비스입니다.

### 3. 팀 구성과 역할

팀 소개는 역할 중심으로 보시면 됩니다. AI, Backend, Frontend, 데이터/시연 구성으로 나누어 각 파트가 하나의 분석 흐름으로 연결되도록 작업했습니다.

### 4. 목차

발표는 필요성에서 시작해 AI 분석 설계, 웹 서버 구축, 인프라와 운영 고려, 마지막 시연 흐름 순서로 진행하겠습니다.

### 5. 전체 기술 스택/구성 한 장 요약

전체 구조는 Next.js 관리자 화면, FastAPI Backend, PostgreSQL, YOLO/OpenCV, XGBoost, WebSocket으로 나뉩니다. 핵심은 이 구성요소들이 따로 있는 것이 아니라 하나의 데이터 흐름으로 연결된다는 점입니다.

## 1. 개발 필요성과 벤치마킹

### 6. 도시 침수와 빗물받이

빗물받이는 도로 위 빗물이 빠져나가는 첫 지점입니다. 이 입구가 막히면 배수 흐름이 제한되고, 강우 상황에서는 침수 위험 관리가 어려워집니다.

### 7. 강우 중 상태 변화

강우 중에는 유입량이 늘고 낙엽이나 쓰레기가 함께 들어오면서 상태가 빠르게 바뀝니다. 정기 점검만으로는 이런 변화를 즉시 반영하기 어렵습니다.

### 8. 기존 점검 방식의 한계

기존 점검, 청소, 시민 신고, QR 관리, 센서 방식은 각각 역할이 있습니다. 다만 자동 상태 확인과 점검 우선순위 판단에는 여전히 공백이 남습니다.

### 9. 기존 방식/서비스 벤치마킹

기존 사례를 보면 신고 접수와 시설 관리번호 연결은 잘 되어 있지만, 발견 단계가 시민이나 현장 점검에 의존하는 경우가 많습니다.

### 10. SmartDrain 차별점

SmartDrain은 이미지 기반 막힘 상태와 수위·유속 데이터를 함께 보고, 개별 빗물받이 단위로 위험도 판단을 보조한다는 점에서 차별화됩니다.

### 11. 참고 자료/정책/사례 기반 목표

목표는 실제 운영 완성형을 주장하는 것이 아니라, MVP 범위에서 상태 확인, 위험도 분류, 점검 우선순위 지원, 관리자 화면 반영을 검증하는 것입니다.

### 12. 일정표

일정은 기획, MVP 개발, AI와 Backend 연동, Frontend 통합, 테스트와 발표 준비 순서로 진행했습니다.

## 2. AI 분석 설계

### 13. AI 분석 설계 개요

AI 분석은 이미지 분석과 센서 데이터를 따로 보지 않고, 최종 위험도 상태 판단으로 연결하는 구조입니다.

### 14. YOLO 단독 분석 한계

YOLO는 이미지 안의 막힘 후보를 찾는 데 유용하지만, 수위와 유속까지 고려한 최종 상태 판단을 혼자 담당하기에는 한계가 있습니다.

### 15. OpenCV 결합 이유

OpenCV는 이미지 전처리와 영역 계산, 차폐율 보조 분석을 위해 결합했습니다. YOLO 결과를 더 구조화된 feature로 바꾸는 역할입니다.

### 16. 차폐율·이미지 품질·객체 탐지

이미지에서 보는 핵심은 막힘 비율, 이미지 품질, 객체 탐지 결과입니다. 분석이 어려운 경우에는 판단불가 상태도 별도로 둡니다.

### 17. XGBoost 입력 feature

XGBoost에는 obstruction ratio, confidence score, water level, flow velocity 같은 feature가 들어갑니다. 이 값들은 MVP 상태 분류를 위한 입력입니다.

### 18. 위험도 분류 로직

최종 상태는 양호, 주의, 위험, 판단불가로 구분합니다. `risk_score`는 물리적 침수 점수가 아니라 모델 분류를 보조하는 내부 값으로 봅니다.

### 19. 결과/검증

검증은 sample images와 mock sensor data로 구성한 시나리오 기준입니다. 실제 현장 검증 완료가 아니라 MVP 동작 확인으로 표현합니다.

## 3. 웹 서버 및 서비스 구축

### 20. 서비스 구축 개요

서비스는 관리자 화면, Backend, AI Service, PostgreSQL, WebSocket으로 구성됩니다. 분석은 동기 응답이 아니라 async analysis로 처리합니다.

### 21. 관리자 대시보드 흐름

대시보드에서는 전체 상태 요약, 지도/목록, 위험 시설 우선 확인이 핵심입니다. 분석 결과가 갱신되면 화면도 최신 상태를 반영합니다.

### 22. 상세 화면 흐름

상세 화면은 왜 특정 상태로 판단됐는지 근거를 보는 화면입니다. 이미지 분석, 수위·유속, AI 결과, 이력을 함께 확인합니다.

### 23. DB 설계 / ERD

callback과 WebSocket을 설명하기 전에 DB 구조를 먼저 봐야 합니다. 분석 작업, 센서 데이터, YOLO 결과, XGBoost 결과가 어떻게 연결되는지가 핵심입니다.

### 24. 비동기 분석 요청

Backend는 최신 센서 데이터를 찾고 AnalysisJob을 생성한 뒤 AI Service에 분석을 요청합니다. 최종 결과를 기다리지 않고 job 상태를 추적합니다.

### 25. callback 저장

AI Service는 YOLO와 XGBoost 결과를 callback으로 전달합니다. Backend는 이를 검증하고 DB에 저장하며, 중복 callback은 idempotent하게 처리합니다.

### 26. WebSocket 갱신

결과가 저장되면 Backend가 WebSocket 이벤트를 발행합니다. Frontend는 이벤트를 받고 필요한 데이터를 다시 반영해 UI를 갱신합니다.

### 27. 전체 서비스 흐름 요약

전체 흐름은 sample image와 mock sensor data 입력, async analysis, callback, DB 저장, WebSocket 이벤트, UI 반영으로 이어집니다.

## 4. 인프라 / 운영 설계

### 28. 시스템 아키텍처

시스템 아키텍처는 현재 MVP 구현 범위와 향후 확장 범위를 구분해서 보여줘야 합니다. 실제 CCTV나 IoT 연동은 향후 확장입니다.

### 29. Docker / Nginx / Jenkins

Docker는 실행 환경 분리, Nginx는 요청 라우팅, Jenkins는 검증과 배포 흐름을 담당하는 구성으로 설명합니다.

### 30. PostgreSQL 저장 구조

PostgreSQL은 시설 정보, 센서 데이터, 분석 작업, AI 결과를 저장합니다. result persistence가 가능한 이유를 DB 구조와 연결해 보여줍니다.

### 31. 운영 모니터링 고려

여기서는 비용이 아니라 운영 중 확인해야 할 지점을 다룹니다. Backend health check, PostgreSQL 상태, AI 실패 로그, WebSocket 연결, callback 실패나 중복 요청 추적이 대상입니다.

### 32. 향후 RTSP, MQTT, 알림 확장

RTSP CCTV, MQTT 센서, 알림과 리포트는 현재 구현이 아니라 향후 확장입니다. MVP와 future work를 분명히 나눠서 말합니다.

## 5. 시연과 마무리

### 33. 시연 시나리오

시연은 sample images와 mock sensor data로 양호, 주의, 위험, 판단불가 흐름을 보여주는 방식입니다.

### 34. 시연 흐름

시연 순서는 센서 데이터 저장, 비동기 분석 실행, callback 저장, WebSocket 이벤트, 대시보드와 상세 화면 갱신입니다.

### 35. 기대효과

기대효과는 시설별 상태 통합 조회, 위험 시설 우선 확인, 판단 근거 확인, 향후 실제 센서와 카메라 연동 가능성입니다.

### 36. Q&A

마지막에는 SmartDrain이 하나의 추적 가능한 분석 흐름을 만든 MVP라는 핵심 메시지로 마무리합니다.

