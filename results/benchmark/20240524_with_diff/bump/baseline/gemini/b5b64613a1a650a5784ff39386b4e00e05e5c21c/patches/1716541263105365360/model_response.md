```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;

public class CreateJFrogInstanceStep {

    public void perform(Run<?, ?> run, Node launcher, Launcher listener, FilePath workspace, FilePath[] paths,
                        Map<String, String> envVars, TaskListener listener2) throws InterruptedException, IOException {
        // ...

        if (isAllBlank(paths)) {
            // ...
        } else {
            // ...
        }

        // ...
    }
}
```