LINK AL DRIVE PER SCARICARE L'AMBIENTE: https://drive.google.com/drive/folders/1YWj5z3cft7d9lK7pebf1Br87ITgrRQlM

Per installare la VM su Mac M1/M2/M3:

Scaricate lo ZIP con la VM compressa di VmWare Fusion
Scompattatelo nella directory ~/Virtual Machines
Fatela partire cliccando sul file .vmx
Rispondete “Spostata” se vi viene chiesto se è stata copiata o spostata
Come condividere una directory del PC con la macchina virtuale
Entrate come Administrator (password “password”)
Create la directory /mnt/hgfs
sudo mkdir -p /mnt/hgfs
Spegnete la VM con “Spegni” (senza salvare lo stato corrente)
Aprite la configurazione della macchina ed aggiugete all’elenco delle directory condivise, quelle che volete che le siano accessibili
Se non volete che la macchina possa modificare i file in una directory, configuratela come read-only
Fate ripartire la macchina, troverete le directory condivise nella directory /mnt/h
