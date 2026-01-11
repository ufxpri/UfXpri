# What I Did - 2020

## Year Theme: Cloud & Infrastructure Transformation

2020년은 **"성장 시작의 기점"**이었다. 클라우드 기반 인프라로의 전환과 현대적 개발 도구 도입을 통해 팀의 생산성을 혁신한 한 해였다.

## Q1 (January - March): Infrastructure Foundation

### 온프레미스 학습 서버 구축
**기간**: 2020.01 ~ 2020.02
**역할**: 시스템 엔지니어 (단독)
**기술 스택**: Linux, Network, Docker

#### 주요 업무
- **Linux 기반 GPU 학습 서버** 환경 도입
- SMB 설정하여 원격 파일 전송 지원
- SSH 원격 학습 서버 사용 방법 팀원 교육
- **NVIDIA Docker** 환경 구축 및 사용 방법 교육

#### Infrastructure Impact
- 기존 Windows 중심 → Linux 기반 서버 환경 전환
- 모든 PC에 Ubuntu 듀얼 부팅 설정 완료
- GPU 활용 학습 환경 표준화

### Tools & Process Improvements

#### Notion 도입 (협업 혁신)
**문제**:
- 프로젝트 담당자 정해지면 완료까지 블랙박스
- 업무 분담 불가능
- 진행 상황 공유 어려움

**해결**:
- Notion 프로젝트 관리 시스템 도입
- 실시간 업무 추적 및 협업 가능
- 팀원 간 업무 가시성 확보

#### Docker 도입 (개발 환경 표준화)
**문제**:
- 환경 설정에 막대한 시간 소요
- 팀원 간 코드 공유 시 환경 차이로 문제 발생
- 논문 코드 테스트 시 매번 새 환경 구축

**해결**:
- Docker 환경 가상화 도구 도입
- 로컬 → 서버 코드 전달 문제 해소
- 환경 설정 시간 획기적 단축

#### Server PC (Truck) 도입
**문제**:
- GUI 지원 없는 Server OS 전용 PC

**해결**:
- Ubuntu Server OS 채택
- 빠른 시간 내 사용 가능 환경 구축 완료
- Linux 우수성 입증으로 전사 Linux 전환 계기

#### OKR 도입
- 3월부터 개인 업무에 OKR (Objective and Key Results) 도입
- KPI 중심 → 목표 중심 업무 관리 전환

### Personal Growth Focus
**관심사 변화**:
- 리눅스
- 도커
- 클라우드

**학습 태도 전환**:
- 논문 읽기 시작
- 새로운 기술 학습에 흥미 발견
- 결과 중심 → 성장 중심 사고방식 전환

## Q2 (April - June): Production Systems

### AI 데모 웹사이트 (Deep Manager)
**기간**: 2020.03 ~ 2020.07
**역할**: 백엔드 엔지니어 (3명 팀)
**기술 스택**: Python, Flask, Nginx, Bootstrap, JWT, MSA, REST API, AWS, TensorFlow

#### 주요 업무
- **13개 딥러닝 모델** 동작 가능한 MSA 환경 구축
- Docker 활용하여 CUDA 의존성 문제 해결 및 개발 기간 단축
- **AWS EC2**를 활용한 서비스 배포
- Flask + Bootstrap으로 단기간 심플한 UI 구현
- AJAX 통한 분석 요청 및 결과 표시 구현

#### Before This Project
- 제대로 구현된 웹 딥러닝 시연 사이트 부재
- 로컬 프로그램 들고 다니며 시연
- C++, Python 기반으로 사용자 친화적 UI 제공 어려움

#### After This Project
- 웹 기반 딥러닝 서비스 시연 가능
- Docker 컨테이너 병렬화로 효율적 관리
- 빠른 업데이트 및 서버 점검 없는 배포

### Poldrone API 설계
**주요 성과**:
- 이화트론과의 원격 협업 프로젝트
- API 통신 방법 및 규약 문서화
- 물리적으로 떨어진 상황에서 문제없는 협업 구현

#### 학습 효과
- API 문서화 능력 향상
- 원격 협업 프로세스 확립
- 외부 업체와의 인터페이스 설계 경험

### 승강기 AI 폭력 검출 시스템
**기간**: 2020.04 ~ 2021.05
**역할**: 백엔드 엔지니어 (2명)
**기술 스택**: Python, RTSP, Stream Data, TensorFlow

#### 주요 업무
- **CCTV 스트리밍 데이터** 분석 시스템 설계 및 개발
- 비디오 클립 데이터 생성 및 프로세싱 처리
- **FFmpeg PIPE 통신** 시스템 적용
- 현장 분석 모니터링 및 개발 피드백 전달

## Q3-Q4 (July - December): Advanced Systems

### 드론 AI 통합 관제 시스템
**기간**: 2020.11 ~ 2022.03
**역할**: 백엔드 엔지니어 (4명 팀)
**기술 스택**: Python, DDD, MJPEG, KLV, AWS, gRPC

#### 주요 업무
- 드론 스트리밍 데이터 **수신, 분석, 전달** 시스템 설계 및 개발
- **스케일 아웃** 가능한 아키텍처 설계
  - 증가하는 분석 요청에 효과적 대처
- MJPEG, RTSP 수신 컴포넌트 작성

## Technical Achievements Summary

### Infrastructure Transformation
**Linux Adoption**:
- Ubuntu: 25대
- Arch: 7대
- CentOS: 4대
- Docker: 16개 설치
- GitHub: 6개 활성화
- VSCode: 6개 설치
- **Total**: 64개 인스턴스

### Docker Ecosystem
**개발된 프로젝트**:
- Deep Manager
- Poldrone API

**Docker Hub 성과**:
- Repository: 7개
- Downloads: 137회

### GitHub Activity
- Repository: 11개
- Active Members: 6명

## Technical Stack Expansion

### Core Technologies
**Backend & Frameworks**:
- Python
- Flask
- Django (학습 시작)

**Infrastructure & DevOps**:
- Linux (Ubuntu, Arch, CentOS)
- Docker
- NVIDIA Docker
- AWS EC2

**Networking & Protocols**:
- Nginx
- SMB
- SSH
- SSL/TLS, HTTPS (학습 목표)
- 인증 프로토콜 (학습 목표)

**Streaming & Media**:
- FFmpeg
- RTSP
- MJPEG
- KLV
- Pipe Communication

**Architecture**:
- MSA (Microservices Architecture)
- REST API
- DDD (Domain-Driven Design)
- gRPC

**Security**:
- JWT (JSON Web Token)

**AI/ML**:
- TensorFlow
- 13개 딥러닝 모델 통합

### Web Technologies
- Bootstrap
- AJAX
- Web 통신
- 브라우저 동작 원리

## Learning & Development Path

### Tech Tree Focus
**Backend Engineer Path**:
- Django
- 보안 프로토콜 (SSL/TLS, HTTPS)
- 인증 프로토콜
- API 설계 및 배포

### Skills Acquired
- Flask 기반 API 개발
- Docker 컨테이너 관리
- AWS 클라우드 배포
- Linux 서버 관리
- 스트리밍 데이터 처리
- MSA 아키텍처 설계

## Process & Culture Changes

### Project Management
- **OKR 도입**: 목표 기반 업무 관리
- **Notion 활용**: 프로젝트 가시성 확보
- **GitHub 활성화**: 코드 버전 관리

### Development Practice
- Docker 환경 표준화
- 문서화 중요성 인식
- 원격 협업 프로세스 확립

### Team Infrastructure
- Linux 듀얼 부팅 전사 적용
- GPU 학습 서버 구축
- 원격 개발 환경 구축

## Looking Forward: Next Quarter Goals

### Q3-Q4 2020 Targets
- **리눅스 사용 활성화**: 팀 전체 Linux 숙련도 향상
- **도커 정착**: Docker 기반 개발 프로세스 표준화
- **깃허브 활용 활성화**: 버전 관리 및 협업 강화
