#!/bin/zsh
set -euo pipefail
script_dir="${0:A:h}"
"$script_dir/publish.sh"
print "GitHub publication completed. Press Return to close this window."
read -r
