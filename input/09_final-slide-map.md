# 우수주의보 Final Slide Map

이 문서는 최종 Korean HTML 발표자료 `output/presentation.html` 제작 기준이다. 스타일은 Style A: 절제된 기술 보고서형으로 고정한다.

## 작성 원칙

- visible project/team name은 `우수주의보`로만 사용한다.
- `SmartDrain`은 visible slide text에 사용하지 않는다.
- `벤치마킹`, `차폐율`, `이미지 품질`은 visible slide text에 사용하지 않는다.
- `MVP`는 가급적 사용하지 않고, 필요한 범위 설명은 `현재 구현 범위`, `구현 흐름`, `서비스 흐름`, `시연 구성`으로 표현한다.
- Frontend가 분석을 요청한다고 쓰지 않는다.
- 분석 작업은 scheduler가 생성한다.
- 우기 운영 가정에서는 scheduler가 10분 주기로 작업을 만들 수 있다고 표현한다.
- Backend가 AI 서버에 분석을 요청하고, Backend가 callback으로 결과를 받는다.
- WebSocket은 화면 갱신 trigger로 설명한다. Frontend는 event를 받은 뒤 최신 데이터를 다시 조회한다.
- 실시간 CCTV, 실제 IoT 센서, MQTT 운영 연동은 현재 구현으로 말하지 않는다.
- `risk_score` 또는 최종 위험 점수는 실제 침수 확률이 아니라 우수주의보 내부 위험도 분류 점수로 설명한다.
- 비용 슬라이드, 별도 운영 모니터링 슬라이드, 상세 시연 시나리오 슬라이드는 제거한다.
- 이미지 asset이 없으면 깨진 이미지 대신 placeholder frame을 둔다.

## 0. 인트로

### 1. 표지

- 제목: 우수주의보
- 부제: 이미지·센서 기반 빗물받이 위험도 모니터링
- 핵심 문장: 강우 중 개별 빗물받이 상태를 이미지 분석과 센서값으로 판단하고, 결과를 DB와 화면 갱신 흐름으로 연결한 프로젝트
- [금지: SmartDrain visible project name]

### 2. 프로젝트 한 줄 요약 + 전체 흐름 도식

- 한 줄 요약: 이미지·센서 입력부터 scheduler, Backend, AI 서버, callback, DB 저장, WebSocket 화면 갱신까지 연결한다.
- [도식: 이미지·센서 입력 → 스케줄러 → Backend → AI 서버 → callback → DB 저장 → WebSocket → 대시보드·상세 화면 갱신]
- [금지: MVP]

### 3. 팀 구성과 역할

- 송희수: YOLO, OpenCV 모델 튜닝, 이미지 데이터 라벨링, AI 파이프라인 설계.
- 이명근: Backend 서버, DB 연동, callback 저장, WebSocket 처리 구조.
- 오택률: Frontend 화면 구현, 인프라 구성, Jenkins CI/CD.
- 김윤섭: 발표자료 구성, XGBoost 학습용 데이터 기준 설계, AI 서버와 Backend 서버 간 통신 구조 설계.

### 4. 목차

- 개발 필요성과 기존 방식 검토
- AI 분석 설계
- 웹 서버 및 서비스 구축
- 인프라 / 운영 설계
- 마무리

### 5. 전체 기술 스택/구성 + 전체 아키텍처 요약

- Frontend: Next.js, React, TypeScript, TanStack Query, Zustand, Kakao Maps, Recharts
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic, WebSocket
- AI: YOLO, OpenCV, XGBoost, scikit-learn
- DB/Infra: PostgreSQL, Docker, Nginx, Jenkins
- [이미지: 전체 시스템 아키텍처 이미지]
- [도식: Frontend → Backend → AI 서버 → DB → WebSocket 화면 갱신 흐름]
- [캡션: 전체 시스템 아키텍처 이미지 삽입 예정]

## 1. 개발 필요성과 기존 방식 검토

### 6. 도시 침수와 빗물받이

- 빗물받이는 도로 위 빗물이 배수관으로 들어가는 첫 유입 지점이다.
- 낙엽, 쓰레기, 토사 등으로 막히면 강우 중 배수 흐름이 제한된다.
- 개별 시설 상태를 빠르게 파악하는 흐름이 점검 우선순위 판단에 도움이 된다.
- [이미지: 막힌 빗물받이 사진 또는 관련 뉴스 이미지]
- [도식: 도로 위 빗물 → 빗물받이 → 배수관 흐름]
- [캡션: 막힌 빗물받이 사진 삽입 예정]

### 7. 강우 중 상태 변화

- 강우량 증가, 이물질 유입, 막힌비율 증가, 수위 상승, 유속 저하가 순차 또는 동시 발생할 수 있다.
- 정기 점검 시점과 실제 강우 중 상태가 달라질 수 있다는 점을 문제로 제시한다.
- [도식: 강우 → 이물질 유입 → 막힌비율 증가 → 수위 상승 → 유속 저하]

### 8. 기존 점검 방식의 한계

- 정기 점검과 청소는 유지관리에서 필요하다.
- 다만 강우 중 빠르게 변하는 현재 상태 판단에는 시간차와 관측 공백이 생긴다.
- 시민 신고는 현장 발견에 유용하지만, 개별 시설의 위험도 우선순위를 자동으로 정리하기는 어렵다.

### 9. 기존 방식/사례 검토 ① 점검·신고

- 정기 점검: 유지관리 기준을 세우는 데 효과적이지만 강우 중 변화 반영이 늦을 수 있다.
- 시민 신고: 현장 발견에 도움이 되지만 신고 접근성과 위치 정확도에 영향을 받는다.
- [표: 기존 방식/사례 검토 ① - 정기 점검, 시민 신고]

### 10. 기존 방식/사례 검토 ② QR·센서·관제

- QR·관리번호: 신고 위치 특정과 관리 이력 연결에 유용하다.
- 센서: 수위·유속 등 수치 상태를 볼 수 있지만 설치·운영 범위가 제한될 수 있다.
- 관제: 여러 지점을 모아 보는 데 유용하지만 개별 빗물받이의 막힘 근거가 부족할 수 있다.
- [표: 기존 방식/사례 검토 ② - QR·관리번호, 센서, 관제]

### 11. 우수주의보 차별점

- 이미지와 센서값을 함께 사용해 개별 빗물받이 단위 상태를 판단한다.
- AI 판단 근거를 DB에 저장하고 대시보드와 상세 화면에 반영한다.
- 신고 대체가 아니라 상태 확인과 점검 우선순위 판단을 보조한다.
- [표: 기존 방식의 한계와 우수주의보 보완점]

### 12. 참고 자료/정책/사례 기반 목표

- 기존 관리·신고 체계와 도시 침수 대응 흐름을 참고해 기능 범위를 잡는다.
- 정확한 출처가 확인되지 않은 수치나 비용은 사용하지 않는다.
- 목표는 개별 빗물받이 상태 판단, 근거 저장, 화면 반영 흐름 구현이다.
- [참고이미지: 관련 정책·사례 자료]
- [캡션: 기존 관리·신고 체계를 참고해 개별 빗물받이 상태 판단 흐름을 목표로 설정]
- [캡션: 정책·사례 참고 이미지 삽입 예정]

### 13. 일정표

- 기획·설계
- AI 분석 설계
- Backend/DB 구현
- Frontend 구현
- 통합·시연 준비
- [도식: 기획·설계 → AI 분석 설계 → Backend/DB 구현 → Frontend 구현 → 통합·시연 준비]

## 2. AI 분석 설계

### 14. AI 분석 설계 개요: YOLO + OpenCV

- YOLO는 visible object/region 탐지에 사용한다.
- OpenCV는 실제 막힌 영역 해석과 전처리 보조에 사용한다.
- 두 결과를 함께 사용해 막힌비율 판단으로 연결한다.
- [이미지: YOLO 탐지 결과 이미지]
- [이미지: OpenCV 처리 결과 이미지]
- [도식: YOLO 탐지 결과 + OpenCV 처리 결과 → 막힌비율 판단]
- [캡션: YOLO 탐지 결과 이미지 삽입 예정]
- [캡션: OpenCV 처리 결과 이미지 삽입 예정]

### 15. 막힌비율 판단 구조

- YOLO는 배수구와 이물질 후보 영역을 탐지한다.
- OpenCV는 전처리, 영역 분리, mask 처리, 그림자·어두운 영역 보정, obstruction area estimation을 보조한다.
- 최종 막힌비율은 YOLO와 OpenCV output을 함께 사용해 판단한다.
- [도식: YOLO 객체 탐지 + OpenCV 마스크 처리 → 막힌비율 계산]
- [이미지: OpenCV 마스크 또는 전처리 결과 이미지]
- [캡션: OpenCV 마스크 처리 이미지 삽입 예정]

### 16. XGBoost 입력과 위험도 분류

- 입력 기준: 막힌비율, 탐지 신뢰도, 수위, 유속.
- 출력 상태: 양호, 주의, 위험, 판단불가.
- 최종 위험 점수는 우수주의보 내부 분류를 위한 계산 점수다.
- [표: XGBoost 입력 기준 - 막힌비율, 탐지 신뢰도, 수위, 유속]
- [도식: 이미지 분석 결과 + 센서값 → XGBoost → 양호·주의·위험·판단불가]

### 17. 결과/검증

- 입력 기준: 막힌비율, 탐지 신뢰도, 수위, 유속.
- 영상 막힘 점수 = 막힌비율 × 탐지 신뢰도.
- 센서 정체 점수 = 수위 × (1 - 유속).
- 최종 위험 점수 = 영상 막힘 점수 45% + 센서 정체 점수 45% + 수위 10%.
- 양호: 위험 점수 0.35 미만이며 배수 흐름이 정상에 가까운 상태.
- 주의: 위험 점수 0.35 이상이거나 막힘·정체 징후가 나타난 상태.
- 위험: 위험 점수 0.65 이상이거나 수위 상승과 유속 저하가 뚜렷한 상태.
- 판단불가: 센서 이상 또는 영상 분석 실패로 신뢰도 있는 판단이 어려운 상태.
- 예외: YOLO 분석이 실패했더라도 센서가 명확히 위험하면 위험으로 분류한다.
- [표: 입력 기준 - 막힌비율, 탐지 신뢰도, 수위, 유속]
- [도식: 영상 막힘 점수 + 센서 정체 점수 + 수위 보정 → 최종 위험 점수]
- [표: 위험도 분류 요약 - 양호, 주의, 위험, 판단불가]
- [캡션: 최종 위험 점수는 실제 침수 확률이 아니라, 우수주의보 내부 위험도 분류를 위한 계산 점수]
- [참고이미지: YOLO + OpenCV 오차 그래프 또는 XGBoost 분류 공간 이미지]
- [캡션: 검증 그래프 또는 분류 공간 이미지 삽입 예정]

## 3. 웹 서버 및 서비스 구축

### 18. 서비스 구축 개요

- 시스템은 dashboard, Backend server, AI server, PostgreSQL, WebSocket으로 구성된다.
- scheduler가 분석 작업을 생성한다.
- Backend는 AI 서버에 분석 요청을 보내고 callback으로 결과를 받는다.
- [도식: 스케줄러 → Backend 작업 생성 → AI 서버 요청 → callback 수신 → DB 저장 → WebSocket 갱신]

### 19. 관리자 대시보드 흐름

- 전체 현황, 지도, 위험 시설 목록, 선택 시설 정보를 확인한다.
- WebSocket event 이후 최신 데이터를 다시 조회해 화면을 갱신한다.
- [이미지: 관리자 대시보드 화면]
- [도식: 전체 현황 확인 → 위험 시설 선택 → 상세 화면 이동]
- [캡션: 관리자 대시보드 화면 삽입 예정]

### 20. 상세 화면 흐름

- 이미지 분석 결과, 센서 추이, AI 결과, 이력을 시설 단위로 확인한다.
- 상세 화면은 왜 해당 상태로 판단됐는지 근거를 보여준다.
- [이미지: 시설 상세 화면]
- [도식: 이미지 근거 + 센서 근거 + AI 결과 + 이력 → 시설별 판단 근거]
- [캡션: 시설 상세 화면 삽입 예정]

### 21. DB 설계 / ERD

- drains, sensor_data, yolo_results, xgboost_results, analysis_jobs 관계를 먼저 보여준다.
- callback 저장과 WebSocket 갱신은 DB 저장 구조 뒤에서 설명한다.
- [이미지: ERD 이미지]
- [도식: drains, sensor_data, yolo_results, xgboost_results, analysis_jobs 관계]
- [캡션: ERD 이미지 삽입 예정]

### 22. 센서 데이터 시계열 조회 기준

- dev 브랜치 실제 코드 기준으로 `sensor_data`는 단일 `id`를 primary key로 사용한다.
- 하나의 빗물받이는 여러 시계열 센서 기록을 가진다.
- 분석 작업은 `drain_id`와 `measured_at` 기준으로 특정 시설의 최신 센서값을 조회해 연결한다.
- [도식: id PK → drain_id FK → measured_at 조회 기준]
- [표: 센서 데이터 시계열 조회 기준 - id, drain_id, measured_at]
- [금지: sensor_data composite primary key claim]

### 23. 스케줄러 기반 비동기 분석 작업 생성

- Frontend가 분석을 요청하지 않는다.
- scheduler가 분석 작업을 생성한다.
- 우기 운영 가정에서는 10분 주기로 작업을 만들 수 있다.
- Backend가 AI 서버에 분석 요청을 보낸다.
- [도식: 스케줄러 → 분석 작업 생성 → Backend → AI 서버 요청]

### 24. callback 저장

- AI 서버는 분석 결과를 callback으로 Backend에 전달한다.
- Backend는 YOLO/OpenCV result와 XGBoost final result를 분리해 저장한다.
- 작업 상태와 중복 callback 처리 기준도 함께 관리한다.
- [도식: AI 서버 → callback → Backend → DB 저장]
- [표: callback 저장 대상 - 이미지 분석 결과, 최종 위험도 결과, 작업 상태]

### 25. WebSocket 갱신

- WebSocket은 화면 갱신 trigger다.
- Frontend는 event를 수신한 뒤 최신 데이터를 재조회하고 dashboard/detail view를 갱신한다.
- [도식: Backend WebSocket 이벤트 → Frontend 수신 → 최신 데이터 재조회 → 화면 갱신]

### 26. 전체 서비스 흐름 요약

- scheduler 작업 생성에서 화면 갱신까지 전체 흐름을 한 장으로 연결한다.
- Backend request, AI analysis, callback receive, DB persist, WebSocket update의 책임을 분리한다.
- [도식: 스케줄러 작업 생성 → Backend 요청 → AI 분석 → callback 수신 → DB 저장 → WebSocket 갱신]

## 4. 인프라 / 운영 설계

### 27. 시스템 아키텍처

- Browser, Nginx, Frontend, Backend, AI server, PostgreSQL 구성을 보여준다.
- 현재 구현과 향후 확장 범위를 구분한다.
- [이미지: 전체 시스템 아키텍처 이미지]
- [도식: Browser → Nginx → Frontend / Backend / AI 서버 / PostgreSQL]
- [캡션: 시스템 아키텍처 이미지 삽입 예정]

### 28. Docker / Nginx / Jenkins CI/CD

- Docker: service runtime과 배포 단위 구성.
- Nginx: request routing과 frontend/backend entry point 구성.
- Jenkins: CI/CD flow 구현에 사용.
- [도식: GitHub → Jenkins → Docker build/deploy → Docker Compose 실행]
- [표: Docker, Nginx, Jenkins 역할]

### 29. 향후 RTSP, MQTT, 알림 확장

- RTSP CCTV, MQTT sensor, alert, report는 향후 확장 범위다.
- 현재 구현 범위와 future work를 분리해 표현한다.
- [도식: 현재 구조 → RTSP CCTV / MQTT 센서 / 알림 / 리포트 확장]
- [표: 현재 구현과 향후 확장 구분]

## 5. 마무리

### 30. 기대효과

- 시설별 상태 확인.
- 위험 시설 우선순위 확인.
- 이미지·센서·AI 판단 근거 확인.
- 분석 결과 저장과 화면 반영 흐름 확인.
- [표: 기대효과 - 상태 확인, 우선순위, 판단 근거, 화면 반영]

### 31. Q&A

- Q&A만 간결하게 표시한다.
- [이미지: GitHub 또는 Demo QR 코드]
- [캡션: Q&A]
- [캡션: GitHub 또는 Demo QR 코드 삽입 예정]
