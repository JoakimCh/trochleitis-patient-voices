# Trochleitis patient voices

A reproducible, three-page US Letter collection for reviewing public patient accounts with journalists. Nine excerpt cards from five Reddit threads. These are typeset verbatim excerpts, not screenshots. Screenshot capture was blocked by Reddit's network security in the research browser on 13 November 2026. No screenshot has been fabricated.

## Build

Use Python 3.10 or later. Install `requirements.txt`, then run `python build.py`. The default font path uses Debian/Ubuntu's `fonts-dejavu-core` package; edit `FONT_DIR` for other operating systems. Output: `output/pdf/trochleitis-patient-voices.pdf`.

## Source and editorial method

`sources.json` contains each exact excerpt, source thread URL, date, diagnostic qualification and relevant context. Text was retrieved through public web search on 13 November 2026. The original Reddit UI was not captured. Thread links are provided rather than guessed comment permalinks. Locate comments by exact quotation and date; excerpt 01's comment date is unverified. Search indexing may omit replies or subsequent updates, and live posts can change.

Do not count cards as separate patients: 02 and 03 are the same commenter. Distinct author identities and medical records were not verified. Usernames are omitted from the PDF, but source links remain identifying. Excerpt 07 combines an opening post and a later reply by the same poster, explicitly marked. Excerpt 09 contains an explicitly marked omission. Spelling is preserved. The typeset layout is editorial, not Reddit branding.

Selection focused on reported dismissal, delayed recognition, injection access and distress. It is not a systematic or representative sample. No country-level comparisons or worldwide frequency estimates are supported. Clinicians' perspectives, reasons for refusal and underlying records are unavailable. Do not treat self-reported or suspected diagnoses as clinically confirmed.

Context was retained deliberately: 02/03 later reported trochlear pain relief after three injections; 01 praised the specialist who eventually treated them; 07 had partial benefit before pandemic delays; 08 received an injection without relief and reported a stated risk-based reason against repetition. A local injection's appropriateness for any individual cannot be established from a post.

## Preparing for media use

This is a reviewable advocacy packet, not independent verification of negligence. Recheck the original threads and updates before publication, seek permission before identifying or interviewing authors, and confirm any clinical or institutional allegation separately. Do not add inferred identities, countries or diagnoses. No posters have been contacted. No material has been sent to media.

## Maintaining the collection

Add records with exact quotations and original URLs; include any contradictory or improving follow-up, diagnostic uncertainty, and access date. Keep consent status and any screenshots separately. Replace text cards with real screenshots only when genuinely captured, preserving context and marking redactions. Never reconstruct a source UI and call it a screenshot.

This repository preserves the editable source collection and build script. Download the [three-page PDF](output/pdf/trochleitis-patient-voices.pdf) to review or print the current packet. Third-party quotations remain their authors' material; no blanket license is asserted over them.
