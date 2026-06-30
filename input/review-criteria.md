# SmartDrain Review Criteria

Use this checklist before accepting style previews or the final presentation.

## Scenario

- The deck follows the implementation narrative from `input/final-slide-map.md`.
- Team introduction appears near the beginning.
- Cost slide is not present.
- Operations slide is qualitative and titled "운영 모니터링 고려".
- DB/ERD appears before callback details.
- Fingtron is used as a scenario benchmark, not as a design to copy.

## MVP Scope

- sample images are clearly described as MVP/demo data.
- mock sensor data is clearly described as MVP/demo data.
- async analysis is included.
- result persistence is included.
- WebSocket UI reflection is included.
- RTSP/CCTV and MQTT/IoT are future extensions, not current features.

## Technical Coverage

- YOLO standalone limitation is explained.
- OpenCV combination reason is explained.
- XGBoost feature inputs are explained.
- risk level classification is explained.
- callback persistence is explained.
- WebSocket update flow is explained.
- PostgreSQL storage structure is explained.
- Docker / Nginx / Jenkins are included.

## Claim Safety

- No exact operating cost estimate without evidence.
- No complete production monitoring claim.
- No real-time CCTV current integration claim.
- No real IoT/MQTT current integration claim.
- No composite primary key claim for `sensor_data`.
- No `risk_score` as physical flood-risk score.
- No field-validated flood prediction claim.

## Design / Layout

- 1920x1080 fixed-stage behavior is preserved.
- No slide has overflow or clipped text.
- Diagrams are readable.
- Screenshots, if used, are readable and relevant.
- No old draft notes or sticky comments appear.
- Korean text is legible.
- Technical names are English only where appropriate.

## Final Output

- Final deck path must be `output/presentation.html`.
- Final deck must remain a single browser-openable HTML file.
- Final deck must include keyboard navigation and slide counter.
- Do not create final deck before user selects a style preview.

