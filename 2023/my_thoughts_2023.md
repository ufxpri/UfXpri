# My Thoughts - 2023

## Q1 Reflections

### Theme: Solidify
Q1의 메인 테마는 "solidify"였다. 소프트웨어 개발자로써 프로세스를 정립하고 단단해지는 것을 목표로 했다.

### Work Intensity
23년 1분기는 매우 바쁜 시기였다. 순식간에 너무 많은 업무가 쏟아졌고 대부분의 개발을 다연님에게 맡기게 되었다.

### Growth in Collaboration
협업하는 방법이 개선되었고 더욱 성숙해질 수 있었다. 2인 체제의 백엔드 팀에서 업무 R&R을 효율적으로 분담하며 상호 성장을 도모했다.

## Key Learnings Throughout 2023

### 1. Technical Spectrum Expansion

#### C Language & Legacy Code
- **새로운 도전**: DNA 프로젝트에서 Python이 아닌 C언어 기반 외부 소스코드를 수정해야 하는 상황에 직면
- **학습 과정**: 외부 업체 소스코드를 단기간에 분석하고 학습
- **극복 방법**: 제작자와의 적극적인 Q&A를 통해 요구사항(KLV 데이터 실시간 전송)에 맞게 코드 수정
- **깨달음**: Python 중심의 기술 스택을 넘어 C언어 기반 시스템까지 다룰 수 있는 기술적 스펙트럼 확대

#### NoSQL & Data Architecture
- **Redis 도입 경험**: 소양강 댐 프로젝트에서 AI 병목 개선을 위해 Redis 검토 및 검증
- **학습 내용**: 오버헤드가 적은 데이터 전송 방식에 대한 이해 향상

### 2. Problem-Solving & Troubleshooting

#### Message Queue Architecture
- **문제 인식**: 네이버 프로젝트에서 대량 이미지 분석 요청 시 예상치 못한 병목 현상 발생
- **분석 과정**: 에러 로그 정밀 분석을 통해 병목 지점(Bottleneck) 식별
- **해결 전략**: Message Queue 아키텍처를 신규 도입하여 부하 분산 및 비동기 처리 구조로 전환
- **핵심 학습**: 대용량 트래픽 처리를 위한 아키텍처 설계 역량 강화

#### System Optimization
- **경험**: 네트워크 라이브러리 특성 이해를 통한 TCP Connection 조절
- **학습**: 세마포어 제거, 로그 로테이션 등 시스템 최적화 기법

### 3. Communication & Collaboration

#### Design/Planning Collaboration Challenges
- **긍정적 변화**: 기획/디자인 업무 이관으로 개발 퀄리티 향상
- **경험한 이슈**: 소통 부재로 인한 기획 디테일 누락 문제 발생
- **중요한 깨달음**: **초기 커뮤니케이션 강화의 중요성** - 프로젝트 초기 기획 단계에서의 디테일한 논의가 재설계 비용을 줄이는 핵심

#### Team Partnership
- **백엔드 파트너십**: 다연 연구원과 함께 다수의 프로젝트 배포 및 모니터링 부담 경감
- **성장 방식**: 코드 리뷰와 기술 토의를 통한 상호 성장

### 4. Project Management Insights

#### Tight Deadlines & Pressure
- **DNA 프로젝트**: 마감 1개월 전의 긴박한 일정 속에서 새로운 기술(C언어) 학습 및 적용
- **학습**: 압박 상황에서도 외부 전문가와의 적극적 소통을 통해 문제 해결 가능

#### Project Completion Rate
- **성과**: 총 8개 프로젝트 중 5건 기한 내 완료 (62% 준수율)
- **반성**: 남은 3건의 지연 원인 분석 필요

## Areas for Improvement

### 1. Network & Traffic Control
- **부족한 부분**: 네트워크 라이브러리 특성에 대한 이해 부족으로 트래픽 처리에 아쉬움
- **개선 필요**: 트래픽 제어 및 최적화 역량 강화 필요

### 2. Service Reliability & Monitoring
- **현재 상태**: 서비스 장애 알림(Alerting) 기능 부족
- **개선 방향**: 장애 감지 및 알림 시스템 고도화 필요

### 3. Deployment Process
- **인식**: 배포 프로세스의 표준화 필요성 체감
- **목표**: 안정적인 배포 체계 구축

## Personal Growth Summary

### Highest Points
- 고난이도 이슈 해결을 통한 시스템 안정화 성공
- C언어 레거시 코드 분석 능력 획득
- Message Queue 아키텍처 도입을 통한 대용량 트래픽 처리 경험
- 협업 능력 향상 및 팀워크 강화

### Key Mindset Shift
- "문제 해결(Troubleshooting)" 역량이 백엔드 엔지니어의 핵심임을 인식
- 단순 구현을 넘어 **시스템 안정성**과 **운영 효율성**의 중요성 깨달음
- 초기 커뮤니케이션과 디테일한 기획이 개발 비용을 줄이는 핵심임을 체득

### Career Identity
**"AI 모델 서빙의 안정성과 효율성을 책임지는 백엔드 리더"**로서의 정체성 확립

## Looking Forward to 2024

### Personal Commitment
- 배포 프로세스의 표준화 확립
- 서비스 안정성 지표(MTTR 등) 관리 체계 구축
- 네트워크 트래픽 제어 및 최적화 역량 강화
- 장애 감지 및 알림 시스템 고도화
