```java
import com.premiumminds.billy.core.test.AbstractTest;
import org.junit.jupiter.api.Test;
import org.yaml.snakeyaml.Yaml;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class AbstractTestTest extends AbstractTest {

    @Test
    public void testYaml() throws IOException {
        File file = new File("src/test/resources/test.yaml");
        Path path = Paths.get(file.toURI());
        String content = new String(Files.readAllBytes(path));
        Yaml yaml = new Yaml();
        Object object = yaml.load(content);
        assertNotNull(object);
        assertEquals("test", object);
    }
}
```