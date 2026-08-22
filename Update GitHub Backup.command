#!/bin/zsh
set -euo pipefail
script_dir="${0:A:h}"
"$script_dir/update.sh" --push
print "GitHub backup completed. Press Return to close this window."
read -r
