# SmartDrain Final Slide Map

이 문서는 최종 HTML 발표자료를 만들기 전 사용하는 구조 기준이다. `output/presentation.html`은 아직 생성하지 않는다.

## 작성 원칙

- 최종 발표자료는 한국어를 기본으로 작성한다.
- 기술명은 필요한 경우에만 English로 유지한다. 예: YOLO, OpenCV, XGBoost, FastAPI, WebSocket, PostgreSQL, Docker, Nginx, Jenkins.
- 슬라이드 번호는 구조 기준점이며 절대적인 장수 제한이 아니다.
- 내용이 조밀하면 슬라이드를 나눈다.
- 기술 내용은 과도하게 줄이지 않는다.
- DB/ERD는 callback 세부 설명보다 먼저 나온다.
- 현재 MVP 범위를 명확히 유지한다.
  - sample images
  - mock sensor data
  - async analysis
  - result persistence
  - WebSocket UI reflection
- 실제 CCTV 또는 실제 IoT 센서가 현재 연동된 것처럼 말하지 않는다.
- `sensor_data`가 composite primary key를 사용한다고 말하지 않는다.
- `risk_score`를 물리적 침수 위험 점수처럼 설명하지 않는다.
- 정확한 근거가 없는 운영 비용 추정은 포함하지 않는다.

## 전체 흐름

Fingtron 벤치마킹 자료의 내부 시나리오처럼, 완성품 소개보다 "필요성 -> 벤치마킹 -> 기술 선택 -> 구축 흐름 -> 운영 고려 -> 시연"의 순서로 설득한다. SmartDrain은 아이디어 소개가 아니라 이미지 분석, 센서 데이터, AI 판단, DB 저장, callback, WebSocket 화면 갱신까지 이어지는 구현형 프로젝트로 보여준다.

## 0. 인트로

### 1. 표지

- 발표 제목: 이미지·센서 기반 빗물받이 위험도 모니터링
- 서비스명: SmartDrain / 우수주의보
- 팀명과 발표자 정보
- 핵심 한 줄: 빗물받이 상태를 이미지와 센서 데이터로 분석해 관리자 화면에 위험도를 반영하는 MVP

### 2. 프로젝트 한 줄 요약

- 개별 빗물받이의 막힘 상태와 수위·유속 정보를 함께 보고 위험도를 판단하는 서비스
- 입력: sample images, mock sensor data
- 처리: YOLO/OpenCV 이미지 분석, XGBoost 위험도 판단, async analysis
- 출력: 위험도 상태 저장, 관리자 대시보드와 상세 화면에 WebSocket UI reflection

### 3. 팀 구성과 역할

- PM / AI: 일정 조율, 모델 실험, 데이터 구성
- Backend: FastAPI, PostgreSQL, async analysis, callback 저장, WebSocket 이벤트
- Frontend: 관리자 대시보드, 상세 화면, 지도/목록 UI, 시연 화면 구성
- AI / Data: YOLO/OpenCV 검토, XGBoost feature 설계, 시연 데이터 구성
- 개인 소개를 길게 하지 않고 역할 중심으로 간결하게 정리한다.

### 4. 목차

- 개발 필요성과 벤치마킹
- AI 분석 설계
- 웹 서버 및 서비스 구축
- 인프라 / 운영 설계
- 시연과 마무리

### 5. 전체 기술 스택/구성 한 장 요약

- Frontend: Next.js, React, TypeScript, TanStack Query, Zustand, Kakao Maps, Recharts
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic, WebSocket
- Database: PostgreSQL
- AI: YOLO, OpenCV, XGBoost, scikit-learn
- Infra / Collaboration: Docker, Nginx, Jenkins, GitHub, Notion, Slack
- 한 장에서 전체 시스템 구성을 먼저 보여주고, 이후 섹션에서 세부 선택 이유를 설명한다.

## 1. 개발 필요성과 벤치마킹

### 6. 도시 침수와 빗물받이

- 도로 위 빗물이 빠져나가는 첫 지점이 빗물받이라는 점을 설명한다.
- 집중호우 시 빗물받이 막힘이 배수 지연과 도로 침수 위험을 높인다는 문제를 제시한다.
- 단순 재난 키워드가 아니라 "관리해야 할 개별 시설" 문제로 좁힌다.

### 7. 강우 중 상태 변화

- 강우 유입량 증가, 낙엽·쓰레기 유입, 입구 차폐, 수위 상승, 유속 저하의 흐름을 보여준다.
- 정기 점검만으로는 강우 중 상태 변화를 즉시 반영하기 어렵다는 문제를 연결한다.
- 상태 변화가 빠르고 동시다발적으로 발생한다는 운영 문제를 강조한다.

### 8. 기존 점검 방식의 한계

- 현장 점검, 청소, 시민 신고, QR 기반 신고, 센서 설치 방식의 장단점을 분리한다.
- 기존 방식이 불필요하다는 주장이 아니라, 자동 상태 확인과 우선순위 판단의 공백이 남는다는 흐름으로 설명한다.

### 9. 기존 방식/서비스 벤치마킹

- 지자체 신고 서비스, QR 신고, 스마트 배수 센서, 안전신문고류 사례를 벤치마킹 대상으로 정리한다.
- 각 방식의 역할과 남는 한계를 표로 비교한다.
- 시민 발견 의존, QR 접근성, 전체 센서 설치 비용, 실시간 위험도 판단 제한을 구분한다.

### 10. SmartDrain 차별점

- 이미지 기반 막힘 상태 확인과 수위·유속 데이터를 함께 사용한다.
- 개별 빗물받이 단위로 상태를 관리한다.
- AI 결과를 DB에 저장하고 관리자 화면에 반영한다.
- 단순 신고 접수가 아니라 점검 우선순위 판단을 지원한다.
- 현재 MVP는 sample images와 mock sensor data 기반임을 명시한다.

### 11. 참고 자료/정책/사례 기반 목표

- 배수 기능 확보와 빗물받이 유지관리 관련 자료, 침수 예방 보도자료, 지자체 신고 사례를 근거로 사용한다.
- 목표는 실제 운영 완성형이 아니라 MVP에서 검증할 기능 범위를 제시하는 것이다.
- 목표: 상태 확인, 위험도 분류, 점검 우선순위 지원, 관리자 화면 반영.

### 12. 일정표

- 기획·설계
- MVP 개발
- AI 분석과 Backend 연동
- Frontend 통합
- 테스트와 발표 준비
- 일정표는 결과물이 아니라 구현 여정을 보여주는 장치로 사용한다.

## 2. AI 분석 설계

### 13. AI 분석 설계 개요

- 이미지 분석과 센서 데이터를 분리하지 않고, 최종 위험도 판단 흐름으로 연결한다.
- 입력: sample image, water level, flow velocity
- 이미지 처리: YOLO/OpenCV
- 위험도 판단: XGBoost
- 저장/반영: Backend callback, result persistence, WebSocket UI reflection

### 14. YOLO 단독 분석 한계

- YOLO는 객체 위치나 막힘 후보를 찾는 데 유용하지만, 수위·유속을 함께 고려한 최종 위험도 판단에는 한계가 있음을 설명한다.
- 이미지 품질 저하, 조명, 차폐 형태, 비정상 이미지 등 판단 불확실성을 언급한다.
- YOLO 결과만으로 물리적 침수 위험을 단정하지 않는다.

### 15. OpenCV 결합 이유

- YOLO 결과를 보완하기 위해 이미지 전처리와 차폐율 계산 보조에 OpenCV를 사용한다.
- 이미지 품질 확인, 영역 처리, 객체 탐지 결과 정리 같은 보조 역할로 설명한다.
- OpenCV가 독립적으로 모든 위험도를 판단한다고 말하지 않는다.

### 16. 차폐율·이미지 품질·객체 탐지

- 차폐율: 빗물받이 입구가 얼마나 가려졌는지 나타내는 이미지 기반 feature
- 이미지 품질: 분석 가능 여부와 신뢰도 판단에 영향을 주는 요소
- 객체 탐지: 낙엽, 쓰레기, 덮개, 그레이팅 영역 등 후보 탐지
- 판단불가 케이스를 별도 상태로 둔 이유를 설명한다.

### 17. XGBoost 입력 feature

- 이미지 분석 결과와 mock sensor data를 feature로 구성한다.
- 예시 feature:
  - blockage ratio
  - image quality flag
  - detected object indicators
  - water level
  - flow velocity
- feature는 MVP 판단 입력값으로 설명하고, 실제 침수 예측 모델처럼 과장하지 않는다.

### 18. 위험도 분류 로직

- 최종 출력 상태: 양호, 주의, 위험, 판단불가
- XGBoost 결과와 예외 조건을 통해 최종 상태를 정리한다.
- `risk_score`가 있다면 내부 분류 보조값으로만 설명한다.
- 물리적 침수 위험 점수로 표현하지 않는다.

### 19. 결과/검증

- sample images와 mock sensor data를 사용한 시나리오별 결과를 보여준다.
- 양호, 주의, 위험, 판단불가 케이스를 비교한다.
- 검증은 MVP 동작 확인과 시연 데이터 기준으로 표현한다.
- 운영 현장 검증이 완료된 것처럼 말하지 않는다.

## 3. 웹 서버 및 서비스 구축

### 20. 서비스 구축 개요

- 관리자 화면, Backend, AI Service, PostgreSQL, WebSocket의 역할을 먼저 나눈다.
- 분석 요청이 즉시 결과를 반환하는 구조가 아니라 async analysis로 처리된다는 점을 설명한다.
- AI 분석과 DB 저장 책임을 분리한다.

### 21. 관리자 대시보드 흐름

- 전체 시설 상태 요약
- 위험도 지도 또는 위치 기반 표시
- 위험 시설 목록
- 선택 시설의 최근 상태 확인
- WebSocket 이벤트 이후 UI가 최신 데이터를 다시 반영하는 흐름을 보여준다.

### 22. 상세 화면 흐름

- 현재 분석 요약
- 이미지 분석 결과
- 수위·유속 추세
- 시설 정보와 과거 상태
- AI 결과 상세 탭
- 상세 화면은 "왜 위험으로 판단했는지" 근거를 확인하는 화면으로 설명한다.

### 23. DB 설계 / ERD

- callback, WebSocket, 상세 화면 설명 전에 DB 구조를 먼저 보여준다.
- 주요 테이블 후보:
  - facilities
  - sensor_data
  - analysis_jobs
  - yolo_results
  - xgboost_results
- `sensor_data`가 composite primary key를 사용한다고 말하지 않는다.
- MVP에서는 단순한 id 참조와 관계 중심으로 설명한다.

### 24. 비동기 분석 요청

- Frontend 또는 Backend에서 분석 요청을 생성한다.
- Backend는 AnalysisJob을 만들고 AI Service에 작업을 전달한다.
- 요청 즉시 최종 결과를 기다리지 않고 job 상태를 추적한다.
- async analysis가 화면 응답성과 분석 처리 분리를 위한 선택임을 설명한다.

### 25. callback 저장

- AI Service가 분석을 마치면 Backend callback으로 결과를 전달한다.
- Backend가 callback payload를 검증하고 DB에 저장한다.
- 동일 job 또는 중복 callback 가능성을 고려해 중복 저장 방지 관점으로 설명한다.
- callback이 실패할 수 있으므로 추적 대상임을 이후 운영 모니터링 고려와 연결한다.

### 26. WebSocket 갱신

- 분석 결과 저장 후 Backend가 WebSocket 이벤트를 발행한다.
- Frontend는 이벤트를 받은 뒤 Query 캐시 재검증 또는 데이터 재조회로 UI를 갱신한다.
- WebSocket은 결과 반영 알림 역할이며, 모든 데이터를 WebSocket으로 직접 밀어 넣는 구조로 과장하지 않는다.

### 27. 전체 서비스 흐름 요약

- sample image / mock sensor data 입력
- Backend 분석 요청
- AI Service 분석
- callback 결과 저장
- PostgreSQL result persistence
- WebSocket event
- dashboard/detail UI reflection
- 이 슬라이드는 20~26번의 연결 관계를 한 장으로 정리한다.

## 4. 인프라 / 운영 설계

### 28. 시스템 아키텍처

- Frontend, Backend, AI Service, PostgreSQL, 배포/프록시 구성 요소를 한 장에 보여준다.
- 현재 구현 범위와 향후 확장 범위를 구분한다.
- 실제 CCTV/IoT 실연동을 현재 구현으로 표시하지 않는다.

### 29. Docker / Nginx / Jenkins

- Docker: 서비스 실행 환경 분리
- Nginx: 요청 라우팅 또는 프록시 구성
- Jenkins: 빌드/배포 자동화 흐름
- 인프라 섹션은 실제 운영 완성도가 아니라 MVP 실행과 통합 환경 기준으로 설명한다.

### 30. PostgreSQL 저장 구조

- 시설 정보, 센서 데이터, 분석 작업, AI 결과 저장 구조를 정리한다.
- result persistence가 가능한 이유를 DB 구조와 연결한다.
- 향후 운영 데이터가 쌓이면 모델 개선이나 리포트 확장에 활용 가능하다는 정도로만 말한다.

### 31. 운영 모니터링 고려

- 비용 슬라이드를 대체하는 안전한 운영 관점 슬라이드다.
- 정량 비용 추정은 포함하지 않는다.
- 완성된 production monitoring system이라고 주장하지 않는다.
- 고려 항목:
  - Backend health check
  - PostgreSQL 상태 확인
  - AI 분석 실패 로그 추적
  - WebSocket 연결 상태 확인
  - callback 실패 또는 중복 요청 추적
  - 향후 알림·리포트 확장 가능성

### 32. 향후 RTSP, MQTT, 알림 확장

- RTSP CCTV 실시간 이미지 수집은 향후 확장으로만 설명한다.
- MQTT 기반 실제 수위·유속 센서 연동도 향후 확장으로만 설명한다.
- 알림, 점검 요청, 리포트, LLM 기반 상황 요약은 운영 확장 후보로 제시한다.
- 현재 MVP와 future work를 시각적으로 분리한다.

## 5. 시연과 마무리

### 33. 시연 시나리오

- sample images와 mock sensor data를 시간순으로 입력한다.
- 예시 상태:
  - 양호
  - 주의
  - 위험
  - 판단불가
- 시연 목적은 실제 현장 운영 증명이 아니라 MVP 데이터 흐름 검증이다.

### 34. 시연 흐름

- 센서 데이터 저장
- 비동기 분석 실행
- callback 저장
- WebSocket 이벤트 발생
- 대시보드와 상세 화면 갱신
- 발표 중 보여줄 화면 순서를 명확히 한다.

### 35. 기대효과

- 시설별 상태와 위치를 통합 조회한다.
- 위험 시설을 우선 확인할 수 있다.
- 이미지, 수위, 유속, AI 결과를 함께 근거로 본다.
- 대시보드와 상세 화면의 상태 반영 흐름을 제공한다.
- 향후 실제 센서/카메라 연동, 알림, 리포트로 확장 가능하다.

### 36. Q&A

- 질문을 받는 마무리 슬라이드.
- 서비스명과 핵심 메시지를 짧게 다시 노출한다.
- 과장된 구현 범위나 비용 수치 없이 마무리한다.

## 제외 기준

- 정확한 근거 없는 정량 운영비는 포함하지 않는다.
- 서버, 인프라, 클라우드 사용 비용을 추정해서 말하지 않는다.
- 운영 관점은 정량 비용이 아니라 health check, 로그 추적, 연결 상태 확인, 알림·리포트 확장 가능성으로만 다룬다.
