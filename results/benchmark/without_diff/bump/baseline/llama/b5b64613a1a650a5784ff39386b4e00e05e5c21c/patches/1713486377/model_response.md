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

In the code above, `isNotBlank()` is not a standard Java method, and its usage causes the error. Replacing it with `StringUtils.isNotBlank()` from the Apache Commons Lang library should fix the issue.