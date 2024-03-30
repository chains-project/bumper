Here's a proposed patch to fix the error:
```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    String url = server.getUrl();
    String artifactoryUrl = server.getArtifactory().getUrl();
    String distributionUrl = server.getDistribution().getUrl();
    String stepUrl = step.url;
    String stepArtifactoryUrl = step.artifactoryUrl;
    String stepDistributionUrl = step.distributionUrl;
    
    if (isAllBlank(url, artifactoryUrl, distributionUrl, stepUrl, stepArtifactoryUrl, stepDistributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    
    if (!isBlank(step.credentialsId) && (isNotBlank(step.username) || isNotBlank(step.password))) {
        throw new IOException("'rtServer' step can't include both credentialsId and username or password");
    }
}

boolean isAllBlank(String... strings) {
    for (String s : strings) {
        if (s != null && !s.isEmpty()) {
            return false;
        }
    }
    return true;
}

boolean isNotBlank(String s) {
    return s != null && !s.isEmpty();
}
```
The patch introduces two new methods, `isAllBlank` and `isNotBlank`, which are used to simplify the conditionals in the `checkInputs` method. The `isAllBlank` method takes an array of strings and returns `true` if all the strings are blank, and `false` otherwise. The `isNotBlank` method takes a single string and returns `true` if the string is not blank, and `false` otherwise.


The `checkInputs` method is then modified to use these new methods, making the code more concise and easier to read. The `isAllBlank` method is used to check if all the URLs are blank, and the `isNotBlank` method is used to check if the credentials ID, username, and password are not all blank.

This patch should fix the error message and make the code more readable.