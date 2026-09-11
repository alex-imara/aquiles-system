#!/usr/bin/env bash
# Gate de voz. Corre antes de que se publique cualquier Artifact.
# Solo aplica a publicaciones: las lecturas, listados y comentarios pasan de largo.
set -uo pipefail

action=$(jq -r '.tool_input.action // "publish"' 2>/dev/null || echo publish)

if [ "$action" != "publish" ]; then
  echo '{}'
  exit 0
fi

cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"GATE DE VOZ — no publiques hasta confirmar que el texto pasó por los skills obligatorios de Alex.\n\n1. alex-voice — OBLIGATORIO en todo texto en prosa. Si no lo invocaste en este turno, invócalo ahora y reescribe antes de publicar. Economía de información: si quitar una oración no cambia lo que hace el lector, sobra.\n2. imara-report-visual — maqueta. Una línea, una idea. Figuras SVG dibujadas adentro. Un solo acento.\n3. imara-client-branding — estructura y reglas de marca cuando el Artifact lo puede ver un cliente.\n\nChecklist antes de publicar:\n- Cero vocabulario prohibido y cero anti-patrones de IA (no es X es Y, transiciones mecánicas, hedging).\n- Cero jerga técnica sin traducir. Cero herramienta o modelo de IA nombrado.\n- Cero precio salvo que Tino lo haya confirmado en esta misma conversación.\n- Datos sin validar marcados [A VALIDAR], visibles.\n- Material de cliente: cero banderas internas, cero riesgos, cero notas de trabajo."}}
JSON
