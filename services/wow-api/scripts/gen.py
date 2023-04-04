from subprocess import run as run_sh

run_sh(
    [
        "datamodel-codegen",
        "--input",
        "./in/raw.json",
        "--input-file-type",
        "json",
        "--output",
        "./out/leaderboard_models.py",
    ]
)
