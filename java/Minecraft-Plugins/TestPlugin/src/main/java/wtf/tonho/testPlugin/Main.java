package wtf.tonho.testPlugin;

import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {

    @Override
    public void onEnable() {
        getCommand("test").setExecutor(new TestCommand());
    }
}