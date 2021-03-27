cd && cd oos
rm -rf frameworks/base && rm -rf packages/apps/Settings && rm -rf packages/apps/OctaviLab && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/frameworks_base.git frameworks/base && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_Settings.git packages/apps/Settings && git clone -b 2.1 https://github.com/Octavi-Broken-Lab/android_packages_apps_OctaviLab.git packages/apps/OctaviLab
cd packages/apps/Settings/res/drawable/
cp ic_device_x00td.png x00td.png
cd && cd oos
cd packages/apps/Settings/src/com/android/settings/
rm -rf AboutPhoneData.java
wget https://raw.githubusercontent.com/dhimanparas20/Octavi_AboutPhone/main/AboutPhoneData.java
cd && cd oos
