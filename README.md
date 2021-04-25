# BuildBot
> does everything for me

So this script basically saves alot of time . It can sync rom repo , sync device trees , compile rom and upload it to gd or sf and alot more ....

## BAnner
<p align="center">
<img src="https://github.com/dhimanparas20/buildbot/blob/main/mst.jpg" />

## Files to edit 
So to make this script is compatible with your environment , you need to do some basic python editing 
> 1: AboutPhoneData.java (only edit this if you are making octavi os )

> 2: romname.sh (edit the name and build commands according your needs and environment )

> 3: compile.py (just replace romname.sh with yours and server name , incase mine is "mst" )

> 4: go.py (the main script , you must have good python knowledge to edit this )

> 5: octavi.py (only edit this if you have acess to private trees , rename the device image in drawables )

> 6: sync.py (edit rom names , sync and init commands and tree links )

> 7: up.py (dit sf project name , also to upload in gd , you must configur rclone beforehand )

## Installation and Running 

Linux:


```sh
cd && git clone https://github.com/dhimanparas20/buildbot.git 
```

```sh
cd buildbot && chmod +x *  && clear && ls
```

```sh
./run.sh
```

## Notes
Dont use this script if you hav 0 knowldge about python and bash .

Dont be a gey by copying or cloning this repo and calling it yours .

If you liked the script or need any kind of help , ping me up  https://t.me/ken_kaneki_69

Im not responsible for any of your data losses , do it at your own will .


