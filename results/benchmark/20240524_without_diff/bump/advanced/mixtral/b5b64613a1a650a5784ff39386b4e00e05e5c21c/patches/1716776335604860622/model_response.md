Here is the proposed patch:

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

boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (org.apache.commons.lang3.StringUtils.isNotBlank(string)) {
            return false;
        }
    }
    return true;
}
```

I created a new method `isAllBlank` that takes a variable number of `String` arguments and checks if they are all blank. This method is used in the `checkInputs` method instead of the original call to `isAllBlank`.

Note: I assumed that the `isAllBlank` method was removed from the external dependency and that is why the original code is failing.