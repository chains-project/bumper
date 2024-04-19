Here's a proposed patch to fix the error in the provided code:
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
    
    if (!isBlank(step.credentialsId)) {
        if (isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (isNotBlank(string)) {
            return false;
        }
    }
    return true;
}

boolean isNotBlank(String string) {
    return string != null && !string.isEmpty();
}
```
The proposed patch introduces two new methods, `isAllBlank` and `isNotBlank`, which are used to simplify the checks for blank strings. The `isAllBlank` method takes an array of strings and returns `true` if all the strings are blank, and `false` otherwise. The `isNotBlank` method takes a single string and returns `true` if the string is not blank, and `false` otherwise.


The `checkInputs` method is then modified to use these new methods to perform the checks. The `isAllBlank` method is used to check if all the URLs are blank, and the `isNotBlank` method is used to check if the credentials ID, username, and password are blank.

This patch should fix the error message you provided and make the code more readable and maintainable.