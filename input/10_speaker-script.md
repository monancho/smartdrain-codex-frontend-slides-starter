# 우수주의보 15분 발표 스크립트

목표 시간은 14분 30초 내외다. 36장 구성이므로 인트로와 마무리는 빠르게 넘기고, AI/DB/callback/WebSocket 파트에 시간을 더 둔다.

## 1. 표지

안녕하세요. 저희 팀 우수주의보는 이미지와 센서 기반으로 빗물받이 상태를 판단하고, 그 결과를 관리 화면에 반영하는 프로젝트입니다. 발표에서는 문제 정의부터 AI 분석, DB 저장, callback, WebSocket 화면 갱신까지 구현 중심으로 설명드리겠습니다.

## 2. 프로젝트 한 줄 요약

핵심은 sample image와 mock sensor data를 분석 작업으로 연결하고, callback 저장 후 WebSocket event로 화면 갱신을 유도하는 흐름입니다. 현재 구현 범위는 sample images, mock sensor data, async analysis, result persistence, WebSocket UI reflection입니다.

## 3. 팀 구성과 역할

역할은 네 축으로 나눴습니다. AI pipeline은 YOLO, OpenCV, 이미지 전처리와 모델 기준을 맡았고, Backend와 DB는 FastAPI, PostgreSQL, callback 저장, WebSocket event를 맡았습니다. Frontend와 Infra는 dashboard/detail UI, Docker, Nginx, Jenkins를 맡았고, 분류 기준과 발표 구성은 XGBoost feature와 판단 기준 정리를 맡았습니다.

## 4. 목차

발표는 다섯 부분입니다. 개발 필요성과 벤치마킹, AI 분석 설계, 웹 서버 및 서비스 구축, 인프라와 운영 설계, 그리고 시연과 마무리 순서입니다.

## 5. 전체 기술 스택/구성 한 장 요약

전체 구성은 Frontend, Backend, AI, DB, Infra로 나눕니다. Frontend는 Next.js와 React 기반이고, Backend는 FastAPI, DB는 PostgreSQL입니다. AI는 YOLO, OpenCV, XGBoost를 조합했고, Docker, Nginx, Jenkins로 실행과 배포 흐름을 구성했습니다.

## 6. 도시 침수와 빗물받이

빗물받이는 도로 위 빗물이 배수관으로 들어가는 첫 지점입니다. 낙엽이나 쓰레기, 토사로 막히면 강우 중 배수 흐름이 제한됩니다. 이 발표의 목표는 도시 침수 전체를 예측하는 것이 아니라 개별 빗물받이 상태 판단과 우선 확인 흐름을 만드는 것입니다.

## 7. 강우 중 상태 변화

강우 중에는 이물질 유입, 막힘 증가, 수위 상승, 유속 저하가 짧은 시간 안에 같이 발생할 수 있습니다. 정기 점검 시점과 실제 강우 중 상태가 다를 수 있기 때문에, 상태 변화가 발생한 뒤 화면에 반영되는 흐름이 중요합니다.

## 8. 기존 점검 방식의 한계

정기 점검과 청소는 유지관리에서 반드시 필요합니다. 다만 강우 중 동시다발적으로 변하는 개별 시설 상태를 빠르게 정렬하기에는 한계가 있습니다. 시민 신고도 현장 발견에는 강점이 있지만, 신고 전 우선순위 계산에는 공백이 있습니다.

## 9. 기존 방식/서비스 벤치마킹

정기 점검, 시민 신고, QR과 관리번호, 센서와 관제 방식의 강점을 비교했습니다. 여기서 벤치마킹은 디자인을 따라 하는 것이 아니라, 어떤 시나리오를 보완할 수 있는지 확인하는 용도입니다.

## 10. 우수주의보 차별점

우수주의보는 이미지 근거와 센서 근거를 같이 사용합니다. 개별 빗물받이 단위로 판단 결과를 저장하고, WebSocket event 이후 화면이 최신 데이터를 다시 조회해 반영합니다. 신고를 대체하기보다 점검 우선순위와 상태 확인을 보조하는 구조입니다.

## 11. 참고 자료/정책/사례 기반 목표

기능 목표는 기존 관리·신고 체계와 사례를 참고해 설정했습니다. 정확한 근거가 없는 비용이나 운영 수치, 현장 검증 수치는 넣지 않았고, 상태 판단, 근거 저장, 화면 반영 흐름에 집중했습니다.

## 12. 일정표

진행은 기획과 설계, AI 분석 설계, Backend와 DB 구현, Frontend 구현, 통합과 시연 준비 순서로 진행했습니다. 뒤쪽 기술 흐름도 이 순서를 따라갑니다.

## 13. AI 분석 설계 개요

AI 분석은 이미지 근거와 센서 근거를 결합해 내부 위험도 분류로 연결합니다. YOLO는 객체와 후보 영역 탐지, OpenCV는 전처리와 영역 보정, XGBoost는 feature 기반 분류를 담당합니다.

## 14. YOLO 단독 분석 한계

YOLO는 보이는 객체와 후보 영역을 찾는 데 강점이 있습니다. 하지만 어두운 이미지나 빗물 반사, 낙엽과 토사가 섞인 상황에서는 단독 결과만으로 막힌비율을 안정적으로 설명하기 어렵습니다. 그래서 후처리와 센서 feature가 필요합니다.

## 15. OpenCV 결합 이유

OpenCV는 전처리, mask 처리, 어두운 영역 보정, obstruction area estimation을 보조합니다. YOLO가 찾은 후보를 실제 막힘 영역 해석으로 연결하는 중간 단계로 사용했습니다.

## 16. 차폐율·이미지 품질·객체 탐지

차폐율은 이미지 기반 막힘 정도를 설명하는 내부 feature입니다. 이미지 품질과 탐지 신뢰도는 결과 해석을 보정하는 기준이고, 판단불가는 실패가 아니라 근거 부족을 명시하는 안전장치입니다.

## 17. XGBoost 입력 feature

XGBoost에는 obstruction ratio, detection confidence, water level, flow velocity를 입력 feature로 사용합니다. 여기서 sensor data는 mock sensor data 기준의 시연 입력입니다.

## 18. 위험도 분류 로직

출력 상태는 양호, 주의, 위험, 판단불가입니다. 중요한 점은 risk_score가 실제 침수 확률이나 물리적 flood-risk score가 아니라 우수주의보 내부 분류용 계산 점수라는 것입니다.

## 19. 결과/검증

검증은 현재 구현 흐름과 sample/mock data 기반 결과 확인 범위로 한정합니다. 현장 검증 완료나 실제 침수 예측 완료라고 말하지 않고, 입력, 중간 결과, 최종 분류, DB 저장 가능성을 보여주는 데 집중합니다.

## 20. 서비스 구축 개요

서비스는 dashboard, Backend, AnalysisJob, AI server, PostgreSQL, WebSocket으로 구성됩니다. 중요한 점은 Frontend가 분석을 직접 요청하는 구조가 아니라 Backend 중심의 비동기 분석 흐름이라는 점입니다.

## 21. 관리자 대시보드 흐름

대시보드에서는 전체 상태, 지도 기반 위치, 위험 시설 목록, 선택 시설 정보를 확인합니다. WebSocket event가 오면 화면이 최신 데이터를 다시 조회해서 반영합니다.

## 22. 상세 화면 흐름

상세 화면은 시설별 이미지 분석 결과, 센서 추이, AI 결과, 과거 이력을 함께 보여줍니다. 왜 특정 상태로 판단됐는지 근거를 확인하는 화면입니다.

## 23. DB 설계 / ERD

DB는 callback과 WebSocket보다 먼저 이해해야 하는 부분입니다. drains, sensor_data, analysis_jobs, yolo_results, xgboost_results가 연결되고, 분석 작업은 센서값, 이미지 분석 결과, 최종 분류 결과를 묶는 중심 역할을 합니다.

## 24. 센서 데이터 시계열 조회 기준

dev 브랜치 실제 코드 기준으로 sensor_data는 단일 id를 primary key로 사용합니다. 하나의 빗물받이는 여러 시계열 데이터를 갖기 때문에, 분석 작업에서는 drain_id와 measured_at을 기준으로 최신 센서값을 조회해 연결합니다.

## 25. 비동기 분석 요청

분석 작업은 scheduler 또는 운영 트리거가 생성합니다. Backend는 AnalysisJob을 기준으로 AI server에 분석 요청을 보내고, 화면 응답과 분석 처리를 분리합니다.

## 26. callback 저장

AI server가 분석을 마치면 Backend callback으로 결과를 전달합니다. Backend는 YOLO/OpenCV 결과와 XGBoost 결과를 저장하고, AnalysisJob 상태도 함께 갱신합니다. callback 실패나 중복 요청은 운영 점검 대상입니다.

## 27. WebSocket 갱신

WebSocket은 전체 데이터를 직접 전달하는 통로가 아니라 화면 갱신 trigger입니다. result persistence 이후 event가 발생하면 Frontend가 최신 데이터를 다시 조회해 대시보드와 상세 화면을 갱신합니다.

## 28. 전체 서비스 흐름 요약

전체 흐름을 다시 묶으면 sample image와 mock sensor data에서 시작해 async analysis, AI processing, callback persistence, WebSocket UI reflection으로 이어집니다. 이것이 우수주의보의 핵심 구현 흐름입니다.

## 29. 시스템 아키텍처

시스템은 Browser, Nginx, Frontend, Backend, AI server, PostgreSQL로 나누어 볼 수 있습니다. Nginx는 routing entry를 맡고, Backend와 AI server는 분석 요청과 결과 저장 책임을 분리합니다.

## 30. Docker / Nginx / Jenkins

Docker는 실행 환경과 배포 단위를 맞추는 역할이고, Nginx는 Frontend, Backend, WebSocket routing entry를 구성합니다. Jenkins는 GitHub 변경 이후 build와 deploy 흐름을 구성하는 데 사용했습니다. 실제 운영 완료로 과장하지 않습니다.

## 31. PostgreSQL 저장 구조

PostgreSQL에서는 drains가 시설 단위, sensor_data가 시계열 센서값, analysis_jobs가 비동기 작업 상태, yolo_results와 xgboost_results가 분석 결과를 맡습니다. 이 구조가 callback 저장과 화면 상태 반영의 기준입니다.

## 32. 운영 모니터링 고려

운영 모니터링은 완성된 production monitoring system으로 주장하지 않습니다. Backend health check, PostgreSQL 상태, AI 분석 실패 로그, WebSocket 연결, callback 실패와 중복 요청을 확인해야 할 항목으로 제시합니다.

## 33. 향후 RTSP, MQTT, 알림 확장

RTSP CCTV, MQTT 기반 실제 센서, 알림과 리포트는 향후 확장입니다. 현재 발표에서는 sample images와 mock sensor data 기반 구현 범위를 명확히 유지합니다.

## 34. 시연 시나리오

시연은 sample drain image와 mock sensor data를 준비한 뒤, 분석 작업 생성, AI server 요청, callback 저장, WebSocket event 이후 화면 갱신으로 설명합니다.

## 35. 시연 흐름

대시보드에서 위험 시설을 확인하고, 상세 화면에서 이미지·센서·AI 근거를 확인합니다. 이 장면은 기능 설명보다 실제 발표 시연 동선을 잡아주는 슬라이드입니다.

## 36. 기대효과 / Q&A

기대효과는 시설별 상태 확인, 위험 시설 우선 확인, 이미지·센서·AI 판단 근거 확인, 분석 결과 저장과 화면 반영 흐름 확인입니다. 이상으로 발표를 마치겠습니다. 질문 받겠습니다.
