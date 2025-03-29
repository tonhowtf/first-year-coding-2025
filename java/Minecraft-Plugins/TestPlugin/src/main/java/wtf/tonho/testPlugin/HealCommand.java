package wtf.tonho.testPlugin;

import org.bukkit.Sound;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class HealCommand implements CommandExecutor {


    @Override
    public boolean onCommand(CommandSender commandSender, Command command, String s, String[] strings) {

        if (commandSender instanceof Player) {
            Player p = (Player) commandSender;
            p.sendMessage("Healed");
            p.setHealth(20);
            p.playSound(p.getLocation(), Sound.ENTITY_CREEPER_PRIMED, 1.0f, 1.0f);

        }

        return false;
    }
}
