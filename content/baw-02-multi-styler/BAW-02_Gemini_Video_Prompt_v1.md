# BAW-02 BLDC Multi Hair Styler | Gemini Video Prompt v1
Reels 9:16 | 10 seconds | 4 scenes | clean footage only (no text, no logo, no app UI)

## Workflow
1. Generate each scene below as a separate 9:16 clip in Gemini (Veo). Attach both reference photos of the real product to every generation.
2. Send the 4 clips back. Claude will cut to exactly 10.00s, mute audio, and add Kanit text plus the official Bwell Beauty logo in post.
3. Text and logo are added in post because AI-rendered logos and Thai text were wrong in the previous version.

## Reference images to attach (every scene)
| File | Shows |
|---|---|
| BAW-02 on display stand (blue Bwell panel) | Handle with curling barrel attached, button layout, rose-gold ribbed air intake, round brush heads beside it |
| Round brush head in hand | Round brush attachment close-up: rose-gold perforated barrel, black bristles, grey end cap with tab, grey base collar |

## Product identity block (paste at the start of every scene prompt)
```
Product: the exact hair styler shown in the attached reference photos. Match it precisely.
- Handle: matte charcoal grey with fine leather-grain texture, slim cylinder.
- Top collar: rose-gold metallic ring where attachments click on.
- Controls on the front, top to bottom: round rose-gold button with snowflake icon, round power button, small vertical slider, round button near the base.
- A small silver "Bwell" wordmark printed vertically on the handle. Do not add any other text, model number or label on the body.
- Base: rose-gold air intake with vertical ribs (not a black mesh grille). Black power cord exits from the bottom.
- Curling barrel attachment: long rose-gold metallic barrel with lengthwise air slots, dark grey tip.
- Round brush attachment: rose-gold perforated metal barrel, black nylon bristles, dark grey end cap with a small tab, dark grey base collar.
Do not invent attachments, colours, buttons or markings that are not in the reference photos.
```

## Global style block (paste after the identity block)
```
Style: premium beauty commercial, vertical 9:16, soft natural window daylight, warm neutral bathroom-vanity / bedroom setting with beige stone and wood, shallow depth of field, slow smooth camera moves, realistic skin and hair texture.
Talent: one Thai woman, early 30s, long straight dark brown hair, natural makeup, sleeveless ivory wrap top. Same person, same outfit, same hair colour in every scene.
Hands: anatomically correct, five fingers, natural grip on the handle.
Strictly no on-screen text, no captions, no subtitles, no logos or watermarks overlaid on the video, no social-media interface (no like/comment/share icons, usernames, music bars or follower counts), no phone frame.
No audio narration.
```

## Scene prompts
| Scene | Time in edit | Generate length | Prompt (after identity + style blocks) | Text added in post |
|---|---|---|---|---|
| 1 Hook | 0.0–2.5s | 4s | Overhead-to-45-degree slow push-in on the styler handle lying on a beige stone vanity, with the round brush attachment and the curling barrel attachment neatly laid beside it. Soft morning light, gentle sheen on the rose-gold parts. | เลือกหัวให้ตรงลุค / 7 in 1 Multi Styler |
| 2 Round brush | 2.5–5.0s | 4s | Medium close-up: the woman, seated at a vanity mirror, attaches the round brush head to the handle (click onto the rose-gold collar), then brushes from roots to ends of a lower section of hair, turning the brush slightly so the ends bend inward with volume. Hair moves naturally with the airflow. | 01 / แปรงกลม · เพิ่มวอลลุ่ม จัดปลายผมให้โค้ง |
| 3 Curling barrel | 5.0–7.5s | 4s | Medium shot from a three-quarter angle: the woman holds the handle with the rose-gold curling barrel attached vertically beside her head; a section of hair wraps around the barrel on its own with the airflow, then she releases it into a soft loose wave. | 02 / แกนม้วน · ลุคลอนสวยแบบอัตโนมัติ [ยืนยันคำว่า "อัตโนมัติ" ตาม Product Master] |
| 4 Result + CTA | 7.5–10.0s | 4s | Slow push-in: the woman turns to camera with soft glossy waves, smiling lightly, the styler held loosely in hand at chest height with the curling barrel attached, product clearly visible. Background softly blurred. | ดู BAW-02 [CTA] |

## Copy to confirm before edit
| Item | Status |
|---|---|
| "7 in 1 Multi Styler" | Taken from the in-store product card in the photo. Confirm with Product Master. |
| Number of attachments | Not stated in any copy until Product Master confirms. Prompt shows only the 2 heads visible in the reference photos. |
| Other heads (paddle brush etc.) | [PLACEHOLDER: add scenes only if Product Master confirms the head exists] |
| "อัตโนมัติ" for curling | Card says "ม้วนผมอัตโนมัติ". Confirm before use. |
| Bwell Beauty logo | Need the official logo file (PNG, transparent) for the post overlay. |

## Post-production spec (Claude)
| Item | Spec |
|---|---|
| Length | Exactly 10.00s, hard cuts at 2.5 / 5.0 / 7.5s |
| Size | 1080x1920 |
| Audio | Muted; music added in-app at posting |
| Text | Kanit, white/grey only, inside 9:16 safe zone (y < 1600) |
| Logo | Official Bwell Beauty logo, one colour for the whole clip, no background box |
| QC | Product compared frame by frame with reference photos before delivery |
