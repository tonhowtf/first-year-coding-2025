package wtf.tonho.testPlugin;

import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {

    @Override
    public void onEnable() {
        getCommand("arena").setExecutor(new ArenaCommand());
        getLogger().info("Arena ativado.com");
    }
}


