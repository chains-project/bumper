Here is the patched method:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNullElse(server.getArtifactory(), "").getUrl(), Objects.requireNonNullElse(server.getDistribution(), "").getUrl(), Objects.requireNonNullElse(step.url, ""), Objects.requireNonNullElse(step.artifactoryUrl, ""), Objects.requireNonNullElse(step.distributionUrl, ""))) {
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
```

The changes made:

1. Imported the missing `java.util.Objects` class to use `Objects.requireNonNullElse` method.
2. Used `Objects.requireNonNullElse` method to provide a default value for `server.getArtifactory()`, `server.getDistribution()`, `step.url`, `step.artifactoryUrl`, and `step.distributionUrl` in case they are `null`.
3. Provided an empty string as the default value for the methods that might return `null`.

Note: This patch assumes that the `isAllBlank` method is defined elsewhere in the code and it checks if all the provided strings are blank or not.