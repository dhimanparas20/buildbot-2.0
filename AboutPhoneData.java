package com.android.settings;

public class AboutPhoneData {
    int index;
    String codename = "Unknown";
    String cpu;
    String soc;
    String battery;
    String display;
    String camera;
    int img;

    public AboutPhoneData(int index) {
        this.index = index;
    }

    public AboutPhoneData(int index, String codename, String cpu, String soc, String battery, String display, String camera, int img) {
        this.index = index;
        this.codename = codename;
        this.cpu = cpu;
        this.soc = soc;
        this.battery = battery;
        this.display = display;
        this.camera = camera;
        this.img = img;
    }

    public int getIndex() {
        return index;
    }

    public String getCodename() {
        return getIndex() == 0 ? "X00TD" : codename;
    }

    public String getCpu() {
        return getIndex() == 0 ? "4x 1.8 GHz Kryo 260, 4x 1.6 GHz Kryo 260" : cpu;
    }

    public String getSoc() {
        return getIndex() == 0 ? "Snapdragon 636" : soc;
    }

    public String getBattery() {
        return getIndex() == 0 ? "5000" : battery + " mAh";
    }

    public String getDisplay() {
        return getIndex() == 0 ? "2160 x 1080, 5.99 inches" : display;
    }

    public String getCamera() {
        return getIndex() == 0 ? "13MP + 5MP + 8MP" : camera;
    }

    public int getImg() {
        return getIndex() == 0 ? R.drawable.x00td  : img;
    }
}
