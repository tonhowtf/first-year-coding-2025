package wtf.tonho.testPlugin;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class ConfigCommand implements CommandExecutor {

    private Main main;

    public ConfigCommand(Main main){
        this.main = main;
    }


    @Override
    public boolean onCommand(CommandSender commandSender, Command command, String s, String[] strings) {

        if (commandSender instanceof Player) {
            Player player = (Player) commandSender;

            player.sendMessage(main.getConfig().getString("Word"));
            player.sendMessage(main.getConfig().getInt("Number") + "");
            if (main.getConfig().getBoolean("Boolean")) {
                player.sendMessage("Já tá habilitada paizão");
            }
            for (String string : main.getConfig().getStringList("String-list")) {
                player.sendMessage(string);
            }
        }


        return false;
    }
}
