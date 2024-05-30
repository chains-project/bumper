Here's a fixed version of the `checkInputs` method that uses `org.apache.commons.lang3.StringUtils.isAnyBlank` instead of `org.apache.commons.lang3.StringUtils.isAllBlank`:

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

The reason for this failure is that `org.apache.commons.lang3.StringUtils.isAllBlank` has been removed from the new library version, and it has been replaced with `org.apache.commons.lang3.StringUtils.isAnyBlank`, which checks whether any of the strings are blank. In this case, `isAnyBlank` is a suitable replacement for `isAllBlank` because the original method checks whether both `server.getUrl()` and `step.url` are blank, which is equivalent to checking whether any of them is blank.