# Writing Guide for the Thesis

Distilled from Tim Skern, *Writing Scientific English: A Workbook* (facultas.wuv / UTB, 2009),
and adapted to this thesis. The book is written for biology manuscripts and for writers whose
first language is German; most of its advice carries over to a computational master thesis
unchanged. Where it clashes with the rules this thesis already follows (CLAUDE.md, the supervisor's
reviews), the clash is stated and the thesis rule wins. Section numbers in brackets point to the
book, e.g. [2.1.6].

**Section 11 holds the supervisor's instructions** (Dmitrii Lachinov, e-mails with reviews 1 and 2,
2026-10-12 and 2026-10-17). They take precedence over the book.

The guide is a summary in my own words. The examples are drawn from this thesis, not from the
book.

---

## 0. The five ideas behind everything else

1. **Write for an anonymous reader, not for your supervisor.** The examiner has not seen the code,
   the run logs or the NOTES. Every sentence has to make sense to someone who knows machine
   learning but not this project [4, take-home messages].
2. **Say things in the right order.** Most unclear writing is a sequencing problem, not a
   vocabulary problem [4, opening].
3. **Simple sentences carry complex ideas best.** One idea per sentence, subject first [2.1.4].
4. **Every text can be improved, and no text will be perfect.** Revise aggressively, then stop
   when it works [3.7, 4.5].
5. **Read your own work as a reviewer would**, before anyone else has to [2.1.8, 4.6].

---

## 1. Formal English: the mechanical rules [1.2]

These are cheap to check and noticed by every examiner.

| Rule | Instead of | Write |
|---|---|---|
| Complete sentences only (titles and headings may be fragments) [1.2.1] | "Results in Table 5.1." | "Table 5.1 lists the results." |
| No contractions [1.2.3] | "doesn't", "it's" | "does not", "it is" (and *its* for possession) |
| Do not open a sentence with *And, But, Because, So* [1.2.4] | "Because the crop is fixed, …" (as a new sentence after a full stop) | join it to the previous sentence ("…, because the crop is fixed") or use *as a result, therefore, however, in addition* |
| Do not end a sentence with *too, also, though, yet* [1.2.5] | "The layer channels are cropped too." | "The layer channels are also cropped." |
| No *get* [1.2.6] | "gets better", "got rid of" | "improves", "removed" |
| No vague quantities [1.2.7] | "a lot of runs", "a bit higher" | "35 runs", "0.017 higher" |
| No sensational adjectives, no exclamation marks [1.2.7] | "a striking / dramatic improvement" | "an improvement of 0.064" |
| No absolute claims or false precision [1.2.7] | "never", "proves", "100 %" | "in every fold tested", "supports", the measured number |

### Punctuation [1.2.2]

- **Commas** are needed in three situations only: (i) in lists; (ii) around inessential inserted
  material, like weak brackets; (iii) after a sentence-initial linking word or introductory phrase
  ("However, …", "At one year, …"). There is **no comma before *that*** in "It was shown that …".
- **Semicolon**: joins two halves of *one* thought. If the halves are two thoughts, use a full stop.
  At most one semicolon per sentence.
- **Colon**: only to introduce a list (and, in titles, to separate topic and subtopic). Not between
  two complete thoughts.
- **Question marks** are legitimate in running text: a question in the Discussion or at the start of
  a results paragraph is a lively way to introduce a theme [1.2.2.4, 4.3.4].
  *Thesis rule:* no question marks in headings (supervisor review 1).
- **Brackets, not dashes**, for inessential material, because brackets show where the aside starts
  and ends [1.2.2.7]. This matches the supervisor's and the editorial review's dislike of em-dash
  constructions. (En-dashes in names and ranges, *Runge--Kutta*, *0.4--0.5*, are unaffected.)
- ***e.g.* and *i.e.* belong inside brackets**, not in the flow of the sentence: "… several
  operators (e.g. the U-Net and the FNO)" [1.2.2.7].
- **Direct quotations** are rare in scientific writing; describe others' work in your own words and
  cite it. Being able to do so is a sign of maturity [1.2.2.6].

### Articles: *a*, *the*, or nothing [1.2.8, box 1.5]

1. *a/an* for one of many: "a validation fold".
2. *the* for a specific one, already identified: "the validation fold of patient 12".
3. No article for a universal concept or a plural in the general sense: "Persistence is a strong
   baseline", "Operators differ in reach".
4. A general concept used specifically takes *the*: "the persistence of the dilated-stencil
   network".
5. No article after a possessive: "its parameters", not "the its parameters".
6. Never delete articles to save words; it ruins the text [4.3.7].

### Spelling and confusable words [1.1, boxes 1.2, 3.3, 3.6, exercise comments]

Pick one variety of English and stick to it; nobody rejects a text for British vs American
spelling [1.1.1]. *Thesis:* the text uses British spellings (*normalisation*, *behaviour*); keep it
that way. A spellchecker does not catch real words used wrongly. Words the book flags, with the
ones relevant here:

- *affect* (verb) / *effect* (noun); *lose* / *loose*; *prove* (verb) / *proof* (noun);
  *latter* / *later*; *its* / *it's*; *discrete* (separate) / *discreet*.
- *amount* (uncountable) / *number* (countable): "the number of eyes", "the amount of padding".
- *rate* means change per unit time. "Growth rate" in mm/yr is correct; "the rate of eyes that
  fail" is not.
- *reason* (why someone did something) / *cause* (what produced an effect).
- *who* for people, *which/that* for things.
- *data* is plural in formal writing: "the data are partitioned" (the thesis currently has one
  singular use, `03-data.tex:448`).
- *prove / disprove* only for theorems, laws and theories. A hypothesis is *tested*, *supported*,
  *falsified*, *not supported* [box 3.6]. For an experimental result, "suggests", "supports",
  "is consistent with" are the right verbs. (Mathematical statements, "convergence can be proven",
  are fine.)
- German false friends: *proband* in English is a family member in a genetic study, not a study
  participant [box 3.3]. Also watch *eventually* (= in the end, not *eventuell*), *actual*
  (= real, not *aktuell*), *consequent* (≠ *konsequent*).

---

## 2. Eight guidelines for clear writing [2.1]

### 2.1 Make a plan [2.1.1]
Before writing a section, list the points it must make, group them by theme, and turn each theme
into a paragraph. For an introduction: the wide field, the specific area, the question addressed.
The plan will change; having one matters more than keeping it.

### 2.2 Clean layout [2.1.2]
The book's advice on fonts and double spacing is for journal submission and is superseded by the
JKU template. What remains: use sub-headings to signal a new topic, and make paragraph starts
visible.

### 2.3 Use paragraphs [2.1.3]
A paragraph is a group of sentences on one theme. A one-sentence paragraph is possible but rare.
Never break a line after every sentence. *Thesis check:* if a paragraph has two themes, split it;
if two paragraphs share one theme, merge them.

### 2.4 Write simple sentences [2.1.4]
- One idea per sentence.
- Subject first, then verb and object. No long introductory phrase, no inserted side remark in the
  middle.
- Write as if you were explaining it to a colleague; people speak in short sentences.
- German-speaking writers in particular tend towards very long sentences; split them.
- Qualify a statement in a second, linked clause rather than burying the caveat inside it:
  "The transport term raises the score by 0.062, although its control has fewer parameters."
- Once simple sentences come easily, two ideas per sentence are fine, but simpler sentences stay
  easier to manage.

### 2.5 Write positive sentences [2.1.5, box 2.2]
Sentences with *no, not, none, never, neither … nor* are harder to read. Say what is, not what is
not.

| Negative | Positive |
|---|---|
| "The per-pixel model does not predict any change." | "The per-pixel model reproduces the baseline mask exactly." |
| "No fold showed a gain above the noise level." | "Every fold stayed within the noise level." |
| "The second round is not without benefit." | "The second round adds about 0.01." |
| "None of the capacity steps raised the score." | "Every capacity step left the score unchanged within noise." |

Some negatives are unavoidable and correct ("The test split is empty"). Keep complex double
negatives to a minimum.

### 2.6 Write active sentences [2.1.6]
The book prefers the active voice and *we*, because it is shorter, clearer and closer to speech,
but says the choice is the writer's.

**Conflict with the thesis rule.** CLAUDE.md requires passive voice and forbids *we* and *I*. The
two fit together better than they seem: what the thesis forbids is a **personal** subject. An
active verb with an **impersonal** subject is allowed and gives most of the clarity the book wants.

| Weak passive | Impersonal active (thesis-compatible) |
|---|---|
| "It can be seen from Table 5.1 that the stencil network scores higher." | "Table 5.1 shows that the stencil network scores higher." |
| "The improved versions are presented in Section 5.3." | "Section 5.3 presents the improved versions." |
| "A gain of 0.064 is obtained by the dilated stencil." | "The dilated stencil gains 0.064." |
| "It is shown by the ladder that the canonical model fails C2." | "The step-size ladder shows that the canonical model fails C2." |

Keep the passive where the actor is the author and the action is a procedure ("The model was trained
for 30 epochs"). Use the impersonal active where the subject is a figure, table, section, model or
result.

### 2.7 Omit needless words [2.1.7, box 2.3]
The idea that serious scientific writing needs many complicated words is wrong; drop it. Typical
padding and its cure:

| Padding | Cut |
|---|---|
| "It can be seen from Figure 5.2 that …" | "Figure 5.2 shows that …" |
| "Due to the fact that …" / "The fact that …" | "Because …" / drop it |
| "has not yet been investigated in any detail" | "remains to be determined" |
| "a significant reduction in the amount of" | "significantly reduces" |
| "in order to" | "to" |
| "It is important to note that …", "It should be emphasised that …" | (drop; if it is important, the sentence shows it) |
| "a total of 75 eyes" | "75 eyes" |
| "both … as well as" | "both … and" |

Every word, sentence, paragraph and figure is a candidate for deletion [3.7, 4.3.1].

### 2.8 Read and think about your work [2.1.8]
- If you have not read it, nobody else should have to.
- Read on a **printout**: inconsistencies between distant pages (two abbreviations for one thing, two
  values for one number) are almost invisible on screen.
- Read **aloud** to find sentences that are too complex and text that does not hang together (a
  PDF read-aloud tool works too) [4.5].
- Ask: Is it formal English? Did I keep the eight guidelines? Did I think of the reader?

Everyone has off-days, including journal editors [2.2]. The aim is to make them rare.

---

## 3. Linking sentences [box 1.4]

Linking words show how a sentence relates to the one before. They replace the forbidden sentence
openers.

| Purpose | Words |
|---|---|
| add information (instead of *And*) | in addition, additionally, furthermore, moreover, indeed |
| contrast (instead of *But*) | however, in contrast, nevertheless, instead, on the other hand, otherwise |
| consequence (instead of *So*) | therefore, thus, hence, consequently, as a result, accordingly, to this end |
| cause (instead of *Because* at the start) | move *because* into the middle of the sentence, after the main clause |
| example | for example, for instance |
| close | in summary, in short, in conclusion, taken together |

Two cautions the book does not need but this thesis does: (i) do not open every sentence with a
linking word; a paragraph that reads "However, … Moreover, … Thus, … Consequently, …" is one of the
patterns the editorial review flagged as machine-like; (ii) the link must be true: *therefore* only
where the second sentence actually follows from the first.

*Thesis status (scan of 2026-10-22, comments excluded):* about 28 sentences open with *Because*
(e.g. `02-background.tex:404`, `04-method.tex:165`, `05-experiments.tex:141`); no sentence opens with
*And*, *But* or *So*. No contractions, no *get*, no *a lot*, no "it can be seen".

---

## 4. Vocabulary and repetition [1.3, ch. 7, exercise comments]

- Build a working vocabulary of precise scientific verbs and nouns (the book lists about 200 in
  box 1.7 and ch. 7). A few that fit this thesis: *assess, attribute, constrain, correlate,
  demonstrate, discrepancy, elucidate, estimate, indicate, infer, pinpoint, plausible, putative,
  quantify, robust, salient, substantiate, verify*.
- Look up an unfamiliar word in context by searching it in Google Scholar or PubMed titles and
  abstracts [1.3].
- The exercise comments repeatedly flag the **same word twice in one sentence** or the same phrase
  three times in a paragraph. Vary *ordinary* words.
- **Exception for this thesis:** never vary a **technical term** for elegance. *Change-region Dice*,
  *operator*, *arm*, *persistence*, *dilated stencil*, *fold* must mean one thing each and keep
  one name each (see CLAUDE.md → Terminology). Repetition of a defined term is a feature.

---

## 5. Building the document [ch. 4]

The book describes a journal manuscript. The thesis is longer but uses the same logic; this table
maps the sections.

| Manuscript section [box 4.3] | Question it answers | Thesis chapter |
|---|---|---|
| Title, keywords | — | title page |
| Abstract | the take-home message | Abstract, Kurzfassung |
| Introduction | what is my theme, why does it matter? | Ch. 1, Ch. 2 |
| Materials and methods | how? | Ch. 3, Ch. 4 |
| Results | what did I do, what did I find? | Ch. 5 |
| Discussion | what does it mean? | Ch. 6, Ch. 7 |
| Figures, tables, legends | the data | throughout |

### 5.1 Order of writing [4.2, box 4.5]
Do not write in reading order. The book's order is: **figures and tables → their captions →
results → discussion → introduction → abstract → title → methods → references →
acknowledgements → abbreviations.** Reasons: the figures *are* the result; reviewers look at them
first; drawing them shows whether data are missing *before* writing starts; and their sequence is
the plan for the results text. Do not run back to the lab (or the cluster) at every chance to
avoid writing [4.2].

*Thesis:* most chapters exist already, so the order now matters for revision: settle each Chapter 5
figure and table first, then make the text follow them. Writing the abstract last is already the
plan (NOTES, 2026-10-14).

Keep a **style sheet**: "Figure" or "Fig.", how units are spaced, which abbreviations are defined,
how numbers are rounded [4.2]. *Thesis:* CLAUDE.md and `style/README.md` already play this role;
add decisions there as they are made (e.g. µm vs mm, "late-epoch mean").

### 5.2 Figures and tables [4.3.1, 4.3.2]
- **A figure must stand on its own**: axes labelled, units stated, nothing that needs the text to be
  understood. If it does not stand alone, improve it or drop it.
- Put the variable you changed on the x-axis and the one you measured on the y-axis.
- Use a bar chart only when there are too few points for a line.
- **Say what the error bars or ± values are** (range, SD, SE, over what). Many published papers
  forget. *Thesis:* "mean ± sd over the five folds" belongs in every caption that shows one.
- If the error bars span the difference being shown, the difference is not established.
- Process images only as far as necessary; never to make them look nicer.
- A figure that shows no difference, or that the text never refers to, is redundant.
- Split a figure that carries too much; never show the same data as both a figure and a table;
  describe a very small table in the text instead. *Supervisor (§11.6):* repeating a small
  excerpt of a main results table next to the ablation that discusses it is wanted; the book's
  rule applies to figure-vs-table duplication only.
- Remove information repeated in every row or column of a table: move it to the title, a single
  column, or a footnote. Round to the significant figures that matter.
- **Captions**: a short title that states either what was done or what was found, then the details
  needed to read the figure (what, how measured, how many runs, what the bars mean). Tables are
  read without a legend, so anything essential goes into a footnote. Captions are hard for
  everyone [4.3.2].
- *Thesis:* this agrees with the figure rule in memory and NOTES (one message per figure, text in
  the caption, not in the plot).

### 5.3 Results [4.3.3]
- Give just enough to understand each result and why the next experiment followed from it. Keep
  interpretation for the Discussion.
- Reflect the research cycle: aim → experiment → result → what it suggests → next experiment.
- In each paragraph: state the aim, what was done, and **tell the reader which panel to look at
  and what to see there**.
- End a run of experiments with a short summary paragraph.
- Anticipate the obvious objection and answer it in the text (e.g. "the gain is not a capacity
  effect, because …").
- Lay figures, captions and results text side by side and adjust them to each other.
- Report results in the order that builds the argument: confirmatory results first, new ones
  after (exercise 5.5, comment 13).
- Leave `(ref)` placeholders while drafting; fill in references once the drafts are complete.
  *Thesis:* use `% TODO: cite …` per CLAUDE.md.

### 5.4 Discussion [4.3.4]
- **Open with the main outcome of your work**, not with other people's work.
- Then: how the findings relate to the literature; what is new; evidence for and against the
  interpretation; whether the questions posed at the start were answered.
- The Discussion is not a review article.
- A direct question is a good way to open a theme: "Why does the reach stop helping beyond ±21
  columns?" (in the text, not in a heading).
- The book warns against long lists of further experiments in a journal paper. A thesis has a
  Future Work section, so the warning becomes: keep future work to what follows from the results,
  and do not list experiments that would have been needed to support the claims already made.
- Watch for speculation; tone down what the data do not carry [4.4].

### 5.5 Results and Discussion combined? [4.3.5]
Possible, and closer to how research is actually done, but less common because readers want to
judge the results before the interpretation. *Thesis:* the chapter plan keeps them apart (Ch. 5 and
Ch. 6); within Ch. 5, each subsection still closes with a one-sentence reading of its result.

### 5.6 Introduction [4.3.6]
Write it after the results and discussion, when you know exactly which parts of the field matter.
The funnel in three steps: (1) the wide area; (2) the specific part studied; (3) the question,
with a brief outline of what was found. This is the hour-glass narrowing of THESIS_STRUCTURE.md.
While drafting, leave a placeholder ("xxx") for any detail that would take long to check; it may
be cut anyway.

### 5.7 Abstract, title, keywords [3.3, 4.3.7]
- Title and abstract are read first and sometimes only. They must be clear, concise and agree with
  each other.
- Write the abstract **early enough to revise it several times**, so that it matches the text.
- Practice exercise: summarise the whole work **in three sentences**. If that is not possible, the
  message is not yet clear. Then expand to the allowed length.
- Shorten by removing padding and rephrasing, never by removing articles.
- Tense: past for what was done and found; present for the closing conclusion.
- Title: plain, no abbreviations, states the content without overstating it.
- Keywords should *extend* the title, not repeat it, so that the work is found from more searches.
  *Thesis:* the current keywords (Geographic Atrophy, OCT, neural PDE solvers, graph neural
  networks, U-Net, medical imaging, longitudinal prediction) partly repeat the title; consider
  terms such as *disease progression modelling* or *spatiotemporal forecasting*.

### 5.8 Methods [4.3.8]
- Complete, linked sentences in the past tense, not a recipe list.
- Enough detail for someone in the field to repeat the work; cite earlier descriptions instead of
  repeating them, and state only the changes.
- Check consistency between Methods and captions (exact conditions) and between Methods and
  Results: every method used in the results is described, and every method described is used.

### 5.9 References [4.3.9]
- Every sentence about someone else's specific work needs a citation; general knowledge of the
  field does not.
- Cite the **original** paper for a method or result, not a review. Reviews are for pointing the
  reader to background; too many reviews suggests shallow reading.
- If two groups published the same thing at the same time, cite both. Cite opposing evidence and
  discuss it.
- When unsure, cite. Nobody objects to a complete bibliography.
- Use a reference manager, and still check every entry (right paper, right format).
- *Thesis:* the citation rules in memory and `literature/_ledger.md` go further than the book
  (every citation verified against the source text).

### 5.10 Acknowledgements, abbreviations [4.3.10, 4.3.11]
Keep acknowledgements simple; name funders and grant numbers. Compile the abbreviation list after
the methods, where most abbreviations appear, and check it is complete.

---

## 6. Tenses [4.3.3, 4.3.4, 4.3.6, 4.3.7]

| Situation | Tense | Thesis example |
|---|---|---|
| what was done and found in this work | past simple | "The model was trained on four folds." "The stencil network scored 0.526." |
| established knowledge, general truths | present | "GA lesions enlarge over time." |
| what a figure, table or section shows | present | "Table 5.1 lists …", "Section 5.6 shows …" |
| conclusions and implications drawn now | present | "Reach at lesion scale is therefore required." |
| earlier literature | past or present perfect | "Mai et al. (2024) predicted …"; "U-Nets have been used as surrogates …" |
| planned work | future | "A matched transport control would …" |

*Thesis note:* for numbers that describe this thesis's results, decide once between past ("scored")
and present ("scores") for Chapter 5 and keep it consistent; the book uses past for results and
present for what a figure shows.

---

## 7. Summarising without plagiarism [3.1, 3.4]

1. Read the source, then put it away.
2. Note the salient points on paper.
3. Draft the summary from the notes only, by hand if possible.
4. Compare with the source. Where your words match the original, find other words; if a technical
   term cannot change, change the sentence around it.
5. Search the source PDF for any phrase you are unsure of.

This also applies to summarising your own earlier texts (the practical report, NOTES) and to text
produced with AI assistance: rewrite from notes, then check.

---

## 8. Revision procedure [box 3.2, 4.4, 4.5, 5.7]

**The first version is never the last.** A first complete draft is an achievement and still far from
final. Revision means more than fixing errors: imagine how the text could help the reader grasp the
result more quickly.

### Pass 1: fast overview
Read quickly. Mark spelling, informal expressions, and places that need a linking word. Ask: does it
make sense, do I understand what is meant? Mark what you do not understand.

### Pass 2: slow reading
For each paragraph and sentence:
- Is the paragraph one theme?
- Is each sentence straightforward and simple? Does it make sense?
- Do the sentences fit together, with correct links?
- Are expressions repeated? Are there needless words?

### Pass 3: backwards
Read the document **from the end, paragraph by paragraph**. This catches style differences between
the beginning and the end, and stops the second half from being checked less carefully because you
ran out of energy halfway.

### Pass 4: the whole document
- Do figures, tables, captions and results text fit together?
- Are the chapters consistent with each other (same numbers, same terms, same claims)?
- Is anything missing from the methods? Is anything said twice in methods and results?
- Is everything relevant? Is the introduction too long? Is the discussion too speculative?
- "What if" questions: What if this sentence goes? What if this paragraph moves to the Discussion?
  What if this section had more detail? Ask them once front to back and once back to front.

### Ten editing commands [5.7]
1. Read the work several times.
2. Check the paragraph structure.
3. Make sure every sentence relates logically to its neighbours.
4. Check that every sentence is complete.
5. Shorten and simplify long or complex sentences.
6. Check the tenses.
7. Find words or expressions that could be better.
8. Check every linking word.
9. Check the meaning of every word you are using for the first time.
10. Omit needless words.

### Habits
- Edit on paper, mark in a bright colour, circle what is too complex.
- Fix spellchecker and grammar-checker marks paragraph by paragraph while typing.
- Save deleted chunks in a separate file; they may be useful later.
- Give the full draft to someone else, take the comments seriously, then reread [box 4.1].
- Read to change the text, not to defend it [4.6].
- Stop when it works. A text never becomes perfect; it has to survive the reader.

---

## 9. Where the book and this thesis disagree

| Book says | Thesis rule | Resolution |
|---|---|---|
| prefer active voice with *we* [2.1.6] | passive, no *we/I* (CLAUDE.md) | impersonal active subjects (figure, table, model, result); passive for the author's procedures |
| question marks are lively, also in headings and titles | no questions in headings (supervisor) | questions only in running text |
| vary words to avoid repetition | one term, one meaning (CLAUDE.md terminology) | vary ordinary words, never technical terms |
| use linking words generously | editorial review flags chains of linking words as machine-like | one link where the relation needs saying, not at every sentence |
| keep the list of future experiments short (journal) | thesis has a Future Work section | keep it, but tie each item to a result |
| never show the same data twice [4.3.1] | repeat a small excerpt of the main table next to each ablation (supervisor) | excerpt tables allowed; no figure and table of the same numbers |
| the Results section is about the data, the Discussion about meaning | every section has intro (with thesis statement), body and conclusion (supervisor) | results subsections state their conclusion briefly; the wider interpretation stays in Ch. 6 |
| double spacing, Arial 12 pt | JKU template | template wins |
| figures and tables at the end of the manuscript | thesis floats figures in the text | template wins |

---

## 10. One-page checklist

**Every sentence**
- [ ] complete, one idea, subject first
- [ ] positive where possible
- [ ] no contraction, no *get*, no *a lot*, no sensational adjective, no "proves"
- [ ] does not start with *And/But/So/Because*, does not end with *too/also/though/yet*
- [ ] articles checked; *e.g./i.e.* in brackets; no dash asides
- [ ] every number has its unit and, if it is a ± value, says what the ± is

**Every paragraph**
- [ ] one theme, linked to the paragraph before
- [ ] no word repeated within a sentence; technical terms unchanged

**Every figure and table**
- [ ] stands alone; caption says what, how, how many, what the bars mean
- [ ] referred to in the text, which says what to look at
- [ ] not duplicated by another figure or table

**Every new term**
- [ ] defined before or at its first use, especially medical terms (§11.2)

**Every sentence (supervisor)**
- [ ] none of the LLM patterns of §11.5 ("What it does is that …", "not X but Y", "X is not what
  decides Y", dramatic or story-like phrasing)

**Every section**
- [ ] intro paragraph with purpose and thesis statement, body that supports it, conclusion that
  states what follows (§11.4)
- [ ] a results subsection has its own table or plot (§11.6)
- [ ] results: aim → done → found → next; interpretation saved for the discussion
- [ ] discussion: opens with the main outcome, weighs evidence for and against

**The whole thesis**
- [ ] read on paper, aloud, and once backwards
- [ ] read once from start to end only to tick off new terms (§11.2)
- [ ] numbers and terms identical everywhere
- [ ] abstract polished last and to near perfection; matches the text; title states without
  overstating (§11.1)
- [ ] contributions as bullets, each saying what is new and why it matters (§11.7)

---

## 11. The supervisor's instructions

Writing-related instructions from Dmitrii Lachinov's two review e-mails, in his order. They take
precedence over the book. The comments inside the review PDFs are tracked separately in
`reviews/supervisor-rev1-2026-10-12.md` and `reviews/worklist-ch4-7-2026-10-17.md`.

### 11.1 The abstract comes first in importance (review 1)
Most readers read only the abstract, and the examiners read it first, so it sets the first
impression. Polish it to near perfection. Combine with §5.7: write it once the rest is settled,
then revise it several times.

### 11.2 Define every term before it is needed (review 1)
Read the thesis from start to end and tick each new term (GA, AMD, fovea, VA, OCT, …) at its first
appearance. Each must be explained there or earlier. Assume the reader knows the mathematics (what
a PDE or a boundary value problem is) but **not** the medical part. A reader who meets AMD, GA,
fovea, visual acuity and OCT in the Introduction without explanation is lost from the start.
(Status: prerequisite audit done 2026-10-14, `reviews/m2-term-table-2026-10-14.md`; repeat it
after large edits.)

### 11.3 The opening chapters follow a fixed order (review 1)
1. **Medical background**: the eye, the retina and its layers (schematic), photoreceptors, RPE;
   how the retina is imaged (OCT, SLO, FAF); GA and its pathophysiology; the new drugs; the needs
   of patient management, predictive methods and personalised medicine.
2. **PDEs and solvers**: formalism and current methods only, **without mentioning GA**.
3. **Motivation**: placed here, where the reader has the medical and mathematical context.
4. **Problem statement**: clear, sharp, concise and **formal**, along the lines of "given
   measurements X sampled at times T on an anisotropic lattice, learn a parametric operator that
   maps the input to the solution". Introduce here the notation used in the rest of the thesis,
   with a few equations.
5. **Thesis outline.**

Headings state a topic, not a question ("Why Neural PDE Solvers?" → "Choice of the Modelling
Approach"). Introduction and Background may stay separate chapters (the supervisor accepted
this), as long as this order holds inside them.

### 11.4 Every section: introduction, body, conclusion (review 2)
1. **Introduction paragraph** with the section's purpose and a **thesis statement** (or a stand-in
   for one), e.g. "As a result, the parameter count had no effect." In a results section, repeat
   briefly what the experiment is and what it is for.
2. **Body**: as many paragraphs as needed, each supporting the thesis statement (e.g. comparing
   large and small models).
3. **Conclusion**: what can be inferred (e.g. "small models suffice").

### 11.5 Academic sentences, not fiction (review 2)
Avoid non-academic language and sentence structures. LLMs ignore Skern's rules and write prose that
can be engaging but suits fiction better. Constructions he names, which are hardly found in real
papers:
- "What it *does* is that …"
- "Not this, but that." / "X is not Y but Z."
- "X is not what decides Y."

To these the reviews of this thesis add: dramatic sentence openers, slogan-like closing sentences,
"What separates … is …", chains of linking words, and emphatic adverbs (*crucially, fundamentally,
entirely*). As a reference for the register, read the MM-PDE paper (Hu et al., ICLR 2024,
<https://openreview.net/pdf?id=hj9ZuNimRl>) or any other paper in `literature/`: state the fact, the
number and the source, in that order.

### 11.6 Tables and plots carry the results (review 2)
- A few large tables that collect all results are good.
- When a subsection discusses one ablation, repeat **a small part of the main table** on the same
  page as the discussion.
- Use box plots, scatter plots and other plots to carry the message.
- Roughly **one results subsection = one plot or table.**

### 11.7 Contributions as bullet points (review 1)
State what was achieved and what is new, and why it is valuable, as a bullet list.

### 11.8 Making figures (review 2)
LLM help with figures is fine. The supervisor himself avoids image generators and instead (i) writes
Python scripts with matplotlib or seaborn for PDF/SVG data plots, (ii) does the same for
simulations or animations of the data, (iii) for complex schematics such as a workflow, generates
SVG sub-elements with Claude and merges them by hand in draw.io. *Thesis:* data figures already
follow (i) through `images/scripts/` and `style/`; Figs. 2.1–2.3 are image-generated drawings with
an AI note in the caption.

### Not writing guidance
The list of the ten layer boundaries (ILM … outer boundary of the RPE) in review 2 is data, not
style. It is already in `03-data.tex` §3.2 (lines 182–193).
