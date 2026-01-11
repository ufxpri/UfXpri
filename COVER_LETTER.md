# Cover Letter

## About Me

I still remember the moment in 2020 when I first truly understood what it means to grow as a software engineer. It wasn't when I successfully deployed my third API service or when I finished a project on time—it was when I realized I had been living on autopilot. "2019 was just another year," I wrote in early 2020, reflecting on how I had focused on results without investing in my own growth. That realization changed everything.

Today, I'm a backend engineer at OGQ with 7+ years of experience building AI/ML infrastructure at scale. I've evolved from someone who "just coded" to someone who designs systems that process 10,000+ CCTV streams, reduce CPU usage by 51.5%, and deploy to 14+ distributed facilities with 100% on-time delivery. But more importantly, I've learned that the best engineering isn't about speed—it's about building systems that go far.

## My Journey

### The Awakening: From Results to Growth (2020-2021)

My career transformation began with a simple question: "What if논문 (research papers) aren't just academic exercises, but guides to the future?" In 2020, I shifted from passive dependency on senior engineers to active learning. I introduced Docker to the team when everyone was comfortable with Windows. I championed Ubuntu Server when others doubted. One successful deployment changed our entire infrastructure—the whole team switched to dual-boot Linux environments.

This wasn't just about technology. It was about understanding that **good tools change how teams work**. Docker eliminated "environment hell" that had wasted weeks of setup time. Notion transformed our black-box workflows into transparent collaboration. These early experiences taught me that infrastructure decisions ripple through everything—team productivity, code quality, even company culture.

In 2021, I cut my teeth on real scale. The K-water project threw 36 simultaneous CCTV streams at a system I'd designed, and it buckled under pressure. I spent sleepless nights debugging, learning gRPC on the fly, and discovering that "working on my machine" means nothing in production. But we delivered. And more importantly, I learned that **architecture matters more than code**—that choosing the right pattern (Request-Reply, Pub-Sub, Eventual Consistency) is often more impactful than optimizing algorithms.

### The Troubleshooter: Solving Hard Problems (2022-2023)

2022 taught me that the hardest problems aren't technical—they're about understanding systems holistically. When our image scheduling system hit unexpected bottlenecks, the issue wasn't the scheduler or the processor in isolation. It was the **timing mismatch between two systems I'd designed separately**. That project crystallized a principle I still follow: "Design for the whole, not the parts."

I also learned that perfection is the enemy of progress. Early in 2022, I was obsessed with building every feature, optimizing every endpoint. But our AI demo project taught me: "Less is more." When requests are infrequent, complex batching and caching add overhead without value. **The right design isn't the most sophisticated—it's the one that matches the use case.**

2023 was my "trial by fire" year. The DNA+ drone project handed me C language code—completely outside my Python comfort zone—with a one-month deadline. I had never worked with C in production. I didn't know KLV data streaming protocols. But I did know how to learn: aggressive Q&A with the original developers, systematic reverse-engineering, and iterative testing. We successfully demonstrated 5G real-time drone video transmission with KLV metadata overlays. **The lesson: Technical depth matters, but learning agility matters more.**

Around the same time, Naver's image tagging API hit a wall with massive traffic. Analysis logs revealed the bottleneck: our synchronous API couldn't handle the burst load. The solution? **Message Queue architecture** (RabbitMQ). Introducing asynchronous processing transformed the system from struggling under load to gracefully scaling. That project taught me that sometimes the biggest performance gains come not from optimizing code, but from **rethinking architecture**.

### The Architect: From Speed to Strategy (2024-Present)

2024 marked my transition from "how fast can I build this?" to "how far ahead am I thinking?" The K-water expansion project became my masterclass in systems thinking. Deploying AI-powered safety monitoring to 14+ water treatment facilities—many in remote areas with 400KB/s bandwidth—demanded more than technical skill. It required:

- **Capacity planning**: When our GPU resource estimates were wrong, we delayed deployment by 2 weeks. I learned: never start a project without hardware requirement analysis.
- **Operational resilience**: Reducing Docker packages from 35GB to 12GB (60% reduction) wasn't just optimization—it meant 7-hour deployments instead of 17 hours over unstable field networks.
- **Performance engineering**: CPU usage spiked to 330% with CLIP models. Through OMP parameter tuning, I brought it down to 160% (51.5% reduction), enabling stable operation within existing infrastructure.

The result? We achieved **100% on-time deployment** (14/14 successful) in Q2-Q3, up from 33% in Q1. Systems ran for **34+ consecutive days** without intervention. MTTR (Mean Time To Recovery) dropped from 75 hours to **0 hours** by Q4.

But my proudest achievement in 2024 wasn't a metric—it was a mindset shift. The Media Cultural Enjoyment project required handling 10+ minute AI analysis tasks without timeout. The technical solution (Django + Celery + RabbitMQ + Redis) was straightforward. The real challenge was **architectural discipline**: using the Sidecar Pattern to isolate AI-generated code from the core system, eliminating unpredictable dependencies.

This wasn't just about technical correctness. It was about answering the question: "If this breaks at 3 AM six months from now, can someone else fix it?" That question now drives every design decision I make.

## What Drives Me

I'm fascinated by the gap between impressive technology and reliable systems. AI models that achieve 99% accuracy in labs often fail in production—not because the model is bad, but because the infrastructure isn't ready. I'm passionate about building that bridge.

What excites me most is the intersection of **AI/ML and production systems engineering**:

- How do you serve 10,000+ concurrent CCTV streams with real-time AI analysis?
- How do you design Active Learning pipelines that continuously improve models in production?
- How do you build systems where AI failures don't cascade into infrastructure failures?

I love these problems because they require both **technical depth** (understanding GPU optimization, async processing, distributed systems) and **strategic thinking** (capacity planning, failure isolation, operational resilience). They force you to balance innovation with pragmatism—to know when to use AI-generated code and when to reach for battle-tested solutions like Airflow or Celery.

Beyond technical challenges, I'm driven by **building team capability, not just individual heroics**. In 2024, I realized: overtime and solo firefighting don't scale. So I invested in documentation, built QC frameworks reusable across projects, and introduced Ansible for remote multi-site management. These aren't glamorous tasks, but they're what turn fragile systems into sustainable ones.

## Looking Forward

Right now, I'm focused on pushing AI/ML infrastructure beyond "works on demo" to "works at scale, reliably." At OGQ, I'm building systems that make intelligent capabilities accessible, not just impressive—infrastructure that serves millions without breaking.

I'm particularly excited about 2025's direction: **100% automation, 100% availability, 100% standardization**. These aren't just metrics—they're commitments to systematic excellence:

- **Automation**: Building common frameworks that eliminate duplication and reduce error-prone manual work
- **Availability**: Designing for zero downtime through better observability, faster recovery, and proactive monitoring
- **Standardization**: Creating reusable patterns so every project doesn't start from scratch

I'm also committed to knowledge sharing—targeting 24 blog posts in 2025 (2 per month) to rediscover my initial passion for learning in public and contributing to the developer community.

What makes me unique isn't just my technical range (from C++ multi-threading to Django async architectures, from TensorRT optimization to Kubernetes exploration). It's my journey from "going fast" to "going far"—the hard-won understanding that **the best systems are built with tomorrow's maintenance in mind, not just today's deadlines**.

## Let's Connect

If you're interested in learning more about my work, building resilient AI infrastructure, or discussing how to balance innovation with operational excellence, I'd love to connect.

**Quick Links:**
- 📄 [Detailed Resume](./RESUME.md)
- 💼 [GitHub Profile](https://github.com/ufxpri)
- 📊 [2024 Career Data](./2024/)
- 📧 Email: cfi02222@gmail.com

I'm always open to conversations about distributed systems, AI/ML infrastructure, production reliability, or the art of building software that lasts.

---

**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
