# What I Did - 2022

## Q1 (January - March)

### Projects

#### 1. 수자원공사 (Water Resources Corporation)
**담당 업무**:
- 도커 스케일 아웃 시스템 구현
- gRPC 기반 통신 구현
- 버퍼링 시스템 설계
- 부하 분산 시스템 구축
- 스트림 프로세싱 구현

**기술부채 해결**:
- 로거의 안전성 확보하여 시스템 교착상태 해결
- FFmpeg 방식의 스트리밍 수신방식을 live555로 변경
  - 이유: FFmpeg는 digest 인증방식을 지원하지 않아 일부 IP camera와 호환성 문제 발생

#### 2. DNA+ 프로젝트
**담당 업무**:
- 클라우드 데이터 스트리밍 시스템 구축
- AWS 인스턴스 유휴 제어 시스템 구현
- API 스케일 아웃 구현

**기술부채 식별**:
- 클라이언트 사이드 제어 필요성 인식
  - 시연 시마다 모니터링 필요 → 클라이언트가 직접 제어할 수 있도록 개선 필요

#### 3. 데모사이트 (AI Demo Website)
**담당 업무**:
- 메세지 큐 시스템 설계 및 구축
- Docker Compose를 활용한 컨테이너 오케스트레이션
- 시스템 아키텍처 설계

### Learning & Knowledge Sharing

**작성하거나 번역한 글 - 5개**:
- 모던 리눅스 관리 책
- 로깅 시스템 강의 준비
- 클레임
- 2022년 시각화와 로깅 매니저 생태계
- 5가지 FastAPI에서 알면 좋은 기능들

**개발자 모임**:
- 인천 개발자 모임 참여
- AWS 소모임 참여

### Areas of Interest
- 모니터링 시스템
- DB 시스템
- IaC (Infrastructure as Code)

## Q2 (April - June)

### Major Projects

#### 1. 데모 사이트 리뉴얼 (AI Demo Website Renewal)
**담당 업무**:
- SSL 인증서 적용
- 불규칙적인 분석 요청에 최적화된 아키텍처 구현

#### 2. DNA+ 프로젝트
**담당 업무**:
- REST API 형태로 시스템 재제작
- 총 3번의 시연 수행
- 모델 구동속도 최적화 작업
- 이미지 스케줄링 문제 해결

#### 3. 수자원 공사
**담당 업무**:
- 클립 데이터 추출 기능 구현
- 클립 저장 코드 버그 해결 작업
  - 이슈: 영상 인코딩 과정에서 불특정 확률로 재생 불가 현상 발생
  - 원인 분석: CPU와 메모리 점유율과 연관 추측

#### 4. 검색 가능한 시스템 (CCTV Detection Search System)
**담당 업무**:
- Elastic Search 학습 및 POC 제작
- 태그 confidence 기준 검색결과 정렬 설계
- 실제 프로젝트 적용 가능한 시스템 방안 설계

### Mini Events
- NAS 견적 작성
- AIhub 서버랙 설치

### Learning Activities

**논문 리뷰**:
- GPGPU (General Purpose Graphical Processing Unit)

**작성하거나 번역한 글 - 2개**:
- 구글 포토의 백엔드 시스템
- 사이드카란?

**개발자 모임 - 2회**:
- 인천 개발자 모임
- Google I/O 소모임

**모니터링 시스템 발표 준비**:
- 카페 방문 횟수: 21회
- 1회당 평균 시간: 3시간
- 총 소모 시간: 63시간
- loglog 프레젠테이션 제작
- GitHub Repository: https://github.com/ufxpri/monitoring-quick-demo.git

### Updated Areas of Interest
- 모니터링 시스템
- DB 시스템
- 하드웨어 가속 (신규 추가)

### H2 Goals
- 리눅스마스터 자격증 취득 계획
  - 07.25: 접수
  - 09.03: 1차 시험
  - 09.26: 접수
  - 11.19: 2차 시험
- 건강 챙기기
- 발음 연습
- GPU 정복하기
- Python 이외의 기술스택 적용 고려

## Q3-Q4 (July - December)

### Major Projects

#### 1. AI 데모 웹사이트 개편
**기간**: 2022.01 ~ 2022.09
**역할**: 백엔드 엔지니어 (3명 팀)
**기술 스택**: FastAPI, RabbitMQ, Docker, Docker-Compose, MSA

**주요 업무**:
- Message Queue 기반 AI 분석 시스템 설계 및 프로젝트 리드
- 신입 백엔드 개발자 교육 및 피드백
- Multi-processing 적용하여 GPU 사용 효율 개선
- 동기식 API 지원으로 인터페이스 복잡도 3배 개선
- 리소스 제한에 따른 요청 수 관리와 fail 시나리오 설계

#### 2. CCTV 검출기록 검색 시스템
**기간**: 2022.09 ~ 진행중
**역할**: 백엔드 엔지니어 (2명)
**기술 스택**: 기획, Elastic Search

**주요 업무**:
- 마케팅 데이터를 통해 사용자 요구사항 분석
- 시계열 이벤트 데이터에 적합한 DB 선택

#### 3. 실시간 스트리밍 모자이크 처리 시스템
**기간**: 2022.10 ~ 진행중
**역할**: 백엔드 엔지니어 (단독)
**기술 스택**: FFmpeg, Python, PyTorch

**주요 업무**:
- 실시간 분석 요구사항을 충족하는 소프트웨어 제작
- 프로젝트 계약 성립

#### 4. 수자원 AI 안전관리 시스템 확대
**기간**: 2022.11 ~ 진행중
**역할**: 백엔드 엔지니어
**기술 스택**: Docker

**주요 업무**:
- RFP 문서 작성

## Technical Stack Summary

### Languages & Frameworks
- Python
- FastAPI
- PyTorch

### Infrastructure & DevOps
- Docker
- Docker Compose
- gRPC
- RabbitMQ (Message Queue)
- AWS

### Data & Search
- Elastic Search

### Streaming & Media
- FFmpeg
- live555
- RTSP

### Architecture Patterns
- MSA (Microservices Architecture)
- Message Queue Architecture
- Stream Processing

## Skills Developed

### Technical Skills
- Docker 스케일 아웃
- 부하 분산 시스템 설계
- 실시간 스트리밍 처리
- GPU 최적화
- Multi-processing
- Elastic Search 활용

### Leadership & Collaboration
- 프로젝트 리드 경험
- 신입 개발자 교육 및 피드백
- 팀 협업 (2-3명 규모)

### Documentation & Knowledge Sharing
- 기술 블로그 글 작성 (7개)
- 논문 리뷰
- 모니터링 시스템 발표
- 개발자 모임 참여 (3회)
