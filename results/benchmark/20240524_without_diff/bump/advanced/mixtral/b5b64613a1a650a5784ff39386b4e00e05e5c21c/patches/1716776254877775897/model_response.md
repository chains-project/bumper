Here's a fixed version of the `checkInputs` method. I added a new helper method `isAllBlank` to make the code more readable and avoid the compilation error.

```java
import static org.apache.commons.lang3.StringUtils.isBlank;

private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new java.io.IOException("Server URL is missing");
    }
    if (org.apache.commons.lang3.StringUtils.isNotBlank(step.credentialsId)) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(step.username)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (org.apache.commons.lang3.StringUtils.isNotBlank(step.password)) {
            throw new java.io.IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

private boolean isAllBlank(String... urls) {
    for (String url : urls) {
        if (!isBlank(url)) {
            return false;
        }
    }
    return true;
}
```