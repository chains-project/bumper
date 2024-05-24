```java
import org.cactoos.text.UncheckedText;
import io.zold.api.WalletsIn;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class WalletsInTest {

    @Test
    void shouldReturnWallets() {
        String expected = "[\n" +
                "  {\n" +
                "    \"id\": \"1234567890\",\n" +
                "    \"name\": \"My Wallet\",\n" +
                "    \"balance\": 1000000000,\n" +
                "    \"created_at\": \"2023-01-01T00:00:00Z\",\n" +
                "    \"updated_at\": \"2023-01-01T00:00:00Z\"\n" +
                "  },\n" +
                "  {\n" +
                "    \"id\": \"9876543210\",\n" +
                "    \"name\": \"Your Wallet\",\n" +
                "    \"balance\": 500000000,\n" +
                "    \"created_at\": \"2023-02-02T00:00:00Z\",\n" +
                "    \"updated_at\": \"2023-02-02T00:00:00Z\"\n" +
                "  }\n" +
                "]";

        String actual = new UncheckedText(new WalletsIn()).asString();

        assertEquals(expected, actual);
    }
}
```