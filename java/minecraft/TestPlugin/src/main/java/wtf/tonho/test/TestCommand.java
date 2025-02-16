package wtf.tonho.test;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;

public class TestCommand implements CommandExecutor {


    @Override
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String s, @NotNull String @NotNull [] args) {

        if (sender instanceof Player){
            ((Player) sender).sendMessage("No, this is console only!");

        }else {
            System.out.println("Hello, console");
        }


        return false;
    }
}
