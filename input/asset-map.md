# SmartDrain Asset Map

## Current Asset Status

No final curated `input/assets` set has been rebuilt yet.

For the next style-preview step, use CSS/SVG/HTML-generated visuals rather than relying on missing image assets. The previews should look like real SmartDrain title slides, but they do not need project screenshots yet.

## Available References

### Source Decks

- `references/source-decks/01-low-density-static-reference.pdf`
  - Use only as a cleanliness reference.
  - Do not copy its slide layout directly.

- `references/source-decks/02-content-heavy-draft-reference.pdf`
  - Use as SmartDrain content reference.
  - Do not copy draft notes, sticky notes, inconsistent density, or old layout.

### Code Excerpts

- `references/code-excerpts/smartdrain-readme.md`
- `references/code-excerpts/frontend-drain-status-socket.ts`
- `references/code-excerpts/backend/models/sensor_data.py`
- `references/code-excerpts/backend/models/analysis_job.py`
- `references/code-excerpts/backend/models/yolo_result.py`
- `references/code-excerpts/backend/models/xgboost_result.py`
- `references/code-excerpts/backend/routers/ai_callback.py`
- `references/code-excerpts/backend/services/analysis_async_service.py`
- `references/code-excerpts/backend/websocket/events.py`
- `references/code-excerpts/ai-service/analysis_service.py`
- `references/code-excerpts/ai-service/xgboost_adapter.py`
- `references/code-excerpts/ai-service/yolo_analyzer.py`

Use these for technical accuracy and claim checking.

## Visuals To Recreate As Diagrams

The final deck should recreate these as clean HTML/CSS/SVG diagrams instead of placing dense screenshots directly:

- AI pipeline: sample image -> YOLO/OpenCV -> XGBoost -> risk level
- async analysis: request -> AnalysisJob -> AI Service -> callback -> DB
- WebSocket update: result persisted -> event -> frontend refresh
- DB/ERD: facilities/drains, sensor_data, analysis_jobs, yolo_results, xgboost_results
- service architecture: Frontend, Backend, AI Service, PostgreSQL, Nginx, Docker/Jenkins

## Visuals To Avoid

- old PPT sticky notes
- draft comments
- blurry diagrams
- unreadable ERD screenshots
- source-code screenshots with tiny text
- news screenshots unless source handling is confirmed
- real CCTV imagery that implies current integration

## Future Asset Work

Before final deck generation, rebuild `input/assets` if screenshots or sample images are needed:

- dashboard screenshot
- detail page screenshot
- sample drain images
- AI result example images
- clean ERD or architecture export

