import subprocess
import sys
from pathlib import Path

default_target = Path(__file__).parent
targets = []
options = []

for arg in sys.argv[1:] if len(sys.argv) > 1 else []:
    if arg.startswith("-"):
        options.append(arg)
    else:
        if not Path(arg).exists() and (default_target / arg).exists():
            arg = str(default_target / arg)
        targets.append(arg)


process = subprocess.run(
    [
        "pytest",
        "--no-cov",
        "--timeout=180",
        # TODO: These should be overridable
        "--benchmark-group-by=func",
        "--benchmark-columns=mean,stddev,min,max,rounds",
        "--benchmark-sort=mean",
        "--benchmark-min-rounds=1",
        # Ignore benchmark machine info warnings that occur due to different CI runner CPU frequencies
        # see https://github.com/ionelmc/pytest-benchmark/issues/255
        "-W",
        "ignore::pytest_benchmark.logger.PytestBenchmarkWarning",
    ]
    + (targets or [default_target])
    + options,
    stdout=sys.stdout,
    stderr=sys.stderr,
)


sys.exit(process.returncode)
