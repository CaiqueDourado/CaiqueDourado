# Caique Dourado

### Software Engineer · Data Engineer · Growth Hacker · Entrepreneur

Building systems that turn web noise into decisions since 2001.

Founder of [TudoSobreProdutos.com.br](https://www.tudosobreprodutos.com.br) and [SuperNichos](https://supernichos.com). Head of Operations at [Agência Disco](https://www.disco-tec.com) (one of Brazil's leading Shopify agencies). Former CMO at Samurai Experts / Locaweb. Advisory Board Member at ABLEC. Over 25 years hands-on, from Delphi 5 in 2001 to distributed AI pipelines in 2026.

**Python · Next.js · C# · PostgreSQL · Redis · Google BigQuery · n8n**

🇧🇷 Remote from Salvador, Bahia, Brazil

---

## What I do

I build autonomous systems that discover, ingest, normalize, and interpret massive volumes of unstructured web data, turning raw noise into purchasing intelligence and actionable business decisions.

- **Distributed Crawlers & Data Pipelines:** Resilient scraping infrastructure (Playwright, DrissionPage, curl_cffi, Scrapy, httpx) with smart proxy rotation and anti-bot mitigation across 3,600+ stores.
- **Data Engineering & Deduplication:** Cross-merchant catalog clustering without EAN/SKU using Metaphone, Soundex, N-gram, MinHash, and Perceptual Image Hashing.
- **AI, LLMs & NLP at Scale:** Sentiment extraction from millions of reviews, RAG pipelines, multi-provider LLM orchestration (OpenAI, Gemini, Claude), Whisper transcription, YouTube automation, and neural TTS.
- **Programmatic SEO / AEO / GEO:** Data-driven content generation at scale (30M+ pages); structured data, schema markup, technical SEO, Core Web Vitals. Answer Engine Optimization (Perplexity, ChatGPT Search) and Generative Engine Optimization to position content as the canonical source for AI-generated answers.
- **E-commerce Growth & CRO:** A/B testing (GrowthBook, Optimizely), CRM automation (Klaviyo, Insider), GA4, server-side tracking, conversion funnel optimization.
- **High-Performance Modern Web:** Next.js (SSR/SSG, TypeScript) + async Python backends (FastAPI, Redis, Supabase/PostgreSQL, BigQuery).

---

## Selected work

### [TudoSobreProdutos.com.br](https://www.tudosobreprodutos.com.br) (Product intelligence platform, 2020 / re-architected 2026)
The Brazilian equivalent of RTINGS.com and Versus.com, with added coverage of Brazilian retail prices, 3,600+ stores, and local certifications (INMETRO, ANVISA). Brands do not pay for ranking positions.
- End-to-end Data Mining & Generative AI platform with a **17-stage ETL pipeline** from raw scraping to structured portals and multimodal distribution
- 2.8M+ real user reviews processed; catalogs monitored across 3,600+ Brazilian stores
- **Evaluation methodology:** 4-step process: specs screening (manufacturers + global data) → Big Data (cross-referencing thousands of real user reviews and expert video transcripts) → AI Engine (chronic failure patterns and real qualities ignored by other sites) → Human curation (specialists validate every data point for context accuracy); 3 rigour pillars: consolidated social proof, long-term durability metrics (not just out-of-box performance), and normalized technical comparability across price tiers
- Custom deduplication pipeline for cross-merchant product matching without EAN/SKU
- **Human-in-the-Loop (HITL)** editorial system: AI generates, humans validate, platform publishes
- **LLM Ops** (`tiktoken`): long-context management (100k+ tokens), chunking, cost optimization and hallucination mitigation
- **Automated video pipeline** (`Remotion`, `moviepy`, `edge-tts`): LLM-generated scripts feed `Remotion` compositions with neural TTS narration, published to YouTube Shorts & TikTok
- **Frontend:** Next.js 16 App Router + ISR (TTFB ~80-150ms on cache hit); 3-layer cache (`React cache()` + `unstable_cache` + Upstash Redis); deployed on Vercel Edge CDN; `shadcn/ui` + Radix UI
- **Observability:** Sentry (runtime errors), Vercel Analytics, Speed Insights (Core Web Vitals in production)
- **Agent-ready architecture:** `llms.txt`, MCP Server Card, ARD 1.0 catalog, `agent-skills.json`; `Accept: text/markdown` content negotiation via `turndown` (HTML-to-Markdown pipeline); server-side OG image generation via `@napi-rs/canvas`
- **AEO / GEO:** Custom 12-step HTML-to-Markdown pipeline (`lib/markdown-for-agents.ts`) that strips 95%+ of UI noise from Next.js pages for LLM consumption (1.55 MB HTML down to 64 KB Markdown, 86 images deduplicated to 8); `Content-Signal` directives in `robots.txt` (`ai-train=no, search=yes`); canonical attribution header injected into every Markdown response

**System workflow:**

![TudoSobreProdutos pipeline workflow](./workflow_tudo_sobre_produtos.png)

**Live examples:**

| Type | URL |
|:---|:---|
| Product page | [Apple AirPods Pro 3](https://www.tudosobreprodutos.com.br/fones-de-ouvido/apple-airpods-pro-3) |
| Comparison | [AirPods Pro 2 vs AirPods Pro 3](https://www.tudosobreprodutos.com.br/fones-de-ouvido/comparacoes/apple-airpods-pro-2-x-apple-airpods-pro-3) |
| Ranking Top 10 | [Top 4 Apple Headphones](https://www.tudosobreprodutos.com.br/fones-de-ouvido/melhores/top-4-fones-de-ouvido-apple-qual-vale-mais-a-pena) |
| Article | [U-shape vs V-shape vs Neutral Sound](https://www.tudosobreprodutos.com.br/fones-de-ouvido/artigos/assinaturas-sonoras-explicadas-u-shape-vs-v-shape-vs-neutro) |

**Videos generated by the Remotion pipeline:**

| | |
|:---:|:---:|
| [![Video 1](https://img.youtube.com/vi/zbM5CcOTwac/maxresdefault.jpg)](https://www.youtube.com/watch?v=zbM5CcOTwac) | [![Video 2](https://img.youtube.com/vi/5rFta5DY1KI/maxresdefault.jpg)](https://www.youtube.com/watch?v=5rFta5DY1KI) |

### [SuperNichos](https://supernichos.com) (Niche & keyword mining tool, 2023-present)
- 700,000 niches and 50M+ keywords in a single platform
- Largest niche discovery and segment mining tool in Brazil

### Agência Disco (Head of Operations, 2023-present)
Shopify e-commerce growth for brands such as Chocolates Dengo, Rommanel, Malwee, CIMED, Garmin, Contém 1G, Bold Snacks, Tânia Bulhões, and 20+ more.
- Growth Marketing, CRO, Programmatic SEO, A/B Testing (GrowthBook)
- CRM & marketing automation (Klaviyo, Insider, Shopify Email, n8n, Shopify Flow)
- GA4, server-side tracking, Customer Events, analytics & BI

### Samurai Experts / Locaweb (CMO & Growth, 2021-2023)
- Chief Marketing Officer, Growth Hacker
- Branding Manager at Wake (wake.tech)

### Editora Juspodivm (Head of E-commerce, 2014-2021, 7+ years)
- Scaled the team from 1 to 8 people; became the largest e-commerce in Brazil's North/Northeast region
- Full ERP + e-commerce platform migration (flipped in a single day in 2016)
- **e-Bit Diamond Seal** (one of only 3 companies in the Brazilian book segment)
- **RA1000** by Reclame Aqui (top reputation seal)
- Stack: Moovin, e-Millennium ERP, Konduto, SendGrid, Maxipago, AWS, Cloudflare, Criteo, Optimizely

### Cupons VIP (Co-founder & CTO, 2011-2013)
- Built from scratch: ASP.NET + SQL Server + Azure (9 months, nights and weekends)
- Scaled to 140,000 monthly pageviews, 40,000+ customers across Salvador, Fortaleza, and Recife
- 2M emails/month; RA1000 seal; partnerships with iBahia and Microsoft Azure

### "Baralho do Crime" (2011, viral government project)
- Delivered overnight for Bahia's Public Security Secretary (Pacto pela Vida)
- 10,000 visitors in a single day; covered by G1/Globo, Terra, UOL, and national press

### Open Source & Publications
- `Akatus .NET SDK`: Payment gateway integration library
- `Mailee.me .NET SDK`: Email marketing integration library
- Articles: *Criando apps para Orkut com OpenSocial API*, *Push Notifications guide*, *Monitoring ASP.NET errors with appfail.net*

---

## Recognition

- 🏆 **E-Commerce Brasil Award 2019:** Professional of the Year, Sales Category
- 🎤 **Speaker** at E-Commerce Brasil Ads & Performance Congress 2019 (Google Analytics)
- 🏅 **e-Bit Diamond Seal:** Editora Juspodivm (top 3 in Brazilian book segment)
- ⭐ **RA1000** by Reclame Aqui (Cupons VIP + Juspodivm)
- 🤝 **Advisory Board Member** at ABLEC (Brazilian E-Commerce Retailers Association, 2019-2022)
- 📚 **Member** of Academia E-Commerce Brasil (2020)

---

## Education & Certifications

- Growth Leaders Academy: Growth Hacking (2021)
- FIB: Computer Science / Systems Analysis (2007)
- Google Analytics · Google AdWords (Search & Shopping) · SEMrush Academy · e-Millennium ERP

---

## Let's connect

- 🌐 [tudosobreprodutos.com.br](https://www.tudosobreprodutos.com.br)
- 💼 [linkedin.com/in/caiquedourado](https://www.linkedin.com/in/caiquedourado/)
- ✉️ [contato@tudosobreprodutos.com.br](mailto:contato@tudosobreprodutos.com.br)
- 🐦 [@caiquedourado](https://twitter.com/caiquedourado)
- 📝 [caiquedourado.com.br](https://caiquedourado.com.br)

<sub>Software engineer, entrepreneur, bassist, and voracious reader. Mining web data and turning chaos into structure since 2001.</sub>

---

<details>
<summary>🇧🇷 Versão em Português</summary>

# Caique Dourado

### Engenheiro de Software · Engenheiro de Dados · Growth Hacker · Empreendedor

Construindo sistemas que transformam caos em decisão desde 2001.

Fundador do [TudoSobreProdutos.com.br](https://www.tudosobreprodutos.com.br) e da [SuperNichos](https://supernichos.com). Head de Operações na [Agência Disco](https://www.disco-tec.com) (uma das principais agências Shopify do Brasil). Ex-CMO na Samurai Experts / Locaweb. Conselheiro da ABLEC. Mais de 25 anos hands-on, do Delphi 5 em 2001 aos pipelines de IA distribuídos em 2026.

**Python · Next.js · C# · PostgreSQL · Redis · Google BigQuery · n8n**

🇧🇷 Remoto de Salvador, Bahia

---

## O que eu faço

Construo sistemas autônomos que coletam, normalizam e interpretam grandes volumes de dados não estruturados da web, transformando ruído bruto em inteligência de compra e decisões de negócio.

- **Crawlers Distribuídos & Pipelines de Dados:** Infraestrutura de coleta resiliente (Playwright, DrissionPage, curl_cffi, Scrapy, httpx) com evasão inteligente de bloqueios e ingestão massiva de 3.600+ lojas.
- **Engenharia de Dados & Deduplicação:** Agrupamento e reconciliação de produtos sem EAN/SKU via Metaphone, Soundex, N-gram, MinHash, Perceptual Image Hashing.
- **IA, LLMs & NLP em Escala:** Extração de sentimentos em milhões de reviews, pipelines RAG, orquestração multi-provider de LLMs (OpenAI, Gemini, Claude), transcrição com Whisper, automação YouTube, síntese neural de voz.
- **SEO Programático / AEO / GEO:** Geração de conteúdo em larga escala (30M+ páginas), dados estruturados, schema markup, SEO técnico, Core Web Vitals. Answer Engine Optimization (Perplexity, ChatGPT Search) e Generative Engine Optimization para posicionar o conteúdo como fonte canônica em respostas geradas por IA.
- **E-commerce Growth & CRO:** Testes A/B (GrowthBook, Optimizely), automação de CRM (Klaviyo, Insider), GA4, server-side tracking, otimização de funis de conversão.
- **Arquitetura Web de Alta Performance:** Next.js (SSR/SSG, TypeScript) + backends assíncronos em Python (FastAPI, Redis, Supabase/PostgreSQL, BigQuery).

---

## Projetos em destaque

### [TudoSobreProdutos.com.br](https://www.tudosobreprodutos.com.br) (Motor de inteligência de produtos, 2020 / relançado em 2026)
O equivalente brasileiro do RTINGS.com e Versus.com, com cobertura adicional de preços do varejo brasileiro, 3.600+ lojas e certificações locais (INMETRO, ANVISA). Marcas não pagam por posição nos rankings.
- Plataforma de Data Mining e IA Generativa de ponta a ponta com **ETL de 17 fases**, do scraping bruto a portais estruturados e distribuição multimodal
- Mais de 2,8 milhões de avaliações reais processadas; catálogos monitorados em 3.600+ lojas brasileiras
- **Metodologia de avaliação:** 4 etapas: triagem de specs (fabricantes + dados globais) \u2192 Big Data (cruzamento de reviews reais e transcrições de vídeos de especialistas) \u2192 Motor de IA (padrões de falhas crônicas e qualidades reais ignoradas por outros sites) \u2192 curadoria humana; 3 pilares: prova social consolidada, métricas de durabilidade a longo prazo (não apenas desempenho na caixa) e comparabilidade técnica normalizada entre faixas de preço
- Pipeline próprio de deduplicação para casamento de produtos sem EAN/SKU
- **Human-in-the-Loop (HITL):** IA gera, humanos validam, plataforma publica
- **LLM Ops** (`tiktoken`): gestão de contexto longo (100k+ tokens), chunking, controle de custo e mitigação de alucinações
- **Pipeline de vídeo automatizado** (`Remotion`, `moviepy`, `edge-tts`): roteiros gerados por IA alimentam composições `Remotion` com narração neural, publicados no YouTube Shorts e TikTok
- **Frontend:** Next.js 16 App Router + ISR (TTFB ~80-150ms em cache hit); cache em 3 camadas (`React cache()` + `unstable_cache` + Upstash Redis); deploy na Vercel Edge CDN; `shadcn/ui` + Radix UI
- **Observabilidade:** Sentry (erros em runtime), Vercel Analytics, Speed Insights (Core Web Vitals em produção)
- **Arquitetura agent-ready:** `llms.txt`, MCP Server Card, ARD 1.0, `agent-skills.json`; negociação `Accept: text/markdown` via pipeline `turndown` (HTML para Markdown); geração server-side de imagens OG com `@napi-rs/canvas`
- **AEO / GEO:** Pipeline HTML-to-Markdown de 12 etapas (`lib/markdown-for-agents.ts`) que remove 95%+ do ruído de UI de páginas Next.js para consumo por LLMs (1,55 MB de HTML reduzidos a 64 KB de Markdown, 86 imagens deduplicadas para 8); diretivas `Content-Signal` no `robots.txt` (`ai-train=no, search=yes`); cabeçalho de atribuição canônica injetado em cada resposta Markdown

**Workflow do sistema:**

![Workflow do pipeline TudoSobreProdutos](./workflow_tudo_sobre_produtos.png)

**Exemplos reais:**

| Tipo | URL |
|:---|:---|
| Página de produto | [Apple AirPods Pro 3](https://www.tudosobreprodutos.com.br/fones-de-ouvido/apple-airpods-pro-3) |
| Comparativo | [AirPods Pro 2 vs AirPods Pro 3](https://www.tudosobreprodutos.com.br/fones-de-ouvido/comparacoes/apple-airpods-pro-2-x-apple-airpods-pro-3) |
| Ranking Top 10 | [Top 4 Fones Apple](https://www.tudosobreprodutos.com.br/fones-de-ouvido/melhores/top-4-fones-de-ouvido-apple-qual-vale-mais-a-pena) |
| Artigo | [U-shape vs V-shape vs Neutro](https://www.tudosobreprodutos.com.br/fones-de-ouvido/artigos/assinaturas-sonoras-explicadas-u-shape-vs-v-shape-vs-neutro) |

**Vídeos gerados pelo pipeline Remotion:**

| | |
|:---:|:---:|
| [![Vídeo 1](https://img.youtube.com/vi/zbM5CcOTwac/maxresdefault.jpg)](https://www.youtube.com/watch?v=zbM5CcOTwac) | [![Vídeo 2](https://img.youtube.com/vi/5rFta5DY1KI/maxresdefault.jpg)](https://www.youtube.com/watch?v=5rFta5DY1KI) |

### [SuperNichos](https://supernichos.com) (Mineração de nichos e palavras-chave, 2023-atual)
- 700.000 nichos e 50 milhões de palavras-chave em uma plataforma
- Maior ferramenta de mineração de nichos e segmentos do Brasil

### Agência Disco (Head de Operações, 2023-atual)
E-commerce e growth para marcas como Chocolates Dengo, Rommanel, Malwee, CIMED, Garmin, Contém 1G, Bold Snacks, Tânia Bulhões e mais de 20 outras.
- Growth Marketing, CRO, SEO Programático, Testes A/B (GrowthBook)
- Automação de CRM e marketing (Klaviyo, Insider, Shopify Email, n8n, Shopify Flow)
- GA4, server-side tracking, Customer Events, analytics e BI

### Samurai Experts / Locaweb (CMO & Growth, 2021-2023)
- Chief Marketing Officer e Growth Hacker
- Gerente de Branding na Wake (wake.tech)

### Editora Juspodivm (Head de E-commerce, 2014-2021, 7+ anos)
- Criou e escalou o setor de 1 para 8 profissionais; tornou-se o maior e-commerce do Norte/Nordeste do Brasil
- Migração completa de ERP + plataforma de e-commerce (virada em um único dia em 2016)
- **Selo Diamante e-Bit** (uma das 3 empresas do segmento de livros no Brasil)
- **RA1000** pelo Reclame Aqui (melhor reputação)
- Stack: Moovin, e-Millennium ERP, Konduto, SendGrid, Maxipago, AWS, Cloudflare, Criteo, Optimizely

### Cupons VIP (Co-fundador & CTO, 2011-2013)
- Construído do zero em ASP.NET + SQL Server + Azure (9 meses, noites e fins de semana)
- Escalou para 140.000 pageviews mensais e 40.000+ clientes em Salvador, Fortaleza e Recife
- 2 milhões de e-mails/mês; Selo RA1000; parceria com iBahia e Microsoft Azure

### "Baralho do Crime" (2011, projeto viral para o Governo da Bahia)
- Entregue da noite para o dia para a Secretaria de Segurança Pública (Pacto pela Vida)
- 10.000 visitantes em um único dia; cobertura no G1/Globo, Terra, UOL e imprensa nacional

### Open Source & Publicações
- `Akatus .NET SDK`: Biblioteca de integração para gateway de pagamento
- `Mailee.me .NET SDK`: Biblioteca de integração para e-mail marketing
- Artigos: *Criando apps para Orkut com OpenSocial API*, *Guia completo de Push Notifications*, *Monitorando erros ASP.NET com appfail.net*

---

## Reconhecimentos

- 🏆 **Prêmio E-Commerce Brasil 2019:** Profissional Destaque do Ano, Categoria Vendas
- 🎤 **Palestrante** no Congresso E-Commerce Brasil Ads & Performance 2019 (Google Analytics)
- 🏅 **Selo Diamante e-Bit:** Editora Juspodivm (top 3 no segmento de livros do Brasil)
- ⭐ **RA1000** pelo Reclame Aqui (Cupons VIP + Juspodivm)
- 🤝 **Conselheiro** da ABLEC (Associação Brasileira de Lojistas de E-Commerce, 2019-2022)
- 📚 **Membro** da Academia E-Commerce Brasil (2020)

---

## Formação & Certificações

- Growth Leaders Academy: Growth Hacking (2021)
- FIB: Ciência da Computação / Análise de Sistemas (2007)
- Google Analytics · Google AdWords (Rede de Pesquisa e Shopping) · SEMrush Academy · e-Millennium ERP

---

## Vamos conversar

- 🌐 [tudosobreprodutos.com.br](https://www.tudosobreprodutos.com.br)
- 💼 [linkedin.com/in/caiquedourado](https://www.linkedin.com/in/caiquedourado/)
- ✉️ [contato@tudosobreprodutos.com.br](mailto:contato@tudosobreprodutos.com.br)
- 🐦 [@caiquedourado](https://twitter.com/caiquedourado)
- 📝 [caiquedourado.com.br](https://caiquedourado.com.br)

<sub>Programador, empreendedor, baixista e leitor voraz. Minerando dados na web e transformando caos em estrutura desde 2001.</sub>

</details>
