# Vendoring

The plugin bundles a self-contained copy of the `prompt_decorators` Python
engine and its JSON decorator registry under `vendor/`. Bundling (rather
than depending on `pip install prompt-decorators` at hook runtime) avoids
cold-start latency, pip/network requirements, and Python-env surprises on
the user's machine.

```
vendor/
└── prompt_decorators/
    ├── core/
    ├── registry/        <- 143 decorator JSON files
    ├── schemas/
    ├── utils/
    └── ...              <- the rest of the upstream package
```

## Sync command

From the repository root:

```bash
# Wipe the vendored tree and copy the upstream engine + registry back in.
rm -rf claude-code-plugin/vendor/prompt_decorators
cp -r prompt_decorators claude-code-plugin/vendor/prompt_decorators

# Strip bytecode that sometimes leaks from editable installs.
find claude-code-plugin/vendor -type d -name __pycache__ -exec rm -rf {} +
find claude-code-plugin/vendor -type f -name '*.pyc' -delete
```

Then run the plugin tests to confirm nothing upstream changed in a way the
plugin's expectations can't absorb:

```bash
cd claude-code-plugin && python3 -m pytest tests/
```

## When to sync

- **Before every plugin release** (when bumping `version` in
  `.claude-plugin/plugin.json`).
- **Whenever `prompt_decorators/core/dynamic_decorator.py` or the registry
  JSONs change in a way that affects parsing, expansion, or decorator
  availability.**
- **After a security fix in the upstream engine.**

## Drift check

A quick way to see whether the vendored tree has drifted from the
source-of-truth package:

```bash
diff -rq prompt_decorators claude-code-plugin/vendor/prompt_decorators
```

The only expected difference is `__pycache__/` entries (never committed).
If any `.py` or `.json` file differs, the vendor needs to be re-synced.

## Local patches applied to `vendor/`

A straight `cp -r` from upstream would revert these local fixes. When
syncing, re-apply each one (or better, land them upstream and then sync):

- **`core/dynamic_decorator.py`** — parameter-value numeric parsing uses
  `int()` / `float()` with try/except instead of `str.isdigit()` /
  `str.replace(".", "", 1).isdigit()`. The upstream check rejects
  negatives and scientific notation (`+++Dec(x=-5)` parsed as the string
  `"-5"`). The local version delegates to Python's own numeric parsers.
  Covered by `tests/test_pd_common.py::test_numeric_parameter_values_parsed`
  and `::test_parse_decorator_negative_number_direct`. Should land
  upstream as a bug fix.

After each sync, run `cd claude-code-plugin && python3 -m pytest tests/`
and check that every listed test still passes. Any failure means a
local patch was reverted.

## Why not a submodule / editable install

- **Submodule:** adds an extra `git submodule update --init` step to plugin
  installation, which the Claude Code marketplace doesn't run.
- **Editable install (`pip install -e ..`):** requires `pip` to be
  available at hook runtime, which is not guaranteed for end users who
  only installed the plugin.

The maintenance cost is small (a copy + a test run, see above) and the
end-user experience is a clean, self-contained plugin.
