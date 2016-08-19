readPassword () {
  echo Ssh Password: 
  read -s SSHPASS
  eval "export SSHPASS='""$SSHPASS""'"
}

# read password

readPassword

# declare list of storms as array
declare -a directories=("OS1_Exit_0005_005" "OS1_Exit_0005_006" "OS1_Exit_0005_007" "OS1_Exit_0005_008")
declare -a files=("DIRatmaxele.63" "fort.13" "fort.14" "fort.15" "fort.16" "fort.22" "fort.221" "fort.222" "fort.223" "fort.224" "fort.26" "fort.61" "fort.67" "fort.80" "HSatmaxele.63" "maxele450sec.63" "maxele450sec_index.63" "maxele.63" "maxrs.63" "maxvel.63" "maxwvel.63" "minpr.63" "swan_DIR_max.63" "swan_HS_max.63" "swan_TMM10_max.63" "swan_TPS_max.63" "swaninit" "TMM10atmaxele.63" "TPSatmaxele.63")
declare remote_root="dorvinen@login1.corral.tacc.utexas.edu:/gpfs/corral3/repl/projects/RIVAECOM/wfl/Prod/runsv8/trop"
for dir in "${directories[@]}"
do
  # create directory variables	
  remote_dir="$remote_root/$dir"
  local_dir="/media/sf_P_DRIVE/04/QC/Tropical/$dir"
  # check if local_dir exists and create it if not
  if [ ! -d "$local_dir" ]; then 
    mkdir $local_dir
  fi	

	for filed in "${files[@]}"
	do
    remote_file="$remote_dir/$filed"
    local_file="$local_dir/$file"
    echo "copying $remote_file to $local_file"
    sshpass -e  scp $remote_file $local_file
	done
done
