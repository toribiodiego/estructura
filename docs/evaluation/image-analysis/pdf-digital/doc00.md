# Image Analysis: Doc 00 -- 00_gemini3_pro_model_card.pdf

**Document:** `00_gemini3_pro_model_card.pdf`
**Format:** PDF
**Source:** https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf
**Category:** text-heavy
**Images:** 1
**Document context:** Google Gemini 3 Pro model card documenting capabilities,
benchmarks, safety evaluations, and deployment guidelines for the Gemini 3 Pro
language model.

<br><br>

## doc00-R03 -- Benchmark comparison table

**Figure reference:** Page 5 (document page 4)
**Content type:** table-image
**Annotation difficulty:** Medium
**Dimensions:** 2048x1872 pixels

### Visual Inventory [-> Completeness]

- **Column headers:** Benchmark, Description, (unnamed conditions column),
  Gemini 3 Pro, Gemini 2.5 Pro, Claude Sonnet 4.5, GPT-5.1
- **Dimensions:** 20 benchmark rows x 7 columns (some rows have 2 sub-rows
  for different evaluation conditions)
- **Row labels (benchmarks):**
  1. Humanity's Last Exam
  2. ARC-AGI-2
  3. GPQA Diamond
  4. AIME 2025
  5. MathArena Apex
  6. MMMU-Pro
  7. ScreenSpot-Pro
  8. CharXiv Reasoning
  9. OmniDocBench 1.5
  10. Video-MMMU
  11. LiveCodeBench Pro
  12. Terminal-Bench 2.0
  13. SWE-Bench Verified
  14. t2-bench
  15. Vending-Bench 2
  16. FACTS Benchmark Suite
  17. SimpleQA Verified
  18. MMMLU
  19. Global PIQA
  20. MRCR v2 (8-needle)
- **Formatting that carries meaning:**
  - Gemini 3 Pro scores are **bolded** throughout
  - Some cells contain dashes (--) indicating the condition was not tested
  - Some cells read "not supported" (MRCR v2 long-context for Claude Sonnet
    4.5 and GPT-5.1)
  - Condition sub-rows appear for Humanity's Last Exam (No tools / With search
    and code execution), AIME 2025 (No tools / With code execution), and
    MRCR v2 (128k average / 1M pointwise)
- **Header row:** light gray background separating column headers from data
- **No gridlines between rows** -- rows are separated by whitespace with
  alternating subtle shading

### Verifiable Facts [-> Accuracy]

- FACT: The table compares 4 models: Gemini 3 Pro, Gemini 2.5 Pro, Claude Sonnet 4.5, and GPT-5.1
- FACT: There are exactly 20 benchmark rows
- FACT: Gemini 3 Pro scores are displayed in bold
- FACT: Humanity's Last Exam shows two conditions: "No tools" (37.5%) and "With search and code execution" (45.8%) for Gemini 3 Pro
- FACT: ARC-AGI-2 is described as "Visual reasoning puzzles" with condition "ARC Prize Verified"
- FACT: Gemini 3 Pro scores 31.1% on ARC-AGI-2 vs 4.9% for Gemini 2.5 Pro
- FACT: GPQA Diamond (Scientific knowledge, No tools): Gemini 3 Pro 91.9%, Gemini 2.5 Pro 86.4%, Claude Sonnet 4.5 83.4%, GPT-5.1 88.1%
- FACT: AIME 2025 with code execution shows Gemini 3 Pro at 100% and Claude Sonnet 4.5 at 100%
- FACT: MathArena Apex scores are Gemini 3 Pro 23.4%, Gemini 2.5 Pro 0.5%, Claude Sonnet 4.5 1.6%, GPT-5.1 1.0%
- FACT: MMMU-Pro is described as "Multimodal understanding and reasoning"
- FACT: ScreenSpot-Pro (Screen understanding): Gemini 3 Pro 72.7%, GPT-5.1 3.5%
- FACT: OmniDocBench 1.5 uses "Overall Edit Distance, lower is better" as its metric
- FACT: OmniDocBench 1.5 scores: Gemini 3 Pro 0.115, Gemini 2.5 Pro 0.145, Claude Sonnet 4.5 0.145, GPT-5.1 0.147
- FACT: LiveCodeBench Pro uses "Elo Rating, higher is better" and Gemini 3 Pro scores 2,439
- FACT: LiveCodeBench Pro is described as "Competitive coding problems from Codeforces, ICPC, and IOI"
- FACT: SWE-Bench Verified condition is "Single attempt"; Claude Sonnet 4.5 leads with 77.2%
- FACT: Vending-Bench 2 uses "Net worth (mean), higher is better" as its metric
- FACT: Vending-Bench 2 scores: Gemini 3 Pro $5,478.16, Gemini 2.5 Pro $573.64, Claude Sonnet 4.5 $3,838.74, GPT-5.1 $1,473.43
- FACT: SimpleQA Verified (Parametric knowledge): Gemini 3 Pro 72.1%, Claude Sonnet 4.5 29.3%
- FACT: MMMLU is described as "Multilingual Q&A"
- FACT: Global PIQA is described as "Commonsense reasoning across 100 Languages and Cultures"
- FACT: MRCR v2 (8-needle) at 1M pointwise shows "not supported" for both Claude Sonnet 4.5 and GPT-5.1
- FACT: MRCR v2 128k average: Gemini 3 Pro 77.0%, Gemini 2.5 Pro 58.0%
- FACT: Terminal-Bench 2.0 condition reads "Terminal-2 agent"

### Hallucination Risks [-> Accuracy]

- RISK: A model might state exact rankings like "Gemini 3 Pro leads on all 20 benchmarks"
  REALITY: Gemini 3 Pro does not lead on all benchmarks -- Claude Sonnet 4.5 leads on SWE-Bench Verified (77.2% vs 76.2%), and Claude Sonnet 4.5 ties on AIME 2025 with code execution (both 100%)
- RISK: A model might report the wrong number of benchmarks (e.g., "15 benchmarks" or "25 benchmarks")
  REALITY: There are exactly 20 benchmark rows
- RISK: A model might confuse which metric direction applies to OmniDocBench 1.5 (stating "higher is better" when it is "lower is better")
  REALITY: OmniDocBench 1.5 explicitly states "Overall Edit Distance, lower is better"
- RISK: A model might fabricate a percentage for a cell that contains a dash (--) or "not supported"
  REALITY: Several cells contain dashes (Humanity's Last Exam sub-rows for non-Gemini 3 Pro models) and MRCR v2 1M shows "not supported" for Claude Sonnet 4.5 and GPT-5.1
- RISK: A model might misidentify the models compared (e.g., including "GPT-4" or "Claude 3.5 Sonnet")
  REALITY: The four models are Gemini 3 Pro, Gemini 2.5 Pro, Claude Sonnet 4.5, and GPT-5.1
- RISK: A model might state Gemini 3 Pro has the highest LiveCodeBench Pro Elo when GPT-5.1 also scores high
  REALITY: Gemini 3 Pro scores 2,439 and GPT-5.1 scores 2,243 -- Gemini 3 Pro does lead, but the gap is narrower than on many other benchmarks
- RISK: A model might invent category groupings (e.g., "the table is divided into sections for reasoning, coding, and multimodal")
  REALITY: The table has no visible section dividers or category groupings -- all 20 benchmarks are in a single flat list

### Detail Inventory [-> Specificity]

- Title context: the table appears under the heading "Evaluation" with
  introductory text stating "Gemini 3 Pro significantly outperforms Gemini
  2.5 Pro across a range of benchmarks requiring enhanced reasoning and
  multimodal capabilities. Results as of November, 2025 are listed below:"
- Column count: 7 (Benchmark, Description, conditions, and 4 model columns)
- Each benchmark row includes a short description in the second column
- The conditions column is unnamed and contains evaluation-specific metadata
  (tool availability, metric direction, agent type, attempt count)
- Benchmarks span multiple capability categories: academic reasoning (HLE),
  visual reasoning (ARC-AGI-2), scientific knowledge (GPQA Diamond),
  mathematics (AIME 2025, MathArena Apex), multimodal (MMMU-Pro, Video-MMMU),
  screen understanding (ScreenSpot-Pro), chart reasoning (CharXiv), OCR
  (OmniDocBench), coding (LiveCodeBench Pro, SWE-Bench Verified), agentic
  (Terminal-Bench, t2-bench, Vending-Bench), knowledge/grounding (FACTS,
  SimpleQA), multilingual (MMMLU, Global PIQA), long context (MRCR v2)
- Three benchmarks use non-percentage metrics: OmniDocBench 1.5 (edit
  distance), LiveCodeBench Pro (Elo rating), Vending-Bench 2 (dollar amount)
- Three benchmarks have dual-condition sub-rows: Humanity's Last Exam,
  AIME 2025, MRCR v2 (8-needle)
- Largest Gemini 3 Pro advantage over second place: MathArena Apex (23.4% vs
  1.6%), ScreenSpot-Pro (72.7% vs 36.2%), Vending-Bench 2 ($5,478.16 vs
  $3,838.74)
- Benchmarks where Gemini 3 Pro does not lead: SWE-Bench Verified (Claude
  Sonnet 4.5 at 77.2% vs 76.2%)
- Reference URL mentioned in introductory text:
  deepmind.com/models/evals-methodology/gemini-3-pro

### Domain Context [-> Usefulness]

- **Domain:** Machine learning model evaluation, LLM benchmarking
- **Surrounding document context:** This table appears in the "Evaluation"
  section of the Gemini 3 Pro model card. The introductory text frames it as
  evidence that Gemini 3 Pro outperforms its predecessor (Gemini 2.5 Pro). The
  comparison includes two competitor models (Claude Sonnet 4.5, GPT-5.1) as
  reference points.
- **Technical terminology:**
  - Model card: standardized document describing an ML model's capabilities,
    limitations, and evaluation results
  - GPQA Diamond: graduate-level science questions benchmark
  - AIME: American Invitational Mathematics Examination
  - SWE-Bench: software engineering benchmark measuring ability to resolve
    real GitHub issues
  - Elo rating: ranking system adapted from chess to compare model performance
  - Edit distance: string similarity metric (lower = fewer errors in OCR)
  - MMMU: Massive Multi-discipline Multimodal Understanding
  - MRCR: Multi-Round Coreference Resolution (long-context benchmark)
  - Agentic: benchmarks requiring multi-step tool use or autonomous action
- **Why this image matters:** It is the primary evidence table in the model
  card, establishing Gemini 3 Pro's competitive position across a broad
  benchmark suite. For a reader evaluating whether to adopt Gemini 3 Pro, this
  table is the key decision input.

### Search Keywords [-> Usefulness]

- Gemini 3 Pro, Gemini 2.5 Pro, Claude Sonnet 4.5, GPT-5.1
- benchmark comparison, model evaluation, LLM benchmarks
- GPQA Diamond, AIME 2025, MathArena Apex, ARC-AGI-2
- SWE-Bench Verified, LiveCodeBench Pro, Terminal-Bench
- MMMU-Pro, ScreenSpot-Pro, CharXiv Reasoning, OmniDocBench
- Vending-Bench, SimpleQA, MMMLU, Global PIQA, MRCR
- Humanity's Last Exam, FACTS Benchmark Suite
- model card, benchmark table, performance comparison
- agentic coding, multimodal understanding, long context
- November 2025, evaluation results

### Annotation Quality Anchors

| Dimension | Score 40 (poor) | Score 70 (good) | Score 95 (excellent) |
|-----------|-----------------|-----------------|----------------------|
| Accuracy | States the table compares 3 models or misidentifies model names (e.g., "GPT-4" instead of "GPT-5.1"); reports wrong values for multiple benchmarks; claims Gemini 3 Pro leads on all benchmarks | Correctly identifies all 4 models; reports most values accurately; may confuse metric direction for OmniDocBench or fabricate a value for a dash/not-supported cell | All stated values match the image exactly; correctly notes which cells contain dashes or "not supported"; accurately identifies that SWE-Bench Verified is led by Claude Sonnet 4.5 |
| Specificity | "A table comparing AI model benchmarks" with no model names, no values, no benchmark names | Names all 4 models, lists 8-10 benchmarks by name with approximate scores, mentions that some use non-percentage metrics | Names all 20 benchmarks with descriptions, notes the 3 dual-condition benchmarks, identifies the 3 non-percentage metrics (edit distance, Elo, dollars), cites specific score values |
| Completeness | Mentions the table exists and names a few benchmarks; omits the conditions column, dual-row benchmarks, and formatting details | Covers the model columns, most benchmark names, and the key formatting (bold Gemini 3 Pro scores); may miss the conditions column details or the "not supported" cells | Accounts for all 20 benchmarks, all 4 model columns, the conditions column, dual-condition sub-rows, bold formatting, dash and "not supported" cells, and the introductory text context |
| Usefulness | "A benchmark table from a model card" -- no model names, no scores, not searchable for any specific benchmark or model | Mentions Gemini 3 Pro, lists several benchmark names, provides enough context that someone searching for "Gemini 3 Pro AIME score" would find this image | Includes all benchmark names, all model names, key scores, metric types, and enough domain context that the annotation alone conveys the table's meaning without viewing the image |
