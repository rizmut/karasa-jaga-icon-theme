#!/bin/sh

set -e

gh_repo="karasa-jaga-icon-theme"
gh_desc="Karasa Jaga icon theme"

cat <<- EOF

  $gh_desc
  https://github.com/rizmut/$gh_repo
  
  
EOF

echo "=> Removing $gh_desc ..."
sudo rm -Rf "/usr/share/icons/Karasa-Jaga"
echo "=> Done!"
