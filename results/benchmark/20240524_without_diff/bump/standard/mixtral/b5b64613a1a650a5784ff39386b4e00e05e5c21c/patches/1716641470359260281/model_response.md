Here is a possible patch for the code:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            Optional.ofNullable(step.url).orElse(""),
            Optional.ofNullable(step.artifactoryUrl).orElse(""),
            Optional.ofNullable(step.distributionUrl).orElse(""))) {
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
    return Arrays.stream(urls).allMatch(String::isBlank);
}
```

The patch adds a new helper method `isAllBlank` that checks if all the given strings are blank. It uses the `Stream` API to iterate over the strings and check if they are blank using the `String::isBlank` method.

The `isAllBlank` method takes a variable number of `String` arguments using the `varargs` feature of Java.

The `checkInputs` method is modified to use the `isAllBlank` method by passing the URLs as arguments. The `Optional` class is used to provide default values for the `step` URLs in case they are null.

Note that this patch assumes that the `java.util.Optional` class is available in the project. If it is not, you might need to add a dependency to it or provide an alternative implementation.