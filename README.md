# Poolish Pro

A progressive web app for planning Neapolitan pizza nights using a poolish preferment.

Tweak number of pizzas, ambient temperature, dinner time, oven type, and flour strength — get a precision timeline and exact ingredient weights.

## Features

- Real-time ingredient calculator (poolish + main dough)
- Temperature-aware timeline that adjusts proof windows automatically
- Collapsible timeline steps — scan at a glance, expand for detail
- Weekend alert scheduling (Chrome/Android) or alarm summary (iOS)
- Works offline once installed
- Installable as a home screen app on iOS and Android

## Deploy

Hosted on GitHub Pages: https://sebarmano.github.io/poolish-pro

## Local dev

```
python3 -m http.server 8080
```

Open http://localhost:8080 — service workers require a server context, not file://.
