Here's the patched method:
```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNullElse(server.getArtifactory(), "").getUrl(), Objects.requireNonNullElse(server.getDistribution(), "").getUrl(), Objects.requireNonNullElse(step.url, ""), Objects.requireNonNullElse(step.artifactoryUrl, ""), Objects.requireNonNullElse(step.distributionUrl, ""))) {
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
```
I added `Objects.requireNonNullElse()` to replace the removed `getUrl()` method from `server.getArtifactory()` and `server.getDistribution()`. Also, I added `StringUtils.isNotBlank()` to replace the removed `getUrl()` method from `step.artifactoryUrl` and `step.distributionUrl`.