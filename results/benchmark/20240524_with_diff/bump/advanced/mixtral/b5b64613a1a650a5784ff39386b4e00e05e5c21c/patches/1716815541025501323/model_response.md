Here's the updated `checkInputs` method with the missing `isAllBlank` method implementation:
```java
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

private boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(String::isBlank);
}
```
The `isAllBlank` method checks if all the provided strings are blank using the `String::isBlank` method, which was introduced in Java 11. If you are using a previous Java version, you can replace `String::isBlank` with `s -> s == null || s.isEmpty()`.