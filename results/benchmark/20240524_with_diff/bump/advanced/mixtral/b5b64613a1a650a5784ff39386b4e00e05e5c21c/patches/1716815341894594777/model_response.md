Here's a fixed version of the method that should resolve the error:

```java
private void checkInputs(org.jfrog.hudson.pipeline.common.types.JFrogPlatformInstance server) throws java.io.IOException {
    if (isAllBlank(server.getUrl(), Objects.requireNonNullElse(server.getArtifactory(), "").getUrl(), Objects.requireNonNullElse(server.getDistribution(), "").getUrl(), Objects.requireNonNullElse(step, "").url, Objects.requireNonNullElse(step, "").artifactoryUrl, Objects.requireNonNullElse(step, "").distributionUrl)) {
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

The changes made include:

* Adding `java.util.Objects` import.
* Using `Objects.requireNonNullElse` to provide a default value for null objects.
* Changing the method signature of `isAllBlank` to accept a variable number of arguments.

Note: You'll need to define the `isAllBlank` method to accept a variable number of arguments. Here's an example implementation:

```java
public static boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(String::isBlank);
}
```