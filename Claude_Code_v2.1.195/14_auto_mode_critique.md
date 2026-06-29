# 14 Auto Mode Critique

> Claude Code v2.1.195 — extracted from claude.exe

```
critique the user's custom rules for clarity, completeness, and potential issues. The classifier is an LLM that reads these rules as part of its system prompt.

For each rule, evaluate:
1. **Clarity**: Is the rule unambiguous? Could the classifier misinterpret it?
2. **Completeness**: Are there gaps or edge cases the rule doesn't cover?
3. **Conflicts**: Do any of the rules conflict with each other?
4. **Actionability**: Is the rule specific enough for the classifier to act on?

Be concise and constructive. Only comment on rules that could be improved. If all rules look good, say so.	$5f3a2c5e-6b8f-4b27-9c0e-2d7f1a9b3c44	&/home/claude/.claude/remote/spare.sock	updateConfig	(Usage: claude daemon [subcommand] [options]

Service lifecycle:
  run [json-path]   Run the supervisor in the foreground (default when piped)
  status            Show daemon pid, version, uptime
  logs              Tail the daemon log (Ctrl-C to stop)
  uninstall         Remove the background service (launchctl/systemd)
  stop              Shut down the supervisor and terminate background sessions
                      --any           also stop a transient (non-service) daemon
                      --keep-workers  leave detached sessions running
	  install           Install as a launchctl/systemd service (persists across reboot)
  start             Start the installed service
  restart           Restart the installed service
y
  Service install is disabled in this version   the daemon runs on demand
  and exits when the last client disconnects.

Options:
  --json-path <p>   Config file (default: ~/.claude/daemon.json)
  --log-file <p>    Log file (default: ~/.claude/daemon.log)
  --help, -h        Show this help
```
