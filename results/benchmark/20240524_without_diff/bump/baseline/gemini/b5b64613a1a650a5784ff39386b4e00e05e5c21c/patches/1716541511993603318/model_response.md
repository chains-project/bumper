```java
import static org.apache.commons.lang3.StringUtils.isNotBlank;

public class CreateJFrogInstanceStep {

    public static final String ARTIFACTORY_URL = "https://artifactory.jfrog.io/artifactory";

    public void execute(StepContext context) throws Exception {
        String artifactoryUrl = context.get(ARTIFACTORY_URL);
        if (isNotBlank(artifactoryUrl)) {
            context.env("ARTIFACTORY_URL", artifactoryUrl);
        }
    }
}
```