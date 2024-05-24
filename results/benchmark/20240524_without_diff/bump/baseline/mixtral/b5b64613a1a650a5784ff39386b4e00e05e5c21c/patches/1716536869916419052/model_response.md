Here's a fixed version of the `checkInputs` method that should resolve the compilation error by using the `isAllBlank` utility method from Apache Commons Lang 3, which is a recommended way to check if a string is blank:

```java
import org.apache.commons.lang3.StringUtils;

private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (StringUtils.isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (StringUtils.isNotBlank(step.credentialsId)) {
        if (StringUtils.isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (StringUtils.isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}
```

This solution doesn't rely on any library methods that were removed in the new version. The `isAllBlank` method is replaced by the `StringUtils.isAllBlank` method from Apache Commons Lang 3, which is a more recommended way to check if a string is blank.