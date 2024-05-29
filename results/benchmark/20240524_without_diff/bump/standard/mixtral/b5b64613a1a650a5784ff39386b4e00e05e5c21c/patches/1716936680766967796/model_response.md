Here's a fixed version of your code. I added a utility method `isAllBlank` to the class to fix the error:

```java
import org.apache.commons.lang3.StringUtils;

// ...

private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (StringUtils.isNotBlank(step.credentialsId)) {
        if (StringUtils.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (StringUtils.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

// New utility method
private boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (StringUtils.isNotBlank(string)) {
            return false;
        }
    }
    return true;
}
```

The `isAllBlank` utility method checks if all given strings are blank.