---
phase: 01-ambiente-y-diagnostico
plan: 02
subsystem: infra
tags: [python, nxt, yolo, diagnostics, windows-venv, day1]
one-liner: "Reproducible Day 1 diagnostics with package checks, editable NXT hardware profile, JSON/Markdown reports, and a working project-local .venv"
requires:
  - phase: 01
    provides: repo scaffold, planning files, classroom docs
provides:
  - dependency doctor command for Day 1
  - NXT motor and sensor diagnostics with dry-run/live modes
  - editable hardware profile in JSON
  - generated Day 1 reports from a working local virtual environment
affects: [phase-1, diagnostics, hardware-bringup]
tech-stack:
  added: [ultralytics, nxt-python, opencv-python, numpy, pyusb]
  patterns: [argparse-cli, report-generation, config-driven-hardware-diagnostics, windows-python-venv-fallback]
key-files:
  created:
    - config/hardware.example.json
    - reports/day1-dry-run-venv.md
    - reports/day1-dry-run-venv.json
  modified:
    - main.py
    - requirements.txt
    - README.md
    - .planning/phases/01-ambiente-y-diagnostico/01-VERIFICATION.md
key-decisions:
  - "Make pyusb a required dependency because USB is the primary NXT path for Day 1."
  - "Use a project-local Windows .venv because the WSL Python on this machine lacks pip and venv."
  - "Keep dry-run mode as a first-class path so diagnostics stay usable without hardware attached."
patterns-established:
  - "Run project diagnostics through .venv/Scripts/python.exe on this machine."
  - "Environment verification and hardware verification are separated but share the same report format."
requirements-completed: [ENV-02, ENV-03]
duration: backfilled
completed: 2026-03-16
---

# Phase 1: Ambiente y diagnostico base Summary

**Reproducible Day 1 diagnostics with package checks, editable NXT hardware profile, JSON/Markdown reports, and a working project-local .venv**

## Performance

- **Duration:** backfilled from implementation plus environment bring-up
- **Started:** not tracked
- **Completed:** 2026-03-16T22:59:21Z
- **Tasks:** 4
- **Files modified:** 6

## Accomplishments
- Implemented `main.py doctor` to verify Python and all key Day 1 packages.
- Implemented configurable Day 1 NXT diagnostics in `robot.py`, including dry-run and live paths plus per-port motor/sensor checks.
- Declared and installed the full Day 1 dependency set into a project-local `.venv`, including `pyusb` for the USB NXT path.
- Generated reusable Day 1 dry-run reports in Markdown and JSON from the working local environment.

## Task Commits

Each task was completed in the working tree and then summarized here:

1. **Task 1: Implement dependency doctor command** - `working-tree` (backfilled)
2. **Task 2: Implement NXT diagnostics and hardware profile** - `working-tree` (backfilled)
3. **Task 3: Finalize package set and local environment bootstrap** - `working-tree` (backfilled)
4. **Task 4: Verify dry-run report generation in .venv** - `working-tree` (backfilled)

**Plan metadata:** `working-tree` (docs: recorded 01-02 completion)

## Files Created/Modified
- `main.py` - CLI with `doctor` and `day1` commands plus report generation.
- `robot.py` - NXT connection helpers, motor/sensor diagnostics, and hardware profile loading.
- `config/hardware.example.json` - Editable mapping for motors and sensors by port.
- `requirements.txt` - Declares Day 1 packages including `pyusb`.
- `README.md` - Documents the Windows `.venv` fallback that works on this machine.
- `reports/day1-dry-run-venv.md` - Verified Day 1 diagnostic report from the local `.venv`.
- `reports/day1-dry-run-venv.json` - Machine-readable Day 1 diagnostic output from the local `.venv`.

## Decisions Made
- Promoted `pyusb` to a required dependency because the guide recommends USB as the primary NXT connection path.
- Used `python.exe -m venv .venv` because the Linux Python environment on this machine cannot create or populate a virtual environment.
- Kept hardware verification pending rather than faking a live run without the brick connected.

## Deviations from Plan

### Auto-fixed Issues

**1. Environment bootstrap mismatch**
- **Found during:** Task 3 (local environment bootstrap)
- **Issue:** The host WSL Python lacks both `venv` and `pip`, so the documented Linux bootstrap path could not work here.
- **Fix:** Created `.venv` with `python.exe`, installed requirements there, and updated the README to document the fallback.
- **Files modified:** `README.md`, `requirements.txt`
- **Verification:** `./.venv/Scripts/python.exe main.py doctor` passed with all required packages installed.
- **Committed in:** `working-tree` (backfilled)

---

**Total deviations:** 1 auto-fixed (environment bootstrap mismatch)
**Impact on plan:** The workaround preserved the plan goal and produced a reproducible local environment without changing scope.

## Issues Encountered

- The Linux Python environment could not be used for package installation on this machine because it lacks `pip` and `venv`.

## User Setup Required

Manual hardware confirmation is still required:
- Connect the NXT brick over USB
- Run `nxt-test`
- Run `./.venv/Scripts/python.exe main.py day1 --config config/hardware.example.json --report reports/day1-live.md --json reports/day1-live.json`
- Fill `docs/checklists/day1.md` and `docs/bitacora.md`

## Next Phase Readiness

- Phase 1 now has both execution plans recorded and a working local environment for Day 1 diagnostics.
- The remaining gap before full Phase 1 sign-off is physical NXT verification in the lab.
- Phase 2 can begin once the team is ready to document the SCARA layout and D-H preliminar.

---
*Phase: 01-ambiente-y-diagnostico*
*Completed: 2026-03-16*

