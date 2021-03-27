. build/envsetup.sh
export USE_CCACHE=1 && ccache -M 50G && export CONFIG_STATE_NOTIFIER=y 
lunch octavi_X00TD-user
export SKIP_ABI_CHECKS=true && export SKIP_API_CHECKS=true
brunch X00TD