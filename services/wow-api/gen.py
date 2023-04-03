from subprocess import run as run_sh

run_sh(
    [
        "datamodel-codegen",
        "--input",
        "./data/key-leaderboard.json",
        "--input-file-type",
        "json",
        "--output",
        "key_models.py",
    ]
)
