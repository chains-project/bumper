Here's a fixed version of the `checkInputs` method that replaces the missing `isAllBlank` method with a custom implementation using `org.apache.commons.lang3.StringUtils.isBlank`:
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
    for (String string : strings) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(string)) {
            return false;
        }
    }
    return true;
}
```
The new `isAllBlank` method checks if all the given strings are blank using `org.apache.commons.lang3.StringUtils.isBlank`.