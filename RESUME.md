# 조승준 (Cho Seungjun)

**Backend Developer | AI Infrastructure Specialist**

📧 cfi02222@gmail.com | 🔗 [github.com/ufxpri](https://github.com/ufxpri)

---

## 전문 요약 (Professional Summary)

6년 경력의 백엔드 개발자로, **AI 모델 서빙부터 대규모 시스템 운영까지** 전 과정을 책임지는 엔지니어입니다. 36대 CCTV 실시간 처리, 네이버 클라우드 대용량 트래픽 핸들링 등 **프로덕션 환경에서 검증된 문제 해결 능력**을 보유하고 있습니다.

**핵심 강점:**
- **Performance Optimization**: CPU 사용량 50% 절감(330%→160%), Docker 이미지 60% 경량화(35GB→12GB), 쿼리 성능 개선 경험
- **System Architecture**: Message Queue 기반 비동기 아키텍처, Sidecar Pattern을 활용한 의존성 분리, MSA 설계
- **Production Excellence**: 배포 일정 준수율 80.5%, MTTR 0시간 달성(Q4 2024), 303 commits/year, 87회 현장 배포 경험
- **AI Collaboration**: AI 도구로 개발 리드타임 단축(1주→1일)하면서도 아키텍처 설계로 불확실성 제어

**기술 철학**: "Going Fast"에서 "Going Far"로 - 초기의 빠른 구현 중심에서, 유지보수성과 모듈 간 의존성 제거를 최우선으로 하는 **장기적 관점의 설계자**로 진화했습니다.

---

## 핵심 기술 (Technical Skills)

### Languages & Frameworks
**Backend**: Python (Django, FastAPI, Flask), C/C++
**Frontend**: JavaScript, Bootstrap

### AI/ML Infrastructure
**Frameworks**: TensorFlow, PyTorch, CLIP, YOLOv7
**Optimization**: TensorRT, Multi-GPU 병렬 처리, OMP 튜닝, Active Learning 파이프라인
**Tools**: LangChain, Antigravity (AI 코딩 도구)

### Backend & Architecture
**Web Frameworks**: Django, FastAPI, Flask, Nginx
**Communication**: gRPC, REST API, WebSocket, TCP/IP Socket, RTSP
**Patterns**: MSA, DDD, Sidecar Pattern, Message Queue Architecture, Pub-Sub, Request-Reply

### DevOps & Infrastructure
**Containerization**: Docker, Docker Compose, 이미지 최적화
**Orchestration**: Ansible (멀티 사이트 원격 관리)
**Cloud**: AWS EC2, NCP (Naver Cloud Platform), Load Balancer
**CI/CD**: GitHub Actions (탐색), rsync 배포 최적화

### Data & Messaging
**Databases**: PostgreSQL, MongoDB, MariaDB, Redis, InfluxDB
**Message Queue**: RabbitMQ, Celery, Kafka (POC)
**Search**: Elastic Search

### Monitoring & Operations
**Logging**: Fluentd, Loki, Grafana
**Monitoring**: 커스텀 QC 프로그램, 성능 벤치마킹 프레임워크
**Deployment**: Offline 환경 배포(Docker tar), Ansible 자동화

### Streaming & Media
**Protocols**: RTSP, MJPEG, KLV
**Processing**: FFmpeg, Pipe Communication, 실시간 스트리밍 분석

### System Integration
**Protocols**: SCADA, Naiz 플랫폼, OpenVPN, SMB
**Network**: 400KB/s 대역폭 환경 최적화, TCP/IP 소켓 통신

---

## 경력 (Work Experience)

### 오지큐 (OGQ) | 백엔드 개발자
**2023.01 ~ 현재**

#### 2024: 최적화 전문가 (Optimization Engineer)

**K-water 수자원 AI 안전관리 시스템 - 성능 최적화 & 확대 구축**
- 소양강댐 관제 시스템에서 **CLIP 모델 최적화 및 OMP 튜닝**을 통해 CPU 사용량 51.5% 절감(330%→160%) 및 오검출 문제 해결
- 폐쇄망 정수장 환경을 위해 **Docker 이미지 60% 경량화**(35GB→12GB) 및 Ansible 기반 배포 자동화 체계 구축
- **14개 수처리 시설 배포 완료**, 400KB/s 대역폭 환경에서 rsync partial transfer로 네트워크 최적화
- 운영사 변경에 따른 이기종 시스템(SCADA, TCP/IP 소켓) 간 유연한 인터페이스 설계 주도
- Active Learning 시스템 아키텍처 설계 및 QC 프로그램 개발로 알고리즘 성능 검증 체계 구축
- **기여**: 149 commits (Q1), 총 303 commits (연간), 77회 현장 출장

**DNA+ 드론 5G 전송 프로젝트 & Police Lab 2.0**
- RTSP 실시간 영상 분석 및 재인코딩 시스템 개발, **TensorRT 통합**으로 모델 추론 최적화
- Multi-GPU 병렬 처리 및 C++ 멀티스레딩 구현으로 30 FPS 처리 목표 달성(RTX4090 Dual GPU)
- **Shared Memory 기반 데이터 파이프라인** 구축으로 프로세스 간 통신 오버헤드 최소화
- ETRI 플랫폼 배포 및 IR 정지 영상 분석 기능 추가

**미디어 문화향유 프로젝트 - TTA 품질 인증 획득**
- Django + Celery + RabbitMQ + Redis로 **10분 이상 장시간 분석 작업 안정 처리** 가능한 비동기 아키텍처 구축
- **Sidecar Pattern 도입**으로 AI 프로세스와 메인 서버 간 의존성 완벽 분리, 시스템 안정성 확보
- Docker 기반 수평 확장 가능한 아키텍처 설계, 모니터링 및 로깅 시스템 구축
- **66 commits** 기여, TTA 품질 인증 획득으로 프로덕션 준비 완료

**성과 지표**: 프로젝트 완성률 80% (Q1 62%→Q4 95% 향상), 배포 일정 준수율 80.5%, MTTR 0시간 달성(Q4), CPU 51.5% 절감, Docker 이미지 60% 경량화

#### 2023: 트러블슈터 (Troubleshooter)

**네이버 클라우드 태깅 시스템 - 병목 해결**
- 대용량 이미지 분석 요청 시 발생한 병목 현상을 **Message Queue(RabbitMQ) 도입**으로 해결
- NCP 환경에서 Load Balancer + FastAPI 기반 서비스 설정 및 배포
- TCP Connection 조절 및 세마포어 제거로 네트워크 최적화
- 디스크 사용량 추이 분석(20%→40%) 및 용량 관리

**DNA 드론 5G 전송 - C++ 레거시 통합**
- 생소한 **C++ 레거시 코드를 1개월 만에 리버스 엔지니어링**하여 KLV 데이터 실시간 전송 구현 성공
- 외부 업체 소스코드 분석 및 5G 실시간 전송 요구사항 충족
- 마감 1개월 전 긴박한 일정 속에서 새로운 기술 스택 습득 및 적용

**수자원공사 확대 구축 제안서 작성 & 인프라 관리**
- A100 서버 구성, Aloha VMS 데모 사이트 구축
- 개발 서버 하드 디스크 용량 관리, 네이버 MyBox 인스턴스 마이그레이션

**협업 강화**: 백엔드 기술 미팅 주도(연간 27회), Redis 성능 테스트, 논문 리뷰 발표

---

### 지와이네트웍스 (GY Networks) | 백엔드 연구원
**2018.09 ~ 2022.12**

#### 2022: 최적화 엔지니어 (Optimization Engineer)

**AI 데모 웹사이트 개편 (프로젝트 리드)**
- 3명 팀 백엔드 리드로 **Message Queue 기반 AI 분석 시스템 아키텍처 설계** 주도
- **인터페이스 복잡도 3배 개선**, Multi-processing 적용으로 GPU 사용 효율 향상
- 동기식 API 지원 추가 및 리소스 제한 기반 요청 수 관리 체계 구축
- 신입 백엔드 개발자 교육 및 피드백 제공
- **기술 스택**: FastAPI, RabbitMQ, Docker, Docker Compose, MSA

**실시간 스트리밍 모자이크 처리 시스템 (단독 개발)**
- FFmpeg + Python + PyTorch 조합으로 **실시간 처리 요구사항 충족**, 프로젝트 계약 성사
- 스트리밍 지연 문제 해결 및 모자이크 처리 소프트웨어 독립 개발

**CCTV 검출기록 검색 시스템**
- 마케팅 데이터 기반 사용자 요구사항 분석 후 **Elastic Search 도입** 결정
- 시계열 이벤트 데이터에 적합한 DB 선택 및 POC 제작, 태그 confidence 기반 검색 결과 정렬 설계

**수자원 AI 안전관리 시스템 확대 - 안정성 개선**
- **Docker 스케일 아웃 시스템** 구현, gRPC 기반 통신 및 부하 분산 시스템 구축
- 로거 안전성 확보로 시스템 교착상태 해결, FFmpeg→live555 전환으로 Digest 인증 IP camera 호환성 확보
- 클립 데이터 추출 기능 구현 및 영상 인코딩 버그 분석

**지식 공유**: 기술 블로그 7개 작성, 모니터링 시스템 발표(63시간 투자, loglog 프레젠테이션), GPGPU 논문 리뷰

#### 2021: 아키텍처 구축자 (Architecture Builder)

**수자원 AI 안전관리 시스템 - 대규모 트래픽 첫 경험**
- **36대 CCTV 동시 스트리밍 데이터 처리** 시스템 설계 및 개발 (5명 팀)
- 동적 스케일링 가능한 아키텍처 설계로 늘어나는 현장 요구사항에 유연 대처
- 시스템 부하 문제 파악 및 납품일 내 아키텍처 개선안 적용 완료
- **Fluentd + InfluxDB 모니터링 시스템** 구축, 현장 출장 및 딥러닝 동작 분석 후 모델 개발팀 피드백 제공
- **기술 스택**: Python, gRPC, Docker, PyTorch, MSA, FFmpeg, On-Premise

**NAS 서버 구축 (단독)**
- **24TB 용량 NAS 서버** 구축, 팀 작업 레벨을 고려한 Windows GUI 환경 선택
- 네트워크 드라이브 + RDP 원격 제어 환경 구성 및 팀원 교육

**DNA+ 프로젝트**
- **DDD(Domain-Driven Design) 적용** 프로그래밍, RTSP/KLV/MJPEG 스트리밍 수신 구현
- 대규모 프로젝트 문서 작성 경험 축적

**승강기 안전공단 프로젝트**
- FFmpeg 스트리밍 활용, Pipe 통신 사용, 소프트웨어 장애 대처 고려한 설계

**지식 공유**: 기술 블로그 17개 작성, 논문 리뷰 11개 발표, CVPR 150개 세션 참여, GoF 디자인 패턴 정독

**성장**: 참여 프로젝트 5개→7개, 제작 API 4개→11개(175% 증가), 서버 셋팅 시간 1주→3일(57% 단축)

#### 2020: 인프라 혁신가 (Infrastructure Innovator)

**AI 데모 웹사이트 (Deep Manager)**
- **13개 딥러닝 모델 MSA 환경** 구축, AWS EC2 클라우드 첫 배포 경험
- Docker 활용으로 CUDA 의존성 해결 및 개발 기간 단축, 컨테이너 병렬화로 효율적 관리
- Flask + Bootstrap으로 심플한 UI 구현, AJAX로 분석 요청 및 결과 표시
- **기술 스택**: Python, Flask, Nginx, Bootstrap, JWT, MSA, REST API, AWS, TensorFlow

**승강기 AI 폭력 검출 시스템**
- CCTV 스트리밍 데이터 분석 시스템 설계, FFmpeg PIPE 통신 시스템 적용
- 비디오 클립 데이터 생성 및 프로세싱 처리, 현장 분석 모니터링

**드론 AI 통합 관제 시스템**
- 드론 스트리밍 데이터 수신-분석-전달 파이프라인 설계, **스케일 아웃 가능한 아키텍처** 구현
- MJPEG/RTSP 수신 컴포넌트 작성
- **기술 스택**: Python, DDD, MJPEG, KLV, AWS, gRPC

**온프레미스 학습 서버 구축 (단독)**
- **Linux 기반 GPU 학습 서버** 환경 도입, NVIDIA Docker 환경 구축
- SMB 원격 파일 전송, SSH 원격 학습 서버 사용법 팀원 교육
- 모든 PC에 Ubuntu 듀얼 부팅 설정 완료, **전사 Linux 전환 주도**

**도구 도입 - 팀 생산성 혁신**
- **Notion**: 프로젝트 블랙박스 해소, 실시간 업무 추적 및 투명한 협업 가능
- **Docker**: 환경 설정 시간 획기적 단축, 로컬→서버 전환 문제 해소
- **OKR**: KPI 중심→목표 중심 업무 관리 전환

**인프라 성과**: Linux 64개 인스턴스 전환(Ubuntu 25대, Arch 7대, CentOS 4대), Docker Hub 7개 레포지토리/137회 다운로드, GitHub 11개 레포지토리 활성화

**마인드셋 전환**: 결과 중심→성장 중심, 수동적→능동적 학습, 개인 작업→팀 협업

#### 2019: 첫 걸음 (Foundation)

**AI API - 첫 프로덕션 서비스**
- **3개 이상 업체에 동시 배포**되는 REST API 개발 및 13개월 운영
- **JWT 인증 시스템** 구현, 배치 단위 GPU 스케줄링으로 리소스 최적화
- **비동기 방식 API** 설계로 분석 단계 추적 가능한 인터페이스 제공
- 업체별 맞춤형 UI 설계 및 클라이언트 요구사항 반영
- **기술 스택**: Flask, TensorFlow, REST API, Async, JWT

---

## 학력 및 자격증 (Education & Certifications)

### 학력
- **인하대학교** | 소프트웨어융합공학과 (재학, 2025.03~)
- **인천전자마이스터 고등학교** | 정보통신기기과 (졸업, 2016.03~2019.01)

### 자격증
- **AWS Certified Solutions Architect – Associate** (2023.10.06)
- **AWS Certified Cloud Practitioner** (2022.10.14)
- **리눅스마스터 1급** (2022.12.09) `LMF-2202-002034`

### 병역
- 산업기능요원 만기 전역 (2021.02 ~ 2023.12)

---

## 커뮤니티 활동 (Activities)

- **GDG 송도 스태프** (2022.08.14)
- **DDD 8기 운영진** (2022.09.01 ~ 2024.09.28)
  - Discord 도입으로 통합 커뮤니케이션 환경 구축
  - 11기 운영팀 멤버로 DDD 프로그램 성공적 완료
- **GDG 인천, 인천 개발자 모임** 활동

---

## 주요 성과 요약 (Key Achievements)

### 성능 최적화
- **CPU 사용량 51.5% 절감** (330%→160%, CLIP 모델 OMP 튜닝)
- **Docker 이미지 60% 경량화** (35GB→12GB, 레이어 구조 최적화)
- **GPU 활용률 향상** (37%→85%, CLIP 모델 적용)
- **인터페이스 복잡도 3배 개선** (Message Queue 아키텍처)

### 시스템 안정성
- **배포 일정 준수율 80.5%** (Q2-Q3 100% 달성)
- **MTTR 0시간 달성** (Q4 2024)
- **34일 연속 무중단 운영** (태백 수처리 시설, 2024.09)
- **프로젝트 완성률 80%** (Q1 62%→Q4 95% 향상)

### 대규모 배포
- **87회 현장 배포** (2024년, K-water 14개 시설 포함)
- **36대 CCTV 동시 처리** (2021년, 수자원공사)
- **3개 이상 업체 동시 서비스** (2019년, AI API)

### 기술 리더십
- **303 commits** (2024년, 2023년 38 commits 대비 700% 증가)
- **백엔드 기술 미팅 27회 주도** (2024년)
- **신입 개발자 멘토링** (2022년, AI 데모 웹사이트 프로젝트 리드)
- **전사 Linux 전환 주도** (2020년, 64개 인스턴스)

### AI 활용 혁신
- **개발 리드타임 단축** (1주→1일, AI 코딩 도구 활용)
- **Sidecar Pattern으로 AI 불확실성 제어** (2024년, 미디어 문화향유 프로젝트)
- **TTA 품질 인증 획득** (2024년)

---

## 경력 성장 스토리 (Career Growth Journey)

**2019-2020: 기초 다지기**
Flask 기반 AI API를 3개 업체에 배포하며 실전 경험 축적. Docker, Notion, OKR 도입으로 팀 생산성 혁신. 64개 인스턴스 Linux 전환 주도. "성장 시작의 기점".

**2021-2022: 아키텍처 역량 강화**
36대 CCTV 동시 처리로 대규모 트래픽 첫 경험. gRPC, MSA, DDD 적용. 프로젝트 리드로 Message Queue 아키텍처 설계하며 인터페이스 복잡도 3배 개선. API 개발 175% 증가(4개→11개).

**2023-2024: 최적화 전문가**
CPU 51.5% 절감, Docker 이미지 60% 경량화 달성. Sidecar Pattern으로 AI 불확실성 제어. 배포 일정 준수율 80.5%, MTTR 0시간 달성. 303 commits로 생산성 폭발.

**2025: 전략적 아키텍트**
AI First 혁신(1주→1일 개발 단축)과 Architecture 고도화(Kafka 비동기 아키텍처, Capacity Planning)로 "Going Far" 철학 실천. 대용량 처리와 GPU 비용 효율화 동시 달성.

**핵심 전환**: 빠른 구현(Going Fast) → 멀리 가는 시스템(Going Far) → 전략적 설계와 AI 활용의 균형
