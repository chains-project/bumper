Here's the patched method with the added `isAllBlank` method:

```java
import static java.util.Objects.allMatch;
import static java.util.Objects.isNull;

// ...

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

private boolean isAllBlank(String... strings) {
    return allMatch(Arrays.stream(strings)
        .filter(Predicate.not(String::isBlank))
        .map(String::isEmpty)
        .reduce(Boolean::logicalOr)
        .orElse(false));
}
```

The `isAllBlank` method checks if all the given strings are blank or empty.