```java
import com.jcabi.aspects.Tv;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestSshByPassword {

    @Test
    public void testSshByPassword() throws Exception {
        // Given
        Tv tv = new Tv();

        // When
        String result = tv.play("Breaking Bad");

        // Then
        assertEquals("Playing Breaking Bad", result);
    }
}
```