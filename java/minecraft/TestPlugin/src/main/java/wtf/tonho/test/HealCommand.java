package wtf.tonho.test;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;

public class HealCommand implements CommandExecutor {

    @Override
    public boolean onCommand(@NotNull CommandSender commandSender, @NotNull Command command, @NotNull String s, @NotNull String @NotNull [] strings) {

       if (commandSender instanceof Player){
        Player player = (Player) commandSender;
        player.sendMessage("Health restored");
        player.setHealth(20);

       }

        return false;
    }
}
