```java
import java.io.IOException;
import org.apache.maven.plugin.MojoExecutionException;

public void execute() throws MojoExecutionException {
    try {
        // code
    } catch (IOException e) {
        throw new MojoExecutionException("Error", e);
    }
}
```