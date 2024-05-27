Here's a possible patch for the code you provided. I created a utility method `isAllBlank` that checks if all the given strings are blank or not.

```java
private boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(String::isBlank);
}

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
```

Note that this patch assumes that the `java.util.stream` package is available, as it uses the `Arrays.stream` method to create a stream of strings. If this package is not available, you can use a different approach to check if all the strings are blank or not.