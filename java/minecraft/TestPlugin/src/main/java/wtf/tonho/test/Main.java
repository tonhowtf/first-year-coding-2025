package wtf.tonho.test;

import org.bukkit.plugin.java.JavaPlugin;


public final class Main extends JavaPlugin {


    @Override
    public void onEnable(){

        getConfig().options().copyDefaults();
        saveDefaultConfig();


        getCommand("config").setExecutor(new ConfigCommand(this));
    }
}
