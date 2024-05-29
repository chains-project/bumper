Here's a possible patch for the code to fix the error:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(), server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl())) {
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
        if (org.apache.commons.lang3.StringUtils.isNotBlank(url)) {
            return false;
        }
    }
    return true;
}
```

The patch defines a new helper method `isAllBlank` that takes a variable number of `String` arguments and checks if all of them are blank. This method is then used in the `checkInputs` method instead of calling the non-existent `isAllBlank` method from the `Execution` class. This should fix the error and make the code compile.