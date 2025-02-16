package wtf.tonho.test;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;

public class ConfigCommand implements CommandExecutor {

    private Main main;

    public ConfigCommand(Main main) {
        this.main = main;
    }

    @Override
    public boolean onCommand(@NotNull CommandSender commandSender, @NotNull Command command, @NotNull String s, @NotNull String @NotNull [] strings) {

        if (commandSender instanceof Player){
            Player player = (Player) commandSender;

            player.sendMessage(main.getConfig().getString("Word"));
            player.sendMessage(main.getConfig().getInt("Number") + "");
        }

        return false;
    }
}
