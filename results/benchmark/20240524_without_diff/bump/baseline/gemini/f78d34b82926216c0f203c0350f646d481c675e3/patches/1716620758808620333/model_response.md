```java
import org.spongepowered.api.Sponge;
import org.spongepowered.api.event.Listener;
import org.spongepowered.api.event.game.state.GameInitializationEvent;
import org.spongepowered.api.plugin.Plugin;

@Plugin(id = "PeyangSuperbAntiCheat", name = "PeyangSuperbAntiCheat", version = "1.0")
public class PeyangSuperbAntiCheat {

    @Listener
    public void onGameInitialization(GameInitializationEvent event) {
        Sponge.getEventManager().registerListeners(this, new NPCTeleport());
    }
}
```