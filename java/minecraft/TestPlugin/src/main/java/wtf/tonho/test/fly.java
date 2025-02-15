package wtf.tonho.test;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.command.ConsoleCommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;


public class fly implements CommandExecutor {

    @Override
    public boolean onCommand(@NotNull CommandSender commandSender, @NotNull Command command, @NotNull String s, @NotNull String @NotNull [] strings) {

        if (commandSender instanceof Player) {
            Player player = (Player) commandSender;


            if(player.getAllowFlight()){
                player.setAllowFlight(false);
                if(player.isFlying()){
                    player.setFlying(false);
                }
                player.sendMessage(ChatColor.RED + "Fly off");
            }else {
                player.setAllowFlight(true);
                player.sendMessage(ChatColor.GREEN + "Fly ativado!");
            }
            return true;
        }else {
            commandSender.sendMessage("Comando apenas para jogadores.");
        }

        return false;
    }
}
