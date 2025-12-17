n=12
m=$(echo "$n-1"|bc)
q="index 0 to 11"
xyz1=$1
xyz2=$2

#write VMD input
echo "
mol new \"$2\"
mol new \"$1\"

set sel0 [atomselect 0 \"$q\"]
set sel0_ [atomselect 0 \"all\"]
set sel1 [atomselect 1 \"$q\"]
set M [measure fit \$sel0 \$sel1]
\$sel0_ move \$M

\$sel0_ writepdb \"tmp.pdb\"
quit
" > tmp.vmd

#run VMD
vmd -e tmp.vmd -dispdev text $> /dev/null
rm tmp.vmd

#convert with obabel
obabel -ipdb tmp.pdb -oxyz -O $2
rm tmp.pdb
