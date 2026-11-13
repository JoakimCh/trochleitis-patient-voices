# Trochleitis patient voices

[Read or download the six-page US Letter PDF](output/pdf/trochleitis-patient-voices.pdf).

17 excerpt cards from 8 public Reddit threads, organized under 14 editorial account labels. Labels refer to reported authors, not independently verified patients or medical case histories. The packet covers reported dismissal, referral barriers, injection access, distress and treatment experiences. These are typeset excerpts, not screenshots; Reddit blocked screenshot capture in the research browser on 13 November 2026.

## Build

Use Python 3.10 or later. Install `requirements.txt`, then run `python build.py`. The default font path uses Debian/Ubuntu's `fonts-dejavu-core` package; edit `FONT_DIR` for another operating system. Output: `output/pdf/trochleitis-patient-voices.pdf`.

The script checks card text against the reserved footer area and stops on overflow. The current PDF was rendered and visually reviewed at US Letter size: 6 pages, 17 clickable source links.

## Sources and account labels

`sources.json` retains exact wording, source thread URL, displayed date, editorial context, diagnostic qualification and access date. Account labels appear discreetly above each source footer; descriptive card headings have no numbers.

| Account | Source / relationship |
| --- | --- |
| 1 | Original poster in `1ax1wwe`; quoted comment date unverified |
| 2.a / 2.b | Same commenter in `wwnd3q`; later reported pain-free trochlea after three injections |
| 3 / 4 | Separate replies in `wwnd3q`; diagnosis not established in the quoted comments |
| 5 | Injection-access reply in `1f1hclp`; diagnosis unspecified |
| 6 | Same poster's opening post and later reply in `f7myrd`, explicitly marked |
| 7 | Original poster in `1e4s88z`; injection did not relieve pain |
| 8.a / 8.b | Original post and self-attributed new-account follow-up in `1f1hclp`; identity link unverified |
| 9 | Swedish-language reply in `1ax1wwe`; suspected trochleitis |
| 10 | Original poster in `1v2kyoi`; asking about trochleitis, undiagnosed |
| 11 | Original poster in `1qt7ui5`; pain after PRK, diagnosis unverified |
| 12.a / 12.b | Two excerpts from the same post in `12d34wf`; earlier trochleitis diagnosis reported, broader symptoms unresolved |
| 13 | Different commenter in `1ax1wwe`; excruciating pain and helpful treatment |
| 14 | Different commenter in `1qt7ui5`; diagnosis and temporary injection relief reported |

Different labels do not prove different real-world identities. Cross-thread author overlap has not been ruled out. Usernames are omitted from the PDF, but source links can identify the authors.

## Translation and quotation policy

Account 9 is translated from Swedish into English. Its exact Swedish wording is retained in `original_quote`, alongside the English translation and a translation note. The translation has not been author-reviewed. Swedish language alone does not establish nationality, gender or country of care. All other excerpts retain the source's English wording and spelling. Brackets mark omissions or editorial notes.

A remembered Swedish account expressing surprise at still being alive could not be verified. Do not attribute that statement to Account 9. An English-language follow-up in Account 8.b expresses similar distress, but no Swedish connection or nationality is established. It is included as an English source, not as a translation or a match to that lead.

Account 8.b claims to be the original poster using a new username. Its displayed date is 28 December 2024, but it refers to seeing a specialist in November; the timing is unclear. This is disclosed, not silently corrected.

## Research method and limitations

Sources were accessed through public web search on 13 November 2026. Direct retrieval of several Reddit pages was unavailable; evidence is publicly indexed text, not a captured live interface. Search text may omit replies, later developments or revisions. Thread links are provided instead of guessed comment permalinks. Locate excerpts by exact wording and displayed date.

Selection focused on access concerns and pain burden. It is not a systematic or representative sample and does not establish country-level patterns, worldwide prevalence or negligence. Records and clinicians' perspectives were not reviewed. A post cannot establish whether a particular patient needs a steroid injection, whether an injection was placed correctly, or why a clinician declined a procedure. Suspected conditions and competing diagnoses remain explicit.

Important context is retained: Account 1 praised the specialist who eventually treated them; Account 2 later reported resolution of trochlear pain; Account 6 reported partial relief before pandemic-related delays; Account 7 reported a risk-based reason against repeating an unsuccessful injection; Accounts 13 and 14 describe helpful care. The packet does not portray successful access as denial of treatment.

## Before media use

Treat these accounts as leads for reporting. Recheck source threads and updates, seek permission before identifying or interviewing authors, and independently confirm clinical or institutional allegations. No posters have been contacted and no material has been sent to media.

For future additions, preserve exact quotations, original language, links, dates, diagnostic uncertainty and improving or contradictory follow-up. Group cards only when authorship is supported. Use real screenshots only when genuinely captured, retaining context and marking any redactions. Do not reconstruct a source interface and call it a screenshot.

Third-party quotations remain their authors' material; no blanket license is asserted over them.
