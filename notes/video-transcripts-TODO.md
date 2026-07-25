# Video transcripts + summaries — content to collect

Decision (2026-07-25): implement **Option A** (populate the existing per-video Transcript
feature + captions) and **Option C** (a short 2–4 bullet text summary of the video's key
points on each result page / PDF). Awaiting transcript text from user/client.

**How this wires in (for Claude, later):**
- Option A → fill each node's `text:[...]` field in `index.html` (the "Transcript" button +
  modal already exist; text shows behind them). The `welcome` node currently holds
  lorem-ipsum placeholder — replace it.
- Captions (`.vtt`) → need final video files or a timestamped transcript to sync against.
  Plain transcripts alone populate the readable modal but NOT synced CC. Personas currently
  render as still images (`vp()` → .jpg); real videos may not be produced yet.
- Option C → Claude drafts the bullet summaries FROM the transcripts (user reviews), rendered
  on the 7 result pages / PDF. Do NOT paste verbatim colloquial transcript onto the result page.

---

## Transcripts (paste plain text under each — persona/node labeled)

### 1. Laurel & Ricky — Welcome ("What best describes you?")  [node: welcome]  ⚠ replaces lorem placeholder
> 

### 2. Laurel — Teaching Artist vs. Credentialed Teacher  [node: taVsCred]
> 

### 3. Laurel / Ricky — Choosing a Discipline  [node: whatTeach]
> 

### 4. Chris — Supplementary Authorization  [node: suppAuth] → Supp Auth page
> 

### 5. Ricky — The CTE Certificate (1000 hours)  [node: cteIntro]
> 

### 6. Tiffany — The CTE Pathway  [node: cteVideo] → CTE Credential page
> 

### 7. Laurel — Life of a Teaching Artist  [node: lifeTA] → Teaching Artist page
> 

### 8. Matthew — Teaching Music  [node: mMusic] → Music page
> 

### 9. Eric — Teaching Theater  [node: mTheater] → Theatre page
> 

### 10. Lindsay — Teaching Dance  [node: mDance] → Dance page
> 

### 11. Kristin — Teaching Visual Art  [node: mArt] → Visual Art page
> 
