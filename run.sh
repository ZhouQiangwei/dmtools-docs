awk '{for (i=1; i<=NF; i++) {if (i==1) printf "``%s`` ", $i; else printf "%s ", $i}; printf "\n\n"}' ts
