Here's a fixed version of the `checkInputs` method that should resolve the compilation error:
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
The changes made:

* Added `Objects.requireNonNullElse` to handle cases where `server.getArtifactory()`, `server.getDistribution()`, `step.url`, `step.artifactoryUrl`, or `step.distributionUrl` are null.
* Added a default value of an empty string to `Objects.requireNonNullElse` to handle cases where the method calls return null.
* Imported `java.util.Objects` and `org.apache.commons.lang3.StringUtils` at the top of the file.

These changes ensure that the `isAllBlank` method is called with non-null arguments, which should resolve the compilation error.