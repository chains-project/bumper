# First, clone the BUMP repository
echo "Setting up benchmarks..."
for directory in ./benchmarks/* ; do
    cd $directory
    echo "----------- $(basename $directory) -----------"
    sh "setup.sh"
    cd $OLDPWD
done
echo "Benchmarks setup completed."
