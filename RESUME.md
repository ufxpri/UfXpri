# 조승준 (Jo Seungjun)

**백엔드 개발자 (Backend Developer)**

📧 cfi02222@gmail.com | 🔗 [github.com/ufxpri](https://github.com/ufxpri)

---

## 💡 Professional Summary

AI 서비스 인프라 구축 및 운영에 특화된 백엔드 개발자입니다. 6년+ 경력 동안 대규모 CCTV 스트리밍 데이터 처리(36대+), 실시간 영상 분석 시스템, 비동기 메시지 큐 아키텍처를 설계하고 배포했습니다. Docker 패키지 최적화로 60% 크기 감축, CPU 사용률 51.5% 절감, GPU 활용률 85% 달성 등 시스템 성능 개선에 강점을 가지고 있습니다.

Python/FastAPI 기반 MSA 아키텍처 설계부터 현장 배포, 모니터링까지 전 과정을 책임지며, 기술 부채를 최소화하고 비즈니스 가치를 창출하는 것을 중요하게 생각합니다. 2024년 303 commits 기여, 배포 일정 준수율 80.5% 달성, MTTR 0시간 기록으로 프로덕션 환경에서의 문제 해결 능력을 검증받았습니다.

---

## 🛠️ Technical Skills

**Languages & Frameworks**
- Python (Django, FastAPI, Flask)
- C++ (TensorRT 최적화, Multi-threading)

**AI/ML Infrastructure**
- TensorRT, PyTorch, TensorFlow, CLIP 모델
- Multi-GPU 병렬 처리, Active Learning 파이프라인

**Backend & Architecture**
- Celery, RabbitMQ, Redis, gRPC, REST API
- MSA, DDD, Sidecar Pattern, Message Queue Architecture
- Shared Memory IPC, Pipe Communication

**Databases**
- PostgreSQL, MySQL, MariaDB, MongoDB
- Redis, Elasticsearch, InfluxDB

**DevOps & Infrastructure**
- Docker, Docker Compose, Ansible
- AWS EC2, GitHub Actions
- rsync, Offline 배포 시스템

**Streaming & Media**
- FFmpeg, RTSP, MJPEG, KLV
- 실시간 스트리밍 분석

**Monitoring & Operations**
- Loki, Grafana, Fluentd
- 커스텀 QC 프레임워크

---

## 💼 Work Experience

### 백엔드 개발자 | 오지큐 (OGQ) | 2023.01 - 현재

#### 2024 주요 성과

**K-water 수자원 AI 안전관리 시스템 확대 구축 및 최적화**
- 14개 정수장에 AI 안전관리 시스템 배포 완료, Ansible 기반 원격 관리 시스템으로 다중 시설 서버 관리 효율화
- CLIP 모델 도입 및 OMP 파라미터 튜닝을 통해 CPU 사용률 51.5% 절감(330% → 160%), GPU 활용률 85% 달성
- Docker 레이어 구조 최적화로 배포 패키지 크기 60% 감축(30GB → 12GB), 저대역폭 환경(400KB/s)에서 배포 시간 17시간 → 7시간 단축
- Frame drop 전략 구현으로 과부하 시스템 안정성 확보, 프로세스 분리로 영상 연결 해제 시 무한 대기 버그 해결
- Active Learning 시스템 아키텍처 설계(Detection DB, Labeling UI, TTD 중복 제거), QC 프로그램 개발로 알고리즘 성능 검증 체계 구축
- 303 commits 기여 (Q1 149 commits, 2023년 대비 700% 증가), 77+ 현장 출장 지원

**Media Cultural Enjoyment Project**
- Django + Celery + RabbitMQ + Redis 기반 비동기 메시지 큐 아키텍처 설계
- 10분+ 장시간 분석 작업을 안정적으로 처리하는 프로덕션 시스템 구축
- Docker 기반 수평 확장 가능한 구조 설계, 모니터링 및 로깅 시스템 통합
- 66 commits 기여

**DNA+ & Police Lab 2.0**
- RTSP 실시간 영상 분석 및 재인코딩 시스템 개발, TensorRT 모델 추론 최적화
- Multi-GPU 병렬 처리 및 C++ 멀티스레딩 구현으로 RTX4090 Dual GPU 환경에서 30 FPS 목표 달성
- Shared Memory 기반 데이터 파이프라인 구축으로 프로세스 간 통신 오버헤드 최소화
- ETRI 플랫폼 배포 및 IR 정지 영상 분석 기능 추가

**백엔드 기술 리더십**
- 백엔드 기술 미팅 27회 주도 (주간), 백엔드 전략 회의 2회 진행
- 백엔드 로드맵 작성, Job Description 작성

**성과 지표**
- 프로젝트 완성률: 80% (Q1 62% → Q4 95%)
- 배포 일정 준수율: 80.5% (Q2-Q3 100% 달성)
- MTTR: 0시간 (Q4)
- 연속 무중단 운영: 34일 (태백 수처리 시설, 2024.09)

#### 2023 주요 성과

**네이버 MyBox 대용량 이미지 분석**
- Message Queue(RabbitMQ) 도입으로 대량 이미지 분석 요청 시 병목 현상 해결
- TCP Connection 조절 및 세마포어 제거로 네트워크 최적화
- 디스크 사용량 추이 분석(20% → 40%) 및 GPU 과다 프로비저닝 제거로 클라우드 인프라 비용 절감
- 인스턴스 마이그레이션 완료

**DNA+ 실시간 드론 영상 분석**
- C언어 기반 외부 소스코드를 1개월 만에 분석하여 KLV 데이터 실시간 전송 구현
- 5G 드론 영상 실시간 수신 시스템 개발, YOLOv7 객체 검출 모델 적용
- 마감 1개월 전 긴박한 일정 속에서도 시연 성공

**수자원공사 확대 구축 제안서 작성 & 인프라 관리**
- Redis 도입 검토를 통한 시스템 병목 개선 방안 수립
- A100 서버 구성, Aloha VMS 데모 사이트 구축
- 소양강댐 시스템 개선 설계 및 배포, 테스트 결과 문서 작성

**협업 및 지식 공유**
- 백엔드 파트너와 다수 프로젝트 협업, 코드 리뷰 및 기술 토의 진행
- 논문 리뷰 발표, Redis 성능 테스트

---

### 백엔드 연구원 | 지와이네트웍스 (GYnetworks) | 2018.09 - 2022.12

#### 2022 주요 성과

**AI 데모 웹사이트 개편 (3인 팀 리드)**
- Message Queue 기반 AI 분석 시스템 아키텍처 설계 및 프로젝트 리드
- Multi-processing 적용으로 GPU 사용 효율 개선, 동기식 API 지원으로 인터페이스 복잡도 3배 개선
- 리소스 제한 기반 요청 수 관리 및 Fail 시나리오 설계
- 신입 백엔드 개발자 교육 및 피드백 제공
- 기술 스택: FastAPI, RabbitMQ, Docker, Docker Compose, MSA

**실시간 스트리밍 모자이크 처리 시스템 (단독 개발)**
- FFmpeg + Python + PyTorch 조합으로 실시간 처리 요구사항 충족
- 프로젝트 계약 성사

**CCTV 검출기록 검색 시스템**
- Elasticsearch POC 제작, 마케팅 데이터 기반 사용자 요구사항 분석
- 시계열 이벤트 데이터에 적합한 DB 선택 및 태그 confidence 기반 검색 결과 정렬 설계

**수자원공사 프로젝트**
- Docker 스케일 아웃 구현, gRPC 기반 통신 및 부하 분산 시스템 구축
- 로거 안전성 확보로 시스템 교착상태 해결
- FFmpeg → live555 변경으로 Digest 인증 IP 카메라 호환성 문제 해결
- 클립 데이터 추출 기능 구현

**DNA+ 프로젝트**
- REST API 형태로 재제작, 3번의 성공적 시연 수행
- 모델 구동속도 최적화, 이미지 스케줄링 문제 해결
- 클라우드 데이터 스트리밍 구축, AWS 인스턴스 유휴 제어, API 스케일 아웃 적용

**지식 공유**
- 기술 블로그 7개 작성 (모니터링 시스템, FastAPI, 구글 포토 백엔드, Sidecar)
- 모니터링 시스템 발표 (63시간 투자, loglog 프레젠테이션)
- GPGPU 논문 리뷰

#### 2021 주요 성과

**수자원 AI 안전관리 시스템 (5인 팀)**
- 36대 CCTV 동시 스트리밍 데이터 처리 시스템 설계 및 개발
- gRPC 기반 동적 스케일링 아키텍처 설계로 증가하는 현장 요구사항에 유연 대응
- 시스템 부하 문제 파악 및 납품일 내 아키텍처 개선안 적용 완료
- Fluentd + InfluxDB 모니터링 시스템 구축
- 현장 출장 및 딥러닝 동작 분석, 모델 개발팀 피드백 제공
- 기술 스택: Python, gRPC, Docker, PyTorch, MSA, FFmpeg

**NAS 서버 구축 (단독)**
- 24TB NAS 서버 구축, 팀 작업 레벨 고려한 Windows GUI 환경 선택
- 네트워크 드라이브 + RDP 원격 제어 환경 구성 및 팀원 교육

**DNA+ 프로젝트**
- DDD(Domain-Driven Design) 적용 프로그래밍
- RTSP/KLV/MJPEG 다중 프로토콜 스트리밍 수신 구현
- 대규모 프로젝트 문서화 경험

**승강기 안전공단 프로젝트**
- FFmpeg 스트리밍, Pipe 통신, 소프트웨어 장애 대처 고려 설계

**드론 AI 통합 관제 시스템 (4인 팀)**
- 드론 스트리밍 데이터 수신-분석-전달 파이프라인 설계
- 스케일 아웃 가능한 아키텍처 구현

**인프라 리더십**
- AI Hub 서버 셋팅 시간 1주일 → 3일 (57% 단축)
- 실제 서버실 물리적 설치 경험

**지식 공유**
- 기술 블로그 17개 작성 (아키텍처, Request-Reply 패턴, FastAPI, 넷플릭스 마이크로서비스, Pub-Sub, Eventual Consistency, DVC)
- 논문 리뷰 11개 발표 (gRPC, JWT, Python Profiling, CI/CD, Docker)
- CVPR 150개 세션 참여
- GoF 디자인 패턴 정독

**성장 지표**
- 프로젝트 수: 5개 → 7개 (40% 증가)
- API 개발: 4개 → 11개 (175% 증가)

#### 2020 주요 성과

**AI 데모 웹사이트 Deep Manager (3인 팀)**
- 13개 딥러닝 모델 MSA 환경 구축, AWS EC2 배포
- Docker 활용으로 CUDA 의존성 해결 및 개발 기간 단축
- Flask + Bootstrap으로 사용자 친화적 웹 기반 AI 서비스 구축
- 로컬 프로그램 → 웹 서비스 전환으로 시연 효율성 향상
- 기술 스택: Python, Flask, Nginx, Bootstrap, JWT, MSA, REST API, AWS, TensorFlow

**승강기 AI 폭력 검출 시스템 (2인 팀)**
- CCTV 스트리밍 데이터 실시간 분석 시스템 설계
- FFmpeg PIPE 통신 시스템 적용, 비디오 클립 자동 생성
- 현장 분석 모니터링 및 개발 피드백

**드론 AI 통합 관제 시스템 (4인 팀)**
- 드론 스트리밍 데이터 수신-분석-전달 파이프라인 설계
- 스케일 아웃 가능한 아키텍처 구현
- MJPEG/RTSP 수신 컴포넌트 작성
- 기술 스택: Python, DDD, MJPEG, KLV, AWS, gRPC

**인프라 혁신 리더십**
- 전사 Linux 전환 주도 (Ubuntu 25대, Arch 7대, CentOS 4대, 총 64 인스턴스)
- Docker 도입 및 교육 (16개 설치, Docker Hub 7개 Repository, 137회 다운로드)
- GitHub 협업 프로세스 확립 (11개 Repository, 6명 활성화)

**온프레미스 학습 서버 구축 (단독)**
- Linux 기반 GPU 학습 서버 환경 도입, NVIDIA Docker 구축 및 팀원 교육
- SMB 원격 파일 전송, SSH 원격 학습 서버 사용법 교육
- 모든 PC에 Ubuntu 듀얼 부팅 설정 완료

**프로세스 혁신**
- Notion 프로젝트 관리 시스템 도입으로 업무 투명성 확보 및 협업 효율화
- OKR 도입으로 KPI 중심 → 목표 중심 업무 관리 전환

**Poldrone API**
- 이화트론과 원격 협업, API 통신 방법 및 규약 문서화
- 문서 기반 협업 프로세스 확립

#### 2019 주요 성과

**AI API (2인 팀, 50% 기여)**
- 3개 이상 업체에 동시 배포되는 REST API 개발 및 13개월 운영
- JWT 인증 시스템 구현, 배치 단위 GPU 스케줄링으로 리소스 최적화
- 비동기 방식 API 설계로 분석 진행 상황 추적 가능한 인터페이스 제공
- 각 업체별 맞춤형 UI 설계로 고객 만족도 확보
- 기술 스택: Flask, TensorFlow, REST API, Async, JWT

---

## 🎓 Education

**인하대학교** - 소프트웨어융합공학과 (2025.03 ~ 재학 중)

**인천전자마이스터고등학교** - 정보통신기기과 (2016.03 ~ 2019.01 졸업)

---

## 🪖 Military Service

**산업기능요원 만기 전역** (2021.02 ~ 2023.12)

---

## 🏅 Certifications

**AWS Certified Solutions Architect – Associate** (2023.10.06)
[badge](https://www.credly.com/badges/d45a1d57-65e9-44c6-96c3-33d1017f8dcf/public_url)

**AWS Certified Cloud Practitioner** (2022.10.14)
[badge](https://www.credly.com/badges/43d4968c-9fd0-46d6-ab7a-b2130f7d359a/public_url)

**리눅스마스터 1급** (2022.12.09) LMF-2202-002034

---

## 🎯 Community Activities

**DDD** - 8기 운영진 (2022.09.01 ~ 2024.09.28)

**GDG 송도** - 스태프 (2022.08.14 ~)

---

## 📊 Key Achievements

### 성능 최적화
- CPU 사용률 51.5% 절감 (330% → 160%, CLIP 모델 OMP 튜닝)
- Docker 패키지 60% 감축 (30GB → 12GB, 레이어 구조 최적화)
- GPU 활용률 85% 달성 (CLIP 모델 적용)
- 인터페이스 복잡도 3배 개선 (Message Queue 아키텍처)

### 시스템 안정성
- 배포 일정 준수율 80.5% (Q2-Q3 100% 달성)
- MTTR 0시간 달성 (Q4 2024)
- 34일 연속 무중단 운영 (태백 수처리 시설, 2024.09)
- 프로젝트 완성률 80% (Q1 62% → Q4 95%)

### 대규모 배포
- 87회 현장 배포 (2024년, K-water 14개 시설 포함)
- 36대 CCTV 동시 처리 (2021년, 수자원공사)
- 3개 이상 업체 동시 서비스 (2019년, AI API)

### 기술 리더십
- 303 commits (2024년, 2023년 대비 700% 증가)
- 백엔드 기술 미팅 27회 주도 (2024년)
- 신입 개발자 멘토링 (2022년, AI 데모 웹사이트 프로젝트 리드)
- 전사 Linux 전환 주도 (2020년, 64개 인스턴스)

### 인프라 혁신
- 서버 셋팅 시간 57% 단축 (1주일 → 3일, 2021년)
- API 개발 175% 증가 (4개 → 11개, 2021년)
- Docker Hub 137회 다운로드 (2020년)

---

## 💭 Career Philosophy

**From "Going Fast" to "Going Far"**

빠른 구현에서 장기적 관점의 설계로 진화했습니다. 초기에는 속도를 중시했지만, 현재는 유지보수성과 확장성을 우선시하며, 기술 부채를 최소화하고 비즈니스 가치를 창출하는 것을 목표로 합니다.

**핵심 가치**
- 성능 최적화를 통한 비용 절감
- 시스템 안정성을 통한 신뢰 확보
- 문서화와 지식 공유를 통한 팀 성장
- 실용적인 아키텍처 설계
