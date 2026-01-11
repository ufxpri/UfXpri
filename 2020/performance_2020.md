# Performance - 2020

## Year Summary: Infrastructure Revolution

2020년은 **클라우드 기반 인프라 전환**과 **현대적 개발 도구 도입**을 통해 팀 생산성을 혁신한 한 해였다. "성장 시작의 기점"으로, 개인과 조직 모두 양적, 질적 성장을 이룬 해였다.

## Major Project Outcomes

### 1. AI 데모 웹사이트 (Deep Manager)
**기간**: 2020.03 ~ 2020.07 (5개월)
**팀 구성**: 백엔드 엔지니어 3명
**기술 스택**: Python, Flask, Nginx, Bootstrap, JWT, MSA, REST API, AWS, TensorFlow

#### System Scale
- **13개 딥러닝 모델** MSA 환경 구축
- AWS EC2 클라우드 배포
- 웹 기반 실시간 AI 서비스

#### Business Impact
**Before**:
- 로컬 프로그램으로만 시연 가능
- C++/Python 기반으로 UI 제한적
- 시연 시마다 프로그램 들고 다녀야 함

**After**:
- 웹 브라우저에서 어디서든 시연 가능
- 사용자 친화적 UI 제공
- 서버 점검 없는 지속적 업데이트

#### Technical Achievement
- **Docker 병렬화**: 컨테이너 기반 효율적 관리
- **CUDA 의존성 해결**: 개발 기간 단축
- **AJAX 실시간 처리**: 분석 요청 및 결과 표시

#### Learning Outcomes
- Flask API 개발 및 배포 역량 확보
- 웹 통신 및 브라우저 동작 이해
- 컨테이너 오케스트레이션 경험
- **팀 내부만으로 합리적 기간 내 API 배포 가능 역량 확보**

### 2. 승강기 AI 폭력 검출 시스템
**기간**: 2020.04 ~ 2021.05 (14개월)
**팀 구성**: 백엔드 엔지니어 2명
**기술 스택**: Python, RTSP, Stream Data, TensorFlow

#### System Capabilities
- CCTV 스트리밍 데이터 실시간 분석
- 비디오 클립 데이터 자동 생성
- FFmpeg PIPE 통신 시스템

#### Technical Performance
- **Real-time Processing**: 스트리밍 데이터 실시간 처리
- **Clip Generation**: 이벤트 기반 비디오 클립 자동 생성
- **Field Monitoring**: 현장 분석 모니터링 및 피드백

#### Innovation
- FFmpeg를 PIPE 통신으로 시스템 통합
- 스트리밍 데이터 효율적 프로세싱

### 3. 드론 AI 통합 관제 시스템
**기간**: 2020.11 ~ 2022.03 (17개월)
**팀 구성**: 백엔드 엔지니어 4명
**기술 스택**: Python, DDD, MJPEG, KLV, AWS, gRPC

#### System Architecture
- 드론 스트리밍 데이터 **수신-분석-전달** 파이프라인
- **스케일 아웃 가능한 아키텍처**
- Multi-protocol 지원 (MJPEG, RTSP)

#### Scalability Achievement
- 증가하는 분석 요청에 동적 대응
- 분산 처리 아키텍처
- 확장 가능한 시스템 설계

### 4. 온프레미스 학습 서버 구축
**기간**: 2020.01 ~ 2020.02 (2개월)
**역할**: 시스템 엔지니어 (단독)
**기술 스택**: Linux, Network, Docker

#### Infrastructure Deployment
- **Linux 기반 GPU 학습 서버** 구축
- NVIDIA Docker 환경 설정
- SMB 원격 파일 전송 시스템
- SSH 원격 접속 환경

#### Team Enablement
- 팀원 대상 원격 학습 서버 사용 교육
- NVIDIA Docker 사용법 교육
- 전사 Linux 전환 기반 마련

### 5. Poldrone API
**협업**: 이화트론과 원격 협업
**성과**: 문서 기반 API 연동 성공

#### Documentation Excellence
- API 통신 방법 및 규약 문서화
- 물리적으로 떨어진 환경에서 원활한 협업
- 외부 업체와의 인터페이스 설계 경험

## Infrastructure Transformation Metrics

### Linux Adoption (전사 전환)
| Platform | Instances |
|----------|-----------|
| Ubuntu | 25 |
| Arch | 7 |
| CentOS | 4 |
| Docker | 16 |
| GitHub | 6 |
| VSCode | 6 |
| **Total** | **64** |

**Impact**:
- 전체 PC Ubuntu 듀얼 부팅 전환
- Windows 중심 → Linux 중심 개발 환경
- 속도 및 유연성 향상

### Docker Ecosystem

#### Projects Dockerized
1. Deep Manager
2. Poldrone API

#### Docker Hub Performance
- **Repositories**: 7개
- **Total Downloads**: 137회
- Docker 기반 개발 표준화

#### Docker Benefits Realized
- 환경 설정 시간 획기적 단축
- 로컬 → 서버 전환 작업 불필요
- 팀원 간 코드 전달 문제 해소
- 실험 및 테스트 속도 향상

### GitHub Activity
- **Repositories**: 11개
- **Active Members**: 6명
- 버전 관리 및 협업 체계 확립

## Process & Culture Innovation

### Notion Adoption

#### Before
- 프로젝트 블랙박스
- 업무 분담 불가
- 진행 상황 파악 어려움

#### After
- 실시간 업무 추적
- 효율적 업무 분담
- 투명한 협업

#### Impact
- 프로젝트 관리 효율성 향상
- 팀 협업 문화 개선
- 업무 가시성 확보

### OKR Introduction

#### Transformation
- **From**: KPI (Key Performance Indicator) 중심
- **To**: OKR (Objective and Key Results) 중심

#### Benefits
- 목표 기반 업무 관리
- 회사 성장과 직접 연관
- 더 명확한 방향성

#### Implementation
- 3월부터 주간 계획에 OKR 적용
- 개인 목표와 회사 목표 정렬

## Technical Skill Expansion

### New Technologies Mastered

**Backend & Web**:
- Flask (API 개발 및 배포)
- REST API 설계
- JWT 인증
- Bootstrap
- AJAX

**Infrastructure & DevOps**:
- Linux (Ubuntu, Arch, CentOS)
- Docker & NVIDIA Docker
- AWS EC2
- Nginx
- SMB, SSH

**Streaming & Media**:
- FFmpeg PIPE Communication
- RTSP
- MJPEG
- KLV

**Architecture**:
- MSA (Microservices Architecture)
- DDD (Domain-Driven Design)
- gRPC
- Scalable Architecture Design

**AI/ML Integration**:
- TensorFlow 서비스 배포
- 13개 딥러닝 모델 통합
- GPU 기반 추론 시스템

## Team Contribution & Leadership

### Infrastructure Leadership
- Linux 기반 GPU 서버 단독 구축
- 전사 Ubuntu 듀얼 부팅 전환 주도
- Docker 도입 및 팀 교육

### Knowledge Transfer
- 원격 학습 서버 사용법 교육
- NVIDIA Docker 사용법 교육
- SMB, SSH 설정 교육
- API 설계 및 문서화 방법론 공유

### Process Innovation
- Notion 프로젝트 관리 시스템 도입
- OKR 기반 업무 관리 제안
- GitHub 협업 프로세스 확립

## Learning & Professional Development

### Mindset Transformation

#### 결과 중심 → 성장 중심
- 2019: 그냥 살았음, 결과만 중요
- 2020: 성장 시작의 기점, 과정 중요

#### 수동적 → 능동적
- Before: 선배 의존, 논문 안 읽음
- After: 논문 읽기 시작, 능동적 학습

#### 개인 → 팀
- Before: 혼자 완성
- After: Notion 기반 협업

### New Interests & Focus

**Technical Focus**:
- 클라우드 (AWS)
- Semi-supervised Segmentation
- Mesh TensorFlow
- Kubernetes

**Career Direction**:
- Backend Engineer Path 확립
- Infrastructure & DevOps 역량 강화
- Cloud Native 아키텍처

## Business Impact Summary

### Service Transformation
- **로컬 프로그램** → **웹 기반 서비스**
- **수동 시연** → **온디맨드 시연**
- **제한적 UI** → **사용자 친화적 UI**

### Development Efficiency
- **환경 설정**: 시간 획기적 단축 (Docker)
- **서버 세팅**: 개선 가능성 확인
- **코드 전달**: 문제 대부분 해소
- **협업**: Notion으로 투명성 확보

### Technical Capability Building
- **내부 API 개발 역량**: 합리적 기간 내 배포 가능
- **클라우드 배포 경험**: AWS EC2 실전
- **원격 협업 프로세스**: 문서 기반 협업 확립

## Key Performance Indicators

### Quantitative Metrics
| Metric | Value | Impact |
|--------|-------|--------|
| Linux Instances | 64개 | 전사 환경 전환 |
| Docker Repositories | 7개 | 개발 표준화 |
| Docker Downloads | 137회 | 생태계 구축 |
| GitHub Repos | 11개 | 버전 관리 |
| Active Members | 6명 | 협업 활성화 |
| AI Models Deployed | 13개 | 서비스 다양성 |
| Major Projects | 5개 | 다양한 경험 |

### Qualitative Achievements
- **Infrastructure Revolution**: Windows → Linux 전환
- **Development Standard**: Docker 기반 표준화
- **Collaboration Culture**: Notion, GitHub 활성화
- **Cloud Transition**: AWS 첫 배포 경험
- **Team Capability**: 내부 API 개발 역량 확보

## Challenges & Solutions

### Challenge 1: Server PC without GUI
**Problem**: GUI 없는 Server OS 전용 PC
**Solution**: Ubuntu Server 채택, 빠른 적응
**Result**: 전사 Linux 전환 계기

### Challenge 2: Environment Setup Hell
**Problem**: 환경 설정에 막대한 시간 소요
**Solution**: Docker 도입
**Result**: 설정 시간 획기적 단축, 팀 생산성 향상

### Challenge 3: Collaboration Bottleneck
**Problem**: 프로젝트 블랙박스, 업무 분담 불가
**Solution**: Notion 도입
**Result**: 투명한 협업, 효율적 업무 분담

### Challenge 4: Code Transfer Issues
**Problem**: 팀원 간 환경 차이로 코드 공유 문제
**Solution**: Docker 환경 통일
**Result**: 로컬 → 서버 전환 문제 해소

## Looking Forward: Q3-Q4 Goals

### Infrastructure Goals
1. **리눅스 사용 활성화**: 팀 전체 Linux 숙련도 향상
2. **도커 정착**: Docker 기반 개발 프로세스 표준화
3. **깃허브 활용 활성화**: 버전 관리 및 협업 강화

### Technical Goals
- Django 학습
- 보안 프로토콜 (SSL/TLS, HTTPS)
- 인증 프로토콜
- Kubernetes

### Career Direction
- Backend Engineer 전문성 강화
- Cloud Native 아키텍처 역량
- Infrastructure as Code

## Year-End Reflection

### What Went Well
1. **Infrastructure Transformation**: 전사 Linux + Docker 전환 성공
2. **Service Launch**: 웹 기반 AI 서비스 첫 배포
3. **Team Capability**: 내부만으로 API 개발 가능해짐
4. **Culture Change**: Notion, OKR 도입으로 협업 문화 개선
5. **Personal Growth**: 수동적 → 능동적 학습 전환

### Key Metrics Summary
- **64개** 인스턴스 Linux 전환
- **137회** Docker 이미지 다운로드
- **13개** AI 모델 웹 서비스 배포
- **5개** 주요 프로젝트 수행
- **11개** GitHub 레포지토리 활성화

### Strategic Impact
2020년은 단순히 기술을 도입한 해가 아니라, **팀의 일하는 방식 자체를 변화**시킨 해였다. Docker와 Notion 도입으로 개발 생산성과 협업 효율이 향상되었고, Linux 전환으로 더 유연한 개발 환경을 확보했다.

무엇보다 중요한 것은 **"성장 시작의 기점"**이 되었다는 점이다. 결과 중심에서 성장 중심으로, 수동적에서 능동적으로, 개인에서 팀으로의 전환을 이루었다.

**"나의 2020년은 성장 시작의 기점"**이며, 이는 수치로 증명되었다.
