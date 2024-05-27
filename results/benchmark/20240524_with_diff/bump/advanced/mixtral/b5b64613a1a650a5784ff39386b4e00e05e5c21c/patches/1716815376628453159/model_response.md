Here's the patched `checkInputs` method:
```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNullElse(server.getArtifactory(), "").getUrl(), Objects.requireNonNullElse(server.getDistribution(), "").getUrl(), Objects.requireNonNullElse(step, "").url, Objects.requireNonNullElse(step, "").artifactoryUrl, Objects.requireNonNullElse(step, "").distributionUrl)) {
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
Changes made:

1. Imported `java.util.Objects` and `org.apache.commons.lang3.StringUtils` for null-safe methods.
2. Replaced `server.getArtifactory().getUrl()` and similar expressions with `Objects.requireNonNullElse(server.getArtifactory(), "").getUrl()` to avoid NullPointerException. This checks if `server.getArtifactory()` is not null, if it is, it defaults to an empty string and then calls `getUrl()` on the empty string, which returns an empty string and avoids the NullPointerException.
3. Made the same change for `step.url`, `step.artifactoryUrl`, and `step.distributionUrl`.
4. No changes were made to the method signature or library methods used.