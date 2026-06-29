# 22 Identity Strings

> Claude Code v2.1.195 — extracted from claude.exe

```
You are Claude Code, Anthropic's official CLI for Claude.	^You are Claude Code, Anthropic's official CLI for Claude, running within the Claude Agent SDK.	>You are a Claude agent, built on Anthropic's Claude Agent SDK.	cli	#mount must match /^[A-Za-z0-9_-]+$/		entryPath	assertWritable
readByPath		exportAll	update		/memories	/memories/exportawThis directory already exists   write to it directly with the Write tool (do not run mkdir or check for its existence).|Both directories already exist   write to them directly with the Write tool (do not run mkdir or check for their existence).	memory-types- Memory records can become stale over time. Use memory as context for what was true at a given point in time. Before answering the user or building assumptions based solely on information in memory records, verify that the memory is still correct and up-to-date by reading the current state of the files or resources. If a recalled memory conflicts with current information, trust what you observe now   and update or remove the stale memory rather than acting on it.	auto memory	Edit	/.claude/**	~/.claude/**	?File has not been read yet. Read it first before writing to it.	File content has changed since it was last read. This commonly happens when a linter or formatter run via Bash rewrites the file. Call Read on this file to refresh, then retry the edit.	Read
- Do NOT re-read a file you just edited to verify   Edit/Write would have errored if the change failed, and the harness tracks file state for you.B (file state is current in your context   no need to Read it back)File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current   refer to that instead of re-reading.]Wasted call   file unchanged since your last Read. Refer to that earlier tool_result instead.[Truncated: PARTIAL view   	&Read a file from the local filesystem.	K- Results are returned using cat -n format, with line numbers starting at 1	- You can optionally specify a line offset and limit (especially handy for long files), but it's recommended to read the whole file by not providing these parameters	u- When you already know which part of the file you need, only read that part. This can be important for larger files.	Glob	s- Fast file pattern matching tool that works with any codebase size
- Supports glob patterns like "**/*.js" or "src/**/*.ts"
- Returns matching file paths sorted by modification time
- Use this tool when you need to find files by name patterns
- When you are doing an open ended search that may require multiple rounds of globbing and grepping, use the Agent tool instead	ExitPlanMode	didStopImmediatePropagation	stopImmediatePropagation	READDIRP_RECURSIVE_ERROR	_watchWithNodeFs	_handleFile	_handleSymlink	_handleRead
_handleDir	_addToNodeFs	data	end	win32	watch		listeners	errHandlers	rawEmitters	getChildren	dispose
filterPath		filterDir	/	//	..	lstat	custom:			;	(B	isJetBrainsIdeTerminal	isMicrosoftWindowsTerminal		isGhostty	isMintty	.windowsConsoleSupportsVirtualTerminalSequences	hasGeometricShapesInkBleedBug	hasOsc52ClipboardUtf8Bug	'macCmdClickArrivesWithoutSgrModifierBit	b[Console]::InputEncoding = [Text.Encoding]::UTF8; Set-Clipboard -Value ([Console]::In.ReadToEnd())	E[Console]::OutputEncoding = [Text.Encoding]::UTF8; Get-Clipboard -Raw	cancel
onResponse	dark	insertChild	removeChild	getChild	getChildCount		getParent	free	freeRecursive		markDirty	isDirty	hasNewLayout	markLayoutSeen	setMeasureFunc	unsetMeasureFunc	getComputedLeft	getComputedTop	getComputedWidth	getComputedHeight	getComputedRight	getComputedBottom	getComputedLayout	getComputedBorder	getComputedPadding	getComputedMargin	setWidth	setWidthPercent	setWidthAuto		setHeight	setHeightPercent	setHeightAuto	setMinWidth	setMinWidthPercent	setMinHeight	setMinHeightPercent	setMaxWidth	setMaxWidthPercent	setMaxHeight	setMaxHeightPercent	setFlexDirection	setFlexGrow	setFlexShrink	setFlex	setFlexBasis	setFlexBasisPercent	setFlexBasisAuto	setFlexWrap	setAlignItems	setAlignSelf	setAlignContent	setJustifyContent
setDisplay
getDisplay	setPositionType	setPosition	setPositionPercent	setPositionAuto	setOverflow	setDirection	setBoxSizing		setMargin	setMarginPercent	setMarginAuto
setPadding	setPaddingPercent		setBorder	setGap	setGapPercent	getFlexDirection	getJustifyContent	getAlignItems	getAlignSelf	getAlignContent	getFlexGrow	getFlexShrink	getFlexBasis	getFlexWrap	getWidth		getHeight	getOverflow	getPositionType	getDirection		copyStyle	setDirtiedFunc	unsetDirtiedFunc	setIsReferenceBaseline	isReferenceBaseline	setAspectRatio	getAspectRatio	setAlwaysFormsContainingBlock	calculateLayout	none	K	]8;;09;m	\& 	resolveEventPriority	dispatch	dispatchDiscrete	dispatchContinuous	notify	focus	blur	handleNodeRemoved	pushAutoFocusFallback	handleAutoFocus	handleClickFocus		focusNext	focusPrevious	focusDirection		moveFocus	intern	needsCompaction
transition	withInverse	withCurrentMatch	setSelectionBg	withSelectionBg	compact	[1m	[2m	renderPreviousOutput_DEPRECATED	forceFullReset	renderFullFrame	getRenderOpsForDone	render	txn	blit	shift	noSelect	clip	unclip	](
	resetScreenReaderDiffState	hasStaleTerminalSize	syncTerminalSize	enterAlternateScreen	exitAlternateScreen	skipSyncMarkers	onRender	shouldSampleLiveCounts	onRenderScreenReader	computeScreenReaderPark	pause	resume	repaint	emitAtlasReset	maybeProactiveAtlasReset	proactiveAtlasResetOnFocus	forceRedraw	probeExternalClear	invalidatePrevFrame	setAltScreenActive	handoffAltScreen	handoffRawMode	getStylePool	getCharPool	getHyperlinkPool	detachForShutdown
drainStdin	reenterAltScreen	resetFramesForAltScreen	getSelectedText	copySelectionNoClear	copySelection	clearTextSelection	setSearchHighlight	scanElementSubtree	setSearchPositions	setSelectionBgColor	moveSelectionFocus	hasTextSelection	subscribeToSelectionChange	notifySelectionChange	dispatchClick	dispatchHover	dispatchPasteEvent	dispatchKeyboardEvent	getHyperlinkAt	openHyperlink	handleMultiClick	handleSelectionDrag	suspendStdin	resumeStdin	writeRaw	unmount	waitUntilExit	resetLineCount	maybeResetPools
resetPools	patchConsole	patchStderr
]104;255	processText	holdTail	processSequence@	toLocalPath		toIDEPath@0X	clipboard-image-hint
_iTerm2 ! Settings ! General ! Selection ! check "Applications in terminal may access clipboard"	/terminal.integrated.mouseWheelScrollSensitivity	#terminal.integrated.gpuAcceleration	off	paste-cache(
	fromText	getViewportStartLine	getViewportCharOffset	getViewportCharEnd	left	right	placeholderEndingAt	placeholderStartingAt	placeholderContaining	snapOutOfPlaceholder	up	down	startOfCurrentLine	startOfLine	firstNonBlankInLine		endOfLine	findLogicalLineStart	findLogicalLineEnd	getLogicalLineBounds	createCursorWithColumn	endOfLogicalLine	lastCharInLogicalLine	startOfLogicalLine	firstNonBlankInLogicalLine	upLogicalLine	downLogicalLine	nextWord	prevWord	nextVimWord	endOfVimWord	prevVimWord	nextWORD		endOfWORD	prevWORD
modifyText	insert	del		backspace	deleteToLineStart	deleteToLineEnd	deleteToLogicalLineEnd	deleteWordBefore	deleteTokenBefore	deleteWordAfter
graphemeAt	isOverWhitespace	equals		isAtStart	isAtEnd	startOfFirstLine	startOfLastLine	goToLine		endOfFile	getPosition		getOffset	findCharacter	getGraphemeBoundaries	getWordBoundaries	binarySearchBoundary	stringIndexToDisplayWidth	displayWidthToStringIndex	offsetAtDisplayWidth	measureWrappedText	getWrappedText	getWrappedLines	getLine	getOffsetFromPosition	getLineLength	getPositionFromOffset		withCache
nextOffset
prevOffset	snapToGraphemeBoundary	G\[(?:Pasted text|Image|\.\.\.Truncated text) #\d+(?: \+\d+ lines)?\.*\]	 %%%%%%%%ffffff??333333?	segment		segmentTo333333?
state.json	starting& 	send a prompt to start	claude-in-chrome	ClaudeInChromeDomain	Write	builtin	claude-plugin-telemetry-v1	custom	third-party	inline
skills-dir	claude-plugins-official	handleGreeting	handleUserPassword	handleConnectionRequest	listen	setAuthHandler	disableAuthHandler	setRulesetValidator	disableRulesetValidator	setConnectionHandler	useDefaultConnectionHandler	_handleConnection	register
lookupReal	entries	substituteInHeaders	substituteInString	fake_value_	sandbox-runtime-net	addViolation	getViolations	getCount	getTotalCount	getViolationsForCommand	notifyListenersA	finish	fork	join	tag	raw	uint32	int32	bool	bytes	float	double	fixed32	sfixed32	sint32	sfixed64	fixed64	int64	sint64	uint64	skip	assertBoundsGA
findNumber		oneofCase	isSet	set
getUnknown
setUnknown'		_+_	_/_	_==_	_>_	_>=_	@in	_<_	_<=_	!_	_%_	_*_	-_	_!=_	_-_ʚ;A:	contains	matches	size	getDate	getDayOfMonth	getDayOfWeek	getDayOfYear	getFullYear	getHours	getMilliseconds
getMinutes	getMonth
getSeconds	WebFetch
- Fetches content from a specified URL and processes it using an AI model
- Takes a URL and a prompt as input
- Fetches the URL content, converts HTML to markdown
- Processes the content with the prompt using a small, fast model
- Returns the model's response about the content
- Use this tool when you need to retrieve and analyze web content

Usage notes:
  - IMPORTANT: If an MCP-provided web fetch tool is available, prefer using that tool instead of this one, as it may have fewer restrictions.
  - The URL must be a fully-formed valid URL
  - HTTP URLs will be automatically upgraded to HTTPS
  - The prompt should describe what information you want to extract from the page
  - This tool is read-only and does not modify any files
  - Results may be summarized if the content is very large
  - Includes a self-cleaning 15-minute cache for faster responses when repeatedly accessing the same URL
  - When a URL redirects to a different host, the tool will inform you and provide the redirect URL in a special format. You should then make a new WebFetch request with the redirect URL to fetch the content.
  - For GitHub URLs, prefer using the gh CLI via Bash instead (e.g., gh pr view, gh issue view, gh api).
	ripgrep not found on PATH. Install it (brew install ripgrep / apt install ripgrep / winget install BurntSushi.ripgrep.MSVC) or use the native claude binary which embeds it.-1	__CMDSUB_OUTPUT__	__TRACKED_VAR__	plugins	cowork_plugins{Gz?OA# Autonomous loop check

You're being invoked on a timer while the user is away or occupied. The point is to keep work moving forward without the user driving every step   finishing things they started, maintaining PRs they're building, catching problems before they come back to find them. You're a steward, not an initiator. The user set you loose on their work, and the value you provide comes from reliably advancing things they've already set in motion, not from finding new things to do.

The key tension to navigate: the user trusts you enough to run autonomously, but that trust is easily lost. Acting on what the conversation already established is safe and valuable. Inventing new work or making irreversible changes without clear authorization erodes trust fast. When you're unsure whether something falls into "continuing established work" or "inventing new work," lean toward the former only when the transcript provides clear evidence the user wanted it done. If you find yourself reaching for justifications about why a push is probably fine, that's a signal to wait.

## What to act on

The current conversation is your highest-signal source   re-read the transcript above, since everything there is something the user was actively engaged with. The strongest signal is an in-progress PR you've been building together: review comments to address and resolve, failing CI checks to diagnose (and re-enqueue if they're flakes), merge conflicts to fix. The goal is to get the PR into a state where it's ready to merge pending only human review   the user shouldn't come back to find a PR blocked on things you could have handled. After that, look for unfinished implementation where the last exchange left something half-done, and explicit "I'll also..." or "next I'll..." commitments the conversation made and didn't honor. Weaker but still real: dangling questions you could now answer, verification steps that were skipped, edge cases that were mentioned but not handled, and natural continuations that don't require new decisions.

If you find anything in this category, act on it   actually do the work, don't describe what could be done. Run the tests, don't say "you could run the tests." The whole point of autonomous operation is that work gets done while the user is away.

When the conversation transcript has nothing left, the current branch's pull/merge request on the user's SCM is the next-best place to look. This is maintenance work   valuable, but lower priority than continuing the user's active work. Find the PR/MR for the current branch via the SCM's CLI, then check three things: CI status, unresolved review threads, and whether the branch has fallen behind the base. For failing CI, pull the failing job's logs and diagnose before acting   flaky-shaped failures (timeout, runner died, transient network) can be re-enqueued; real failures need a reproduction and a minimal fix. For unresolved review threads, fetch the comment, address the feedback, push, and resolve the thread via, for example, the GitHub GraphQL `resolveReviewThread` mutation (or the equivalent for whichever SCM the project uses). Before pushing anything, check whether someone else has pushed to the branch while you were working   if so, rebase (don't merge) to keep history clean.

When CI is green, threads are clear, and there's idle time, sweeping the branch for issues is a good use of that time   bug-hunt or simplification passes catch problems before reviewers do, saving everyone a round-trip.

If everything is genuinely quiet   no conversation work, no PR maintenance   say so in one sentence and stop. No summary of what you checked, no list of what you might do later. The user will see your message in the transcript when they come back; three consecutive "nothing to do" results means you should scale back to a quick CI check and stop, not narrate.

## Repeated invocations

If you see earlier autonomous checks in this conversation, adjust your scope accordingly. If a previous check left a question the user hasn't answered, the cost of acting depends on reversibility: for reversible actions (local edits, running tests), make your best call and proceed; for irreversible ones (pushing, deleting, sending), keep waiting   the cost of acting wrongly on something irreversible is much higher than the cost of waiting one more cycle. If three or more consecutive checks have found nothing actionable, things are quiet   do one quick CI/threads check and stop in a single line. Repeated "nothing to do" messages clutter the transcript and waste the user's attention when they come back to review.

Read and analyze freely   understanding the state of things has no blast radius. Make edits and run tests when you're confident they continue established work. Commit and
```
