# SmartDrain Content Spec

This file defines what the final presentation must cover. It should be used together with `input/final-slide-map.md`.

## Required Sections

### 0. 인트로

Goal: 프로젝트를 짧게 정의하고 발표자가 어떤 구현 범위를 보여줄지 잡아준다.

Required slides:

- 표지
- 프로젝트 한 줄 요약
- 팀 구성과 역할
- 목차
- 전체 기술 스택/구성 한 장 요약

Required message:

- SmartDrain은 빗물받이 상태를 이미지와 센서 데이터로 판단하는 MVP다.
- 팀 소개는 역할 중심으로 짧게 정리한다.
- 전체 기술 스택을 먼저 보여준 뒤 세부 구현 여정을 따라간다.

### 1. 개발 필요성과 벤치마킹

Goal: 빗물받이 관리가 왜 필요한지, 기존 방식이 어떤 한계를 남기는지, SmartDrain이 어떤 공백을 채우는지 설명한다.

Required slides:

- 도시 침수와 빗물받이
- 강우 중 상태 변화
- 기존 점검 방식의 한계
- 기존 방식/서비스 벤치마킹
- SmartDrain 차별점
- 참고 자료/정책/사례 기반 목표
- 일정표

Required message:

- 빗물받이는 도로 배수의 첫 유입 지점이다.
- 낙엽, 쓰레기, 토사 등으로 차폐되면 배수 흐름이 제한된다.
- 정기 점검과 시민 신고는 중요하지만, 강우 중 동시다발 상태 변화를 자동으로 반영하기 어렵다.
- SmartDrain은 신고 대체 서비스가 아니라 상태 확인과 점검 우선순위 판단을 보조하는 MVP다.

### 2. AI 분석 설계

Goal: YOLO/OpenCV/XGBoost를 왜 나누어 사용했는지, 어떤 feature로 최종 위험도 상태를 판단하는지 설명한다.

Required slides:

- AI 분석 설계 개요
- YOLO 단독 분석 한계
- OpenCV 결합 이유
- 차폐율·이미지 품질·객체 탐지
- XGBoost 입력 feature
- 위험도 분류 로직
- 결과/검증

Required message:

- YOLO는 이미지 안의 막힘 후보와 영역을 찾는 데 사용한다.
- OpenCV는 이미지 전처리, 영역 계산, 차폐율 보조 분석에 사용한다.
- XGBoost는 이미지 분석 결과와 센서 데이터를 함께 입력받아 상태를 분류한다.
- 출력 상태는 양호, 주의, 위험, 판단불가다.
- `risk_score`는 내부 분류 보조값이며 물리적 침수 위험 점수가 아니다.

### 3. 웹 서버 및 서비스 구축

Goal: 사용자 화면, Backend, AI Service, DB, WebSocket이 하나의 서비스 흐름으로 연결되는 구조를 보여준다.

Required slides:

- 서비스 구축 개요
- 관리자 대시보드 흐름
- 상세 화면 흐름
- DB 설계 / ERD
- 비동기 분석 요청
- callback 저장
- WebSocket 갱신
- 전체 서비스 흐름 요약

Required message:

- DB/ERD는 callback 세부 설명보다 먼저 나온다.
- Backend는 분석 요청 전에 AnalysisJob을 생성한다.
- AI Service는 YOLO와 XGBoost 결과를 callback으로 전달한다.
- Backend는 callback 결과를 DB에 저장하고 WebSocket 이벤트를 발행한다.
- Frontend는 이벤트를 받은 뒤 UI 상태를 갱신한다.

### 4. 인프라 / 운영 설계

Goal: MVP 실행 환경과 향후 운영 고려사항을 보여주되, production-complete claim은 피한다.

Required slides:

- 시스템 아키텍처
- Docker / Nginx / Jenkins
- PostgreSQL 저장 구조
- 운영 모니터링 고려
- 향후 RTSP, MQTT, 알림 확장

Required message:

- Docker, Nginx, Jenkins는 MVP 실행과 통합 환경의 구성 요소로 설명한다.
- 운영 모니터링은 고려사항으로만 제시한다.
- 비용 추정은 포함하지 않는다.
- RTSP, MQTT, 알림, 리포트는 향후 확장이다.

### 5. 시연과 마무리

Goal: sample images와 mock sensor data를 사용한 MVP 데이터 흐름 검증을 보여준다.

Required slides:

- 시연 시나리오
- 시연 흐름
- 기대효과
- Q&A

Required message:

- 시연은 실제 현장 운영 증명이 아니라 MVP 흐름 검증이다.
- 시연 순서는 센서 데이터 저장, 비동기 분석 실행, callback 저장, WebSocket 이벤트, UI 갱신이다.
- 기대효과는 상태 통합 조회, 위험 시설 우선 확인, 판단 근거 확인, 향후 확장 가능성이다.

## Content Density

Use high-density / reading-first as the default because this is a technical project report. However, avoid cramped slides. Split dense topics into multiple slides rather than reducing important technical content.

## Required Technical Terms

Keep these terms in English:

- YOLO
- OpenCV
- XGBoost
- FastAPI
- PostgreSQL
- WebSocket
- callback
- async analysis
- Docker
- Nginx
- Jenkins
- RTSP
- MQTT

## Must Not Include

- unsupported exact operating cost
- complete production monitoring claim
- real-time CCTV integration as current implementation
- real IoT/MQTT integration as current implementation
- composite primary key claim for `sensor_data`
- `risk_score` as a physical flood-risk score
- final `output/presentation.html` before style preview selection

