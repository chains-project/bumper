Here's the proposed patch for the given failing client code:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.ArtifactoryServer server) throws java.io.IOException {
    if (org.apache.commons.lang3.StringUtils.isBlank(server.getUrl()) && org.apache.commons.lang3.StringUtils.isBlank(step.url)) {
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

The patch replaces the `isAllBlank` method call with two separate `isBlank` method calls for each string argument.

The `isAllBlank` method was introduced in Apache Commons Lang 3.10, while the `isBlank` method has been available since version 3.0.
By using `isBlank` instead, the code should work with earlier versions of Apache Commons Lang.

The failing test case should now pass with the updated code.