# SmartDrain Project Context

## Project Identity

- Project name: SmartDrain
- Presentation title: 이미지·센서 기반 빗물받이 위험도 모니터링
- Korean service name: 우수주의보
- Presentation language: Korean
- Deck type: technical project report / portfolio-style presentation
- Core benchmark: Fingtron-style implementation narrative

## One-Line Summary

SmartDrain은 개별 빗물받이의 sample image와 mock sensor data를 함께 분석해 위험도 상태를 판단하고, 결과를 PostgreSQL에 저장한 뒤 WebSocket 이벤트로 관리자 화면에 반영하는 MVP다.

## Core Narrative

이 발표는 아이디어 소개형 발표가 아니라 구현 과정을 보여주는 프로젝트 보고서형 발표다. Fingtron 벤치마킹 자료처럼 다음 흐름을 따른다.

1. 왜 필요한가
2. 기존 방식은 무엇을 해결하고 무엇을 남기는가
3. 어떤 기술을 검토했고 왜 선택했는가
4. AI 분석은 어떤 입력과 출력을 가지는가
5. Backend, DB, callback, WebSocket은 어떻게 연결되는가
6. MVP는 어디까지 구현됐고 무엇은 향후 확장인가
7. 시연에서 어떤 데이터 흐름을 검증하는가

## MVP Scope

Current MVP includes:

- sample images by drain/facility
- mock water level and flow velocity data
- async analysis job creation
- YOLO/OpenCV image analysis
- XGBoost risk level classification
- YOLO and XGBoost callback persistence
- PostgreSQL result persistence
- WebSocket event broadcast
- dashboard/detail UI reflection

Current MVP does not include:

- real-time CCTV or RTSP integration
- real IoT sensor or MQTT integration
- complete production monitoring system
- field-validated flood prediction model
- exact operating cost model
- user authentication/authorization as a central presentation claim

## Technical Stack

Frontend:

- Next.js
- React
- TypeScript
- TanStack Query
- Zustand
- Kakao Maps
- Recharts

Backend:

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- WebSocket

Database:

- PostgreSQL

AI:

- YOLO
- OpenCV
- XGBoost
- scikit-learn

Infra / Collaboration:

- Docker
- Nginx
- Jenkins
- GitHub
- Notion
- Slack

## Confirmed Implementation Facts From Code Excerpts

- `sensor_data` has a single `id` primary key.
- `sensor_data` stores `drain_id`, `water_level_cm`, `flow_velocity_mps`, `measured_at`, and `created_at`.
- `analysis_jobs` stores `request_id`, `job_id`, `drain_id`, `sensor_data_id`, `sensor_measured_at`, `yolo_result_id`, `status`, and `trigger_type`.
- Backend creates an `AnalysisJob` before requesting AI analysis.
- Backend sends the latest sensor data to AI Service.
- AI Service resolves an image source by `drain_id`.
- AI Service runs YOLO first, then builds XGBoost input from sensor data and YOLO result.
- XGBoost input features include `obstruction_ratio`, `confidence_score`, `water_level`, and `flow_velocity`.
- YOLO callback and XGBoost callback are separate endpoints.
- Duplicate YOLO and XGBoost callbacks are treated idempotently and do not rebroadcast events.
- XGBoost callback stores final result, updates drain status, and generates WebSocket events.
- Frontend WebSocket listener handles `DRAIN_STATUS_UPDATED`, `YOLO_RESULT_UPDATED`, and `XGBOOST_RESULT_UPDATED`.
- Frontend reconnects when the WebSocket closes unexpectedly.

## Presentation Tone

- Confident but not overclaiming.
- Technical enough to show implementation depth.
- Clear about MVP boundaries.
- Avoid marketing-heavy wording.
- Avoid saying the system is field-proven or production-complete.
- Emphasize traceable service flow: input -> analysis -> callback -> DB -> WebSocket -> UI.

