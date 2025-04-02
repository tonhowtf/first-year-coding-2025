package wtf.tonho.testPlugin;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class ArenaCommand implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender commandSender, Command command, String s, String[] strings) {

        if (!(commandSender instanceof Player)) {
            commandSender.sendMessage("Apenas instancias de player podem fazer uma arena, zé.");
            return false;
        }

        Player player = (Player) commandSender;

        if (strings.length != 3) {
            player.sendMessage("São necessários 3 argumentos: <largura> <comprimento> <altura>");
            return false;
        }

        int width, length, height;

        try {
            width = Integer.parseInt(strings[0]);
            length = Integer.parseInt(strings[1]);
            height = Integer.parseInt(strings[2]);
        } catch (NumberFormatException e) {
            player.sendMessage("Apenas números inteiros.");
            return false;
        }

        if (width < 2 || length < 2 || height < 1) {
            player.sendMessage("Largura e comprimento precisam ser maior do que 2 e altura precisa ser maior do que 0 ");
            return false;
        }

        Location playerLoc = player.getLocation();

        int startX = playerLoc.getBlockX() - (width / 2);
        int startY = playerLoc.getBlockY();
        int startZ = playerLoc.getBlockZ() - (length / 2);

        createArena(player.getWorld(), startX, startY, startZ, width, length, height);

        player.sendMessage("Arena criada?");
        return true;
    }

    private void createArena(org.bukkit.World world, int startX, int startY, int startZ, int width, int length, int height) {

        for (int x = 0; x < width; x++) {
            for (int z = 0; z < length; z++) {
                world.getBlockAt(startX + x, startY, startZ + z).setType(Material.GLOWSTONE);

            }
        }

        for (int y = 1; y < height; y++) {
            for (int x = 0; x < width; x++) {
                world.getBlockAt(startX + x, startY + y, startZ).setType(Material.GLOWSTONE);
                world.getBlockAt(startX + x, startY + y, startZ + length - 1).setType(Material.GLOWSTONE);
            }

            for (int z = 0; z < length; z++) {
                world.getBlockAt(startX, startY + y, startZ + z).setType(Material.GLOWSTONE);
                world.getBlockAt(startX + width - 1, startY + y, startZ + z).setType(Material.GLOWSTONE);
            }
        }

        for (int x = 0; x < width; x++) {
            for (int z = 0; z < length; z++) {
                world.getBlockAt(startX + x, startY + height, startZ + z).setType(Material.GLOWSTONE);
            }
        }

    }
}
