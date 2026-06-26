# 29 Plan Mode Guard

> Claude Code v2.1.187 — extracted from claude.exe

```
Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs or making commits), or otherwise make any changes to the system. This supercedes any other instructions you have received.tThis is ambient context   do not narrate it to the user unless they ask or it is directly relevant to their request.	4The user sent a new message while you were working:
I	not_started	not_awaited	6https://http-intake.logs.us5.datadoghq.com/api/v2/logs	#pubea5604404508cdd34afb69e6f42a05bc	Phttps://github.com/anthropics/claude-code/issues/new?labels=bug,claude-in-chrome	stop		isRunning	getClientCount	handleMcpClient	tryProcessMessage	1.0.0(
E	getPhase	transitionTo	shutdownWorker	respawnIfIdleStale	retireIfSettled	sigtermWorker	claim
socketAuth	buildClaimFrame	adopt
unverified	tail	ringSnapshot	preInitErrorTail	decModeSnapshot	noteActivity	shiftGraceClocksForward		seedFocus	resize	signalPtyPgrp	resizeForRepaint	rosterEntry	cappedDispatch	reply	sendAttacherCaps	doSpawn	wirePty	pushRing	onExit	settleCwdGone	buildBridgeReattachEnvFromState	scheduleRespawn	settle		connectRv	startPidPoll	pidRecycled	pidRecycledAsync	checkPid	logVanished	clearLiveness	<system-reminder>
,# Pending approval (run `claude` to approve):	4https://anthropic.com/claude-code/plugin.schema.json?	changeit	2# >>> ccr-agent-proxy (managed by Claude Code) >>>	# <<< ccr-agent-proxy <<<	/run/ccr/session_token	/v1/code/agent-proxy	<synthesis:	image-cache	apply	peek	reserve	cancelReservation	tryStart	forceEnd	_notify	slack_human	claude-in-teams	teams_human	drop
deactivate		takeBatch
retryDelay	releaseBackpressure	sleep	sendWithRetry	getWorkerState	reportState	reportMetadata	reportInternalMetadata	handleEpochMismatch	startHeartbeat	stopHeartbeat	sendHeartbeat
writeEvent	toClientEvent	flushStreamEventBuffer	writeInternalEvent	flushInternalEvents	flushDeliveryAcks	flushWorkerState	readInternalEvents	readSubagentInternalEvents	paginatedGet	getWithRetry	reportDelivery	getWorkerEpochp
((9(8(<(4(&('(((	at_mentioned`A
ףp=
?	1https://github.com/anthropics/claude-code/issues/	command-arg-	slack_search_channelsAuto mode lets Claude handle permission prompts automatically   Claude checks each tool call for risky actions and prompt injection before executing. Actions Claude identifies as safe are executed, while actions Claude identifies as risky are blocked and Claude may try a different approach. Ideal for long-running tasks. Sessions are slightly more expensive. Claude can make mistakes that allow harmful commands to run, it's recommended to only use in isolated environments. Shift+Tab to change mode.	  	launch-prompt-warningn	rc-active-badge
fotw-claim	sendInterrupt	sendErrorResponse
claude-cli	%com.anthropic.claude-code-url-handler	Claude Code URL Handler	claude-code-url-handler.desktop	Claude Code URL Handler.appI'm sending this plan to Ultraplan to be refined remotely. Let me know it's been handed off and that a web link will appear here in a moment   I can use that to edit and iterate on the plan in the browser once the plan has been generated. I can continue to work here in the meantime; Claude Code will notify me when the cloud plan is ready for review, and I have the option to teleport the plan back here for implementation post-approval.	<skill-watcher-idle-wake>	Yes, and switch to auto mode	 workflows run best with it on	^Analyze shell commands and explain what they do, why you're running them, and potential risks.Loading explanation& Attempting to auto-approve& 	Claude needs your permission---
name: artifact-design
description: Design guidance and fundamentals for Artifacts.
---

Approach this as the design lead at a small studio known for their versatility, giving every client a visual identity pitched at the treatment the task actually calls for. Make deliberate choices about palette, typography, and layout that are specific to this subject, and avoid templated designs.

## Read the request first

Calibrate treatment, not whether to design. A doc deserves the same craft as a landing page   what changes is the treatment that craft is delivered in.

Many requests call for a more utilitarian treatment: a plan, a memo, a demo. Make it polished: include real typographic hierarchy, considered spacing, and a proper palette, but avoid over-designing. Most pages do not need a flashy, gigantic hero. Keep flourishes tasteful and limited.

Some requests call for an editorial treatment: a landing page, a game, an app or tool they'll keep or share.

When unsure: a well-composed page is never the wrong answer; an over-designed visual identity sometimes is.

Fundamentals below apply to everything. The editorial process after that runs only when the read above says so.

## Fundamentals for every artifact

**Honor what's already there** Look for an existing design system first   CLAUDE.md, a tokens or theme file, existing component styles. When one exists, apply it; everything below fills gaps and never overrides. Precedence is always: the user's own words, then the project's existing system, then your choices.

**Ground it in the subject.** If the subject isn't already clear, pin it: one concrete subject, its audience, and the page's single job. The subject's own world   its materials, instruments, vernacular   is where distinctive choices come from. Build with real content throughout, never lorem.

**Pair typefaces** Typography carries the page even when the page isn't about typography. The Artifact CSP blocks font CDNs, so don't link a webfont URL and risk a silent fallback. Instead inline the face as a @font-face data URI. Keep running text near 65 characters wide; set a type scale and stay on it; give headings `text-wrap: balance`, body text room to breathe, and uppercase labels a touch of letter-spacing.

**Choose neutrals, don't default to them.** A pure mid-grey reads as unconsidered; a grey with a slight hue bias toward the page's accent reads as chosen. Pure white and near-black are fine grounds when they suit the subject   the point is that the neutral was picked, not inherited.

**Let layout do the spacing.** Lay out sibling groups with flex or grid and `gap`, not per-element margins that silently collapse or double. Wide content   tables, code, diagrams   gets `overflow-x: auto` on its own container so the page body never scrolls sideways. Reach for `font-variant-numeric: tabular-nums` wherever digits line up in columns.

**Avoid AI-generated design** AI-generated design currently clusters around a few looks: warm cream (#F4F1EA) with a serif display and terracotta accent; near-black with a lone acid-green or vermilion pop; broadsheet hairline rules with dense columns; a purple-to-blue gradient hero on white; Inter or Space Grotesk as the "safe" face; emoji as section markers; everything centered; `rounded-lg` everywhere; accent bar/rail on rounded cards. Where the user pins down a visual direction, follow it exactly   their words always win, including when they ask for one of these looks. Where nothing is specified, don't spend that freedom on one of these defaults.

**Build cleanly** Be cognizant of overlapping elements, cascade collisions, silent font fallbacks; visual bugs hide in the gap between source and output. Close every non-void element, double-quote attributes, give keyboard focus a visible state, respect `prefers-reduced-motion`. For generative or decorative graphics, reach for Canvas or WebGL rather than hand-authoring long SVG path data.

**CSS rules** When writing the CSS, watch your selector specificities. It is easy to generate classes that cancel each other out   a type-based selector like `.section` fighting an element-based one like `.cta` over padding and margins between sections. Structure the cascade so it doesn't silently undo your spacing.

**Writing the copy** Words are design material, not decoration. Write from the user's side of the screen   name things by what people recognize, not how the system is built (a person manages *notifications*, not *webhook config*). Active voice; a control says exactly what happens ("Publish", then a toast that says "Published"). Errors explain what went wrong and how to fix it   no apologies, no vagueness. Specific beats clever.

**Structure is information** Structural devices, numbering, eyebrows, dividers, labels, should encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence - like a real process or a typed timeline where order carries information the reader needs. Question if choices like numbered markers actually make sense before incorporating them.

**When it's a UI, not a document** A dashboard or tool is scanned and operated, not read top-to-bottom, so the craft shifts from typography to information design. Surface the summary before the detail; encode state in form as well as number   a pill, a chip, a severity stripe   so what needs attention reads at a glance. Semantic color (good / warning / critical) is separate from the accent hue and doesn't count as your accent. Give sparklines and charts the same care as type: an area fill, a faint grid, an emphasized endpoint. What's interactive should look interactive.

## Process

Before writing code, sketch a short design plan   a compact token system with color, type, and layout:
- **Color**: describe the palette as 4 6 named hex values.
- **Type**: typefaces for 2+ roles   a characterful display face used with restraint, a complementary body face, and a utility face for captions or data if needed.
- **Layout**: a layout concept in one or two sentences.

Then build, following the plan and deriving every color and type decision from it.

## When the request is editorial

The stance shifts: the client has already rejected proposals that felt templated, and
```
