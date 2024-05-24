Here's the updated `checkInputs` method with the new `isAllBlank` utility method that accepts a variable number of arguments:

```java
import static org.jenkinsci.plugins.p4.util.StringUtils.isAllBlank;

private void checkInputs(JFrogPlatformInstance server) throws IOException {
    if (isAllBlank(server.getUrl(), server.getArtifactory().getUrl(), server.getDistribution().getUrl(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(step.credentialsId)) {
        if (isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

static boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(String::isBlank);
}
```

The `isAllBlank` utility method checks if all the given strings are blank. The method uses the Java 8 Stream API to simplify the code.

The `isBlank` method is not present in the given library version changes, but it is a part of the Apache Commons Lang library. If you don't have it in your project, you can implement it yourself:

```java
import static java.util.Objects.requireNonNullElse;

public static boolean isBlank(String string) {
    return requireNonNullElse(string, "").isBlank();
}
```

This implementation uses `java.util.Objects.requireNonNullElse` to handle null values gracefully, returning an empty string if the input is null.