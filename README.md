# Claude Code - UC4N

> Claude Code'un her sürümünden çıkarılan sistem promptu (system prompt) parçaları — sürüm sürüm arşivlenir ve yenilikler haber olarak yorumlanır.

Her sürüm kendi klasöründe (`Claude_Code_vX.Y.ZZZ/`) tutulur. İçindeki numaralı `.md` dosyaları, promptun ayrı bölümlerini temsil eder (kimlik string'leri, ajan promptları, araç açıklamaları, çıktı stilleri vb.).

> **Metodolojik not:** Parçalar `claude.exe` ikili dosyasından çıkarılmıştır. Numaralı önekler sürümler arasında yeniden numaralandırılabilir; bu yüzden aynı numara = aynı bölüm **değildir**. Bölümleri başlık/içerikten eşleştirin. Ayrıca bazı sürümlerde çıkarma sırasında dosyalara ikili string-tablo çöpü (MIME listeleri, HTML entity tabloları, sembol isimleri) karışabilir — boyut artışı her zaman gerçek içerik artışı demek değildir.

---

## Sürümler

| Sürüm | Klasör | Bölüm sayısı |
|---|---|---|
| v2.1.187 | `Claude_Code_v2.1.187/` | 33 |
| v2.1.195 | `Claude_Code_v2.1.195/` | 26 |

---

## Değişiklik Günlüğü: v2.1.187 → v2.1.195

> Aşağıda yalnızca **doğrulanmış / anlamlı** prompt değişiklikleri listelenmiştir. v2.1.195 çıkarımındaki büyük bayt artışlarının çoğu (verification_agent 30 KB, auto_mode_classifier 28 KB, identity/fable 15 KB, todo_reminder, statusline) gerçek prompt metni değil, çıkarma gürültüsüdür ve elenmiştir.

### 🆕 Yeni eklenenler

- **`34_autonomous_loop` — Otonom / zamanlanmış tetikleme.** Yeni bir parça: *"You're being invoked on a timer while…"* Claude Code artık bir **zamanlayıcı üzerinden kullanıcı etkileşimi olmadan kendini çağırabiliyor**. Zamanlanmış cloud agent / routine ve sürekli çalışan ajan döngüsü davranışıyla örtüşüyor.
- **`35_agent_sdk_identity` — Claude Agent SDK kimliği.** Yeni kimlik fragmanı: *"running within the Claude Agent SDK."* Claude Code'un SDK içinde çalışan bir varyantının resmîleştiğini gösteriyor.
- **Yeni kimlik string'leri** (`identity_strings` içinde): tek satıra ek olarak
  - *"You are Claude Code, Anthropic's official CLI for Claude, **running within the Claude Agent SDK**."*
  - *"You are a **Claude agent, built on Anthropic's Claude Agent SDK**."*
- **`04_doing_tasks_section` — "Reversibility & blast radius" güvenlik politikası.** Önceki sürümde **boş** olan bölüm artık dolu: geri döndürülemez / paylaşımlı sistemleri etkileyen eylemlerden (git push, branch silme, mesaj gönderme) önce **varsayılan olarak onay iste**; tek seferlik onay kalıcı onay sayılmaz.
- **Yeni model string'leri** (`claude_fable_unavailable` içinde): gerçek model etiketleri görünür hale geldi — *"Fable 5, Opus 4.7+"*, *"Fable 5, Opus 4.6+, Sonnet 4.6"* — ve *"Use sparingly for the hardest tasks"* (aşırı token/overthinking) uyarısı.

### ✳️ Genişletilen / olgunlaşan

- **`14_auto_mode_critique`** — tek cümleden **4 maddelik yapılandırılmış rubriğe** dönüştü: **Clarity**, **Completeness**, **Conflicts**, **Actionability**. Kullanıcının yazdığı izin/deny kurallarını daha sistematik denetliyor.

### ➖ Bu çıkarımda bulunmayan bölümler

> Tüm v2.1.195 klasörü bu bölümlerin ayırt edici cümleleri için tarandı, hiçbiri başka dosyaya taşınmamıştı. Çıkarma kapsamı farkı mı yoksa gerçek kaldırma mı olduğu yalnızca bu veriyle kesinleştirilemez.

- `17_output_style_learning` (Learning output style)
- `26_plan_agent` (salt-okunur planlama uzmanı promptu)
- `31_memory_selection` (hafıza seçici promptu)
- `32_github_issue_title` (GitHub issue başlığı üreteci)
- `33_team_coordination` (takım/teammate promptu)
- `09_agent_env_notes`, `30_builtin_agents` — ayrı dosya olarak yok (chrome içeriği `21_chrome_browser_automation`'da yaşıyor)
- `06_tone_conciseness`, `25_js_prompt_assemblies` — zaten boş/placeholder'dı; gerçek kayıp sayılmaz

### 🔧 Küçük / format düzeyi

- `01_cyber_risk`, `03_system_harness`, `05_executing_actions`, `07_git_operations`, `10_explore_agent`, `19_session_title`, `21_chrome_browser_automation`, `24_tool_prompts`, `28_context_management`: yalnızca birkaç on bayt fark — anlamlı içerik değişikliği yok.
- `08_default_agent_prompt`, `12_coordinator_system_prompt` (§2), `02_simple_mode_intro`: v2.1.195 çıkarımı cümle ortasında kesilmiş; içerik kaldırma değil, **çıkarma kesintisi** olarak okunmalı.

---

## ⭐ Öne çıkan başlıklar

1. **Claude Agent SDK kimliği geldi** — Claude Code artık "Agent SDK içinde çalışan" / "Agent SDK üzerine kurulu Claude ajanı" olarak da konumlanıyor.
2. **Otonom / zamanlayıcı tetiklemeli döngü** (`34_autonomous_loop`) — kullanıcı olmadan periyodik kendini çağırma.
3. **Yeni "reversibility & blast radius" politikası** — yıkıcı eylemlerden önce varsayılan onay.
4. **Yeni model kademesi: Fable 5** (Opus 4.7+ / Opus 4.6+ + Sonnet 4.6), aşırı token uyarısıyla.
5. **Auto-mode kural eleştirmeni olgunlaştı** — 4 boyutlu değerlendirme rubriği.

---

<div align="center">

### U-C4N

[![X](https://img.shields.io/badge/%F0%9D%95%8F-@UEdizaslan-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/UEdizaslan)

𝕏 [@UEdizaslan](https://x.com/UEdizaslan)

</div>
