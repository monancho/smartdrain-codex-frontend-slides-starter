# SmartDrain Claim Safety

Use this file to prevent unsupported or exaggerated claims in the final presentation.

## Safe Core Claim

SmartDrain is an MVP that connects sample images, mock sensor data, AI analysis, database persistence, callback handling, and WebSocket-based UI reflection into one traceable service flow.

## Current MVP: Safe To Say

- sample images are used for image analysis scenarios.
- mock sensor data is used for water level and flow velocity scenarios.
- Backend creates and tracks async analysis jobs.
- AI Service analyzes an image source resolved by `drain_id`.
- YOLO/OpenCV output is converted into XGBoost input features.
- XGBoost classifies status using image-derived values and sensor values.
- Backend receives YOLO and XGBoost callbacks.
- Backend stores callback results in PostgreSQL.
- Backend treats duplicate callbacks idempotently.
- Backend broadcasts WebSocket events after result persistence.
- Frontend listens to WebSocket events and reflects updated drain status in the UI.
- The presentation may describe RTSP, MQTT, alerts, and reports as future extensions.

## Must Not Say

Do not say:

- "실시간 CCTV가 현재 연동되어 있다."
- "실제 IoT 센서가 현재 운영 연동되어 있다."
- "MQTT 센서 연동이 현재 구현되어 운영 중이다."
- "현장 침수 위험을 정확히 예측한다."
- "risk_score는 실제 물리적 침수 위험 점수다."
- "`sensor_data`는 composite primary key를 사용한다."
- "운영 비용은 월/일 단위로 얼마다."
- "production monitoring system이 완성되어 있다."
- "실제 지자체 운영 환경에서 검증됐다."
- "AI가 현장 출동 여부를 자동 결정한다."

## Preferred Wording

Use these safer expressions:

- "현재 MVP는 sample images와 mock sensor data를 사용합니다."
- "RTSP CCTV 연동은 향후 확장 범위입니다."
- "MQTT 기반 실제 센서 연동은 향후 확장 범위입니다."
- "`risk_score`는 모델 분류를 보조하는 내부 값으로 다룹니다."
- "`sensor_data`는 단일 `id`를 primary key로 가지며, `drain_id`로 시설과 연결됩니다."
- "운영 모니터링은 health check, 로그 추적, 연결 상태 확인 관점에서 고려합니다."
- "시연은 실제 현장 운영 증명이 아니라 MVP 데이터 흐름 검증입니다."
- "AI 결과는 점검 우선순위 판단을 보조합니다."

## Specific Risk Areas

### CCTV / Image Source

Safe:

- sample image
- mock image source
- future RTSP integration

Unsafe:

- real-time CCTV integration as current feature
- live CCTV stream analysis as implemented production function

### Sensor Data

Safe:

- mock sensor data
- water level
- flow velocity
- latest sensor data is used for analysis

Unsafe:

- real IoT sensor deployment
- MQTT operational integration as current implementation
- physical sensor accuracy validation

### AI Model

Safe:

- YOLO/OpenCV helps analyze obstruction-related image features.
- XGBoost classifies status from image-derived and sensor-derived features.
- output status: good, caution, danger, unknown

Unsafe:

- field-validated flood prediction
- deterministic flood-risk calculation
- AI decides emergency dispatch by itself

### Database / ERD

Safe:

- `sensor_data.id` is the primary key.
- `sensor_data.drain_id` links to the drain/facility.
- `analysis_jobs` links a request to sensor data, YOLO result, and status tracking.
- XGBoost result links to `sensor_data_id` and `yolo_result_id`.

Unsafe:

- `sensor_data` composite primary key claim
- unverified table names not present in source context

### Callback / WebSocket

Safe:

- YOLO and XGBoost callbacks are separate.
- duplicate callbacks are handled idempotently.
- WebSocket events notify frontend after result persistence.
- frontend reconnects when the socket closes.

Unsafe:

- every UI field is streamed directly over WebSocket
- WebSocket alone is the source of all data
- callback delivery is guaranteed under all network conditions

### Operations

Safe:

- Backend health check
- PostgreSQL status check
- AI analysis failure log tracking
- WebSocket connection status check
- callback failure or duplicate request tracking
- future alert/report extension

Unsafe:

- exact operating cost estimate
- complete production observability platform
- field operation SLA

