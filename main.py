"""The Long Roast: Lawmakers and the File They Cannot Convert.

Entry: one satirical sentence (gate 1-320 characters) roasting lawmakers
who would regulate AI, crypto or the internet but cannot convert a file
to PDF. Judged pairwise on: on-topic roast first, a real turn (authority
set up, then undercut by the file), aim kept on lawmakers and the rules
they write, a clean one-pass read with the punch on the last few words,
and a specific unexpected detail over a worn tech-illiteracy cliche.

DECISION RECORD

Candidate A (rejected -- flat, punch lands mid-sentence):
  "The senator who wrote the AI Safety Act still emails his staff the
  bill as a .docx and asks them to 'turn it into a PDF, or whatever
  the kids call it'."
  The setup is fine, but the joke spends itself on "or whatever the
  kids call it" and then keeps going; the last words are filler, not
  the punch. Also leans on the tired "old man baffled by computers"
  frame rather than on the rules he writes.

Candidate B (rejected -- generic, no detail):
  "Congress can pass a law governing artificial intelligence before
  lunch, but the committee that wrote it has spent three weeks trying
  to turn its own report into a PDF."
  The turn is real (can legislate AI / cannot convert its own report),
  but "three weeks" and "its own report" are placeholders -- any
  committee, any report. Criterion 5 (specific unexpected detail)
  fails, and "into a PDF" as the last words is the brief restated,
  not a punch.

Candidate C (rejected -- worn trope):
  "The lawmaker who wants a kill switch on every AI model first needs
  IT to show him where the 'Save as PDF' button went in the update."
  "Needs IT to show him" is the oldest tech-illiteracy gag there is;
  the judge's criterion 5 explicitly punishes it. The turn is also
  backwards: it starts with the demand and never builds the authority
  it undercuts.

Candidate D (rejected -- muddy turn, long tail):
  "He chairs the committee on the future of the internet, but his
  office's most feared document is the 400-page AI bill that nobody
  can convert to PDF, so they just print it."
  "So they just print it" is a decent kicker, but the sentence takes
  two clauses to reach the file, the authority ("chairs the
  committee") is asserted rather than shown doing anything, and the
  file itself has no identity -- it is just "the 400-page AI bill".

Candidate E (CHOSEN):
  "They write the laws for the algorithms that will run the future,
  yet their own AI bill is still a Word file named
  FINAL_v7_ACTUALLY_FINAL.docx, waiting for an intern to turn it
  into a PDF."

Writing pass 1 (draft):
  "They regulate the algorithms that will run the future, yet the
  draft of their own AI bill is still a Word file called
  FINAL_v7_ACTUALLY_FINAL.docx, waiting for an intern to make it a
  PDF."
  Worked, but "regulate" is weaker than the act itself, "the draft
  of" adds a word that does no work, "called" is flatter than
  "named", and "make it a PDF" is vaguer than the brief's own verb.

Writing pass 2 (final):
  "Regulate" became "write the laws for" -- the judge's criterion 3
  rewards aim on lawmakers and the rules they write, so the sentence
  now opens on the act of writing law. "The draft of" was cut, "named"
  replaced "called", and "turn it into a PDF" replaced "make it a
  PDF", echoing the brief's own phrasing so the last words land as
  the file's fate, not as a paraphrase.

Why E wins, criterion by criterion:
  1. On-topic: lawmakers writing law for AI, undercut by the one
     file they cannot convert. Nothing else is in the frame.
  2. Real turn: the first clause grants them authority over the
     algorithms that will run the future; "yet" flips it to their
     own bill, a Word file, waiting on an intern.
  3. Aim: the joke is about power and competence -- the people who
     write the rules cannot operate on their own document. No random
     abuse, no shock value.
  4. One clean pass, punch at the end: the sentence reads straight
     through and the last words -- "turn it into a PDF" -- are the
     humiliation, delivered after the filename has already done its
     work.
  5. Specific detail: FINAL_v7_ACTUALLY_FINAL.docx is a concrete,
     lived-in artifact (every office has one); it is not the worn
     "can't use email" cliche, and it makes the lawmakers' own
     bill the evidence against them.

Final line: 188 characters, one sentence, inside the 1-320 gate
(hand-counted; the program asserts the gate on every run).

REVISION PASS (24 Nov 2026)

Critique of the chosen line, honestly:
  The opening, the "yet" turn, and the filename are all strong --
  but the ending fails the writer's own test. Candidate B was
  rejected because "into a PDF" as the last words is "the brief
  restated, not a punch" -- and the chosen line does the same thing:
  its last words are "turn it into a PDF", softened only by
  "waiting for an intern". "Still" and "waiting" also double up the
  same stalled-state signal. The sentence needed last words that
  are a new fact, not the brief repeated.

Fresh alternative weighed (F, rejected):
  "They write the laws for the algorithms that will run the future,
  yet their own AI bill is still a Word file named
  FINAL_v7_ACTUALLY_FINAL.docx, printed out and faxed to the
  committee." (183 characters)
  The fax is a vivid, unexpected image and "faxed to the committee"
  lands as a punch -- but it is a second old-technology gag stacked
  on the Word file, and the punch is about the office's workaround
  rather than the lawmakers' competence. Two verbs ("printed out
  and faxed") where one image would do.

Revision (kept the opening and the filename, replaced the ending):
  Before: "...waiting for an intern to turn it into a PDF."
  After:  "... — the only intern who could convert it quit in
          March."
  The em dash snaps the sentence into its kicker: the institution
  has not merely stalled, it has lost the only person who could do
  the trivial thing. "Quit in March" is dated and specific, so the
  bill has been stuck for months; the last words are a fact the
  judge has not seen before, not the brief restated. Criterion 4
  (punch on the last few words) and criterion 3 (competence) both
  improve; criteria 1, 2 and 5 are unchanged.

Final line after revision: 196 characters, one sentence, inside the
1-320 gate (hand-counted; the program asserts the gate on every
run).
"""

import os
import sys

LINE = (
    "They write the laws for the algorithms that will run the future, "
    "yet their own AI bill is still a Word file named "
    "FINAL_v7_ACTUALLY_FINAL.docx \u2014 the only intern who could "
    "convert it quit in March."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = "/output/entry.txt"
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print("chars: %d" % len(LINE), file=sys.stderr)
    # Read-back verification: the file must hold exactly the intended
    # line, inside the 1-320 character gate, or fail loudly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt mismatch: file does not match LINE")
    if not 1 <= len(written) <= 320 or not written.strip():
        raise SystemExit("entry.txt fails the 1-320 character gate")


if __name__ == "__main__":
    main()
