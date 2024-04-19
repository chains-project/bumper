```
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

Change `isNotBlank()` to `StringUtils.isNotBlank()`

The `isNotBlank()` method is not a standard Java method, and it's not part of the `java.lang.String` class.
It's likely that the `isNotBlank()` method was added to the `org.jfrog.hudson.pipeline.declarative.steps` package as a custom method, but it's not available in the standard Java API.

By changing `isNotBlank()` to `StringUtils.isNotBlank()`, we're using a standard Java method that's part of the `java.util.StringUtils` class, which is available in the Java API.
This change should fix the error and allow the code to compile successfully.