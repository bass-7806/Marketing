# Bwell App QR - Print / Brochure

| Item | Value |
|---|---|
| Short link | https://bit.ly/bwell-app |
| Bitly link ID | bit.ly/bwell-app |
| QR code ID | Qq9i1BG209RweY3 |
| QR download | https://app.bitly.com/Bq328eyMUNy/qrcodes/Qq9i1BG209RweY3/details |
| Bitly workspace | Bq328eyMUNy (org Bwell, Growth plan) |
| Tags | qr, print, app-bwell |
| Created | 2026-09-18 |

## UTM

| Parameter | Value |
|---|---|
| utm_source | qr |
| utm_medium | print |
| utm_campaign | app-bwell |
| utm_content | ios / android / desktop (set by Bitly dynamic routing per OS) |

## Routing (Bitly dynamic routing, evaluated top to bottom)

| Visitor OS | Destination |
|---|---|
| iOS (iPhone, iPad) | https://apps.apple.com/th/app/bwell/id6787315911?utm_source=qr&utm_medium=print&utm_campaign=app-bwell&utm_content=ios |
| Android (incl. Huawei) | https://bwell-app-smart-link.vercel.app/?utm_source=qr&utm_medium=print&utm_campaign=app-bwell&utm_content=android |
| Other / desktop (default) | https://bwell-app-smart-link.vercel.app/?utm_source=qr&utm_medium=print&utm_campaign=app-bwell&utm_content=desktop |

Huawei devices are routed by Bitly as Android; the smart link page then detects HMS and sends them to AppGallery (C118407839). Google Play destination is com.bwell.smart.

## Verification (2026-09-18)

| Test | Result |
|---|---|
| curl with iOS UA | 301 to App Store URL with utm_content=ios |
| curl with Android UA | 301 to smart link with utm_content=android |
| curl with Huawei UA | 301 to smart link with utm_content=android |
| curl with desktop UA | 301 to smart link with utm_content=desktop |

## Notes

- bwellinter.com is registered on the Bitly account but not attached to this workspace, so the link was created on bit.ly. Attach the domain in Bitly (Settings > Custom domains) before creating future branded links.
- Apple App Store ignores UTM parameters. iOS attribution comes from Bitly click analytics by OS. Add pt= and ct= campaign tokens if an Apple App Analytics provider token becomes available.
- QR design: Bwell navy #005D9D dots and corners, white background, error correction level H, Bitly branding off.
