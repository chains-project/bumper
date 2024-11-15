```java
import develop.p2p.lib.WaveCreator;
import develop.p2p.lib.WaveCreator.WaveCreatorException;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.entity.Player;

import ml.peya.plugins.Peya;
import ml.peya.plugins.Utils;
import ml.peya.plugins.Utils.PlayerInfo;
import ml.peya.plugins.Utils.UtilsException;
import ml.peya.plugins.Utils.UtilsException.UtilsExceptionType;
import ml.peya.plugins.Objects.Decorations;

public class Decorations
{
    public static void spawnRandomDecoration(Player player)
            throws Decorations.DecorationsException, UtilsException, WaveCreatorException, IOException
    {
        FileConfiguration config = Peya.getInstance().getConfig();
        File dataFolder = Peya.getInstance().getDataFolder();
        PlayerInfo playerInfo = Utils.getPlayerInfo(player);

        List<String> list = new ArrayList<>();
        for (String key : config.getConfigurationSection("decorations").getKeys(false))
        {
            if (playerInfo.getDecorationTime(key) < System.currentTimeMillis())
            {
                list.add(key);
            }
        }

        if (list.isEmpty())
        {
            return;
        }

        String decorationName = list.get(new Random().nextInt(list.size()));
        File decorationFile = new File(dataFolder, "decorations/" + decorationName + ".wav");
        if (!decorationFile.exists())
        {
            throw new DecorationsException("Decoration file does not exist: " + decorationFile.getAbsolutePath());
        }

        byte[] data = Files.readAllBytes(Paths.get(decorationFile.getAbsolutePath()));
        WaveCreator waveCreator = new WaveCreator(data);
        waveCreator.play(player);

        playerInfo.setDecorationTime(decorationName, System.currentTimeMillis() + config.getInt("decorations." + decorationName + ".cooldown") * 1000);
        Utils.savePlayerInfo(playerInfo);
    }

    public static class DecorationsException extends Exception
    {
        public DecorationsException(String message)
        {
            super(message);
        }
    }
}
```