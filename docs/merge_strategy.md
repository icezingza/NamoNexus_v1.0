# Merge Strategy

This Codex deployment branch retains Codex changes when merging from main.

## Automated merge helper

Use `auto_phase5_merge_resolver.py` to fetch and merge with the ours strategy:

```
python3 auto_phase5_merge_resolver.py \
  --remote origin \
  --target-branch codex/create-namonexus-v1.0-deploy \
  --main-ref origin/main
```

If the remote or branch is missing locally, the script will explain how to add or fetch it before retrying.
