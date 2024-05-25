```java
import org.cactoos.scalar.UncheckedScalar;

import java.util.concurrent.Callable;

public class RtTransaction {

    private final RtClient client;
    private final String id;

    public RtTransaction(RtClient client, String id) {
        this.client = client;
        this.id = id;
    }

    public <T> T execute(Callable<T> callable) throws Exception {
        try {
            return callable.call();
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            client.close();
        }
    }

    public void close() {
        client.close();
    }

    public String getId() {
        return id;
    }

    public RtClient getClient() {
        return client;
    }

    public static RtTransaction of(RtClient client, String id) {
        return new RtTransaction(client, id);
    }

    public static RtTransaction of(RtClient client, UncheckedScalar<String> id) {
        return new RtTransaction(client, id.value());
    }
}
```