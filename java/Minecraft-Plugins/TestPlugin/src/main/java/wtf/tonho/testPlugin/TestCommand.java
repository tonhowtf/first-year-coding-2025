package wtf.tonho.testPlugin;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.command.ConsoleCommandSender;
import org.bukkit.entity.Player;

public class TestCommand implements CommandExecutor {


    @Override
    public boolean onCommand(CommandSender commandSender, Command command, String s, String[] strings) {

        if (commandSender instanceof Player) {
            Player player = (Player) commandSender;

            if (player.hasPermission("testplugin.use")) {
                player.sendMessage(ChatColor.GREEN + "Você tem permissão de usar o comando.");
            } else {
                player.sendMessage(ChatColor.RED + "Você não tem permissão de usar o comando.");
            }


        }

        return false;
    }
}
