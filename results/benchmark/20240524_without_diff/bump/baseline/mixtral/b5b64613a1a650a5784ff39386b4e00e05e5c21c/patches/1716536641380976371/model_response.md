Here's a fixed version of the `checkInputs` method that should resolve the compilation error by using the new `isAllBlank` utility method from the `org.jenkinsci.plugins.p4.util` package:

```java
import static org.jenkinsci.plugins.p4.util.P4Util.isAllBlank;

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
```

This solution assumes that the `isNotBlank` method is still available in the new version or is defined elsewhere in the client code. If `isNotBlank` is not available, you can define it as follows:

```java
private boolean isNotBlank(String s) {
    return s != null && !s.trim().isEmpty();
}
```