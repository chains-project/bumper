Here is a fixed version of the `checkInputs` method that uses `org.apache.commons.lang3.StringUtils.isAnyBlank` instead of `org.apache.commons.lang3.StringUtils.isAllBlank`:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.ArtifactoryServer server) throws java.io.IOException {
    if (org.apache.commons.lang3.StringUtils.isAnyBlank(server.getUrl(), step.url)) {
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

`org.apache.commons.lang3.StringUtils.isAnyBlank` checks if any of the strings passed to it is blank, whereas `org.apache.commons.lang3.StringUtils.isAllBlank` checks if all of the strings passed to it are blank. In this case, `org.apache.commons.lang3.StringUtils.isAnyBlank` is the appropriate method to use, because the server URL and the step URL should not both be blank, but at least one of them must be non-blank.