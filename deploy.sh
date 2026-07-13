#!/bin/bash
cd /Users/raulxxx/fiscalidadcanaria
git add -A
git commit -m "Update website $(date '+%Y-%m-%d %H:%M')"
git push origin main
echo "✓ Publicado en https://rick3007.github.io/fiscalidadcanaria/"
