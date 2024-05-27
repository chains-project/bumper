```java
import develop.p2p.lib.*;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class NPCTeleport {

    public static void main(String[] args) {
        try {
            Class<?> clazz = Class.forName("develop.p2p.lib.P2P");
            Method method = clazz.getMethod("getInstance");
            Object instance = method.invoke(null);
            Method method2 = clazz.getMethod("getOnlinePlayers");
            List<?> players = (List<?>) method2.invoke(instance);
            List<String> names = new ArrayList<>();
            for (Object player : players) {
                Field field = player.getClass().getDeclaredField("name");
                field.setAccessible(true);
                names.add((String) field.get(player));
            }
            System.out.println(names);
        } catch (ClassNotFoundException | NoSuchMethodException | IllegalAccessException | InvocationTargetException | NoSuchFieldException e) {
            e.printStackTrace();
        }
    }
}
```